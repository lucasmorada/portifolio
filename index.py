"use client"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import {
  Github,
  Linkedin,
  Mail,
  ExternalLink,
  Code2,
  Globe,
  MapPin,
  Calendar,
  Star,
  Quote,
  Terminal,
  Braces,
  Coffee,
} from "lucide-react"
import Image from "next/image"
import Link from "next/link"

export default function Portfolio() {
  const skills = [
    "React",
    "Next.js",
    "TypeScript",
    "Node.js",
    "Python",
    "PostgreSQL",
    "MongoDB",
    "AWS",
    "Docker",
    "Kubernetes",
    "GraphQL",
    "REST APIs",
    "Tailwind CSS",
    "React Native",
    "Vue.js",
    "Express.js",
    "Django",
    "Redis",
  ]

  const projects = [
    {
      title: "E-commerce Platform",
      description:
        "Plataforma completa de e-commerce com pagamentos integrados, dashboard administrativo e sistema de inventário.",
      tech: ["Next.js", "Stripe", "PostgreSQL", "Prisma"],
      image: "/placeholder.svg?height=200&width=300",
      link: "#",
      github: "#",
    },
    {
      title: "SaaS Analytics Dashboard",
      description:
        "Dashboard de analytics em tempo real para empresas SaaS com métricas avançadas e relatórios customizáveis.",
      tech: ["React", "D3.js", "Node.js", "MongoDB"],
      image: "/placeholder.svg?height=200&width=300",
      link: "#",
      github: "#",
    },
    {
      title: "Mobile Banking App",
      description: "Aplicativo bancário mobile com autenticação biométrica, transferências e controle financeiro.",
      tech: ["React Native", "Firebase", "Redux", "Expo"],
      image: "/placeholder.svg?height=200&width=300",
      link: "#",
      github: "#",
    },
    {
      title: "AI Content Generator",
      description:
        "Plataforma de geração de conteúdo usando IA, com templates personalizáveis e integração com redes sociais.",
      tech: ["Python", "OpenAI API", "FastAPI", "React"],
      image: "/placeholder.svg?height=200&width=300",
      link: "#",
      github: "#",
    },
  ]

  const testimonials = [
    {
      name: "Maria Silva",
      role: "CEO, TechStart",
      content:
        "Trabalhar com ele foi incrível. Entregou o projeto antes do prazo e superou todas as expectativas. Recomendo 100%!",
      avatar: "/placeholder.svg?height=60&width=60",
    },
    {
      name: "John Anderson",
      role: "CTO, GlobalTech",
      content:
        "Exceptional developer with great problem-solving skills. His full-stack expertise helped us scale our platform efficiently.",
      avatar: "/placeholder.svg?height=60&width=60",
    },
    {
      name: "Carlos Rodriguez",
      role: "Product Manager, InnovaCorp",
      content:
        "Profissional extremamente dedicado e técnico. Conseguiu resolver problemas complexos que outros desenvolvedores não conseguiram.",
      avatar: "/placeholder.svg?height=60&width=60",
    },
  ]

  const experiences = [
    {
      country: "Estados Unidos",
      city: "San Francisco",
      period: "2023 - 2024",
      role: "Senior Full Stack Developer",
      company: "Tech Unicorn Inc.",
      description:
        "Liderou o desenvolvimento de features críticas para uma startup unicórnio, trabalhando com tecnologias de ponta.",
      flag: "🇺🇸",
    },
    {
      country: "Alemanha",
      city: "Berlin",
      period: "2022 - 2023",
      role: "Full Stack Developer",
      company: "European FinTech",
      description: "Desenvolveu soluções fintech para o mercado europeu, focando em compliance e segurança.",
      flag: "🇩🇪",
    },
    {
      country: "Canadá",
      city: "Toronto",
      period: "2021 - 2022",
      role: "Software Engineer",
      company: "Maple Tech Solutions",
      description:
        "Trabalhou em projetos de grande escala para clientes enterprise, utilizando arquiteturas distribuídas.",
      flag: "🇨🇦",
    },
  ]

  return (
    <div className="min-h-screen bg-background">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-14 items-center">
          <div className="mr-4 flex">
            <Link href="/" className="mr-6 flex items-center space-x-2">
              <Terminal className="h-6 w-6" />
              <span className="font-bold">DevPortfolio</span>
            </Link>
          </div>
          <nav className="flex items-center space-x-6 text-sm font-medium">
            <Link href="#about" className="transition-colors hover:text-foreground/80">
              Sobre
            </Link>
            <Link href="#skills" className="transition-colors hover:text-foreground/80">
              Skills
            </Link>
            <Link href="#portfolio" className="transition-colors hover:text-foreground/80">
              Portfólio
            </Link>
            <Link href="#experience" className="transition-colors hover:text-foreground/80">
              Experiência
            </Link>
            <Link href="#testimonials" className="transition-colors hover:text-foreground/80">
              Depoimentos
            </Link>
          </nav>
          <div className="flex flex-1 items-center justify-end space-x-2">
            <Button variant="ghost" size="icon">
              <Github className="h-4 w-4" />
            </Button>
            <Button variant="ghost" size="icon">
              <Linkedin className="h-4 w-4" />
            </Button>
            <Button size="sm">
              <Mail className="mr-2 h-4 w-4" />
              Contato
            </Button>
          </div>
        </div>
      </header>

      {/* Hero Section */}
      <section className="container py-24 md:py-32">
        <div className="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
          <div className="flex flex-col justify-center space-y-4">
            <div className="space-y-2">
              <div className="inline-block rounded-lg bg-muted px-3 py-1 text-sm font-mono">
                {'> console.log("Hello World!")'}
              </div>
              <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none">
                Full Stack Developer
                <br />
                <span className="text-primary">& Code Architect</span>
              </h1>
              <p className="max-w-[600px] text-muted-foreground md:text-xl">
                Transformo ideias em código e código em soluções reais. Especialista em desenvolvimento full stack com
                experiência internacional e paixão por criar produtos que fazem a diferença.
              </p>
            </div>
            <div className="flex flex-col gap-2 min-[400px]:flex-row">
              <Button size="lg" className="gap-2">
                <Code2 className="h-4 w-4" />
                Ver Projetos
              </Button>
              <Button variant="outline" size="lg" className="gap-2 bg-transparent">
                <Coffee className="h-4 w-4" />
                Vamos conversar
              </Button>
            </div>
            <div className="flex items-center space-x-4 text-sm text-muted-foreground">
              <div className="flex items-center space-x-1">
                <MapPin className="h-4 w-4" />
                <span>São Paulo, Brasil</span>
              </div>
              <div className="flex items-center space-x-1">
                <Globe className="h-4 w-4" />
                <span>Disponível globalmente</span>
              </div>
            </div>
          </div>
          <div className="flex items-center justify-center">
            <div className="relative">
              <div className="absolute inset-0 bg-gradient-to-r from-primary/20 to-secondary/20 rounded-full blur-3xl"></div>
              <Image
                src="/placeholder.svg?height=400&width=400"
                width={400}
                height={400}
                alt="Foto do desenvolvedor"
                className="relative rounded-full border-4 border-background shadow-2xl"
              />
              <div className="absolute -bottom-4 -right-4 bg-primary text-primary-foreground rounded-full p-3">
                <Braces className="h-6 w-6" />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="container py-24 bg-muted/50">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Sobre Mim</h2>
          <p className="mt-4 text-muted-foreground md:text-xl">Desenvolvedor apaixonado por tecnologia e inovação</p>
        </div>
        <div className="mx-auto mt-16 max-w-4xl">
          <div className="grid gap-8 md:grid-cols-2">
            <div className="space-y-4">
              <h3 className="text-2xl font-bold">Minha Jornada</h3>
              <p className="text-muted-foreground">
                Comecei minha jornada na programação há mais de 8 anos, sempre buscando aprender novas tecnologias e
                resolver problemas complexos. Minha experiência internacional me deu uma perspectiva única sobre
                desenvolvimento de software e trabalho em equipe.
              </p>
              <p className="text-muted-foreground">
                Especializo-me em criar soluções full stack robustas, desde APIs escaláveis até interfaces de usuário
                intuitivas. Acredito que bom código é aquele que resolve problemas reais de forma elegante e eficiente.
              </p>
            </div>
            <div className="space-y-4">
              <h3 className="text-2xl font-bold">Filosofia de Trabalho</h3>
              <div className="space-y-3">
                <div className="flex items-start space-x-3">
                  <div className="mt-1 h-2 w-2 rounded-full bg-primary"></div>
                  <p className="text-sm text-muted-foreground">
                    <strong>Clean Code:</strong> Código limpo e bem documentado é fundamental
                  </p>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="mt-1 h-2 w-2 rounded-full bg-primary"></div>
                  <p className="text-sm text-muted-foreground">
                    <strong>User First:</strong> Sempre penso na experiência do usuário final
                  </p>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="mt-1 h-2 w-2 rounded-full bg-primary"></div>
                  <p className="text-sm text-muted-foreground">
                    <strong>Continuous Learning:</strong> Tecnologia evolui, eu evoluo junto
                  </p>
                </div>
                <div className="flex items-start space-x-3">
                  <div className="mt-1 h-2 w-2 rounded-full bg-primary"></div>
                  <p className="text-sm text-muted-foreground">
                    <strong>Team Player:</strong> Acredito no poder da colaboração
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="container py-24">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Tech Stack</h2>
          <p className="mt-4 text-muted-foreground md:text-xl">Tecnologias que domino e uso no dia a dia</p>
        </div>
        <div className="mx-auto mt-16 max-w-4xl">
          <div className="flex flex-wrap gap-3 justify-center">
            {skills.map((skill, index) => (
              <Badge key={index} variant="secondary" className="px-4 py-2 text-sm font-mono">
                {skill}
              </Badge>
            ))}
          </div>
        </div>
      </section>

      {/* Portfolio Section */}
      <section id="portfolio" className="container py-24 bg-muted/50">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Meus Projetos</h2>
          <p className="mt-4 text-muted-foreground md:text-xl">
            Alguns dos projetos que desenvolvi e que mais me orgulho
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-6xl">
          <div className="grid gap-8 md:grid-cols-2">
            {projects.map((project, index) => (
              <Card key={index} className="overflow-hidden">
                <div className="aspect-video relative">
                  <Image src={project.image || "/placeholder.svg"} alt={project.title} fill className="object-cover" />
                </div>
                <CardHeader>
                  <CardTitle className="flex items-center justify-between">
                    {project.title}
                    <div className="flex space-x-2">
                      <Button size="icon" variant="ghost">
                        <ExternalLink className="h-4 w-4" />
                      </Button>
                      <Button size="icon" variant="ghost">
                        <Github className="h-4 w-4" />
                      </Button>
                    </div>
                  </CardTitle>
                  <CardDescription>{project.description}</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="flex flex-wrap gap-2">
                    {project.tech.map((tech, techIndex) => (
                      <Badge key={techIndex} variant="outline" className="text-xs">
                        {tech}
                      </Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* International Experience */}
      <section id="experience" className="container py-24">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Experiência Internacional</h2>
          <p className="mt-4 text-muted-foreground md:text-xl">
            Trabalhei em diferentes países, absorvendo culturas e metodologias diversas
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-4xl">
          <div className="space-y-8">
            {experiences.map((exp, index) => (
              <Card key={index} className="p-6">
                <div className="flex items-start space-x-4">
                  <div className="text-4xl">{exp.flag}</div>
                  <div className="flex-1">
                    <div className="flex items-center justify-between">
                      <h3 className="text-xl font-bold">{exp.role}</h3>
                      <Badge variant="outline" className="flex items-center space-x-1">
                        <Calendar className="h-3 w-3" />
                        <span>{exp.period}</span>
                      </Badge>
                    </div>
                    <p className="text-primary font-semibold">{exp.company}</p>
                    <p className="text-sm text-muted-foreground flex items-center space-x-1 mt-1">
                      <MapPin className="h-3 w-3" />
                      <span>
                        {exp.city}, {exp.country}
                      </span>
                    </p>
                    <p className="mt-3 text-muted-foreground">{exp.description}</p>
                  </div>
                </div>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section id="testimonials" className="container py-24 bg-muted/50">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">O que dizem sobre mim</h2>
          <p className="mt-4 text-muted-foreground md:text-xl">Depoimentos de clientes e colegas de trabalho</p>
        </div>
        <div className="mx-auto mt-16 max-w-6xl">
          <div className="grid gap-8 md:grid-cols-3">
            {testimonials.map((testimonial, index) => (
              <Card key={index} className="p-6">
                <CardContent className="space-y-4 p-0">
                  <Quote className="h-8 w-8 text-primary" />
                  <p className="text-muted-foreground italic">"{testimonial.content}"</p>
                  <div className="flex items-center space-x-3">
                    <Image
                      src={testimonial.avatar || "/placeholder.svg"}
                      alt={testimonial.name}
                      width={40}
                      height={40}
                      className="rounded-full"
                    />
                    <div>
                      <p className="font-semibold">{testimonial.name}</p>
                      <p className="text-sm text-muted-foreground">{testimonial.role}</p>
                    </div>
                  </div>
                  <div className="flex space-x-1">
                    {[...Array(5)].map((_, i) => (
                      <Star key={i} className="h-4 w-4 fill-primary text-primary" />
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="container py-24">
        <div className="mx-auto max-w-3xl text-center">
          <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">Vamos trabalhar juntos?</h2>
          <p className="mt-4 text-muted-foreground md:text-xl">
            Estou sempre aberto a novos desafios e oportunidades interessantes
          </p>
          <div className="mt-8 flex flex-col gap-4 sm:flex-row sm:justify-center">
            <Button size="lg" className="gap-2">
              <Mail className="h-4 w-4" />
              Entre em contato
            </Button>
            <Button variant="outline" size="lg" className="gap-2 bg-transparent">
              <Github className="h-4 w-4" />
              Ver no GitHub
            </Button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t bg-muted/50">
        <div className="container py-8">
          <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
            <div className="flex items-center space-x-2">
              <Terminal className="h-5 w-5" />
              <span className="font-bold">DevPortfolio</span>
            </div>
            <p className="text-sm text-muted-foreground">© 2024 Desenvolvido com ❤️ e muito ☕</p>
            <div className="flex space-x-4">
              <Button variant="ghost" size="icon">
                <Github className="h-4 w-4" />
              </Button>
              <Button variant="ghost" size="icon">
                <Linkedin className="h-4 w-4" />
              </Button>
              <Button variant="ghost" size="icon">
                <Mail className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}
