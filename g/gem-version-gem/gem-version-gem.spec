%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname version_gem

Name:          gem-version-gem
Version:       1.1.9
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/version_gem
Vcs:           https://gitlab.com/oauth-xx/version_gem/-/tree/v1.1.1.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal2) >= 3.0
BuildRequires: gem(benchmark) >= 0.4.1
BuildRequires: gem(bundler-audit) >= 0.9.2
BuildRequires: gem(gitmoji-regex) >= 1.0.3
BuildRequires: gem(kettle-dev) >= 1.1.3
BuildRequires: gem(kettle-soup-cover) >= 1.0.10
BuildRequires: gem(kettle-test) >= 1.0
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(reek) >= 6.5
BuildRequires: gem(require_bench) >= 1.0.4
BuildRequires: gem(rspec-pending_for) >= 0.0.17
BuildRequires: gem(rubocop-lts) >= 8.0
BuildRequires: gem(rubocop-on-rbs) >= 1.8
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(rubocop-ruby2_2) >= 0
BuildRequires: gem(ruby-progressbar) >= 1.13
BuildRequires: gem(standard) >= 1.50
BuildRequires: gem(stone_checksums) >= 1.0.2
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0.10
BuildRequires: gem(yard-relative_markdown_links) >= 0.5.0
BuildConflicts: gem(appraisal2) >= 4
BuildConflicts: gem(benchmark) >= 1
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(gitmoji-regex) >= 2
BuildConflicts: gem(kettle-dev) >= 2
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kettle-test) >= 2
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(require_bench) >= 2
BuildConflicts: gem(rspec-pending_for) >= 1
BuildConflicts: gem(rubocop-lts) >= 9
BuildConflicts: gem(rubocop-on-rbs) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(ruby-progressbar) >= 2
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-relative_markdown_links) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_alias_names version_gem,version-gem
Requires:      ruby >= 2.2
Provides:      gem(version_gem) = 1.1.9

%description
Versions are good. Versions are cool. Versions will win.


%if_enabled    doc
%package       -n gem-version-gem-doc
Version:       1.1.9
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета version_gem
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(version_gem) = 1.1.9

%description   -n gem-version-gem-doc
Enhance your VERSION! Sugar for Version modules documentation files.

Versions are good. Versions are cool. Versions will win.

%description   -n gem-version-gem-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета version_gem.
%endif


%if_enabled    devel
%package       -n gem-version-gem-devel
Version:       1.1.9
Release:       alt1
Summary:       Enhance your VERSION! Sugar for Version modules development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета version_gem
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(version_gem) = 1.1.9
Requires:      gem(appraisal2) >= 3.0
Requires:      gem(bundler-audit) >= 0.9.2
Requires:      gem(gitmoji-regex) >= 1.0.3
Requires:      gem(kettle-dev) >= 1.1.3
Requires:      gem(kettle-test) >= 1.0
Requires:      gem(rake) >= 13.0
Requires:      gem(require_bench) >= 1.0.4
Requires:      gem(rspec-pending_for) >= 0.0.17
Requires:      gem(ruby-progressbar) >= 1.13
Requires:      gem(stone_checksums) >= 1.0.2
Requires:      gem(benchmark) >= 0.4.1
Requires:      gem(kettle-soup-cover) >= 1.0.10
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(reek) >= 6.5
Requires:      gem(rubocop-on-rbs) >= 1.8
Requires:      gem(standard) >= 1.50
Requires:      gem(yard-relative_markdown_links) >= 0.5.0
Conflicts:     gem(kettle-soup-cover) >= 2
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(reek) >= 7
Conflicts:     gem(rubocop-on-rbs) >= 2
Conflicts:     gem(yard-relative_markdown_links) >= 0.6
Conflicts:     gem(benchmark) >= 1
Conflicts:     gem(appraisal2) >= 4
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(gitmoji-regex) >= 2
Conflicts:     gem(kettle-dev) >= 2
Conflicts:     gem(kettle-test) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(require_bench) >= 2
Conflicts:     gem(rspec-pending_for) >= 1
Conflicts:     gem(ruby-progressbar) >= 2
Conflicts:     gem(stone_checksums) >= 2

%description   -n gem-version-gem-devel
Enhance your VERSION! Sugar for Version modules development package.

Versions are good. Versions are cool. Versions will win.

%description   -n gem-version-gem-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета version_gem.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-version-gem-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-version-gem-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Fri Oct 17 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.9-alt1
- ^ 1.1.3 -> 1.1.9

* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- ^ 1.1.1 -> 1.1.3

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
