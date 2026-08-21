%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hana

Name:          gem-hana
Version:       1.3.7.8
Release:       alt1.1
Summary:       Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/tenderlove/hana
Vcs:           https://github.com/tenderlove/hana.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(hoe) >= 0
BuildRequires: gem(hoe-gemspec2) >= 1.3
BuildRequires: gem(hoe-git2) >= 1.8
BuildRequires: gem(hoe-seattlerb) >= 1.3
BuildRequires: gem(minitest) >= 5.0
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git2) >= 2
BuildConflicts: gem(hoe-seattlerb) >= 2
BuildConflicts: gem(minitest) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 6.0
Requires:      gem(hoe) >= 0
Requires:      gem(minitest) >= 5.0
Conflicts:     gem(minitest) >= 7
Provides:      gem(hana) = 1.3.7.8

%ruby_use_gem_version hana:1.3.7.8

%description
Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC.


%if_enabled    doc
%package       -n gem-hana-doc
Version:       1.3.7.8
Release:       alt1.1
Summary:       Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hana
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hana) = 1.3.7.8

%description   -n gem-hana-doc
Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC documentation files.

%description   -n gem-hana-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hana.
%endif


%if_enabled    devel
%package       -n gem-hana-devel
Version:       1.3.7.8
Release:       alt1.1
Summary:       Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hana
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hana) = 1.3.7.8
Requires:      gem(hoe-gemspec2) >= 1.3
Requires:      gem(hoe-git2) >= 1.8
Requires:      gem(hoe-seattlerb) >= 1.3
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git2) >= 2
Conflicts:     gem(hoe-seattlerb) >= 2

%description   -n gem-hana-devel
Implementation of [JSON Patch][1] and [JSON Pointer][2] RFC development package.

%description   -n gem-hana-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hana.
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
%doc README.md LICENSE
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hana-doc
%doc README.md LICENSE
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hana-devel
%doc README.md LICENSE
%endif


%changelog
* Wed Aug 19 2026 Pavel Skrylev <majioa@altlinux.org> 1.3.7.8-alt1.1
- ! fixed dep to minitest gem

* Fri Aug 30 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.7.8-alt1
- ^ 1.3.7 -> 1.3.7p8

* Sat Oct 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.7-alt1
- + packaged gem with Ruby Policy 2.0
