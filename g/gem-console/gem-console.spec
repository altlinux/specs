%define        gemname console

Name:          gem-console
Version:       1.16.2
Release:       alt1
Summary:       Beautiful logging for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/console
Vcs:           https://github.com/socketry/console.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(fiber-local) >= 0
BuildRequires: gem(bake) >= 0
BuildRequires: gem(bake-test) >= 0
BuildRequires: gem(bake-test-external) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(covered) >= 0.18.1 gem(covered) < 0.19
BuildRequires: gem(sus) >= 0.14 gem(sus) < 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fiber-local) >= 0
Provides:      gem(console) = 1.16.2


%description
Provides beautiful console logging for Ruby applications. Implements fast,
buffered log output. Features:
* Thread safe global logger with per-fiber context
* Carry along context with nested loggers
* Enable/disable log levels per-class
* Detailed logging of exceptions
* Beautiful logging to the terminal or structured logging using JSON


%package       -n gem-console-doc
Version:       1.16.2
Release:       alt1
Summary:       Beautiful logging for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета console
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(console) = 1.16.2

%description   -n gem-console-doc
Beautiful logging for Ruby documentation files.

Provides beautiful console logging for Ruby applications. Implements fast,
buffered log output. Features:
* Thread safe global logger with per-fiber context
* Carry along context with nested loggers
* Enable/disable log levels per-class
* Detailed logging of exceptions
* Beautiful logging to the terminal or structured logging using JSON

%description   -n gem-console-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета console.


%package       -n gem-console-devel
Version:       1.16.2
Release:       alt1
Summary:       Beautiful logging for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета console
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(console) = 1.16.2
Requires:      gem(bake) >= 0
Requires:      gem(bake-test) >= 0
Requires:      gem(bake-test-external) >= 0
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0.18.1 gem(covered) < 0.19
Requires:      gem(sus) >= 0.14 gem(sus) < 1

%description   -n gem-console-devel
Beautiful logging for Ruby development package.

Provides beautiful console logging for Ruby applications. Implements fast,
buffered log output. Features:
* Thread safe global logger with per-fiber context
* Carry along context with nested loggers
* Enable/disable log levels per-class
* Detailed logging of exceptions
* Beautiful logging to the terminal or structured logging using JSON

%description   -n gem-console-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета console.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-console-doc
%doc readme.md
%ruby_gemdocdir

%files         -n gem-console-devel
%doc readme.md


%changelog
* Wed Oct 12 2022 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt1
- ^ 1.13.1 -> 1.16.2

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.13.1-alt1
- + packaged gem with Ruby Policy 2.0
