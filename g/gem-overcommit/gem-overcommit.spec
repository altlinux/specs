%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname overcommit

Name:          gem-overcommit
Version:       0.70.0
Release:       alt1
Summary:       Git hook manager
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sds/overcommit
Vcs:           https://github.com/sds/overcommit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb
%if_enabled check
BuildRequires: gem(childprocess) >= 0.6.3
BuildRequires: gem(iniparse) >= 1.4
BuildRequires: gem(rexml) >= 3.3.9
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8.0
BuildConflicts: gem(childprocess) >= 6
BuildConflicts: gem(iniparse) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency simplecov-lcov >= 0.9,simplecov-lcov < 1
Requires:      ruby >= 2.6
Requires:      gem(childprocess) >= 0.6.3
Requires:      gem(iniparse) >= 1.4
Requires:      gem(rexml) >= 3.3.9
Conflicts:     gem(childprocess) >= 6
Conflicts:     gem(iniparse) >= 2
Provides:      gem(overcommit) = 0.70.0

%description
Utility to install, configure, and extend Git hooks


%package       -n overcommit
Version:       0.70.0
Release:       alt1
Summary:       Git hook manager executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета overcommit
Group:         Other
BuildArch:     noarch

Requires:      gem(overcommit) = 0.70.0

%description   -n overcommit
Git hook manager executable(s).

Utility to install, configure, and extend Git hooks

%description   -n overcommit -l ru_RU.UTF-8
Исполнямка для самоцвета overcommit.


%if_enabled    doc
%package       -n gem-overcommit-doc
Version:       0.70.0
Release:       alt1
Summary:       Git hook manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета overcommit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(overcommit) = 0.70.0

%description   -n gem-overcommit-doc
Git hook manager documentation files.

Utility to install, configure, and extend Git hooks

%description   -n gem-overcommit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета overcommit.
%endif


%if_enabled    devel
%package       -n gem-overcommit-devel
Version:       0.70.0
Release:       alt1
Summary:       Git hook manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета overcommit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(overcommit) = 0.70.0
Requires:      gem(childprocess) >= 0.6.3
Requires:      gem(iniparse) >= 1.4
Requires:      gem(rexml) >= 3.3.9
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8.0
Conflicts:     gem(childprocess) >= 6
Conflicts:     gem(iniparse) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1

%description   -n gem-overcommit-devel
Git hook manager development package.

Utility to install, configure, and extend Git hooks

%description   -n gem-overcommit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета overcommit.
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
%doc CHANGELOG.md CONTRIBUTING.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n overcommit
%doc CHANGELOG.md CONTRIBUTING.md MIT-LICENSE README.md
%_bindir/overcommit

%if_enabled    doc
%files         -n gem-overcommit-doc
%doc CHANGELOG.md CONTRIBUTING.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-overcommit-devel
%doc CHANGELOG.md CONTRIBUTING.md MIT-LICENSE README.md
%endif


%changelog
* Sun May 31 2026 Pavel Skrylev <majioa@altlinux.org> 0.70.0-alt1
- ^ 0.63.0 -> 0.70.0

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.63.0-alt1
- ^ 0.60.0 -> 0.63.0

* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.60.0-alt1
- + packaged gem with Ruby Policy 2.0
