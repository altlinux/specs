%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname async

Name:          gem-async
Version:       2.14.2
Release:       alt1
Summary:       A concurrency framework for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async
Vcs:           https://github.com/socketry/async.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(console) >= 1.25.2
BuildRequires: gem(fiber-annotation) >= 0
BuildRequires: gem(io-event) >= 1.6.5
BuildConflicts: gem(console) >= 2
BuildConflicts: gem(io-event) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(console) >= 1.25.2
Requires:      gem(fiber-annotation) >= 0
Requires:      gem(io-event) >= 1.6.5
Conflicts:     gem(console) >= 2
Conflicts:     gem(io-event) >= 2
Provides:      gem(async) = 2.14.2


%description
An awesome asynchronous event-driven reactor for Ruby.

Async is a composable asynchronous I/O framework for Ruby based on nio4r and
timers. Features:
* Scalable event-driven I/O for Ruby. Thousands of clients per process!
* Light weight fiber-based concurrency. No need for callbacks!
* Multi-thread/process containers for parallelism.
* Growing eco-system of event-driven components.


%if_enabled    doc
%package       -n gem-async-doc
Version:       2.14.2
Release:       alt1
Summary:       A concurrency framework for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async) = 2.14.2

%description   -n gem-async-doc
A concurrency framework for Ruby documentation files.

An awesome asynchronous event-driven reactor for Ruby.

Async is a composable asynchronous I/O framework for Ruby based on nio4r and
timers. Features:
* Scalable event-driven I/O for Ruby. Thousands of clients per process!
* Light weight fiber-based concurrency. No need for callbacks!
* Multi-thread/process containers for parallelism.
* Growing eco-system of event-driven components.

%description   -n gem-async-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета async.
%endif


%if_enabled    devel
%package       -n gem-async-devel
Version:       2.14.2
Release:       alt1
Summary:       A concurrency framework for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async) = 2.14.2

%description   -n gem-async-devel
A concurrency framework for Ruby development package.

An awesome asynchronous event-driven reactor for Ruby.

Async is a composable asynchronous I/O framework for Ruby based on nio4r and
timers. Features:
* Scalable event-driven I/O for Ruby. Thousands of clients per process!
* Light weight fiber-based concurrency. No need for callbacks!
* Multi-thread/process containers for parallelism.
* Growing eco-system of event-driven components.

%description   -n gem-async-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета async.
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
%files         -n gem-async-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-async-devel
%doc readme.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 2.14.2-alt1
- ^ 2.1.0 -> 2.14.2

* Wed Oct 12 2022 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 1.30.1 -> 2.1.0

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.30.1-alt1
- + packaged gem with Ruby Policy 2.0
