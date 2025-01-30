%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname spring

Name:          gem-spring
Version:       4.2.1
Release:       alt1
Summary:       Rails application preloader
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/spring
Vcs:           https://github.com/rails/spring.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 0
BuildRequires: gem(bump) >= 0
BuildRequires: gem(rake) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(activesupport) >= 0
Requires:      gem(bump) >= 0
Requires:      gem(rake) >= 0
Provides:      gem(spring) = 4.2.1

%description
Preloads your application so things like console, rake and tests run faster


%package       -n spring
Version:       4.2.1
Release:       alt1
Summary:       Rails application preloader executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета spring
Group:         Other
BuildArch:     noarch

Requires:      gem(spring) = 4.2.1

%description   -n spring
Rails application preloader executable(s).

Preloads your application so things like console, rake and tests run faster

%description   -n spring -l ru_RU.UTF-8
Исполнямка для самоцвета spring.


%if_enabled    doc
%package       -n gem-spring-doc
Version:       4.2.1
Release:       alt1
Summary:       Rails application preloader documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spring
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(spring) = 4.2.1

%description   -n gem-spring-doc
Rails application preloader documentation files.

Preloads your application so things like console, rake and tests run faster

%description   -n gem-spring-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spring.
%endif


%if_enabled    devel
%package       -n gem-spring-devel
Version:       4.2.1
Release:       alt1
Summary:       Rails application preloader development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spring
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(spring) = 4.2.1

%description   -n gem-spring-devel
Rails application preloader development package.

Preloads your application so things like console, rake and tests run faster

%description   -n gem-spring-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spring.
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
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n spring
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%_bindir/spring

%if_enabled    doc
%files         -n gem-spring-doc
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-spring-devel
%doc LICENSE.txt README.md CHANGELOG.md CONTRIBUTING.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 4.2.1-alt1
- ^ 2.1.1 -> 4.2.1

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt0.1
- + packaged gem with Ruby Policy 2.0
