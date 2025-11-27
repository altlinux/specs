%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname byebug

Name:          gem-byebug
Version:       12.0.0
Release:       alt1
Summary:       Ruby fast debugger - base + CLI
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/deivid-rodriguez/byebug
Vcs:           https://github.com/deivid-rodriguez/byebug.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(chandler) >= 0.9.0
BuildRequires: gem(faraday) >= 2.6.0
BuildRequires: gem(faraday-retry) >= 2.2
BuildRequires: gem(irb) >= 1.15
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(reline) >= 0.6.0
BuildRequires: gem(yard) >= 0.9.34
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday-retry) >= 3
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency chandler >= 0.9,chandler < 1
Requires:      ruby >= 3.2.0
Requires:      gem(reline) >= 0.6.0
Provides:      gem(byebug) = 12.0.0

%description
Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.


%package       -n byebug
Version:       12.0.0
Release:       alt1
Summary:       Ruby fast debugger - base + CLI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета byebug
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(byebug) = 12.0.0

%description   -n byebug
Ruby fast debugger - base + CLI executable(s).

Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.

%description   -n byebug -l ru_RU.UTF-8
Исполнямка для самоцвета byebug.


%if_enabled    doc
%package       -n gem-byebug-doc
Version:       12.0.0
Release:       alt1
Summary:       Ruby fast debugger - base + CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета byebug
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(byebug) = 12.0.0

%description   -n gem-byebug-doc
Ruby fast debugger - base + CLI documentation files.

Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.

%description   -n gem-byebug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета byebug.
%endif


%if_enabled    devel
%package       -n gem-byebug-devel
Version:       12.0.0
Release:       alt1
Summary:       Ruby fast debugger - base + CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета byebug
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(byebug) = 12.0.0
Requires:      gem(bundler) >= 2.0
Requires:      gem(faraday) >= 2.6.0
Requires:      gem(faraday-retry) >= 2.2
Requires:      gem(irb) >= 1.15
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday-retry) >= 3
Conflicts:     gem(irb) >= 2

%description   -n gem-byebug-devel
Ruby fast debugger - base + CLI development package.

Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.

%description   -n gem-byebug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета byebug.
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
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md code_of_conduct.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n byebug
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md code_of_conduct.md
%_bindir/byebug

%if_enabled    doc
%files         -n gem-byebug-doc
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md code_of_conduct.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-byebug-devel
%doc CHANGELOG.md CONTRIBUTING.md LICENSE README.md code_of_conduct.md
%ruby_includedir/*
%endif


%changelog
* Wed Nov 26 2025 Pavel Skrylev <majioa@altlinux.org> 12.0.0-alt1
- ^ 11.1.3p105 -> 12.0.0

* Mon Mar 03 2025 Pavel Skrylev <majioa@altlinux.org> 11.1.3.105-alt0.1
- ^ 11.1.3 -> 11.1.3p105

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 11.1.3-alt1.1
- !fix spec to conform dependencies

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 11.1.3-alt1
- + packaged gem with Ruby Policy 2.0
