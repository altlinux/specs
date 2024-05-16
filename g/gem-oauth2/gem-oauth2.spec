%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname oauth2

Name:          gem-oauth2
Version:       2.0.9
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oauth-xx/oauth2
Vcs:           https://github.com/oauth-xx/oauth2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(addressable) >= 2
BuildRequires: gem(backports) >= 3
BuildRequires: gem(bundler) >= 2
BuildRequires: gem(rexml) >= 3
BuildRequires: gem(rspec-block_is_expected) >= 0
BuildRequires: gem(rspec-pending_for) >= 0
BuildRequires: gem(rspec-stubbed_env) >= 0
BuildRequires: gem(rubocop-lts) >= 8.0
BuildRequires: gem(silent_stream) >= 0
BuildRequires: gem(rake) >= 12
BuildRequires: gem(rspec) >= 3
BuildRequires: gem(overcommit) >= 0.58
BuildRequires: gem(rubocop-md) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(rubocop-thread_safety) >= 0
BuildRequires: gem(codecov) >= 0.6
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(simplecov-json) >= 0
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(faraday) >= 0.17.3
BuildRequires: gem(jwt) >= 1.0
BuildRequires: gem(multi_xml) >= 0.5
BuildRequires: gem(rack) >= 1.2
BuildRequires: gem(snaky_hash) >= 2.0
BuildRequires: gem(version_gem) >= 1.1
BuildConflicts: gem(rubocop-lts) >= 25
BuildConflicts: gem(overcommit) >= 1
BuildConflicts: gem(codecov) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(jwt) >= 3
BuildConflicts: gem(multi_xml) >= 1
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(snaky_hash) >= 3
BuildConflicts: gem(version_gem) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rubocop-lts < 25
Requires:      gem(faraday) >= 0.17.3
Requires:      gem(jwt) >= 1.0
Requires:      gem(multi_xml) >= 0.5
Requires:      gem(rack) >= 1.2
Requires:      gem(snaky_hash) >= 2.0
Requires:      gem(version_gem) >= 1.1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(jwt) >= 3
Conflicts:     gem(multi_xml) >= 1
Conflicts:     gem(rack) >= 4
Conflicts:     gem(snaky_hash) >= 3
Conflicts:     gem(version_gem) >= 2
Obsoletes:     ruby-oauth2 < %EVR
Provides:      ruby-oauth2 = %EVR
Provides:      gem(oauth2) = 2.0.9


%description
A Ruby wrapper for the OAuth 2.0 protocol.


%if_enabled    doc
%package       -n gem-oauth2-doc
Version:       2.0.9
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth2) = 2.0.9

%description   -n gem-oauth2-doc
A Ruby wrapper for the OAuth 2.0 protocol documentation files.
%description   -n gem-oauth2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth2.
%endif


%if_enabled    devel
%package       -n gem-oauth2-devel
Version:       2.0.9
Release:       alt1
Summary:       A Ruby wrapper for the OAuth 2.0 protocol development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth2) = 2.0.9
Requires:      gem(addressable) >= 2
Requires:      gem(backports) >= 3
Requires:      gem(bundler) >= 2
Requires:      gem(rexml) >= 3
Requires:      gem(rspec-block_is_expected) >= 0
Requires:      gem(rspec-pending_for) >= 0
Requires:      gem(rspec-stubbed_env) >= 0
Requires:      gem(rubocop-lts) >= 8.0
Requires:      gem(silent_stream) >= 0
Requires:      gem(rake) >= 12
Requires:      gem(rspec) >= 3
Requires:      gem(overcommit) >= 0.58
Requires:      gem(rubocop-md) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(rubocop-thread_safety) >= 0
Requires:      gem(codecov) >= 0.6
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(simplecov-json) >= 0
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(byebug) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0
Conflicts:     gem(rubocop-lts) >= 25
Conflicts:     gem(overcommit) >= 1
Conflicts:     gem(codecov) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-oauth2-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-oauth2-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.9-alt1
- ^ 1.4.4 -> 2.0.9

* Thu Oct 20 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1.1
- ! fix gem build requires to novel gems

* Wed Dec 02 2020 Pavel Skrylev <majioa@altlinux.org> 1.4.4-alt1
- > Ruby Policy 2.0
- ^ 1.4.1 -> 1.4.4

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.4.1-alt1
- Initial build for Sisyphus
