%define        gemname smart_proxy

Name:          gem-smart-proxy
Version:       3.5.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/smart-proxy
Vcs:           https://github.com/theforeman/smart-proxy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       settings.yml
Source2:       smart-proxy.service
Source3:       smart-proxy.conf
Source4:       puppetca_http_api.yml
Patch:         deps.patch
Patch1:        config.patch
Patch2:        config-path.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
BuildRequires: gem(rubyipmi) >= 0.10.0
BuildRequires: gem(redfish_client) >= 0.5.1
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(rsec) >= 1.0.0
BuildRequires: gem(rb-inotify) >= 0
BuildRequires: gem(rb-kqueue) >= 0
BuildRequires: gem(logging-journald) >= 2.0 gem(logging-journald) < 3
BuildRequires: gem(rkerberos) >= 0.1.1
BuildRequires: gem(gssapi) >= 0
BuildRequires: gem(ruby-libvirt) >= 0.6.0
BuildRequires: gem(jwt) >= 0
BuildRequires: gem(xmlrpc) >= 0.2 gem(xmlrpc) < 1
BuildRequires: gem(mocha) >= 1.10 gem(mocha) < 2
BuildRequires: gem(ci_reporter) >= 1.6.3 gem(ci_reporter) < 3
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(ruby-prof) < 1.4
BuildRequires: gem(rubocop) >= 0.89.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-performance) >= 1.5.2 gem(rubocop-performance) < 2
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rubocop-checkstyle_formatter) >= 0.2 gem(rubocop-checkstyle_formatter) < 1
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(facter) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(logging) >= 0
BuildRequires: gem(rack) >= 1.3
BuildRequires: gem(sd_notify) >= 0.1 gem(sd_notify) < 1
BuildRequires: gem(sinatra) >= 2.0 gem(sinatra) < 3
BuildRequires: gem(webrick) >= 1.0 gem(webrick) < 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rsec >= 1.0.0,rsec < 2
%ruby_use_gem_dependency ci_reporter >= 2.0.0,ci_reporter < 3
%ruby_alias_names smart_proxy,smart-proxy
Requires:      gem(json) >= 0
Requires:      gem(logging) >= 0
Requires:      gem(rack) >= 1.3
Requires:      gem(sd_notify) >= 0.1 gem(sd_notify) < 1
Requires:      gem(sinatra) >= 2.0 gem(sinatra) < 3
Requires:      gem(webrick) >= 1.0 gem(webrick) < 2
Provides:      gem(smart_proxy) = 3.5.1
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
Version:       3.5.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета smart_proxy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy) = 3.5.1
Requires:      gem(redfish_client) >= 0.5.1
Requires:      gem(psych) = 4.0.3
Requires:      gem(rubyipmi) >= 0.10.0
Requires:      gem(pry) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rsec) >= 0
Requires:      gem(rb-inotify) >= 0
Requires:      gem(rb-kqueue) >= 0
Requires:      gem(logging-journald) >= 2.0
Requires:      gem(rkerberos) >= 0.1.1
Requires:      gem(gssapi) >= 0
Requires:      gem(ruby-libvirt) >= 0.6.0
Requires:      gem(jwt) >= 0
Requires:      gem(xmlrpc) >= 0.2
Requires:      gem(smart_proxy_salt) >= 2.0
Requires:      gem(smart_proxy_dynflow) >= 0.5
Requires:      gem(smart_proxy_remote_execution_ssh) >= 0.4.1
Requires:      gem(smart_proxy_ansible) >= 3.0.1
Requires:      gem(smart_proxy_discovery) >= 1.0.5
Requires:      gem(smart_proxy_pulp) >= 2.1.0
Requires:      gem(smart_proxy_chef) >= 0.2.0
Requires:      gem(ed25519) >= 0
Requires:      gem(bcrypt_pbkdf) >= 0
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
Version:       3.5.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета smart_proxy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(smart_proxy) = 3.5.1
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
Version:       3.5.1
Release:       alt1
Summary:       RESTful proxies for DNS, DHCP, TFTP, BMC and Puppet development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета smart_proxy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(smart_proxy) = 3.5.1
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(rubyipmi) >= 0.10.0
Requires:      gem(redfish_client) >= 0.5.1
Requires:      gem(pry) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(rsec) >= 1.0.0
Requires:      gem(rb-inotify) >= 0
Requires:      gem(rb-kqueue) >= 0
Requires:      gem(logging-journald) >= 2.0 gem(logging-journald) < 3
Requires:      gem(rkerberos) >= 0.1.1
Requires:      gem(gssapi) >= 0
Requires:      gem(ruby-libvirt) >= 0.6.0
Requires:      gem(jwt) >= 0
Requires:      gem(xmlrpc) >= 0.2 gem(xmlrpc) < 1
Requires:      gem(mocha) >= 1.10 gem(mocha) < 2
Requires:      gem(ci_reporter) >= 1.6.3 gem(ci_reporter) < 3
Requires:      gem(test-unit) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(ruby-prof) < 1.4
Requires:      gem(rubocop) >= 0.89.0 gem(rubocop) < 2
Requires:      gem(rubocop-performance) >= 1.5.2 gem(rubocop-performance) < 2
Requires:      gem(rack-test) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rubocop-checkstyle_formatter) >= 0.2 gem(rubocop-checkstyle_formatter) < 1
Requires:      gem(webmock) >= 0
Requires:      gem(facter) >= 0

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
%autopatch

