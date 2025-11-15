%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname oauth-tty

Name:          gem-oauth-tty
Version:       1.0.6
Release:       alt1
Summary:       OAuth 1.0 TTY CLI
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/oauth-tty
Vcs:           https://gitlab.com/oauth-xx/oauth-tty.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal2) >= 3.0
BuildRequires: gem(backports) >= 3.25.1
BuildRequires: gem(benchmark) >= 0.4.1
BuildRequires: gem(bundler-audit) >= 0.9.2
BuildRequires: gem(erb) >= 5.0
BuildRequires: gem(gem_bench) >= 2.0.5
BuildRequires: gem(gitmoji-regex) >= 1.0.3
BuildRequires: gem(irb) >= 1.15.2
BuildRequires: gem(kettle-dev) >= 1.1
BuildRequires: gem(kettle-soup-cover) >= 1.0.10
BuildRequires: gem(kettle-test) >= 1.0
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(mutex_m) >= 0.2
BuildRequires: gem(oauth) >= 0
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(reek) >= 6.5
BuildRequires: gem(require_bench) >= 1.0.4
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rspec-pending_for) >= 0.0.17
BuildRequires: gem(rubocop-lts) >= 10.0
BuildRequires: gem(rubocop-on-rbs) >= 1.8
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(rubocop-ruby2_3) >= 0
BuildRequires: gem(ruby-progressbar) >= 1.13
BuildRequires: gem(standard) >= 1.50
BuildRequires: gem(stone_checksums) >= 1.0.2
BuildRequires: gem(stringio) >= 3.0
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(vcr) >= 4
BuildRequires: gem(version_gem) >= 1.1.9
BuildRequires: gem(webmock) >= 3
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0.10
BuildRequires: gem(yard-relative_markdown_links) >= 0.5.0
BuildConflicts: gem(appraisal2) >= 4
BuildConflicts: gem(backports) >= 4
BuildConflicts: gem(benchmark) >= 1
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(erb) >= 6
BuildConflicts: gem(gem_bench) >= 3
BuildConflicts: gem(gitmoji-regex) >= 2
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(kettle-dev) >= 2
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kettle-test) >= 2
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(mutex_m) >= 1
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(require_bench) >= 2
BuildConflicts: gem(rspec-pending_for) >= 1
BuildConflicts: gem(rubocop-lts) >= 11
BuildConflicts: gem(rubocop-on-rbs) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(ruby-progressbar) >= 2
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(version_gem) >= 2
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-relative_markdown_links) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rack >= 3.0.0,rack < 4
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.3.0
Requires:      gem(version_gem) >= 1.1.9
Conflicts:     gem(version_gem) >= 2
Provides:      gem(oauth-tty) = 1.0.6

%description
OAuth 1.0 TTY Command Line Interface.


%package       -n oauth
Version:       1.0.6
Release:       alt1
Summary:       OAuth 1.0 TTY CLI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета oauth-tty
Group:         Other
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.6

%description   -n oauth
OAuth 1.0 TTY CLI executable(s).

OAuth 1.0 TTY Command Line Interface.

%description   -n oauth -l ru_RU.UTF-8
Исполнямка для самоцвета oauth-tty.


%if_enabled    doc
%package       -n gem-oauth-tty-doc
Version:       1.0.6
Release:       alt1
Summary:       OAuth 1.0 TTY CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth-tty
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.6

%description   -n gem-oauth-tty-doc
OAuth 1.0 TTY CLI documentation files.

OAuth 1.0 TTY Command Line Interface.

%description   -n gem-oauth-tty-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth-tty.
%endif


%if_enabled    devel
%package       -n gem-oauth-tty-devel
Version:       1.0.6
Release:       alt1
Summary:       OAuth 1.0 TTY CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth-tty
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.6
Requires:      gem(appraisal2) >= 3.0
Requires:      gem(backports) >= 3.25.1
Requires:      gem(bundler-audit) >= 0.9.2
Requires:      gem(gitmoji-regex) >= 1.0.3
Requires:      gem(kettle-dev) >= 1.1
Requires:      gem(kettle-test) >= 1.0
Requires:      gem(mocha) >= 0
Requires:      gem(rack) >= 2.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(require_bench) >= 1.0.4
Requires:      gem(rest-client) >= 0
Requires:      gem(rspec-pending_for) >= 0.0.17
Requires:      gem(ruby-progressbar) >= 1.13
Requires:      gem(stone_checksums) >= 1.0.2
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(vcr) >= 4
Requires:      gem(webmock) >= 3
Requires:      gem(benchmark) >= 0.4.1
Requires:      gem(erb) >= 5.0
Requires:      gem(gem_bench) >= 2.0.5
Requires:      gem(irb) >= 1.15.2
Requires:      gem(kettle-soup-cover) >= 1.0.10
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(mutex_m) >= 0.2
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(reek) >= 6.5
Requires:      gem(rubocop-on-rbs) >= 1.8
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(rubocop-ruby2_3) >= 0
Requires:      gem(standard) >= 1.50
Requires:      gem(stringio) >= 3.0
Requires:      gem(yard-junk) >= 0.0.10
Requires:      gem(yard-relative_markdown_links) >= 0.5.0
Conflicts:     gem(benchmark) >= 1
Conflicts:     gem(erb) >= 6
Conflicts:     gem(gem_bench) >= 3
Conflicts:     gem(irb) >= 2
Conflicts:     gem(kettle-soup-cover) >= 2
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(mutex_m) >= 1
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(reek) >= 7
Conflicts:     gem(rubocop-on-rbs) >= 2
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(yard-junk) >= 1
Conflicts:     gem(yard-relative_markdown_links) >= 0.6
Conflicts:     gem(appraisal2) >= 4
Conflicts:     gem(backports) >= 4
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(gitmoji-regex) >= 2
Conflicts:     gem(kettle-dev) >= 2
Conflicts:     gem(kettle-test) >= 2
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(require_bench) >= 2
Conflicts:     gem(rspec-pending_for) >= 1
Conflicts:     gem(ruby-progressbar) >= 2
Conflicts:     gem(stone_checksums) >= 2

%description   -n gem-oauth-tty-devel
OAuth 1.0 TTY CLI development package.

OAuth 1.0 TTY Command Line Interface.

%description   -n gem-oauth-tty-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oauth-tty.
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

%files         -n oauth
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%_bindir/oauth

%if_enabled    doc
%files         -n gem-oauth-tty-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-oauth-tty-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Fri Oct 17 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.6-alt1
- ^ 1.0.5.2 -> 1.0.6 (closes ALT#49786)

* Mon May 20 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.5.2-alt0.2
- ! dep to rack and rubocop-lts

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.5.2-alt0.1
- ^ 1.0.5 -> 1.0.5p2
- ! fixed dep to oauth gem

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
