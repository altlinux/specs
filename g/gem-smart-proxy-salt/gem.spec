%define        gemname smart_proxy_salt

Name:          gem-smart-proxy-salt
Version:       2.1.9
Release:       alt1
Summary:       SaltStack Plug-In for Foreman's Smart Proxy
License:       GPLv3
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_salt
Vcs:           https://github.com/theforeman/smart_proxy_salt.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%ruby_alias_names smart_proxy_salt,smart-proxy-salt
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(smart_proxy_salt) = 2.1.9


%description
This plug-in adds support for Salt to Foreman's Smart Proxy.


%package       -n gem-smart-proxy-salt-doc
Version:       2.1.9
Release:       alt1
Summary:       SaltStack Plug-In for Foreman's Smart Proxy documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_salt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_salt) = 2.1.9

%description   -n gem-smart-proxy-salt-doc
SaltStack Plug-In for Foreman's Smart Proxy documentation files.

This plug-in adds support for Salt to Foreman's Smart Proxy.

%description   -n gem-smart-proxy-salt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_salt.


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

%files         -n gem-smart-proxy-salt-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Nov 19 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.9-alt1
- + packaged gem with Ruby Policy 2.0
