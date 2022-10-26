%define        gemname oauth-tty

Name:          gem-oauth-tty
Version:       1.0.5
Release:       alt1
Summary:       OAuth 1.0 TTY CLI
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/oauth-xx/oauth-tty
Vcs:           https://gitlab.com/oauth-xx/oauth-tty.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(version_gem) >= 1.1.1 gem(version_gem) < 2
BuildRequires: gem(em-http-request) >= 1.1.7 gem(em-http-request) < 1.2
BuildRequires: gem(iconv) >= 0
BuildRequires: gem(minitest) >= 5.15.0 gem(minitest) < 6
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(rack) >= 2.0 gem(rack) < 3
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rest-client) >= 0
BuildRequires: gem(rubocop-lts) >= 22.0.1 gem(rubocop-lts) < 23
BuildRequires: gem(typhoeus) >= 0.1.13
BuildRequires: gem(webmock) <= 3.19.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rubocop-lts >= 22.0.1,rubocop-lts < 23
Requires:      gem(version_gem) >= 1.1.1 gem(version_gem) < 2
Provides:      gem(oauth-tty) = 1.0.5


%description
OAuth 1.0 TTY Command Line Interface.


%package       -n oauth
Version:       1.0.5
Release:       alt1
Summary:       OAuth 1.0 TTY CLI executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета oauth-tty
Group:         Other
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.5

%description   -n oauth
OAuth 1.0 TTY CLI executable(s).

OAuth 1.0 TTY Command Line Interface.

%description   -n oauth -l ru_RU.UTF-8
Исполнямка для самоцвета oauth-tty.


%package       -n gem-oauth-tty-doc
Version:       1.0.5
Release:       alt1
Summary:       OAuth 1.0 TTY CLI documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета oauth-tty
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.5

%description   -n gem-oauth-tty-doc
OAuth 1.0 TTY CLI documentation files.

OAuth 1.0 TTY Command Line Interface.

%description   -n gem-oauth-tty-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета oauth-tty.


%package       -n gem-oauth-tty-devel
Version:       1.0.5
Release:       alt1
Summary:       OAuth 1.0 TTY CLI development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета oauth-tty
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(oauth-tty) = 1.0.5
Requires:      gem(em-http-request) >= 1.1.7 gem(em-http-request) < 1.2
Requires:      gem(iconv) >= 0
Requires:      gem(minitest) >= 5.15.0 gem(minitest) < 6
Requires:      gem(mocha) >= 0
Requires:      gem(rack) >= 2.0 gem(rack) < 3
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rest-client) >= 0
Requires:      gem(rubocop-lts) >= 22.0.1 gem(rubocop-lts) < 23
Requires:      gem(typhoeus) >= 0.1.13
Requires:      gem(webmock) <= 3.19.0

%description   -n gem-oauth-tty-devel
OAuth 1.0 TTY CLI development package.

OAuth 1.0 TTY Command Line Interface

%description   -n gem-oauth-tty-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета oauth-tty.


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

%files         -n oauth
%doc README.md
%_bindir/oauth

%files         -n gem-oauth-tty-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-oauth-tty-devel
%doc README.md


%changelog
* Thu Sep 29 2022 Pavel Skrylev <majioa@altlinux.org> 1.0.5-alt1
- + packaged gem with Ruby Policy 2.0