%build
%ruby_build

%install
%ruby_install

install -dm750 %buildroot%_logdir/smart-proxy \
               %buildroot%_sysconfdir/smart-proxy/config/settings.d \
               %buildroot/run/smart-proxy
install -m644 %SOURCE1 %buildroot%_sysconfdir/smart-proxy/config/
install -Dm644 %SOURCE2 %buildroot%_unitdir/smart-proxy.service
install -Dm644 %SOURCE3 %buildroot%_tmpfilesdir/smart-proxy.conf
install -Dm750 %buildroot%ruby_gemlibdir/Gemfile %buildroot%_localstatedir/smart-proxy/Gemfile
#TODO move to setup.rb
cp -p config/settings.d/*.yml.example %buildroot%_sysconfdir/smart-proxy/config/settings.d
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/smart-proxy/config/settings.d/puppetca_http_api.yml

%check
%ruby_test

%pre           -n smart-proxy
getent group puppet >/dev/null || %_sbindir/groupadd -r puppet
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent passwd _smartforeman >/dev/null || \
   %_sbindir/useradd -r -G puppet,foreman -d %_localstatedir/smart-proxy -s /bin/bash -c "Foreman" _smartforeman

%post          -n smart-proxy
rm -rf %_localstatedir/smart-proxy/Gemfile.lock
%post_service  smart-proxy

%preun         -n smart-proxy
%preun_service smart-proxy


%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%config(noreplace) %_sysconfdir/smart-proxy/config/settings.yml
%config(noreplace) %_sysconfdir/smart-proxy/config/settings.d/*.yml.example

%files         -n smart-proxy
%doc README.md
%_bindir/smart-proxy
%_unitdir/smart-proxy.service
%_tmpfilesdir/smart-proxy.conf
%attr(750,_smartforeman,foreman) %_logdir/smart-proxy
%attr(751,_smartforeman,foreman) %_localstatedir/smart-proxy
%attr(751,_smartforeman,foreman) /run/smart-proxy

%files         -n gem-smart-proxy-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-smart-proxy-devel
%doc README.md


%changelog
* Mon Dec 19 2022 Pavel Skrylev <majioa@altlinux.org> 3.5.1-alt1
- ^ 3.4.0 -> 3.5.1
- ! fixed default smart-proxy.service file

* Fri Sep 16 2022 Pavel Skrylev <majioa@altlinux.org> 3.4.0-alt1
- ^ 3.0.0 -> 3.4.0

* Wed Oct 20 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.5.0 -> 3.0.0

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
