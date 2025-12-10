%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname snaky_hash

Name:          gem-snaky-hash
Version:       2.0.3
Release:       alt1
Summary:       A very snaky hash
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/snaky_hash
Vcs:           https://gitlab.com/oauth-xx/snaky_hash.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(backports) >= 3.25.1
BuildRequires: gem(benchmark) >= 0.4
BuildRequires: gem(bundler-audit) >= 0.9.2
BuildRequires: gem(hashie) >= 0.1.0
BuildRequires: gem(kettle-soup-cover) >= 1.0.6
BuildRequires: gem(kramdown) >= 2.3.1
BuildRequires: gem(kramdown-parser-gfm) >= 1.1
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(reek) >= 6.4
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-block_is_expected) >= 1.0.6
BuildRequires: gem(rspec-pending_for) >= 0.1.17
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-lts) >= 8.1.1
BuildRequires: gem(rubocop-packaging) >= 0.5
BuildRequires: gem(rubocop-rspec) >= 3.2
BuildRequires: gem(standard) >= 1.47
BuildRequires: gem(stone_checksums) >= 1.0
BuildRequires: gem(version_gem) >= 1.1.8
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-junk) >= 0.0.10
BuildRequires: gem(yard-relative_markdown_links) >= 0.5.0
BuildConflicts: gem(backports) >= 4
BuildConflicts: gem(benchmark) >= 1
BuildConflicts: gem(bundler-audit) >= 0.10
BuildConflicts: gem(hashie) >= 6
BuildConflicts: gem(kettle-soup-cover) >= 2
BuildConflicts: gem(kramdown-parser-gfm) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(reek) >= 7
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-block_is_expected) >= 2
BuildConflicts: gem(rspec-pending_for) >= 1
BuildConflicts: gem(rubocop-lts) >= 9
BuildConflicts: gem(rubocop-rspec) >= 4
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(stone_checksums) >= 2
BuildConflicts: gem(version_gem) >= 3
BuildConflicts: gem(yard-junk) >= 1
BuildConflicts: gem(yard-relative_markdown_links) >= 0.6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency kramdown >= 2.3.1,kramdown < 3
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_alias_names snaky_hash,snaky-hash
Requires:      ruby >= 2.2.0
Requires:      gem(hashie) >= 0.1.0
Requires:      gem(version_gem) >= 1.1.8
Conflicts:     gem(hashie) >= 6
Conflicts:     gem(version_gem) >= 3
Provides:      gem(snaky_hash) = 2.0.3

%description
A Hashie::Mash joint to make #snakelife better


%if_enabled    doc
%package       -n gem-snaky-hash-doc
Version:       2.0.3
Release:       alt1
Summary:       A very snaky hash documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета snaky_hash
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(snaky_hash) = 2.0.3

%description   -n gem-snaky-hash-doc
A very snaky hash documentation files.

A Hashie::Mash joint to make #snakelife better

%description   -n gem-snaky-hash-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета snaky_hash.
%endif


%if_enabled    devel
%package       -n gem-snaky-hash-devel
Version:       2.0.3
Release:       alt1
Summary:       A very snaky hash development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета snaky_hash
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(snaky_hash) = 2.0.3
Requires:      gem(appraisal) >= 0
Requires:      gem(backports) >= 3.25.1
Requires:      gem(benchmark) >= 0.4
Requires:      gem(bundler-audit) >= 0.9.2
Requires:      gem(hashie) >= 0.1.0
Requires:      gem(kettle-soup-cover) >= 1.0.6
Requires:      gem(kramdown) >= 2.3.1
Requires:      gem(kramdown-parser-gfm) >= 1.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(reek) >= 6.4
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-block_is_expected) >= 1.0.6
Requires:      gem(rspec-pending_for) >= 0.1.17
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-lts) >= 8.1.1
Requires:      gem(rubocop-packaging) >= 0.5
Requires:      gem(rubocop-rspec) >= 3.2
Requires:      gem(standard) >= 1.47
Requires:      gem(stone_checksums) >= 1.0
Requires:      gem(version_gem) >= 1.1.8
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-junk) >= 0.0.10
Requires:      gem(yard-relative_markdown_links) >= 0.5.0
Conflicts:     gem(backports) >= 4
Conflicts:     gem(benchmark) >= 1
Conflicts:     gem(bundler-audit) >= 0.10
Conflicts:     gem(hashie) >= 6
Conflicts:     gem(kettle-soup-cover) >= 2
Conflicts:     gem(kramdown-parser-gfm) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(reek) >= 7
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-block_is_expected) >= 2
Conflicts:     gem(rspec-pending_for) >= 1
Conflicts:     gem(rubocop-lts) >= 9
Conflicts:     gem(rubocop-rspec) >= 4
Conflicts:     gem(standard) >= 2
Conflicts:     gem(stone_checksums) >= 2
Conflicts:     gem(version_gem) >= 3
Conflicts:     gem(yard-junk) >= 1
Conflicts:     gem(yard-relative_markdown_links) >= 0.6

%description   -n gem-snaky-hash-devel
A very snaky hash development package.

A Hashie::Mash joint to make #snakelife better

%description   -n gem-snaky-hash-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета snaky_hash.
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
%files         -n gem-snaky-hash-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-snaky-hash-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.txt README.md
%endif


%changelog
* Sat Nov 29 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.3-alt1
- ^ 2.0.1.2 -> 2.0.3

* Fri Apr 19 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.1.2-alt0.1
- ^ 2.0.1 -> 2.0.1p2

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
