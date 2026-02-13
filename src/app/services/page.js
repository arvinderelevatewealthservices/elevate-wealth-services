'use client'

import AnimatedSection from '@/components/AnimatedSection'
import Link from 'next/link'
import { 
  TrendingUp, 
  Shield, 
  BarChart3, 
  Target, 
  Heart, 
  Car, 
  Home, 
  Zap,
  CheckCircle2,
  ArrowRight,
  PieChart,
  Calculator,
  FileText,
  Phone,
  AlertCircle
} from 'lucide-react'

export default function ServicesPage() {
  return (
    <div className="pt-20">
      {/* Hero Section */}
      <section className="py-20 bg-gradient-to-br from-primary-50 via-blue-50 to-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <AnimatedSection>
            <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
              Our Services
            </h1>
            <p className="text-xl text-gray-600 leading-relaxed">
              Comprehensive financial solutions tailored to your unique needs—from wealth building to complete risk protection
            </p>
          </AnimatedSection>
        </div>
      </section>

      {/* Mutual Funds Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-16">
            <AnimatedSection>
              <div className="bg-gradient-to-br from-blue-500 to-blue-700 rounded-2xl p-12 text-white shadow-2xl">
                <TrendingUp className="w-16 h-16 mb-6" />
                <h2 className="text-4xl font-bold mb-4">
                  Mutual Fund Advisory
                </h2>
                <p className="text-blue-100 text-lg mb-6">
                  Build long-term wealth through systematic, disciplined investing
                </p>
                <div className="bg-white/20 backdrop-blur-sm rounded-lg p-4">
                  <p className="text-sm">
                    <strong>AMFI Registered Distributor</strong><br />
                    Professional guidance backed by regulatory compliance
                  </p>
                </div>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="space-y-6">
                <div>
                  <h3 className="text-3xl font-bold text-gray-900 mb-4">
                    What We Offer
                  </h3>
                  <p className="text-gray-600 leading-relaxed text-lg mb-6">
                    As AMFI-registered Mutual Fund Distributors, we help investors build diversified portfolios aligned with their financial goals, risk appetite, and investment horizon. Whether you're saving for retirement, your child's education, or wealth creation—we design strategies that work.
                  </p>
                </div>

                <div className="bg-blue-50 rounded-xl p-6">
                  <h4 className="text-xl font-bold text-gray-900 mb-4 flex items-center">
                    <PieChart className="w-6 h-6 text-blue-600 mr-3" />
                    Investment Categories We Cover
                  </h4>
                  <div className="grid grid-cols-2 gap-3">
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">Equity Funds</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">Debt Funds</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">Hybrid Funds</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">ELSS (Tax Saving)</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">Index Funds</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-blue-600" />
                      <span className="text-gray-700">Liquid Funds</span>
                    </div>
                  </div>
                </div>
              </div>
            </AnimatedSection>
          </div>

          {/* Mutual Fund Details */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            <AnimatedSection>
              <div className="bg-gradient-to-br from-gray-50 to-white rounded-xl p-8 border border-gray-200 h-full">
                <h4 className="text-xl font-bold text-gray-900 mb-4">Key Features & Benefits</h4>
                <ul className="space-y-3">
                  {[
                    'Goal-based investment planning (retirement, education, home, wealth)',
                    'Personalized portfolio construction based on detailed risk profiling',
                    'SIP (Systematic Investment Plan) setup starting from ₹500/month',
                    'Portfolio diversification across asset classes and fund houses',
                    'Regular performance monitoring with quarterly reviews',
                    'Tax-efficient investment strategies and ELSS recommendations',
                    'Access to top-performing funds from leading AMCs',
                    'Paperless onboarding with instant account activation',
                  ].map((feature, index) => (
                    <li key={index} className="flex items-start space-x-3">
                      <CheckCircle2 className="w-5 h-5 text-green-600 mt-0.5 flex-shrink-0" />
                      <span className="text-gray-700">{feature}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="space-y-6">
                <div className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl p-8 border border-blue-200">
                  <h4 className="text-xl font-bold text-gray-900 mb-3 flex items-center">
                    <Target className="w-6 h-6 text-blue-600 mr-3" />
                    Who Should Invest?
                  </h4>
                  <ul className="space-y-2 text-gray-700">
                    <li>• First-time investors looking to start their wealth journey</li>
                    <li>• Salaried professionals seeking disciplined savings</li>
                    <li>• Parents planning for children's education expenses</li>
                    <li>• Individuals building retirement corpus</li>
                    <li>• Anyone looking for tax-saving investments under 80C</li>
                    <li>• Investors seeking professional portfolio management</li>
                  </ul>
                </div>

                <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-xl p-8 border border-green-200">
                  <h4 className="text-xl font-bold text-gray-900 mb-3 flex items-center">
                    <Calculator className="w-6 h-6 text-green-600 mr-3" />
                    Investment Options
                  </h4>
                  <div className="space-y-3 text-gray-700">
                    <p><strong>SIP (Systematic Investment Plan):</strong> Start with ₹500/month</p>
                    <p><strong>Lumpsum Investment:</strong> Minimum ₹5,000 (varies by fund)</p>
                    <p><strong>Step-Up SIP:</strong> Increase SIP amount annually</p>
                    <p><strong>Flexible Withdrawal:</strong> Redeem anytime (subject to exit loads)</p>
                  </div>
                </div>
              </div>
            </AnimatedSection>
          </div>

          <AnimatedSection>
            <div className="bg-yellow-50 border-l-4 border-yellow-400 p-6 rounded-lg mb-8">
              <div className="flex items-start">
                <AlertCircle className="w-6 h-6 text-yellow-600 mr-3 mt-0.5 flex-shrink-0" />
                <div>
                  <p className="text-sm text-gray-700 leading-relaxed">
                    <strong className="text-gray-900">Mutual Fund Disclaimer:</strong> Mutual Fund investments are subject to market risks. Read all scheme-related documents carefully before investing. Past performance is not indicative of future returns. The NAV of the scheme may go up or down depending upon the factors and forces affecting securities market. ElevateWealthServices is an AMFI-registered Mutual Fund Distributor (ARN: [Your ARN]). We earn commissions on Regular Plan investments sold.
                  </p>
                </div>
              </div>
            </div>
          </AnimatedSection>

          <AnimatedSection>
            <div className="text-center">
              <Link
                href="/contact"
                className="inline-flex items-center space-x-2 bg-gradient-to-r from-blue-600 to-blue-700 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition-all hover:scale-105"
              >
                <span>Start Investing in Mutual Funds</span>
                <ArrowRight className="w-5 h-5" />
              </Link>
            </div>
          </AnimatedSection>
        </div>
      </section>

      {/* Insurance Section */}
      <section className="py-20 bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-16">
            <AnimatedSection>
              <div className="space-y-6 order-2 lg:order-1">
                <div>
                  <h2 className="text-4xl font-bold text-gray-900 mb-4">
                    Insurance Solutions
                  </h2>
                  <p className="text-gray-600 leading-relaxed text-lg mb-6">
                    Comprehensive protection plans for you and your loved ones. We help you choose the right insurance coverage to safeguard against life's uncertainties and secure your family's financial future.
                  </p>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-6">
                  <div className="bg-white rounded-xl p-6 shadow-md text-center hover:shadow-lg transition-all">
                    <Heart className="w-10 h-10 text-green-600 mx-auto mb-3" />
                    <h5 className="font-bold text-gray-900 mb-1">Life Insurance</h5>
                    <p className="text-sm text-gray-600">Financial security for your family</p>
                  </div>
                  <div className="bg-white rounded-xl p-6 shadow-md text-center hover:shadow-lg transition-all">
                    <Shield className="w-10 h-10 text-blue-600 mx-auto mb-3" />
                    <h5 className="font-bold text-gray-900 mb-1">Health Insurance</h5>
                    <p className="text-sm text-gray-600">Medical expense coverage</p>
                  </div>
                  <div className="bg-white rounded-xl p-6 shadow-md text-center hover:shadow-lg transition-all">
                    <Car className="w-10 h-10 text-purple-600 mx-auto mb-3" />
                    <h5 className="font-bold text-gray-900 mb-1">General Insurance</h5>
                    <p className="text-sm text-gray-600">Asset protection plans</p>
                  </div>
                </div>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-gradient-to-br from-green-500 to-emerald-700 rounded-2xl p-12 text-white order-1 lg:order-2 shadow-2xl">
                <Shield className="w-16 h-16 mb-6" />
                <h3 className="text-3xl font-bold mb-4">
                  Protection You Can Trust
                </h3>
                <p className="text-green-100 text-lg mb-6">
                  Secure your family's future with comprehensive insurance coverage tailored to your needs
                </p>
                <div className="space-y-3">
                  <div className="flex items-center space-x-3 bg-white/20 backdrop-blur-sm rounded-lg p-3">
                    <Home className="w-5 h-5" />
                    <span>Property & Asset Protection</span>
                  </div>
                  <div className="flex items-center space-x-3 bg-white/20 backdrop-blur-sm rounded-lg p-3">
                    <Heart className="w-5 h-5" />
                    <span>Health & Wellness Coverage</span>
                  </div>
                  <div className="flex items-center space-x-3 bg-white/20 backdrop-blur-sm rounded-lg p-3">
                    <Shield className="w-5 h-5" />
                    <span>Life & Income Security</span>
                  </div>
                </div>
              </div>
            </AnimatedSection>
          </div>

          {/* Insurance Details */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
            <AnimatedSection>
              <div className="bg-white rounded-xl p-8 shadow-lg h-full">
                <Heart className="w-12 h-12 text-red-600 mb-4" />
                <h4 className="text-2xl font-bold text-gray-900 mb-4">Life Insurance</h4>
                <ul className="space-y-3 text-gray-700">
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Term Plans:</strong> Pure protection at affordable premiums</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Endowment Policies:</strong> Savings + insurance</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>ULIPs:</strong> Market-linked investment + insurance</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Retirement Plans:</strong> Pension and annuity options</span>
                  </li>
                </ul>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-xl p-8 shadow-lg h-full">
                <Shield className="w-12 h-12 text-blue-600 mb-4" />
                <h4 className="text-2xl font-bold text-gray-900 mb-4">Health Insurance</h4>
                <ul className="space-y-3 text-gray-700">
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Individual Plans:</strong> Personal health coverage</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Family Floater:</strong> Coverage for entire family</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Critical Illness:</strong> Lump sum for major diseases</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Senior Citizen Plans:</strong> Specialized elderly coverage</span>
                  </li>
                </ul>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="bg-white rounded-xl p-8 shadow-lg h-full">
                <Car className="w-12 h-12 text-purple-600 mb-4" />
                <h4 className="text-2xl font-bold text-gray-900 mb-4">General Insurance</h4>
                <ul className="space-y-3 text-gray-700">
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Motor Insurance:</strong> Car and bike coverage</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Home Insurance:</strong> Property and contents protection</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Travel Insurance:</strong> International trip coverage</span>
                  </li>
                  <li className="flex items-start">
                    <CheckCircle2 className="w-5 h-5 text-green-600 mr-2 mt-0.5 flex-shrink-0" />
                    <span><strong>Personal Accident:</strong> Accidental death/disability cover</span>
                  </li>
                </ul>
              </div>
            </AnimatedSection>
          </div>

          <AnimatedSection>
            <div className="bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl p-8 mb-8">
              <h4 className="text-2xl font-bold text-gray-900 mb-6 flex items-center">
                <FileText className="w-7 h-7 text-green-600 mr-3" />
                Our Insurance Process
              </h4>
              <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div>
                  <div className="bg-white rounded-lg p-4 text-center shadow-md">
                    <div className="text-2xl font-bold text-green-600 mb-2">1</div>
                    <h5 className="font-semibold text-gray-900 mb-2">Needs Analysis</h5>
                    <p className="text-sm text-gray-600">Assess coverage requirements and identify gaps</p>
                  </div>
                </div>
                <div>
                  <div className="bg-white rounded-lg p-4 text-center shadow-md">
                    <div className="text-2xl font-bold text-green-600 mb-2">2</div>
                    <h5 className="font-semibold text-gray-900 mb-2">Policy Comparison</h5>
                    <p className="text-sm text-gray-600">Compare quotes from multiple insurers</p>
                  </div>
                </div>
                <div>
                  <div className="bg-white rounded-lg p-4 text-center shadow-md">
                    <div className="text-2xl font-bold text-green-600 mb-2">3</div>
                    <h5 className="font-semibold text-gray-900 mb-2">Easy Purchase</h5>
                    <p className="text-sm text-gray-600">Hassle-free online/offline policy issuance</p>
                  </div>
                </div>
                <div>
                  <div className="bg-white rounded-lg p-4 text-center shadow-md">
                    <div className="text-2xl font-bold text-green-600 mb-2">4</div>
                    <h5 className="font-semibold text-gray-900 mb-2">Claims Support</h5>
                    <p className="text-sm text-gray-600">End-to-end assistance until settlement</p>
                  </div>
                </div>
              </div>
            </div>
          </AnimatedSection>

          <AnimatedSection>
            <div className="bg-blue-50 border-l-4 border-blue-400 p-6 rounded-lg mb-8">
              <div className="flex items-start">
                <AlertCircle className="w-6 h-6 text-blue-600 mr-3 mt-0.5 flex-shrink-0" />
                <div>
                  <p className="text-sm text-gray-700 leading-relaxed">
                    <strong className="text-gray-900">Insurance Disclaimer:</strong> Insurance is the subject matter of solicitation. For more details on risk factors, terms, and conditions, please read the sales brochure/policy wording carefully before concluding a sale. ElevateWealthServices is a registered insurance intermediary/broker (License: [Your License No.]). Proposals are subject to underwriting and acceptance by the insurance company.
                  </p>
                </div>
              </div>
            </div>
          </AnimatedSection>

          <AnimatedSection>
            <div className="text-center">
              <Link
                href="/contact"
                className="inline-flex items-center space-x-2 bg-gradient-to-r from-green-600 to-emerald-700 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition-all hover:scale-105"
              >
                <span>Get Insurance Quote</span>
                <ArrowRight className="w-5 h-5" />
              </Link>
            </div>
          </AnimatedSection>
        </div>
      </section>

      {/* Trading & Brokerage Section */}
      <section className="py-20 bg-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center mb-16">
            <AnimatedSection>
              <div className="bg-gradient-to-br from-purple-500 to-indigo-700 rounded-2xl p-12 text-white shadow-2xl">
                <BarChart3 className="w-16 h-16 mb-6" />
                <h2 className="text-4xl font-bold mb-4">
                  Trading & Brokerage
                </h2>
                <p className="text-purple-100 text-lg mb-6">
                  Execute trades efficiently with expert guidance and advanced platforms
                </p>
                <div className="bg-white/20 backdrop-blur-sm rounded-lg p-4">
                  <p className="text-sm">
                    <strong>SEBI-Regulated Services</strong><br />
                    Partnered with leading brokerage platforms
                  </p>
                </div>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="space-y-6">
                <div>
                  <h3 className="text-3xl font-bold text-gray-900 mb-4">
                    For Active Traders & Investors
                  </h3>
                  <p className="text-gray-600 leading-relaxed text-lg mb-6">
                    Partner with us for seamless trading execution backed by professional advisory support. Whether you're a day trader, swing trader, or long-term investor—we provide the platforms, insights, and guidance you need to make informed decisions.
                  </p>
                </div>

                <div className="bg-purple-50 rounded-xl p-6">
                  <h4 className="text-xl font-bold text-gray-900 mb-4">Trading Segments</h4>
                  <div className="grid grid-cols-2 gap-3">
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-purple-600" />
                      <span className="text-gray-700">Equity Cash</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-purple-600" />
                      <span className="text-gray-700">Intraday</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-purple-600" />
                      <span className="text-gray-700">Futures & Options</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-purple-600" />
                      <span className="text-gray-700">Currency Trading</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-purple-600" />
                      <span className="text-gray-700">Commodities</span>
                    </div>
                    <div className="flex items-center space-x-2">
                      <CheckCircle2 className="w-5 h-5 text-purple-600" />
                      <span className="text-gray-700">IPO Applications</span>
                    </div>
                  </div>
                </div>
              </div>
            </AnimatedSection>
          </div>

          {/* Trading Details */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
            <AnimatedSection>
              <div className="bg-gradient-to-br from-gray-50 to-white rounded-xl p-8 border border-gray-200 h-full">
                <h4 className="text-xl font-bold text-gray-900 mb-4">Platform Features</h4>
                <ul className="space-y-3">
                  {[
                    'Advanced trading platforms (web, mobile, desktop)',
                    'Real-time market data and live streaming quotes',
                    'Advanced charting tools with 100+ indicators',
                    'Pre-market and after-market analysis',
                    'Research reports and stock recommendations',
                    'Option chain analysis and strategy builder',
                    'Portfolio tracking and P&L statements',
                    'Fast order execution with multiple order types',
                  ].map((feature, index) => (
                    <li key={index} className="flex items-start space-x-3">
                      <CheckCircle2 className="w-5 h-5 text-green-600 mt-0.5 flex-shrink-0" />
                      <span className="text-gray-700">{feature}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </AnimatedSection>

            <AnimatedSection>
              <div className="space-y-6">
                <div className="bg-gradient-to-br from-purple-50 to-indigo-50 rounded-xl p-8 border border-purple-200">
                  <h4 className="text-xl font-bold text-gray-900 mb-3 flex items-center">
                    <Zap className="w-6 h-6 text-purple-600 mr-3" />
                    Our Advisory Support
                  </h4>
                  <ul className="space-y-2 text-gray-700">
                    <li>• Daily market analysis and outlook</li>
                    <li>• Stock-specific buy/sell recommendations</li>
                    <li>• Technical and fundamental research</li>
                    <li>• Risk management strategies</li>
                    <li>• Portfolio diversification guidance</li>
                    <li>• Entry/exit level suggestions</li>
                  </ul>
                </div>

                <div className="bg-gradient-to-br from-orange-50 to-red-50 rounded-xl p-8 border border-orange-200">
                  <h4 className="text-xl font-bold text-gray-900 mb-3 flex items-center">
                    <Target className="w-6 h-6 text-orange-600 mr-3" />
                    Who Should Trade?
                  </h4>
                  <ul className="space-y-2 text-gray-700">
                    <li>• Active traders seeking regular income</li>
                    <li>• Investors with market knowledge</li>
                    <li>• Those who can dedicate time to markets</li>
                    <li>• Risk-takers with capital allocation skills</li>
                  </ul>
                </div>
              </div>
            </AnimatedSection>
          </div>

          <AnimatedSection>
            <div className="bg-red-50 border-l-4 border-red-400 p-6 rounded-lg mb-8">
              <div className="flex items-start">
                <AlertCircle className="w-6 h-6 text-red-600 mr-3 mt-0.5 flex-shrink-0" />
                <div>
                  <p className="text-sm text-gray-700 leading-relaxed">
                    <strong className="text-gray-900">Trading Disclaimer:</strong> Trading in securities markets carries inherent risks including the risk of loss of capital. Investors should carefully consider their risk appetite and financial situation before trading. Past performance is not indicative of future results. Services provided in partnership with SEBI-registered brokers. ElevateWealthServices provides advisory support but investment decisions are solely yours.
                  </p>
                </div>
              </div>
            </div>
          </AnimatedSection>

          <AnimatedSection>
            <div className="text-center">
              <Link
                href="/contact"
                className="inline-flex items-center space-x-2 bg-gradient-to-r from-purple-600 to-indigo-700 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:shadow-lg transition-all hover:scale-105"
              >
                <span>Open Trading Account</span>
                <ArrowRight className="w-5 h-5" />
              </Link>
            </div>
          </AnimatedSection>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-br from-gray-900 to-gray-800 text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <AnimatedSection>
            <Phone className="w-16 h-16 mx-auto mb-6 text-primary-400" />
            <h2 className="text-3xl md:text-4xl font-bold mb-6">
              Not Sure Which Service Is Right for You?
            </h2>
            <p className="text-xl text-gray-300 mb-8">
              Book a free consultation and let our experts help you design a personalized financial strategy based on your unique goals and circumstances.
            </p>
            <Link
              href="/contact"
              className="inline-flex items-center space-x-2 bg-white text-gray-900 px-8 py-4 rounded-xl font-semibold text-lg hover:bg-gray-100 transition-all hover:scale-105 shadow-xl"
            >
              <span>Schedule Free Consultation</span>
              <ArrowRight className="w-5 h-5" />
            </Link>
          </AnimatedSection>
        </div>
      </section>
    </div>
  )
}
