%define        gemname oauth

Name:          gem-oauth
Version:       0.5.6
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
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(actionpack) >= 5.0
BuildRequires: gem(iconv) >= 0
BuildRequires: gem(rack) >= 2.0 gem(rack) < 3
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(mocha) >= 0.9.12 gem(mocha) < 2
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(em-http-request) >= 0.2.11
BuildRequires: gem(curb) >= 0
BuildRequires: gem(webmock) >= 3.13.0 gem(webmock) < 4
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(rest-client) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
Provides:      gem(oauth) = 0.5.6


%description
This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.


%package       -n oauth
Version:       0.5.6
Release:       alt1
Summary:       OAuth Core Ruby implementation executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета oauth
Group:         Other
BuildArch:     noarch

Requires:      gem(oauth) = 0.5.6

%description   -n oauth
OAuth Core Ruby implementation executable(s).

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n oauth -l ru_RU.UTF-8
Исполнямка для самоцвета oauth.


%package       -n gem-oauth-doc
Version:       0.5.6
Release:       alt1
Summary:       OAuth Core Ruby implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth) = 0.5.6

%description   -n gem-oauth-doc
OAuth Core Ruby implementation documentation files.

This is a RubyGem for implementing both OAuth clients and servers in Ruby
applications.

%description   -n gem-oauth-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth.


%package       -n gem-oauth-devel
Version:       0.5.6
Release:       alt1
Summary:       OAuth Core Ruby implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth) = 0.5.6
Requires:      apache2-devel >= 2.2.5
Requires:      zlib-devel
Requires:      libapr1-devel
Requires:      libaprutil1-devel
Requires:      libssl-devel
Requires:      libcurl-devel
Requires:      apache2-httpd-worker
Requires:      gcc-c++
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(actionpack) >= 5.0
Requires:      gem(iconv) >= 0
Requires:      gem(rack) >= 2.0 gem(rack) < 3
Requires:      gem(rack-test) >= 0
Requires:      gem(mocha) >= 0.9.12 gem(mocha) < 2
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(em-http-request) >= 0.2.11
Requires:      gem(curb) >= 0
Requires:      gem(webmock) >= 3.13.0 gem(webmock) < 4
Requires:      gem(codeclimate-test-reporter) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(rest-client) >= 0

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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n oauth
%doc README.rdoc
%_bindir/oauth

%files         -n gem-oauth-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-oauth-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6-alt1
- + packaged gem with Ruby Policy 2.0
