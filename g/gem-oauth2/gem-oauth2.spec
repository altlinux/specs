%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname oauth2

Name:          gem-oauth2
Version:       2.0.18
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oauth-xx/oauth2
Vcs:           https://github.com/oauth-xx/oauth2.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(addressable) >= 2.8.0
BuildRequires: gem(appraisal2) >= 3.0
BuildRequires: gem(backports) >= 3.25.1
BuildRequires: gem(benchmark) >= 0.4.1
BuildRequires: gem(bundler-audit) >= 0.9.2
BuildRequires: gem(erb) >= 5.0
BuildRequires: gem(faraday) >= 0.17.3
BuildRequires: gem(gem_bench) >= 2.0.5
BuildRequires: gem(gitmoji-regex) >= 1.0.3
BuildRequires: gem(irb) >= 1.15.2
BuildRequires: gem(jwt) >= 1.0
BuildRequires: gem(kettle-dev) >= 1.1
BuildRequires: gem(kettle-soup-cover) >= 1.0.10
BuildRequires: gem(kettle-test) >= 1.0.6
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(logger) >= 1.2
BuildRequires: gem(multi_xml) >= 0.5
BuildRequires: gem(mutex_m) >= 0.2
BuildRequires: gem(nkf) >= 0.2
BuildRequires: gem(rack) >= 1.2
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(reek) >= 6.5
BuildRequires: gem(require_bench) >= 1.0.4
BuildRequires: gem(rexml) >= 3.2.5
BuildRequires: gem(rubocop-lts) >= 8.0
BuildRequires: gem(rubocop-on-rbs) >= 1.8
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-rspec) >= 3.6
BuildRequires: gem(rubocop-ruby2_2) >= 0
BuildRequires: gem(ruby-progressbar) >= 1.13
BuildRequires: gem(snaky_hash) >= 2.0.3
BuildRequires: gem(standard) >= 1.50
BuildRequires: gem(stone_checksums) >= 1.0.2
BuildRequires: gem(stringio) >= 3.0
BuildRequires: gem(version_gem) >= 1.1.9
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-fence) >= 0.4
BuildRequires: gem(yard-junk) >= 0.0.10
BuildRequires: gem(yard-relative_markdown_links) >= 0.5.0
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(appraisal2) >= 4
BuildConflicts: gem(backports) >= 4
BuildConflicts: gem(benchmark) >= 1
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(erb) >= 6
BuildConflicts: gem(faraday) >= 4.0
BuildConflicts: gem(gem_bench) >= 3
BuildConflicts: gem(gitmoji-regex) >= 2
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(jwt) >= 4.0
BuildConflicts: gem(kettle-dev) >= 2
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kettle-test) >= 2
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(logger) >= 2
BuildConflicts: gem(multi_xml) >= 1
BuildConflicts: gem(mutex_m) >= 1
BuildConflicts: gem(nkf) >= 1
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(require_bench) >= 2
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rubocop-lts) >= 9
BuildConflicts: gem(rubocop-on-rbs) >= 2
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(ruby-progressbar) >= 2
BuildConflicts: gem(snaky_hash) >= 3
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(version_gem) >= 2
BuildConflicts: gem(yard-fence) >= 1
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-relative_markdown_links) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency addressable >= 2.8.0,addressable < 3
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
Requires:      ruby >= 2.2.0
Requires:      gem(faraday) >= 0.17.3
Requires:      gem(jwt) >= 1.0
Requires:      gem(logger) >= 1.2
Requires:      gem(rack) >= 1.2
Requires:      gem(snaky_hash) >= 2.0.3
Requires:      gem(version_gem) >= 1.1.9
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(faraday) >= 4.0
Conflicts:     gem(jwt) >= 4.0
Conflicts:     gem(logger) >= 2
Conflicts:     gem(rack) >= 4
Conflicts:     gem(version_gem) >= 2
Obsoletes:     ruby-oauth2 < %EVR
Provides:      ruby-oauth2 = %EVR
Provides:      gem(oauth2) = 2.0.18

%description
A Ruby wrapper for the OAuth 2.0 protocol.


