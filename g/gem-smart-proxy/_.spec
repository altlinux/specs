%define        gemname smart_proxy

Name:          gem-smart-proxy
Version:       2.5.0
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart-proxy
Vcs:           https://github.com/theforeman/smart-proxy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source4:       puppetca_http_api.yml
Source3:       smart-proxy.conf
Source2:       smart-proxy.service
Source1:       settings.yml
Source:        %name-%version.tar
Patch2:        config-path.patch
Patch1:        config.patch
Patch:         2.1.0.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(json) >= 0
BuildRequires: gem(logging) >= 0
BuildRequires: gem(rack) >= 1.3
BuildRequires: gem(sd_notify) >= 0.1 gem(sd_notify) < 1
BuildRequires: gem(sinatra) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names smart_proxy,smart-proxy
Requires:      gem(json) >= 0
Requires:      gem(logging) >= 0
Requires:      gem(rack) >= 1.3
Requires:      gem(sd_notify) >= 0.1 gem(sd_notify) < 1
Requires:      gem(sinatra) >= 0
Provides:      gem(smart_proxy) = 2.5.0
Conflicts:     gem-smart-proxy-compat


%description
Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy


%package       -n smart-proxy
Version:       2.5.0
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета smart_proxy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy) = 2.5.0
Conflicts:     smart-proxy-compat

%description   -n smart-proxy
RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet executable(s).

Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy

%description   -n smart-proxy -l ru_RU.UTF-8
Исполнямка для самоцвета smart_proxy.


%package       -n gem-smart-proxy-doc
Version:       2.5.0
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy) = 2.5.0
Conflicts:     gem-smart-proxy-compat-doc

%description   -n gem-smart-proxy-doc
RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet documentation files.

Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy

%description   -n gem-smart-proxy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета smart_proxy.


%package       -n gem-smart-proxy-devel
Version:       2.5.0
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy) = 2.5.0
Requires:      gem(json) >= 2.3.1

%description   -n gem-smart-proxy-devel
RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet development package.

Smart Proxy is a free open source project that provides restful API to
subsystems such as DNS, DHCP, etc, for higher level orchestration tools such as
Foreman.

Currently Supported modules:

* BMC - BMC management of devices supported by freeipmi and ipmitool
* DHCP - ISC DHCP and MS DHCP Servers
* DNS - Bind and MS DNS Servers
* Puppet - Any Puppet server from 0.24.x
* Puppet CA - Manage certificate signing, cleaning and autosign on a Puppet CA
server
* Realm - Manage host registration to a realm (e.g. FreeIPA)
* TFTP - any UNIX based tftp server
* Facts - module to gather facts from facter (used only on discovered nodes)
* HTTPBoot - endpoint exposing a (TFTP) directory via HTTP(s) for UEFI HTTP
booting
* Logs - log buffer of proxy logs for easier troubleshooting
* Templates - unattended Foreman endpoint proxy

%description   -n gem-smart-proxy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета smart_proxy.


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

%files         -n smart-proxy
%doc README.md
%_bindir/smart-proxy

%files         -n gem-smart-proxy-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-smart-proxy-devel
%doc README.md


%changelog
* Fri Jul 02 2021 Pavel Skrylev <majioa@altlinux.org> 2.5.0-alt1
- ^ 2.1.0 -> 2.5.0

* Mon Nov 30 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2.1
- + requires dep to facter executable
- + explicitly the other required gems to Gemfile as a patch
- + conflicts to compat packages

* Thu Jul 16 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt2
- + conf file to keep rights on some folders after reset
- + _smartforeman user with home of /var/lib/smart-proxy
- * moving config files to sysconf folder
- ! config dependent code
- ! config syntax

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- ^ 2.0.0 -> 2.1.0
- + _foreman user to puppet group

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt4
- + copy Gemfile to %%_localstatedir/smart-proxy
- + setup foreman user and groups
- - service dep out of the foreman
- ! service work dir

* Thu Jul 09 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt3
- + settings yamls

* Mon Jun 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt2
- * dependencies by patch

* Tue Jun 9 2020 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with usage Ruby Policy 2.0
