'use client'

import { UserCheck, FileText, TrendingUp, BarChart } from 'lucide-react'

export default function ProcessTimeline() {
  const steps = [
    {
      icon: UserCheck,
      title: 'Free Consultation',
      description: 'Book a no-obligation consultation. We understand your financial goals, risk profile, and investment horizon.',
      duration: '30-45 mins',
      color: 'from-blue-500 to-blue-700',
    },
    {
      icon: FileText,
      title: 'Personalized Plan',
      description: 'Receive a customized investment strategy with detailed fund recommendations, asset allocation, and expected returns.',
      duration: '2-3 days',
      color: 'from-green-500 to-emerald-700',
    },
    {
      icon: TrendingUp,
      title: 'Easy Onboarding',
      description: 'Complete paperless KYC online in 15 minutes. Start investing through SIP or lumpsum with zero hassle.',
      duration: '15 mins',
      color: 'from-purple-500 to-indigo-700',
    },
    {
      icon: BarChart,
      title: 'Ongoing Support',
      description: 'Get monthly reports, quarterly reviews, and continuous guidance to keep your financial plan on track.',
      duration: 'Lifetime',
      color: 'from-orange-500 to-red-600',
    },
  ]

  return (
    <section className="py-20 bg-gradient-to-b from-white to-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
            Your Investment Journey
          </h2>
          <p className="text-xl text-gray-600 max-w-3xl mx-auto">
            A simple, transparent process from consultation to wealth creation
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 relative">
          {/* Connecting line for desktop */}
          <div className="hidden lg:block absolute top-20 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-green-500 via-purple-500 to-orange-500 opacity-20" style={{ width: 'calc(100% - 160px)', marginLeft: '80px' }}></div>

          {steps.map((step, index) => (
            <div key={index} className="relative">
              <div className="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-all hover:-translate-y-2 border border-gray-100 relative z-10">
                <div className={`inline-flex items-center justify-center w-16 h-16 rounded-xl bg-gradient-to-br ${step.color} mb-4 shadow-lg`}>
                  <step.icon className="w-8 h-8 text-white" />
                </div>
                
                <div className="absolute top-6 right-6 bg-primary-100 text-primary-700 text-xs font-bold px-3 py-1 rounded-full">
                  Step {index + 1}
                </div>

                <h3 className="text-xl font-bold text-gray-900 mb-3">
                  {step.title}
                </h3>

                <p className="text-gray-600 leading-relaxed mb-4 text-sm">
                  {step.description}
                </p>

                <div className="flex items-center text-sm text-gray-500">
                  <span className="mr-2">⏱️</span>
                  <span>{step.duration}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
