%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-moar

Name:          gem-minitest-moar
Version:       0.0.4.3
Release:       alt1
Summary:       Moar Minitest Please!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/dockyard/minitest-moar
Vcs:           https://github.com/dockyard/minitest-moar.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 1.6
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(m) >= 0
BuildRequires: gem(minitest) >= 5.1
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Requires:      gem(byebug) >= 0
Requires:      gem(m) >= 0
Provides:      gem(minitest-moar) = 0.0.4.3

%ruby_use_gem_version minitest-moar:0.0.4.3

%description
Moar Minitest Please!


%if_enabled    doc
%package       -n gem-minitest-moar-doc
Version:       0.0.4.3
Release:       alt1
Summary:       Moar Minitest Please! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-moar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-moar) = 0.0.4.3

%description   -n gem-minitest-moar-doc
Moar Minitest Please! documentation files.

%description   -n gem-minitest-moar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-moar.
%endif


%if_enabled    devel
%package       -n gem-minitest-moar-devel
Version:       0.0.4.3
Release:       alt1
Summary:       Moar Minitest Please! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-moar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-moar) = 0.0.4.3
Requires:      gem(bundler) >= 1.6
Requires:      gem(minitest) >= 5.1
Requires:      gem(rake) >= 10.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rake) >= 14

%description   -n gem-minitest-moar-devel
Moar Minitest Please! development package.

%description   -n gem-minitest-moar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-moar.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-moar-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-moar-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 0.0.4.3-alt1
- ^ 0.0.4 -> 0.0.4p3

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.0.4-alt1
- + packaged gem with Ruby Policy 2.0
