%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ruby-debug-ide

Name:          gem-ruby-debug-ide
Version:       0.7.3.2
Release:       alt0.1
Summary:       IDE interface for ruby-debug
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-debug/ruby-debug-ide
Vcs:           https://github.com/ruby-debug/ruby-debug-ide.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0.8.1
BuildRequires: gem(debase) >= 0.2.2
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildConflicts: gem(debase) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names ruby-debug-ide,gem-ruby-debug-ide
Requires:      gem(ruby-debug-base19x) >= 0.11.32
Requires:      gem(rake) >= 0.8.1
Provides:      gem(ruby-debug-ide) = 0.7.3.2

%ruby_use_gem_version ruby-debug-ide:0.7.3.2

%description
An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.


%package       -n ruby-debug-ide
Version:       0.7.3.2
Release:       alt0.1
Summary:       IDE interface for ruby-debug executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-debug-ide
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-debug-ide) = 0.7.3.2

%description   -n ruby-debug-ide
IDE interface for ruby-debug executable(s).

An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.

%description   -n ruby-debug-ide -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-debug-ide.


%if_enabled    doc
%package       -n gem-ruby-debug-ide-doc
Version:       0.7.3.2
Release:       alt0.1
Summary:       IDE interface for ruby-debug documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-debug-ide
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug-ide) = 0.7.3.2

%description   -n gem-ruby-debug-ide-doc
IDE interface for ruby-debug documentation files.

An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.

%description   -n gem-ruby-debug-ide-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-debug-ide.
%endif


%if_enabled    devel
%package       -n gem-ruby-debug-ide-devel
Version:       0.7.3.2
Release:       alt0.1
Summary:       IDE interface for ruby-debug development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-debug-ide
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-debug-ide) = 0.7.3.2
Requires:      gem(debase) >= 0.2.2
Requires:      gem(bundler) >= 0
Requires:      gem(test-unit) >= 0
Conflicts:     gem(debase) >= 1

%description   -n gem-ruby-debug-ide-devel
IDE interface for ruby-debug development package.

An interface which glues ruby-debug to IDEs like Eclipse (RDT), NetBeans and
RubyMine.

%description   -n gem-ruby-debug-ide-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-debug-ide.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc ChangeLog.archive ChangeLog.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n ruby-debug-ide
%doc ChangeLog.archive ChangeLog.md MIT-LICENSE README.md
%_bindir/rdebug-ide
%_bindir/gdb_wrapper

%if_enabled    doc
%files         -n gem-ruby-debug-ide-doc
%doc ChangeLog.archive ChangeLog.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ruby-debug-ide-devel
%doc ChangeLog.archive ChangeLog.md MIT-LICENSE README.md
%endif


%changelog
* Mon Aug 12 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.3.2-alt0.1
- ^ 0.7.3 -> 0.7.3p2

* Tue Oct 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1.1
- ! spec

* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1
- + packaged gem with Ruby Policy 2.0
