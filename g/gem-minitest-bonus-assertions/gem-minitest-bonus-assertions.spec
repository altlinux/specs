%define        gemname minitest-bonus-assertions

Name:          gem-minitest-bonus-assertions
Version:       3.0
Release:       alt1.1
Summary:       Bonus assertions for {Minitest}
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitest-bonus-assertions
Vcs:           https://github.com/halostatue/minitest-bonus-assertions.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5.10
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git) >= 1.6
BuildRequires: gem(hoe-travis) >= 1.2
BuildRequires: gem(minitest-around) >= 0.3
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-bisect) >= 1.2
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(minitest-moar) >= 0.0
BuildRequires: gem(minitest-pretty_diff) >= 0.1
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(coveralls) >= 0.7
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 3.16
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git) >= 2
BuildConflicts: gem(hoe-travis) >= 2
BuildConflicts: gem(minitest-around) >= 1
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-bisect) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(minitest-moar) >= 1
BuildConflicts: gem(minitest-pretty_diff) >= 1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(coveralls) >= 1
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(minitest-bonus-assertions) = 3.0


%description
Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest],
providing assertions I use frequently, supporting only Ruby 2.0 or better.


%package       -n gem-minitest-bonus-assertions-doc
Version:       3.0
Release:       alt1.1
Summary:       Bonus assertions for {Minitest} documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-bonus-assertions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-bonus-assertions) = 3.0

%description   -n gem-minitest-bonus-assertions-doc
Bonus assertions for {Minitest} documentation files.

Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest],
providing assertions I use frequently, supporting only Ruby 2.0 or better.

%description   -n gem-minitest-bonus-assertions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-bonus-assertions.


%package       -n gem-minitest-bonus-assertions-devel
Version:       3.0
Release:       alt1.1
Summary:       Bonus assertions for {Minitest} development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-bonus-assertions
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-bonus-assertions) = 3.0
Requires:      gem(minitest) >= 5.10
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git) >= 1.6
Requires:      gem(hoe-travis) >= 1.2
Requires:      gem(minitest-around) >= 0.3
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-bisect) >= 1.2
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(minitest-moar) >= 0.0
Requires:      gem(minitest-pretty_diff) >= 0.1
Requires:      gem(rake) >= 10.0
Requires:      gem(simplecov) >= 0.7
Requires:      gem(coveralls) >= 0.7
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 3.16
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git) >= 2
Conflicts:     gem(hoe-travis) >= 2
Conflicts:     gem(minitest-around) >= 1
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-bisect) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(minitest-moar) >= 1
Conflicts:     gem(minitest-pretty_diff) >= 1
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(coveralls) >= 1
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 4

%description   -n gem-minitest-bonus-assertions-devel
Bonus assertions for {Minitest} development package.

Bonus assertions for {Minitest}[https://github.com/seattlerb/minitest],
providing assertions I use frequently, supporting only Ruby 2.0 or better.

%description   -n gem-minitest-bonus-assertions-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-bonus-assertions.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-minitest-bonus-assertions-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitest-bonus-assertions-devel
%doc README.rdoc


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 3.0-alt1.1
- ! closes build deps under check condition

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 3.0-alt1
- + packaged gem with Ruby Policy 2.0
