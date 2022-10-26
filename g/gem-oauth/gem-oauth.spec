%define        gemname oauth

Name:          gem-oauth
Version:       1.1.0.1
Release:       alt1
Summary:       OAuth Core Ruby implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/oauth-xx/oauth-ruby
Vcs:           https://github.com/oauth-xx/oauth-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
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
BuildRequires: gem(oauth-tty) >= 1.0.1 gem(oauth-tty) < 2
BuildRequires: gem(snaky_hash) >= 2.0 gem(snaky_hash) < 3
BuildRequires: gem(version_gem) >= 1.1 gem(version_gem) < 2
BuildRequires: gem(em-http-request) >= 1.1.7 gem(em-http-request) < 1.2
BuildRequires: gem(iconv) >= 0
BuildRequires: gem(minitest) >= 5.15.0 gem(minitest) < 6
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rack) >= 2.0 gem(rack) < 3
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rubocop-lts) >= 18.0 gem(rubocop-lts) < 23
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(webmock) <= 3.19.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version oauth:1.1.0.1
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rubocop-lts >= 22.0.1,rubocop-lts < 23
Requires:      gem(oauth-tty) >= 1.0.1 gem(oauth-tty) < 2
Requires:      gem(snaky_hash) >= 2.0 gem(snaky_hash) < 3
Requires:      gem(version_gem) >= 1.1 gem(version_gem) < 2
Provides:      gem(oauth) = 1.1.0.1


%description
This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.


%package       -n gem-oauth-doc
Version:       1.1.0.1
Release:       alt1
Summary:       OAuth Core Ruby implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth) = 1.1.0.1

%description   -n gem-oauth-doc
OAuth Core Ruby implementation documentation files.

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n gem-oauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth.


%package       -n gem-oauth-devel
Version:       1.1.0.1
Release:       alt1
Summary:       OAuth Core Ruby implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth) = 1.1.0.1
Requires:      gem(em-http-request) >= 1.1.7 gem(em-http-request) < 1.2
Requires:      gem(iconv) >= 0
Requires:      gem(minitest) >= 5.15.0 gem(minitest) < 6
Requires:      gem(mocha) >= 0
Requires:      gem(rack) >= 2.0 gem(rack) < 3
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rest-client) >= 0
Requires:      gem(rubocop-lts) >= 18.0 gem(rubocop-lts) < 23
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(webmock) <= 3.19.0
Requires:      apache2-devel >= 2.2.5
Requires:      zlib-devel
Requires:      libapr1-devel
Requires:      libaprutil1-devel
Requires:      libssl-devel
Requires:      libcurl-devel
Requires:      apache2-httpd-worker
Requires:      gcc-c++

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
* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0.1-alt1
- ^ 1.1.0 -> 1.1.0.1

* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- ^ 0.5.6 -> 1.1.0

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6-alt1
- + packaged gem with Ruby Policy 2.0
