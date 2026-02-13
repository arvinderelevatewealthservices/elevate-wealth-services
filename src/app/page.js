'use client'

import Hero from '@/components/Hero'
import AnimatedBrandBanner from '@/components/AnimatedBrandBanner'
import ServiceCard from '@/components/ServiceCard'
import AnimatedSection from '@/components/AnimatedSection'
import StatsCounter from '@/components/StatsCounter'
import ProcessTimeline from '@/components/ProcessTimeline'
import FAQSection from '@/components/FAQSection'
import { TrendingUp, Shield, BarChart3, Target, Users, Award, CheckCircle2, Lock, Clock, Phone } from 'lucide-react'
import Link from 'next/link'

export default function Home() {
  const services = [
    {
      icon: TrendingUp,
      title: 'Mutual Fund Advisory',
      description: 'Build long-term wealth through systematic investing with professionally curated mutual fund portfolios. Our goal-based approach ensures your investments align perfectly with your financial objectives.',
      features: [
        'Personalized portfolio construction based on risk profile',
        'Diversification across equity, debt, and hybrid funds',
        'SIP planning and automated investment setup',
        'Regular performance monitoring and rebalancing',
        'Tax-efficient investment strategies (ELSS)',
        'Access to top-performing funds from leading AMCs',
      ],
      gradient: 'from-blue-500 to-blue-700',
    },
    {
      icon: Shield,
      title: 'Insurance Solutions',
      description: 'Comprehensive protection for you and your loved ones. We analyze your needs and recommend optimal coverage across life, health, and general insurance to secure your family\'s financial future.',
      features: [
        'Life insurance (term plans, endowment, ULIPs)',
        'Health insurance (individual, family floater, critical illness)',
        'General insurance (motor, home, travel)',
        'Coverage gap analysis and needs assessment',
        'Policy comparison from multiple insurers',
        'End-to-end claims assistance and support',
      ],
      gradient: 'from-green-500 to-emerald-700',
    },
    {
      icon: BarChart3,
      title: 'Trading & Brokerage',
      description: 'Execute trades efficiently with platform-backed execution and professional advisory support. Whether you\'re an active trader or strategic investor, we provide the tools and guidance you need.',
      features: [
        'Equity trading (delivery and intraday)',
        'Derivatives trading (futures and options)',
        'Real-time market insights and research',
        'Advanced trading platforms and tools',
        'Strategic guidance for informed decisions',
        'Risk management and portfolio advisory',
      ],
      gradient: 'from-purple-500 to-indigo-700',
    },
  ]

  const whyChooseUs = [
    {
      icon: Target,
      title: 'Goal-Based Planning',
      description: 'We don\'t just sell products—we design strategies aligned with your specific financial goals, whether it\'s retirement, children\'s education, or wealth creation.',
    },
    {
      icon: Users,
      title: 'Client-First Approach',
      description: 'Your financial well-being is our priority. Every recommendation is made with your best interests in mind, not commission potential.',
    },
    {
      icon: Lock,
      title: 'Complete Transparency',
      description: 'No hidden charges, no fine print surprises. We explain everything clearly—fees, risks, returns, and processes—so you make informed decisions.',
    },
    {
      icon: Award,
      title: 'Regulatory Compliance',
      description: 'AMFI-registered, IRDAI-compliant, and SEBI-regulated. We adhere to all regulatory standards ensuring your investments are in safe hands.',
    },
    {
      icon: Clock,
      title: 'Long-Term Partnership',
      description: 'We build lasting relationships, not one-time transactions. Our commitment extends beyond the sale through continuous support and guidance.',
    },
    {
      icon: Phone,
      title: 'Accessible Support',
      description: 'Reach us via phone, WhatsApp, email, or visit our office. We\'re available 6 days a week to answer queries and provide assistance.',
    },
  ]

  return (
    <>
      {/* Hero Section */}
      <Hero />

      {/* Brand Banner */}
      <AnimatedBrandBanner />

      {/* Stats Counter */}
      <StatsCounter />

      {/* Services Snapshot */}
      <section className="py-20 bg-gradient-to-b from-white to-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="text-center mb-16">
              <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
                Comprehensive Financial Services
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                From wealth building to risk protection—everything you need under one trusted platform
              </p>
            </div>
          </AnimatedSection>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <AnimatedSection key={index}>
                <ServiceCard {...service} />
              </AnimatedSection>
            ))}
          </div>
        </div>
      </section>

      {/* Why Choose Us */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="text-center mb-16">
              <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
                Why Choose ElevateWealthServices
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                Built on trust, driven by your success, committed to excellence
              </p>
            </div>
          </AnimatedSection>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {whyChooseUs.map((item, index) => (
              <AnimatedSection key={index}>
                <div className="bg-gradient-to-br from-gray-50 to-white rounded-2xl p-8 border border-gray-100 hover:shadow-xl transition-all hover:-translate-y-1">
                  <div className="inline-flex items-center justify-center w-14 h-14 rounded-xl bg-gradient-to-br from-primary-100 to-primary-200 mb-6">
                    <item.icon className="w-7 h-7 text-primary-700" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 mb-3">
                    {item.title}
                  </h3>
                  <p className="text-gray-600 leading-relaxed">
                    {item.description}
                  </p>
                </div>
              </AnimatedSection>
            ))}
          </div>

          {/* Additional Info Boxes */}
          <AnimatedSection>
            <div className="mt-16 grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="bg-gradient-to-br from-primary-50 to-blue-50 rounded-2xl p-8">
                <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                  <span className="text-3xl mr-3">🏢</span>
                  Offline Office Support
                </h3>
                <p className="text-gray-700 leading-relaxed">
                  Visit our office in Ludhiana for face-to-face consultations. We believe in building personal relationships beyond digital interactions. Meet our team, discuss your financial plans over coffee, and get the reassurance of a physical presence you can trust.
                </p>
              </div>

              <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-8">
                <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                  <span className="text-3xl mr-3">📚</span>
                  Financial Literacy Focus
                </h3>
                <p className="text-gray-700 leading-relaxed">
                  We don't just manage your money—we educate you about it. Through detailed explanations, regular market updates, and investment insights, we empower you to understand your financial decisions and build lasting wealth intelligence.
                </p>
              </div>
            </div>
          </AnimatedSection>
        </div>
      </section>

      {/* Process Timeline */}
      <ProcessTimeline />

      {/* Trust & Compliance Section */}
      <section className="py-20 bg-gradient-to-br from-gray-50 to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="text-center mb-12">
              <h2 className="text-4xl md:text-5xl font-bold text-gray-900 mb-4">
                Certified & Compliant
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                Your financial security is backed by regulatory compliance and professional certifications
              </p>
            </div>
          </AnimatedSection>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg border-2 border-primary-100">
                <div className="text-center">
                  <div className="text-6xl mb-4">📜</div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-3">
                    AMFI Registered
                  </h3>
                  <p className="text-gray-600 mb-4">
                    Association of Mutual Funds in India registered distributor ensuring professional mutual fund advisory services.
                  </p>
                  <div className="bg-primary-50 rounded-lg p-3">
                    <p className="text-sm font-semibold text-primary-700">
                      ARN: [Your ARN Number]
                    </p>
                  </div>
                </div>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg border-2 border-green-100">
                <div className="text-center">
                  <div className="text-6xl mb-4">🛡️</div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-3">
                    IRDAI Compliant
                  </h3>
                  <p className="text-gray-600 mb-4">
                    Insurance Regulatory and Development Authority of India compliant for all insurance distribution activities.
                  </p>
                  <div className="bg-green-50 rounded-lg p-3">
                    <p className="text-sm font-semibold text-green-700">
                      Licensed Insurance Intermediary
                    </p>
                  </div>
                </div>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg border-2 border-purple-100">
                <div className="text-center">
                  <div className="text-6xl mb-4">✓</div>
                  <h3 className="text-2xl font-bold text-gray-900 mb-3">
                    SEBI Regulated
                  </h3>
                  <p className="text-gray-600 mb-4">
                    Securities and Exchange Board of India regulated operations for trading and brokerage services.
                  </p>
                  <div className="bg-purple-50 rounded-lg p-3">
                    <p className="text-sm font-semibold text-purple-700">
                      Full Regulatory Compliance
                    </p>
                  </div>
                </div>
              </div>
            </AnimatedSection>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <FAQSection />

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-br from-primary-600 via-primary-700 to-blue-800 text-white relative overflow-hidden">
        <div className="absolute inset-0">
          <div className="absolute top-0 left-1/4 w-96 h-96 bg-white rounded-full filter blur-3xl opacity-10"></div>
          <div className="absolute bottom-0 right-1/4 w-96 h-96 bg-white rounded-full filter blur-3xl opacity-10"></div>
        </div>
        
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
          <AnimatedSection>
            <h2 className="text-4xl md:text-5xl font-bold mb-6">
              Ready to Elevate Your Financial Future?
            </h2>
            <p className="text-xl mb-8 text-primary-100 leading-relaxed">
              Schedule a free, no-obligation consultation with our financial experts. Let's discuss your goals and create a personalized strategy to achieve them.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link
                href="/contact"
                className="bg-white text-primary-700 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-gray-100 transition-all hover:scale-105 shadow-xl flex items-center space-x-2"
              >
                <span>Book Free Consultation</span>
                <span>→</span>
              </Link>
              <a
                href="https://wa.me/919876543210"
                target="_blank"
                rel="noopener noreferrer"
                className="bg-transparent border-2 border-white text-white px-8 py-4 rounded-xl font-semibold text-lg hover:bg-white/10 transition-all flex items-center space-x-2"
              >
                <span>💬</span>
                <span>WhatsApp Us</span>
              </a>
            </div>
            
            <div className="mt-8 text-primary-100">
              <p className="text-sm">📞 Call: +91 98765 43210 | 📧 Email: info@elevatewealthservices.com</p>
            </div>
          </AnimatedSection>
        </div>
      </section>
    </>
  )
}
