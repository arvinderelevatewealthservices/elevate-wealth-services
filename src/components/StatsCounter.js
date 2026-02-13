'use client'

import { useState, useEffect, useRef } from 'react'

export default function StatsCounter() {
  const [isVisible, setIsVisible] = useState(false)
  const [counts, setCounts] = useState({
    experience: 0,
    services: 0,
    compliance: 0,
    support: 0,
  })
  const sectionRef = useRef(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !isVisible) {
          setIsVisible(true)
        }
      },
      { threshold: 0.3 }
    )

    if (sectionRef.current) {
      observer.observe(sectionRef.current)
    }

    return () => observer.disconnect()
  }, [isVisible])

  useEffect(() => {
    if (!isVisible) return

    const duration = 2000
    const steps = 60
    const interval = duration / steps

    const targets = {
      experience: 5,
      services: 3,
      compliance: 100,
      support: 6,
    }

    let currentStep = 0

    const timer = setInterval(() => {
      currentStep++
      const progress = currentStep / steps

      setCounts({
        experience: Math.floor(targets.experience * progress),
        services: Math.floor(targets.services * progress),
        compliance: Math.floor(targets.compliance * progress),
        support: Math.floor(targets.support * progress),
      })

      if (currentStep >= steps) {
        setCounts(targets)
        clearInterval(timer)
      }
    }, interval)

    return () => clearInterval(timer)
  }, [isVisible])

  const stats = [
    {
      value: `${counts.experience}+`,
      label: 'Years of Excellence',
      icon: '🏆',
      color: 'from-blue-500 to-blue-700',
    },
    {
      value: `${counts.services}`,
      label: 'Core Services',
      icon: '💼',
      color: 'from-green-500 to-emerald-700',
    },
    {
      value: `${counts.compliance}%`,
      label: 'Regulatory Compliant',
      icon: '✓',
      color: 'from-purple-500 to-indigo-700',
    },
    {
      value: `${counts.support} Days`,
      label: 'Weekly Support',
      icon: '📞',
      color: 'from-orange-500 to-red-600',
    },
  ]

  return (
    <section ref={sectionRef} className="py-20 bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white relative overflow-hidden">
      <div className="absolute inset-0 opacity-10">
        <div className="absolute top-0 left-1/4 w-96 h-96 bg-primary-500 rounded-full filter blur-3xl animate-pulse"></div>
        <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-purple-500 rounded-full filter blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div className="text-center mb-12">
          <h2 className="text-4xl md:text-5xl font-bold mb-4">
            Built on Trust & Excellence
          </h2>
          <p className="text-xl text-gray-300">
            Our commitment to professional financial services
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((stat, index) => (
            <div
              key={index}
              className="relative group"
              style={{ animationDelay: `${index * 100}ms` }}
            >
              <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8 border border-white/20 hover:bg-white/20 transition-all duration-300 hover:scale-105 hover:shadow-2xl">
                <div className="text-center">
                  <div className="text-5xl mb-4">{stat.icon}</div>
                  <div className={`text-5xl font-bold bg-gradient-to-r ${stat.color} bg-clip-text text-transparent mb-2`}>
                    {stat.value}
                  </div>
                  <div className="text-gray-300 font-medium">
                    {stat.label}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
