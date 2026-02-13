'use client'

import AnimatedSection from '@/components/AnimatedSection'
import { Target, Eye, Shield, Award, TrendingUp, Users, Heart, Zap, CheckCircle2, MapPin, Clock, Phone } from 'lucide-react'

export default function AboutPage() {
  const values = [
    {
      icon: Shield,
      title: 'Trust & Integrity',
      description: 'We operate with complete honesty and transparency. Your trust is our most valuable asset, and we protect it through ethical practices and genuine advice.',
    },
    {
      icon: Target,
      title: 'Client-Centric Focus',
      description: 'Every strategy, every recommendation, every decision is made with one question in mind: "Is this in the client\'s best interest?" Your goals drive our actions.',
    },
    {
      icon: Award,
      title: 'Professional Excellence',
      description: 'AMFI-certified, IRDAI-compliant, continuously updated with market knowledge. We maintain the highest standards of professional competence.',
    },
    {
      icon: TrendingUp,
      title: 'Long-Term Vision',
      description: 'We focus on sustainable wealth creation, not quick gains. Our strategies are designed for lasting financial security and generational wealth building.',
    },
    {
      icon: Heart,
      title: 'Empathy & Understanding',
      description: 'We recognize that behind every investment decision is a dream, a responsibility, a future. We listen, understand, and care about your financial journey.',
    },
    {
      icon: Zap,
      title: 'Innovation & Adaptability',
      description: 'While our values are timeless, our methods evolve. We leverage technology and adapt to market changes to serve you better.',
    },
  ]

  const approach = [
    {
      title: 'Comprehensive Financial Assessment',
      description: 'We begin by understanding your complete financial picture—income, expenses, assets, liabilities, existing investments, and insurance coverage. This holistic view helps us identify gaps and opportunities.',
      icon: '📊',
    },
    {
      title: 'Goal Identification & Prioritization',
      description: 'Whether it\'s retirement planning, children\'s education, buying a home, or building an emergency fund—we help you define clear, measurable financial goals with realistic timelines.',
      icon: '🎯',
    },
    {
      title: 'Risk Profile Analysis',
      description: 'Through detailed discussions and assessment questionnaires, we determine your risk tolerance, investment horizon, and comfort level with market volatility. This ensures recommendations match your personality.',
      icon: '⚖️',
    },
    {
      title: 'Customized Strategy Design',
      description: 'Based on your goals and risk profile, we design a personalized investment and protection strategy. This includes asset allocation, fund selection, insurance coverage, and tax optimization.',
      icon: '📝',
    },
    {
      title: 'Implementation Support',
      description: 'We handle all the paperwork, KYC processes, and account setups. Our goal is to make investing as simple as possible for you—just approve the plan and we execute it.',
      icon: '🚀',
    },
    {
      title: 'Continuous Monitoring & Review',
      description: 'Markets change, life changes, goals change. We provide regular performance updates, conduct quarterly reviews, and recommend adjustments to keep your financial plan on track.',
      icon: '🔄',
    },
  ]

  return (
    <div className="pt-20">
      {/* Hero Section */}
      <section className="py-20 bg-gradient-to-br from-primary-50 via-blue-50 to-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <AnimatedSection>
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
              About ElevateWealthServices
            </h1>
            <p className="text-xl text-gray-600 leading-relaxed">
              A professional financial services platform committed to helping individuals and families achieve financial freedom through transparent, client-first advisory and comprehensive wealth solutions.
            </p>
          </AnimatedSection>
        </div>
      </section>

      {/* Who We Are */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <AnimatedSection>
              <div>
                <h2 className="text-4xl font-bold text-gray-900 mb-6">
                  Who We Are
                </h2>
                <div className="space-y-4 text-gray-600 leading-relaxed text-lg">
                  <p>
                    ElevateWealthServices is a comprehensive financial services platform headquartered in Ludhiana, Punjab, specializing in Mutual Fund distribution, Insurance solutions, and Trading & Brokerage services.
                  </p>
                  <p>
                    As an <strong className="text-gray-900">AMFI-registered Mutual Fund Distributor</strong>, we are committed to providing professional, transparent, and goal-oriented financial advisory services to investors across India. Our registration ensures that we adhere to the highest standards of compliance and ethical conduct set by regulatory authorities.
                  </p>
                  <p>
                    Founded with a vision to democratize quality financial advice, we bridge the gap between complex financial products and everyday investors. Our approach combines the convenience of digital platforms with the trust of face-to-face consultations at our physical office.
                  </p>
                  <p>
                    We serve diverse clients—from first-time investors taking their initial steps in mutual funds to experienced traders seeking strategic guidance. What unites them all is their trust in our commitment to their financial well-being.
                  </p>
                </div>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-gradient-to-br from-primary-100 to-blue-100 rounded-2xl p-8 md:p-12 space-y-8">
                <div className="flex items-start space-x-4">
                  <Eye className="w-8 h-8 text-primary-700 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-2xl font-bold text-gray-900 mb-3">Our Vision</h3>
                    <p className="text-gray-700 leading-relaxed">
                      To be the most trusted financial services partner in India, empowering every individual—regardless of their starting point—to achieve financial independence through disciplined investing, adequate protection, and informed financial decisions.
                    </p>
                  </div>
                </div>
                <div className="flex items-start space-x-4">
                  <Target className="w-8 h-8 text-primary-700 mt-1 flex-shrink-0" />
                  <div>
                    <h3 className="text-2xl font-bold text-gray-900 mb-3">Our Mission</h3>
                    <p className="text-gray-700 leading-relaxed">
                      To simplify financial planning through transparent advice, personalized strategies, continuous education, and unwavering commitment to our clients' success. We measure our success by the financial goals our clients achieve.
                    </p>
                  </div>
                </div>
              </div>
            </AnimatedSection>
          </div>
        </div>
      </section>

      {/* Our Values */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="text-center mb-16">
              <h2 className="text-4xl font-bold text-gray-900 mb-4">
                Our Core Values
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                The principles that guide every decision we make and every recommendation we provide
              </p>
            </div>
          </AnimatedSection>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {values.map((value, index) => (
              <AnimatedSection key={index}>
                <div className="bg-white rounded-xl p-8 shadow-lg hover:shadow-xl transition-all hover:-translate-y-1 h-full">
                  <div className="inline-flex items-center justify-center w-14 h-14 rounded-lg bg-gradient-to-br from-primary-500 to-primary-700 mb-6">
                    <value.icon className="w-7 h-7 text-white" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 mb-3">
                    {value.title}
                  </h3>
                  <p className="text-gray-600 leading-relaxed">
                    {value.description}
                  </p>
                </div>
              </AnimatedSection>
            ))}
          </div>
        </div>
      </section>

      {/* Our Approach */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="text-center mb-16">
              <h2 className="text-4xl font-bold text-gray-900 mb-4">
                Our Approach to Financial Planning
              </h2>
              <p className="text-xl text-gray-600 max-w-3xl mx-auto">
                A systematic, client-centric methodology that puts your goals at the center
              </p>
            </div>
          </AnimatedSection>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {approach.map((step, index) => (
              <AnimatedSection key={index}>
                <div className="relative">
                  <div className="absolute -top-4 -left-4 w-12 h-12 bg-gradient-to-br from-primary-500 to-primary-700 rounded-full flex items-center justify-center text-white font-bold text-lg shadow-lg">
                    {index + 1}
                  </div>
                  <div className="bg-gradient-to-br from-gray-50 to-white rounded-2xl p-8 border border-gray-200 hover:shadow-xl transition-all h-full">
                    <div className="text-5xl mb-4">{step.icon}</div>
                    <h3 className="text-xl font-bold text-gray-900 mb-3">
                      {step.title}
                    </h3>
                    <p className="text-gray-600 leading-relaxed">
                      {step.description}
                    </p>
                  </div>
                </div>
              </AnimatedSection>
            ))}
          </div>
        </div>
      </section>

      {/* What Sets Us Apart */}
      <section className="py-20 bg-gradient-to-br from-primary-50 to-blue-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="text-center mb-12">
              <h2 className="text-4xl font-bold text-gray-900 mb-4">
                What Sets Us Apart
              </h2>
            </div>
          </AnimatedSection>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg">
                <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                  <CheckCircle2 className="w-7 h-7 text-green-600 mr-3" />
                  Hybrid Model: Online + Offline
                </h3>
                <p className="text-gray-600 leading-relaxed mb-4">
                  While most distributors are either purely online or traditional offline, we offer both. Access your portfolio digitally 24/7, but also have the option to walk into our Ludhiana office for face-to-face consultations.
                </p>
                <p className="text-gray-600 leading-relaxed">
                  This hybrid approach gives you the convenience of digital platforms with the trust and personal touch of in-person meetings.
                </p>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg">
                <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                  <CheckCircle2 className="w-7 h-7 text-green-600 mr-3" />
                  Educational Focus
                </h3>
                <p className="text-gray-600 leading-relaxed mb-4">
                  We believe informed investors make better decisions. That's why we don't just execute transactions—we educate you about investment concepts, market dynamics, and financial planning principles.
                </p>
                <p className="text-gray-600 leading-relaxed">
                  Through detailed explanations, regular updates, and responsive communication, we empower you with financial literacy.
                </p>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg">
                <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                  <CheckCircle2 className="w-7 h-7 text-green-600 mr-3" />
                  No Product Pushing
                </h3>
                <p className="text-gray-600 leading-relaxed mb-4">
                  We're not salespeople trying to meet targets. We're advisors focused on your financial well-being. If a particular product doesn't suit your needs, we'll tell you—even if it means lower commission for us.
                </p>
                <p className="text-gray-600 leading-relaxed">
                  Our recommendations are based on thorough analysis of your situation, not what earns us the most.
                </p>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-2xl p-8 shadow-lg">
                <h3 className="text-2xl font-bold text-gray-900 mb-4 flex items-center">
                  <CheckCircle2 className="w-7 h-7 text-green-600 mr-3" />
                  Lifelong Support
                </h3>
                <p className="text-gray-600 leading-relaxed mb-4">
                  Your financial journey doesn't end after the first investment. We provide continuous support—answering queries, reviewing portfolios, adjusting strategies as your life evolves, and helping with claims when needed.
                </p>
                <p className="text-gray-600 leading-relaxed">
                  Many of our clients have been with us for years, and we're committed to being your financial partner for life.
                </p>
              </div>
            </AnimatedSection>
          </div>
        </div>
      </section>

      {/* Office & Contact Info */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <AnimatedSection>
            <div className="bg-gradient-to-br from-gray-900 to-gray-800 rounded-3xl p-12 text-white">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-12">
                <div>
                  <h2 className="text-3xl font-bold mb-6">Visit Our Office</h2>
                  <p className="text-gray-300 leading-relaxed mb-8">
                    We believe in the power of personal connections. While we offer full digital services, our office in Ludhiana is always open for consultations, document signing, or simply a friendly conversation about your financial goals.
                  </p>
                  
                  <div className="space-y-4">
                    <div className="flex items-start space-x-4">
                      <MapPin className="w-6 h-6 text-primary-400 mt-1 flex-shrink-0" />
                      <div>
                        <h3 className="font-semibold mb-1">Address</h3>
                        <p className="text-gray-300">
                          ElevateWealthServices<br />
                          Ludhiana, Punjab<br />
                          India - 141001
                        </p>
                      </div>
                    </div>

                    <div className="flex items-start space-x-4">
                      <Clock className="w-6 h-6 text-primary-400 mt-1 flex-shrink-0" />
                      <div>
                        <h3 className="font-semibold mb-1">Office Hours</h3>
                        <p className="text-gray-300">
                          Monday - Friday: 9:30 AM - 6:30 PM<br />
                          Saturday: 10:00 AM - 4:00 PM<br />
                          Sunday: Closed
                        </p>
                      </div>
                    </div>

                    <div className="flex items-start space-x-4">
                      <Phone className="w-6 h-6 text-primary-400 mt-1 flex-shrink-0" />
                      <div>
                        <h3 className="font-semibold mb-1">Contact</h3>
                        <p className="text-gray-300">
                          +91 98765 43210<br />
                          info@elevatewealthservices.com
                        </p>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="bg-white/10 backdrop-blur-lg rounded-2xl p-8">
                  <h3 className="text-2xl font-bold mb-6">Our Commitment to You</h3>
                  <div className="space-y-4 text-gray-300">
                    <p className="flex items-start">
                      <span className="text-2xl mr-3">🤝</span>
                      <span>Always putting your financial interests first</span>
                    </p>
                    <p className="flex items-start">
                      <span className="text-2xl mr-3">🔒</span>
                      <span>Maintaining complete confidentiality of your financial data</span>
                    </p>
                    <p className="flex items-start">
                      <span className="text-2xl mr-3">📊</span>
                      <span>Providing honest, unbiased, research-backed advice</span>
                    </p>
                    <p className="flex items-start">
                      <span className="text-2xl mr-3">⚡</span>
                      <span>Responding promptly to your queries and concerns</span>
                    </p>
                    <p className="flex items-start">
                      <span className="text-2xl mr-3">📈</span>
                      <span>Continuously working to help you achieve your goals</span>
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </AnimatedSection>
        </div>
      </section>
    </div>
  )
}
