%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname blade

Name:          gem-blade
Version:       0.7.3
Release:       alt1
Summary:       Sprockets test runner and toolkit
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/javan/blade
Vcs:           https://github.com/javan/blade.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(blade-qunit_adapter) >= 2.0.1
BuildRequires: gem(activesupport) >= 3.0.0
BuildRequires: gem(coffee-script) >= 0
BuildRequires: gem(coffee-script-source) >= 0
BuildRequires: gem(curses) >= 1.4.0
BuildRequires: gem(eventmachine) >= 0
BuildRequires: gem(faye) >= 0
BuildRequires: gem(sprockets) >= 3.0
BuildRequires: gem(thin) >= 1.6.0
BuildRequires: gem(useragent) >= 0.16.7
BuildRequires: gem(thor) >= 0.19.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(blade-qunit_adapter) >= 2.0.1
Requires:      gem(activesupport) >= 3.0.0
Requires:      gem(coffee-script) >= 0
Requires:      gem(coffee-script-source) >= 0
Requires:      gem(curses) >= 1.4.0
Requires:      gem(eventmachine) >= 0
Requires:      gem(faye) >= 0
Requires:      gem(sprockets) >= 3.0
Requires:      gem(thin) >= 1.6.0
Requires:      gem(useragent) >= 0.16.7
Requires:      gem(thor) >= 0.19.1
Provides:      gem(blade) = 0.7.3


%description
A Sprockets Toolkit for Building and Testing JavaScript Libraries.


%package       -n blade
Version:       0.7.3
Release:       alt1
Summary:       Blade executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета blade
Group:         Other
BuildArch:     noarch

Requires:      gem(blade) = 0.7.3

%description   -n blade
Blade executable(s).

A Sprockets Toolkit for Building and Testing JavaScript Libraries.

%description   -n blade -l ru_RU.UTF-8
Исполнямка для самоцвета blade.


%if_enabled    doc
%package       -n gem-blade-doc
Version:       0.7.3
Release:       alt1
Summary:       Blade documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета blade
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(blade) = 0.7.3

%description   -n gem-blade-doc
Blade documentation files.

A Sprockets Toolkit for Building and Testing JavaScript Libraries.

%description   -n gem-blade-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета blade.
%endif


%if_enabled    devel
%package       -n gem-blade-devel
Version:       0.7.3
Release:       alt1
Summary:       Blade development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета blade
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(blade) = 0.7.3
Requires:      gem(bundler) >= 2.0
Requires:      gem(rake) >= 10.0

%description   -n gem-blade-devel
Blade development package.

A Sprockets Toolkit for Building and Testing JavaScript Libraries.

%description   -n gem-blade-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета blade.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n blade
%doc README.md
%_bindir/blade

%if_enabled    doc
%files         -n gem-blade-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-blade-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1
- + packaged gem with Ruby Policy 2.0
