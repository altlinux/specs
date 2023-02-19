%define        gemname overcommit

Name:          gem-overcommit
Version:       0.60.0
Release:       alt1
Summary:       Git hook manager
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sds/overcommit
Vcs:           https://github.com/sds/overcommit.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-lcov) >= 0.8.0
BuildRequires: gem(rubocop) >= 0.82.0
BuildRequires: gem(childprocess) >= 0.6.3
BuildRequires: gem(iniparse) >= 1.4
BuildRequires: gem(rexml) >= 3.2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 0.9
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(childprocess) >= 5
BuildConflicts: gem(iniparse) >= 2
BuildConflicts: gem(rexml) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(childprocess) >= 0.6.3
Requires:      gem(iniparse) >= 1.4
Requires:      gem(rexml) >= 3.2
Conflicts:     gem(childprocess) >= 5
Conflicts:     gem(iniparse) >= 2
Conflicts:     gem(rexml) >= 4
Provides:      gem(overcommit) = 0.60.0


%description
Utility to install, configure, and extend Git hooks


%package       -n overcommit
Version:       0.60.0
Release:       alt1
Summary:       Git hook manager executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета overcommit
Group:         Other
BuildArch:     noarch

Requires:      gem(overcommit) = 0.60.0

%description   -n overcommit
Git hook manager executable(s).

Utility to install, configure, and extend Git hooks

%description   -n overcommit -l ru_RU.UTF-8
Исполнямка для самоцвета overcommit.


%package       -n gem-overcommit-doc
Version:       0.60.0
Release:       alt1
Summary:       Git hook manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета overcommit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(overcommit) = 0.60.0

%description   -n gem-overcommit-doc
Git hook manager documentation files.

Utility to install, configure, and extend Git hooks

%description   -n gem-overcommit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета overcommit.


%package       -n gem-overcommit-devel
Version:       0.60.0
Release:       alt1
Summary:       Git hook manager development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета overcommit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(overcommit) = 0.60.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-lcov) >= 0.8.0
Requires:      gem(rubocop) >= 0.82.0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 0.9
Conflicts:     gem(rubocop) >= 2

%description   -n gem-overcommit-devel
Git hook manager development package.

Utility to install, configure, and extend Git hooks

%description   -n gem-overcommit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета overcommit.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n overcommit
%_bindir/overcommit

%files         -n gem-overcommit-doc
%ruby_gemdocdir

%files         -n gem-overcommit-devel


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.60.0-alt1
- + packaged gem with Ruby Policy 2.0
