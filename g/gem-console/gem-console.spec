%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname console

Name:          gem-console
Version:       1.27.0
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
%if_enabled check
BuildRequires: gem(fiber-annotation) >= 0
BuildRequires: gem(fiber-local) >= 1.1
BuildRequires: gem(json) >= 0
BuildConflicts: gem(fiber-local) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(fiber-annotation) >= 0
Requires:      gem(fiber-local) >= 1.1
Requires:      gem(json) >= 0
Conflicts:     gem(fiber-local) >= 2
Provides:      gem(console) = 1.27.0


%description
Provides beautiful console logging for Ruby applications. Implements fast,
buffered log output. Features:
* Thread safe global logger with per-fiber context
* Carry along context with nested loggers
* Enable/disable log levels per-class
* Detailed logging of exceptions
* Beautiful logging to the terminal or structured logging using JSON


%if_enabled    doc
%package       -n gem-console-doc
Version:       1.27.0
Release:       alt1
Summary:       Beautiful logging for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета console
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(console) = 1.27.0

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
%endif


%if_enabled    devel
%package       -n gem-console-devel
Version:       1.27.0
Release:       alt1
Summary:       Beautiful logging for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета console
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(console) = 1.27.0

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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-console-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-console-devel
%doc readme.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.27.0-alt1
- ^ 1.16.2 -> 1.27.0

* Wed Oct 12 2022 Pavel Skrylev <majioa@altlinux.org> 1.16.2-alt1
- ^ 1.13.1 -> 1.16.2

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.13.1-alt1
- + packaged gem with Ruby Policy 2.0
