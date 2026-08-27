%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname train-habitat

Name:          gem-train-habitat
Version:       0.2.38
Release:       alt1
Summary:       Habitat API Transport for Train
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/inspec/train-habitat
Vcs:           https://github.com/inspec/train-habitat.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(googleauth)
BuildRequires: gem(byebug) >= 11.0
BuildRequires: gem(chefstyle) >= 2.2.0
BuildRequires: gem(m) >= 1.5
BuildRequires: gem(minitest) >= 5.11
BuildRequires: gem(mocha) >= 1.8
BuildRequires: gem(pry) >= 0.11
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(train-core) >= 1.7.5
BuildConflicts: gem(byebug) >= 14
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(m) >= 2
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(pry) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(train-core) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.7.1,mocha < 3
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
%ruby_use_gem_dependency byebug >= 12.0
Requires:      gem(train-core) >= 1.7.5
Conflicts:     gem(train-core) >= 4
Provides:      gem(train-habitat) = 0.2.38

%description
Allows applications using Train to speak to Habitat.

train-habitat is a Train plugin and is used as a Train Transport to connect to
Habitat installations.


%if_enabled    doc
%package       -n gem-train-habitat-doc
Version:       0.2.38
Release:       alt1
Summary:       Habitat API Transport for Train documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета train-habitat
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(train-habitat) = 0.2.38

%description   -n gem-train-habitat-doc
Habitat API Transport for Train documentation files.

Allows applications using Train to speak to Habitat.

train-habitat is a Train plugin and is used as a Train Transport to connect to
Habitat installations.

%description   -n gem-train-habitat-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета train-habitat.
%endif


%if_enabled    devel
%package       -n gem-train-habitat-devel
Version:       0.2.38
Release:       alt1
Summary:       Habitat API Transport for Train development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета train-habitat
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(train-habitat) = 0.2.38
Requires:      gem(byebug) >= 11.0
Requires:      gem(chefstyle) >= 2.2.0
Requires:      gem(m) >= 1.5
Requires:      gem(minitest) >= 5.11
Requires:      gem(mocha) >= 1.8
Requires:      gem(pry) >= 0.11
Requires:      gem(rake) >= 13.0
Conflicts:     gem(byebug) >= 14
Conflicts:     gem(chefstyle) >= 3
Conflicts:     gem(m) >= 2
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(pry) >= 1
Conflicts:     gem(rake) >= 14

%description   -n gem-train-habitat-devel
Habitat API Transport for Train development package.

Allows applications using Train to speak to Habitat.

train-habitat is a Train plugin and is used as a Train Transport to connect to
Habitat installations.

%description   -n gem-train-habitat-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета train-habitat.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-train-habitat-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-train-habitat-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Mon Aug 24 2026 Pavel Skrylev <majioa@altlinux.org> 0.2.38-alt1
- ^ 0.2.32 -> 0.2.38

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.32-alt1
- + packaged gem with Ruby Policy 2.0