%if_enabled    doc
%package       -n gem-oauth2-doc
Version:       2.0.18
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth2
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(oauth2) = 2.0.18

%description   -n gem-oauth2-doc
A Ruby wrapper for the OAuth 2.0 protocol documentation files.

%description   -n gem-oauth2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth2.
%endif


%if_enabled    devel
%package       -n gem-oauth2-devel
Version:       2.0.18
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth2
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(oauth2) = 2.0.18
Requires:      gem(addressable) >= 2.8.0
Requires:      gem(appraisal2) >= 3.0
Requires:      gem(backports) >= 3.25.1
Requires:      gem(benchmark) >= 0.4.1
Requires:      gem(bundler-audit) >= 0.9.2
Requires:      gem(erb) >= 5.0
Requires:      gem(faraday) >= 0.17.3
Requires:      gem(gem_bench) >= 2.0.5
Requires:      gem(gitmoji-regex) >= 1.0.3
Requires:      gem(irb) >= 1.15.2
Requires:      gem(jwt) >= 1.0
Requires:      gem(kettle-dev) >= 1.1
Requires:      gem(kettle-soup-cover) >= 1.0.10
Requires:      gem(kettle-test) >= 1.0.6
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(logger) >= 1.2
Requires:      gem(multi_xml) >= 0.5
Requires:      gem(mutex_m) >= 0.2
Requires:      gem(nkf) >= 0.2
Requires:      gem(rack) >= 1.2
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(reek) >= 6.5
Requires:      gem(require_bench) >= 1.0.4
Requires:      gem(rexml) >= 3.2.5
Requires:      gem(rubocop-lts) >= 8.0
Requires:      gem(rubocop-on-rbs) >= 1.8
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-rspec) >= 3.6
Requires:      gem(rubocop-ruby2_2) >= 0
Requires:      gem(ruby-progressbar) >= 1.13
Requires:      gem(snaky_hash) >= 2.0.3
Requires:      gem(standard) >= 1.50
Requires:      gem(stone_checksums) >= 1.0.2
Requires:      gem(stringio) >= 3.0
Requires:      gem(version_gem) >= 1.1.9
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-fence) >= 0.4
Requires:      gem(yard-junk) >= 0.0.10
Requires:      gem(yard-relative_markdown_links) >= 0.5.0
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(appraisal2) >= 4
Conflicts:     gem(backports) >= 4
Conflicts:     gem(benchmark) >= 1
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(erb) >= 6
Conflicts:     gem(faraday) >= 4.0
Conflicts:     gem(gem_bench) >= 3
Conflicts:     gem(gitmoji-regex) >= 2
Conflicts:     gem(irb) >= 2
Conflicts:     gem(jwt) >= 4.0
Conflicts:     gem(kettle-dev) >= 2
Conflicts:     gem(kettle-soup-cover) >= 2
Conflicts:     gem(kettle-test) >= 2
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(logger) >= 2
Conflicts:     gem(multi_xml) >= 1
Conflicts:     gem(mutex_m) >= 1
Conflicts:     gem(nkf) >= 1
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(reek) >= 7
Conflicts:     gem(require_bench) >= 2
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(rubocop-lts) >= 9
Conflicts:     gem(rubocop-on-rbs) >= 2
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(ruby-progressbar) >= 2
Conflicts:     gem(snaky_hash) >= 3
Conflicts:     gem(stone_checksums) >= 2
Conflicts:     gem(version_gem) >= 2
Conflicts:     gem(yard-fence) >= 1
Conflicts:     gem(yard-junk) >= 1
Conflicts:     gem(yard-relative_markdown_links) >= 0.6

%description   -n gem-oauth2-devel
A Ruby wrapper for the OAuth 2.0 protocol development package.

%description   -n gem-oauth2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oauth2.
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
%files         -n gem-oauth2-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-oauth2-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Sat Nov 29 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.18-alt1
- ^ 2.0.9 -> 2.0.18

* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.9-alt1
- ^ 1.4.4 -> 2.0.9

* Thu Oct 20 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1.1
- ! fix gem build requires to novel gems

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1
- > Ruby Policy 2.0
- ^ 1.4.1 -> 1.4.4

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
