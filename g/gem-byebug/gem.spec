%define        gemname byebug

Name:          gem-byebug
Version:       11.1.3
Release:       alt1
Summary:       Ruby fast debugger - base + CLI
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/deivid-rodriguez/byebug
Vcs:           https://github.com/deivid-rodriguez/byebug.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(byebug) = 11.1.3


%description
Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.


%package       -n byebug
Version:       11.1.3
Release:       alt1
Summary:       Ruby fast debugger - base + CLI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета byebug
Group:         Other
BuildArch:     noarch

Requires:      gem(byebug) = 11.1.3

%description   -n byebug
Ruby fast debugger - base + CLI executable(s).

Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.

%description   -n byebug -l ru_RU.UTF-8
Исполнямка для самоцвета byebug.


%package       -n gem-byebug-doc
Version:       11.1.3
Release:       alt1
Summary:       Ruby fast debugger - base + CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета byebug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(byebug) = 11.1.3

%description   -n gem-byebug-doc
Ruby fast debugger - base + CLI documentation files.

Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.

%description   -n gem-byebug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета byebug.


%package       -n gem-byebug-devel
Version:       11.1.3
Release:       alt1
Summary:       Ruby fast debugger - base + CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета byebug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(byebug) = 11.1.3
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3

%description   -n gem-byebug-devel
Ruby fast debugger - base + CLI development package.

Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.

%description   -n gem-byebug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета byebug.


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
%ruby_gemextdir

%files         -n byebug
%doc README.md
%_bindir/byebug

%files         -n gem-byebug-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-byebug-devel
%doc README.md
%ruby_includedir/*


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 11.1.3-alt1
- + packaged gem with Ruby Policy 2.0
