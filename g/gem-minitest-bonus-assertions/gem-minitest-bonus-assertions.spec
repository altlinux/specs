%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-bonus-assertions

Name:          gem-minitest-bonus-assertions
Version:       3.1.0
Release:       alt1
Summary:       Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest], providing assertions I use frequently, supporting only Ruby 2.0 or better
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitest-bonus-assertions
Vcs:           https://github.com/halostatue/minitest-bonus-assertions.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(minitest) >= 5.16
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 0.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(standard) >= 1.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(standard) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17
%ruby_use_gem_dependency hoe-halostatue >= 2.1.1
%ruby_use_gem_dependency minitest >= 5.16
Requires:      ruby >= 2.0
Provides:      gem(minitest-bonus-assertions) = 3.1.0

%ruby_use_gem_version minitest-bonus-assertions:3.1.0

%description
Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest],
providing assertions I use frequently, supporting only Ruby 2.0 or better.


%if_enabled    doc
%package       -n gem-minitest-bonus-assertions-doc
Version:       3.1.0
Release:       alt1
Summary:       Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest], providing assertions I use frequently, supporting only Ruby 2.0 or better documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-bonus-assertions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-bonus-assertions) = 3.1.0

%description   -n gem-minitest-bonus-assertions-doc
Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest],
providing assertions I use frequently, supporting only Ruby 2.0 or better
documentation files.

%description   -n gem-minitest-bonus-assertions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-bonus-assertions.
%endif


%if_enabled    devel
%package       -n gem-minitest-bonus-assertions-devel
Version:       3.1.0
Release:       alt1
Summary:       Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest], providing assertions I use frequently, supporting only Ruby 2.0 or better development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-bonus-assertions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-bonus-assertions) = 3.1.0
Requires:      gem(hoe) >= 4.0
Requires:      gem(hoe-halostatue) >= 2.1.1
Requires:      gem(minitest) >= 5.16
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 0.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(standard) >= 1.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(standard) >= 2

%description   -n gem-minitest-bonus-assertions-devel
Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest],
providing assertions I use frequently, supporting only Ruby 2.0 or better
development package.

%description   -n gem-minitest-bonus-assertions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-bonus-assertions.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md History.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-bonus-assertions-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md History.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-bonus-assertions-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md History.rdoc
%endif


%changelog
* Wed Sep 23 2026 Pavel Skrylev <majioa@altlinux.org> 3.1.0-alt1
- ^ 3.0.2 -> 3.1.0

* Tue Aug 27 2024 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt1
- ^ 3.0 -> 3.0.2

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.0-alt1
- + packaged gem with Ruby Policy 2.0
