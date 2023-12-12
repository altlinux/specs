%define        _unpackaged_files_terminate_build 1
%define        gemname oauth

Name:          gem-oauth
Version:       1.1.0.18
Release:       alt0.1
Summary:       OAuth Core Ruby implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oauth-xx/oauth-ruby
Vcs:           https://github.com/oauth-xx/oauth-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires(pre): rpm-macros-apache2
BuildRequires: %(eval echo %apache2_apr_buildreq)
BuildRequires: apache2-devel >= 2.2.5
BuildRequires: zlib-devel
BuildRequires: libapr1-devel
BuildRequires: libaprutil1-devel
BuildRequires: libssl-devel
BuildRequires: libcurl-devel
BuildRequires: apache2-httpd-worker
BuildRequires: gcc-c++
%if_with check
BuildRequires: gem(em-http-request) >= 1.1.7
BuildRequires: gem(iconv) >= 0
BuildRequires: gem(minitest) >= 5.15.0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rubocop-lts) >= 18.0
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(pry) >= 0
BuildRequires: gem(codecov) >= 0.6
BuildRequires: gem(overcommit) >= 0.58
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
BuildRequires: gem(oauth-tty) >= 1.0.1
BuildRequires: gem(snaky_hash) >= 2.0
BuildRequires: gem(version_gem) >= 1.1
BuildConflicts: gem(em-http-request) >= 1.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rack) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop-lts) >= 23
BuildConflicts: gem(webmock) > 3.19.0
BuildConflicts: gem(codecov) >= 1
BuildConflicts: gem(overcommit) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(curb) >= 1.1
BuildConflicts: gem(oauth-tty) >= 2
BuildConflicts: gem(snaky_hash) >= 3
BuildConflicts: gem(version_gem) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-lts >= 22.0.1,rubocop-lts < 23
Requires:      gem(oauth-tty) >= 1.0.1
Requires:      gem(snaky_hash) >= 2.0
Requires:      gem(version_gem) >= 1.1
Conflicts:     gem(oauth-tty) >= 2
Conflicts:     gem(snaky_hash) >= 3
Conflicts:     gem(version_gem) >= 2
Provides:      gem(oauth) = 1.1.0.18

%ruby_use_gem_version oauth:1.1.0.18

%description
This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.


%package       -n gem-oauth-doc
Version:       1.1.0.18
Release:       alt0.1
Summary:       OAuth Core Ruby implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth) = 1.1.0.18

%description   -n gem-oauth-doc
OAuth Core Ruby implementation documentation files.

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n gem-oauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth.


%package       -n gem-oauth-devel
Version:       1.1.0.18
Release:       alt0.1
Summary:       OAuth Core Ruby implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth) = 1.1.0.18
Requires:      gem(em-http-request) >= 1.1.7
Requires:      gem(iconv) >= 0
Requires:      gem(minitest) >= 5.15.0
Requires:      gem(mocha) >= 0
Requires:      gem(rack) >= 2.0
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 13.0
Requires:      gem(rest-client) >= 0
Requires:      gem(rubocop-lts) >= 18.0
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(pry) >= 0
Requires:      gem(codecov) >= 0.6
Requires:      gem(overcommit) >= 0.58
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
Requires:      apache2-devel >= 2.2.5
Requires:      zlib-devel
Requires:      libapr1-devel
Requires:      libaprutil1-devel
Requires:      libssl-devel
Requires:      libcurl-devel
Requires:      apache2-httpd-worker
Requires:      gcc-c++
Conflicts:     gem(em-http-request) >= 1.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rack) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop-lts) >= 23
Conflicts:     gem(webmock) > 3.19.0
Conflicts:     gem(codecov) >= 1
Conflicts:     gem(overcommit) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(curb) >= 1.1

%description   -n gem-oauth-devel
OAuth Core Ruby implementation development package.

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n gem-oauth-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oauth.


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

%files         -n gem-oauth-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-oauth-devel
%doc README.md


%changelog
* Mon Dec 11 2023 Pavel Skrylev <majioa@altlinux.org> 1.1.0.18-alt0.1
- ^ 1.1.0[1] -> 1.1.0p18

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0.1-alt1
- ^ 1.1.0 -> 1.1.0[1]

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 0.5.6 -> 1.1.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6-alt1
- + packaged gem with Ruby Policy 2.0
