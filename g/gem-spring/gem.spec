%define        gemname spring

Name:          gem-spring
Version:       2.1.1
Release:       alt1
Summary:       Rails application preloader
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/spring
Vcs:           https://github.com/rails/spring.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0 gem(rake) < 14
BuildRequires: gem(bump) >= 0
BuildRequires: gem(activesupport) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(spring) = 2.1.1


%description
Preloads your application so things like console, rake and tests run faster


%package       -n spring
Version:       2.1.1
Release:       alt1
Summary:       Rails application preloader executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета spring
Group:         Other
BuildArch:     noarch

Requires:      gem(spring) = 2.1.1

%description   -n spring
Rails application preloader executable(s).

Preloads your application so things like console, rake and tests run faster

%description   -n spring -l ru_RU.UTF-8
Исполнямка для самоцвета spring.


%package       -n gem-spring-doc
Version:       2.1.1
Release:       alt1
Summary:       Rails application preloader documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spring
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(spring) = 2.1.1

%description   -n gem-spring-doc
Rails application preloader documentation files.

Preloads your application so things like console, rake and tests run faster

%description   -n gem-spring-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spring.


%package       -n gem-spring-devel
Version:       2.1.1
Release:       alt1
Summary:       Rails application preloader development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spring
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(spring) = 2.1.1
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(bump) >= 0
Requires:      gem(activesupport) >= 0

%description   -n gem-spring-devel
Rails application preloader development package.

Preloads your application so things like console, rake and tests run faster

%description   -n gem-spring-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spring.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n spring
%doc README.md
%_bindir/spring

%files         -n gem-spring-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-spring-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- + packaged gem with Ruby Policy 2.0
