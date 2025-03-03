%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname byebug

Name:          gem-byebug
Version:       11.1.3.105
Release:       alt0.1
Summary:       Ruby fast debugger - base + CLI
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/deivid-rodriguez/byebug
Vcs:           https://github.com/deivid-rodriguez/byebug.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(chandler) >= 0.9.0
BuildRequires: gem(mdl) = 0.11.0
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(pry) >= 0.13.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-performance) >= 1.3
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0.9.26
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency chandler >= 0.9.0.5,chandler < 1
Requires:      ruby >= 2.5.0
Provides:      gem(byebug) = 11.1.3.105

%ruby_use_gem_version byebug:11.1.3.105

%description
Byebug is a Ruby debugger. It's implemented using the TracePoint C API for
execution control and the Debug Inspector C API for call stack navigation. The
core component provides support that front-ends can build on. It provides
breakpoint handling and bindings for stack frames among other things and it
comes with an easy to use command line interface.


%package       -n byebug
Version:       11.1.3.105
Release:       alt0.1
Summary:       Ruby fast debugger - base + CLI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета byebug
Group:         Other
BuildArch:     noarch

Requires:      gem(byebug) = 11.1.3.105

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
Version:       11.1.3.105
Release:       alt0.1
Summary:       Ruby fast debugger - base + CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета byebug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(byebug) = 11.1.3.105

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
Version:       11.1.3.105
Release:       alt0.1
Summary:       Ruby fast debugger - base + CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета byebug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(byebug) = 11.1.3.105
Requires:      gem(bundler) >= 2.0
Requires:      gem(chandler) >= 0.9.0
Requires:      gem(minitest) >= 5.11
Requires:      gem(pry) >= 0.13.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-performance) >= 1.3
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0.9.26
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yard) >= 1

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
* Mon Mar 03 2025 Pavel Skrylev <majioa@altlinux.org> 11.1.3.105-alt0.1
- ^ 11.1.3 -> 11.1.3p105

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 11.1.3-alt1.1
- !fix spec to conform dependencies

* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 11.1.3-alt1
- + packaged gem with Ruby Policy 2.0
