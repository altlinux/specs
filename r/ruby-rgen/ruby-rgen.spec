%define        pkgname rgen

Name:          ruby-%pkgname
Version:       0.8.4
Release:       alt2
Summary:       Ruby Modelling and Generator Framework
Group:         Development/Ruby
License:       MIT/
URL:           https://github.com/mthiede/rgen
# VCS:         https://github.com/mthiede/rgen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch
Source:        %pkgname-%version.tar

BuildRequires(pre): rpm-build-ruby

%description
RGen is a framework for Model Driven Software Development (MDSD)in Ruby.
This means that it helps you build Metamodels, instantiate Models,
modify and transform Models and finally generate arbitrary textual
content from it.

RGen features include:
* Supporting Ruby 1.8.6, 1.8.7 and 1.9.x
* Metamodel definition language (internal Ruby DSL)
* ECore Meta-metamodel with an ECore instance available for every
  Metamodel
* Generator creating the Ruby metamodel definition from an ECore
  instance
* Transformer creating Ruby metamodel classes/modules from an ECore
  instance
* Instantiation of Metamodels, i.e. creation of Models (e.g. from XML)
* Model builder, internal Ruby DSL
* Model fragmentation over several several files and per-fragment
  caching
* Model Transformation language (internal Ruby DSL)
* Powerful template based generator language (internal Ruby DSL inside
  of ERB)
* UML 1.3 metamodel and XMI 1.1 instantiator included
* ECore XML support (XMI 2.0)
* UML-to-ECore and ECore-to-UML transformation (UML class models)
* Enterprise Architect support (UML1.3/XMI1.1)

%package       doc
Summary:       Documentation for %name
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation for %{name}.

%prep
%setup -n %pkgname-%version

%build
%gem_build

%install
%gem_install

%check
%gem_test

%files
%ruby_gemspec
%ruby_gemlibdir/*

%files         doc
%ruby_gemdocdir/*

%changelog
* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.4-alt2
- Use Ruby Policy 2.0.

* Thu Nov 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.8.4-alt1
- Bump gemified to 0.8.4.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for ALT Linux
