%define        gemname smart_proxy_onboard

Name:          gem-smart-proxy-onboard
Version:       0.2.1
Release:       alt1
Summary:       Support functions for onboarding new servers into Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart_proxy_onboard
Vcs:           https://github.com/theforeman/smart_proxy_onboard.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(concurrent-ruby) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names smart_proxy_onboard,smart-proxy-onboard
Requires:      gem(concurrent-ruby) >= 0
Provides:      gem(smart_proxy_onboard) = 0.2.1


%description
This plugin exposes API calls that can be used to onboard new hosts in bulk into
Foreman through PXE boot and the foreman_discovery image.


%package       -n gem-smart-proxy-onboard-doc
Version:       0.2.1
Release:       alt1
Summary:       Support functions for onboarding new servers into Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy_onboard
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy_onboard) = 0.2.1

%description   -n gem-smart-proxy-onboard-doc
Support functions for onboarding new servers into Foreman documentation
files.

This plugin exposes API calls that can be used to onboard new hosts in bulk into
Foreman through PXE boot and the foreman_discovery image.

%description   -n gem-smart-proxy-onboard-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy_onboard.


%package       -n gem-smart-proxy-onboard-devel
Version:       0.2.1
Release:       alt1
Summary:       Support functions for onboarding new servers into Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy_onboard
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy_onboard) = 0.2.1
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(rack) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(mocha) >= 0
Requires:      gem(webmock) >= 0

%description   -n gem-smart-proxy-onboard-devel
Support functions for onboarding new servers into Foreman development
package.

This plugin exposes API calls that can be used to onboard new hosts in bulk into
Foreman through PXE boot and the foreman_discovery image.

%description   -n gem-smart-proxy-onboard-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy_onboard.


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

%files         -n gem-smart-proxy-onboard-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-smart-proxy-onboard-devel
%doc README.md


%changelog
* Thu Sep 22 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
