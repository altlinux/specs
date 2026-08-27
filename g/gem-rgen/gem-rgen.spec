%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rgen

Name:          gem-rgen
Version:       0.10.2
Release:       alt1
Summary:       Ruby Modelling and Generator Framework
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mthiede/rgen
Vcs:           https://github.com/mthiede/rgen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(andand) >= 1.3.3
BuildRequires: gem(minitest) >= 5.20.0
BuildRequires: gem(minitest-fail-fast) >= 0.1.0
BuildRequires: gem(nokogiri) >= 1.15.4
BuildRequires: gem(rake) >= 13.0.0
BuildConflicts: gem(andand) >= 1.4
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-fail-fast) >= 1
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency nokogiri >= 1.16,nokogiri < 2
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
%ruby_use_gem_dependency minitest-fail-fast >= 0.2, minitest-fail-fast < 1
Requires:      gem(andand) >= 1.3.3
Requires:      gem(minitest) >= 5.20.0
Requires:      gem(minitest-fail-fast) >= 0.1.0
Requires:      gem(nokogiri) >= 1.15.4
Requires:      gem(rake) >= 13.0.0
Conflicts:     gem(andand) >= 1.4
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-fail-fast) >= 1
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(rake) >= 14
Obsoletes:     ruby-rgen < %EVR
Provides:      ruby-rgen = %EVR
Provides:      gem(rgen) = 0.10.2

%description
RGen is a framework for Model Driven Software Development (MDSD)in Ruby. This
means that it helps you build Metamodels, instantiate Models, modify and
transform Models and finally generate arbitrary textual content from it.

RGen features include:
* Supporting Ruby 1.8.6, 1.8.7 and 1.9.x
* Metamodel definition language (internal Ruby DSL)
* ECore Meta-metamodel with an ECore instance available for every Metamodel
* Generator creating the Ruby metamodel definition from an ECore instance
* Transformer creating Ruby metamodel classes/modules from an ECore instance
* Instantiation of Metamodels, i.e. creation of Models (e.g. from XML)
* Model builder, internal Ruby DSL
* Model fragmentation over several several files and per-fragment caching
* Model Transformation language (internal Ruby DSL)
* Powerful template based generator language (internal Ruby DSL inside of ERB)
* UML 1.3 metamodel and XMI 1.1 instantiator included
* ECore XML support (XMI 2.0)
* UML-to-ECore and ECore-to-UML transformation (UML class models)
* Enterprise Architect support (UML1.3/XMI1.1)


%if_enabled    doc
%package       -n gem-rgen-doc
Version:       0.10.2
Release:       alt1
Summary:       Ruby Modelling and Generator Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rgen
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rgen) = 0.10.2

%description   -n gem-rgen-doc
Ruby Modelling and Generator Framework documentation files.

RGen is a framework for Model Driven Software Development (MDSD)in Ruby. This
means that it helps you build Metamodels, instantiate Models, modify and
transform Models and finally generate arbitrary textual content from it.

RGen features include:
* Supporting Ruby 1.8.6, 1.8.7 and 1.9.x
* Metamodel definition language (internal Ruby DSL)
* ECore Meta-metamodel with an ECore instance available for every Metamodel
* Generator creating the Ruby metamodel definition from an ECore instance
* Transformer creating Ruby metamodel classes/modules from an ECore instance
* Instantiation of Metamodels, i.e. creation of Models (e.g. from XML)
* Model builder, internal Ruby DSL
* Model fragmentation over several several files and per-fragment caching
* Model Transformation language (internal Ruby DSL)
* Powerful template based generator language (internal Ruby DSL inside of ERB)
* UML 1.3 metamodel and XMI 1.1 instantiator included
* ECore XML support (XMI 2.0)
* UML-to-ECore and ECore-to-UML transformation (UML class models)
* Enterprise Architect support (UML1.3/XMI1.1)

%description   -n gem-rgen-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rgen.
%endif


%if_enabled    devel
%package       -n gem-rgen-devel
Version:       0.10.2
Release:       alt1
Summary:       Ruby Modelling and Generator Framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rgen
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rgen) = 0.10.2

%description   -n gem-rgen-devel
Ruby Modelling and Generator Framework development package.

RGen is a framework for Model Driven Software Development (MDSD)in Ruby. This
means that it helps you build Metamodels, instantiate Models, modify and
transform Models and finally generate arbitrary textual content from it.

RGen features include:
* Supporting Ruby 1.8.6, 1.8.7 and 1.9.x
* Metamodel definition language (internal Ruby DSL)
* ECore Meta-metamodel with an ECore instance available for every Metamodel
* Generator creating the Ruby metamodel definition from an ECore instance
* Transformer creating Ruby metamodel classes/modules from an ECore instance
* Instantiation of Metamodels, i.e. creation of Models (e.g. from XML)
* Model builder, internal Ruby DSL
* Model fragmentation over several several files and per-fragment caching
* Model Transformation language (internal Ruby DSL)
* Powerful template based generator language (internal Ruby DSL inside of ERB)
* UML 1.3 metamodel and XMI 1.1 instantiator included
* ECore XML support (XMI 2.0)
* UML-to-ECore and ECore-to-UML transformation (UML class models)
* Enterprise Architect support (UML1.3/XMI1.1)

%description   -n gem-rgen-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rgen.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG MIT-LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rgen-doc
%doc CHANGELOG MIT-LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rgen-devel
%doc CHANGELOG MIT-LICENSE README.rdoc
%endif


%changelog
* Sat Aug 22 2026 Pavel Skrylev <majioa@altlinux.org> 0.10.2-alt1
- ^ 0.9.0 -> 0.10.2

* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.0-alt1
- ^ 0.8.4 -> 0.9.0

* Tue Feb 19 2019 Pavel Skrylev <majioa@altlinux.org> 0.8.4-alt2
- Use Ruby Policy 2.0.

* Thu Nov 29 2018 Pavel Skrylev <majioa@altlinux.org> 0.8.4-alt1
- Bump gemified to 0.8.4.

* Sat Sep 09 2017 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1.1
- Rebuild with Ruby 2.4.1

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.7.0-alt1
- Initial build for ALT Linux
