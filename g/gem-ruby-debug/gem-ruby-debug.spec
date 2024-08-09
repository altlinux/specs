%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-debug

Name:          gem-ruby-debug
Version:       0.11.0.3
Release:       alt0.1
Summary:       Command line interface (CLI) for ruby-debug-base
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/ruby-debug/
Vcs:           https://github.com/ruby-debug/ruby-debug.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rake-compiler) >= 0.8.1
BuildRequires: gem(columnize) >= 0.1
BuildRequires: gem(linecache2) >= 1.4
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(linecache2) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_alias_names ruby-debug,debug
Requires:      gem(ruby-debug-base) = 0.11.0.3
Requires:      gem(columnize) >= 0.1
Requires:      gem(linecache2) >= 1.4
Conflicts:     gem(linecache2) >= 2
Provides:      gem(ruby-debug) = 0.11.0.3

%ruby_use_gem_version ruby-debug:0.11.0.3
%ruby_use_gem_version ruby-debug-base:0.11.0.3

%description
A generic command line interface for ruby-debug.

ruby-debug is a fast implementation of the standard debugger debug.rb.
The faster execution speed is achieved by utilizing a new hook in the
Ruby C API.


%package       -n gem-ruby-debug-base
Version:       0.11.0.3
Release:       alt0.1
Summary:       Fast Ruby debugger - core component
Group:         Development/Ruby

Provides:      gem(ruby-debug-base) = 0.11.0.3

%description   -n gem-ruby-debug-base
ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.


%if_enabled    doc
%package       -n gem-ruby-debug-base-doc
Version:       0.11.0.3
Release:       alt0.1
Summary:       Fast Ruby debugger - core component documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-debug-base
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-debug-base) = 0.11.0.3

%description   -n gem-ruby-debug-base-doc
Fast Ruby debugger - core component documentation files.

ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.

%description   -n gem-ruby-debug-base-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-debug-base.
%endif


%if_enabled    devel
%package       -n gem-ruby-debug-base-devel
Version:       0.11.0.3
Release:       alt0.1
Summary:       Fast Ruby debugger - core component development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-debug-base
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug-base) = 0.11.0.3
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rake-compiler) >= 0.8.1
Requires:      gem(ruby-debug) = 0.11.0.3
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-ruby-debug-base-devel
Fast Ruby debugger - core component development package.

ruby-debug is a fast implementation of the standard Ruby debugger debug.rb. It
is implemented by utilizing a new Ruby C API hook. The core component provides
support that front-ends can build on. It provides breakpoint handling, bindings
for stack frames among other things.

%description   -n gem-ruby-debug-base-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-debug-base.
%endif


%package       -n rdebug
Version:       0.11.0.3
Release:       alt0.1
Summary:       Command line interface (CLI) for ruby-debug-base executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-debug
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-debug) = 0.11.0.3

%description   -n rdebug
Command line interface (CLI) for ruby-debug-base executable(s).

A generic command line interface for ruby-debug.

%description   -n rdebug -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-debug.


%if_enabled    doc
%package       -n gem-ruby-debug-doc
Version:       0.11.0.3
Release:       alt0.1
Summary:       Command line interface (CLI) for ruby-debug-base documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-debug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-debug) = 0.11.0.3

%description   -n gem-ruby-debug-doc
Command line interface (CLI) for ruby-debug-base documentation files.

A generic command line interface for ruby-debug.

ruby-debug is a fast implementation of the standard debugger debug.rb.
The faster execution speed is achieved by utilizing a new hook in the
Ruby C API.

%description   -n gem-ruby-debug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-debug.
%endif


%if_enabled    devel
%package       -n gem-ruby-debug-devel
Version:       0.11.0.3
Release:       alt0.1
Summary:       Command line interface (CLI) for ruby-debug-base development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-debug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug) = 0.11.0.3
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rake-compiler) >= 0.8.1
Conflicts:     gem(rake-compiler) >= 2

%description   -n gem-ruby-debug-devel
Command line interface (CLI) for ruby-debug-base development package.

A generic command line interface for ruby-debug.

ruby-debug is a fast implementation of the standard debugger debug.rb.
The faster execution speed is achieved by utilizing a new hook in the
Ruby C API.

%description   -n gem-ruby-debug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-debug.
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
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-ruby-debug-base
%doc README
%ruby_gemspecdir/ruby-debug-base-0.11.0.3.gemspec
%ruby_gemslibdir/ruby-debug-base-0.11.0.3
%ruby_gemsextdir/ruby-debug-base-0.11.0.3

%if_enabled    doc
%files         -n gem-ruby-debug-base-doc
%doc README
%ruby_gemsdocdir/ruby-debug-base-0.11.0.3
%endif

%if_enabled    devel
%files         -n gem-ruby-debug-base-devel
%doc README
%ruby_includedir/*
%endif

%files         -n rdebug
%doc README
%_bindir/rdebug
%_mandir/rdebug.1.xz

%if_enabled    doc
%files         -n gem-ruby-debug-doc
%doc README
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-debug-devel
%doc README
%endif


%changelog
* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 0.11.0.3-alt0.1
- + packaged gem with Ruby Policy 2.0
