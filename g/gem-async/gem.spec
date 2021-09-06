%define        gemname async

Name:          gem-async
Version:       1.30.1
Release:       alt1
Summary:       A concurrency framework for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/socketry/async
Vcs:           https://github.com/socketry/async.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(console) >= 1.10 gem(console) < 2
BuildRequires: gem(nio4r) >= 2.3 gem(nio4r) < 3
BuildRequires: gem(timers) >= 4.1 gem(timers) < 5
# BuildRequires: gem(async-rspec) >= 1.1 gem(async-rspec) < 2
BuildRequires: gem(bake) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0.10 gem(covered) < 1
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(console) >= 1.10 gem(console) < 2
Requires:      gem(nio4r) >= 2.3 gem(nio4r) < 3
Requires:      gem(timers) >= 4.1 gem(timers) < 5
Provides:      gem(async) = 1.30.1

%description
An awesome asynchronous event-driven reactor for Ruby.

Async is a composable asynchronous I/O framework for Ruby based on nio4r and
timers. Features:
* Scalable event-driven I/O for Ruby. Thousands of clients per process!
* Light weight fiber-based concurrency. No need for callbacks!
* Multi-thread/process containers for parallelism.
* Growing eco-system of event-driven components.


%package       -n gem-async-doc
Version:       1.30.1
Release:       alt1
Summary:       A concurrency framework for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета async
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(async) = 1.30.1

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


%package       -n gem-async-devel
Version:       1.30.1
Release:       alt1
Summary:       A concurrency framework for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета async
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(async) = 1.30.1
Requires:      gem(async-rspec) >= 1.1 gem(async-rspec) < 2
Requires:      gem(bake) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(covered) >= 0.10 gem(covered) < 1
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

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


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-async-doc
%ruby_gemdocdir

%files         -n gem-async-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.30.1-alt1
- + packaged gem with Ruby Policy 2.0
