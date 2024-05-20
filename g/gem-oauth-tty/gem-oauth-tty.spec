%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname oauth-tty

Name:          gem-oauth-tty
Version:       1.0.5.2
Release:       alt0.2
Summary:       OAuth 1.0 TTY CLI
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/oauth-tty
Vcs:           https://gitlab.com/oauth-xx/oauth-tty.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix-dep-to-oauth.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(oauth) >= 1.1.0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(codecov) >= 0.6
BuildRequires: gem(overcommit) >= 0.58
BuildRequires: gem(rubocop-md) >= 0
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-packaging) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-thread_safety) >= 0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(simplecov-cobertura) >= 0
BuildRequires: gem(simplecov-json) >= 0
BuildRequires: gem(simplecov-lcov) >= 0.8
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(curb) > 0.8.7
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(github-markup) >= 0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(minitest) >= 5.15.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(em-http-request) >= 1.1.7
BuildRequires: gem(iconv) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop-lts) >= 18.0
BuildRequires: gem(version_gem) >= 1.1.1
BuildConflicts: gem(codecov) >= 1
BuildConflicts: gem(overcommit) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(curb) >= 1.1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(webmock) > 3.19.0
BuildConflicts: gem(em-http-request) >= 1.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(version_gem) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-lts >= 23.0
%ruby_use_gem_dependency rack >= 3.0
Requires:      gem(version_gem) >= 1.1.1
Requires:      gem(oauth) >= 1.1.0
Conflicts:     gem(version_gem) >= 2
Provides:      gem(oauth-tty) = 1.0.5.2

%ruby_use_gem_version oauth-tty:1.0.5.2

%description
OAuth 1.0 TTY Command Line Interface.


%package       -n oauth
Version:       1.0.5.2
Release:       alt0.2
Summary:       OAuth 1.0 TTY CLI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета oauth-tty
Group:         Other
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.5.2

%description   -n oauth
OAuth 1.0 TTY CLI executable(s).

OAuth 1.0 TTY Command Line Interface.
%description   -n oauth -l ru_RU.UTF-8
Исполнямка для самоцвета oauth-tty.


%if_enabled    doc
%package       -n gem-oauth-tty-doc
Version:       1.0.5.2
Release:       alt0.2
Summary:       OAuth 1.0 TTY CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth-tty
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.5.2

%description   -n gem-oauth-tty-doc
OAuth 1.0 TTY CLI documentation files.

OAuth 1.0 TTY Command Line Interface.
%description   -n gem-oauth-tty-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth-tty.
%endif


%if_enabled    devel
%package       -n gem-oauth-tty-devel
Version:       1.0.5.2
Release:       alt0.2
Summary:       OAuth 1.0 TTY CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth-tty
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.5.2
Requires:      gem(pry) >= 0
Requires:      gem(codecov) >= 0.6
Requires:      gem(overcommit) >= 0.58
Requires:      gem(rubocop-md) >= 0
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-packaging) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-thread_safety) >= 0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(simplecov-cobertura) >= 0
Requires:      gem(simplecov-json) >= 0
Requires:      gem(simplecov-lcov) >= 0.8
Requires:      gem(byebug) >= 0
Requires:      gem(curb) > 0.8.7
Requires:      gem(pry-byebug) >= 0
Requires:      gem(github-markup) >= 0
Requires:      gem(redcarpet) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(minitest) >= 5.15.0
Requires:      gem(mocha) >= 0
Requires:      gem(rack) >= 2.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rest-client) >= 0
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(em-http-request) >= 1.1.7
Requires:      gem(iconv) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop-lts) >= 18.0
Conflicts:     gem(codecov) >= 1
Conflicts:     gem(overcommit) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(curb) >= 1.1
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rack) >= 4
Conflicts:     gem(webmock) > 3.19.0
Conflicts:     gem(em-http-request) >= 1.2
Conflicts:     gem(rake) >= 14

%description   -n gem-oauth-tty-devel
OAuth 1.0 TTY CLI development package.

OAuth 1.0 TTY Command Line Interface.
%description   -n gem-oauth-tty-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oauth-tty.
%endif


%prep
%setup
# %autopatch # NOTE raises dep exception in prod due to runtime dep to oauth

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

%files         -n oauth
%doc README.md
%_bindir/oauth

%if_enabled    doc
%files         -n gem-oauth-tty-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-oauth-tty-devel
%doc README.md
%endif


%changelog
* Mon May 20 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.5.2-alt0.2
- ! dep to rack and rubocop-lts

* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.5.2-alt0.1
- ^ 1.0.5 -> 1.0.5p2
- ! fixed dep to oauth gem

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
