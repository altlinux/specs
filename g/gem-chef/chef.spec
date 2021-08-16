# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname chef

Name:          gem-chef
Version:       16.13.16
Release:       alt1
Summary:       Clients for the chef systems integration framework
Group:         Networking/Other
License:       Apache-2.0
Url:           https://www.chef.io/
Vcs:           https://github.com/opscode/chef.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       chef-client.init
Source2:       chef-client.service
Source3:       chef-client.default
Source4:       chef-client.rb

BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-config) >= 2.2.12 gem(mixlib-config) < 4.0
BuildRequires: gem(fuzzyurl) >= 0
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(tomlrb) >= 1.2 gem(tomlrb) < 3
BuildRequires: gem(train-core) >= 3.2.28 gem(train-core) < 4
BuildRequires: gem(train-winrm) >= 0.2.5
# BuildRequires: gem(license-acceptance) >= 1.0.5 gem(license-acceptance) < 3
BuildRequires: gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3.0
BuildRequires: gem(mixlib-log) >= 2.0.3 gem(mixlib-log) < 4.0
BuildRequires: gem(mixlib-authentication) >= 2.1 gem(mixlib-authentication) < 4
BuildRequires: gem(mixlib-shellout) >= 3.1.1 gem(mixlib-shellout) < 4.0
BuildRequires: gem(mixlib-archive) >= 0.4 gem(mixlib-archive) < 2.0
# BuildRequires: gem(ohai) >= 16.0 gem(ohai) < 17
# BuildRequires: gem(inspec-core) >= 4.23 gem(inspec-core) < 5
BuildRequires: gem(ffi) >= 1.9.25
BuildRequires: gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
BuildRequires: gem(net-ssh) >= 5.1 gem(net-ssh) < 7
BuildRequires: gem(net-ssh-multi) >= 1.2.1 gem(net-ssh-multi) < 2
BuildRequires: gem(net-sftp) >= 2.1.2 gem(net-sftp) < 4.0
BuildRequires: gem(ed25519) >= 1.2 gem(ed25519) < 2
BuildRequires: gem(bcrypt_pbkdf) >= 1.1 gem(bcrypt_pbkdf) < 2
BuildRequires: gem(highline) >= 1.6.9 gem(highline) < 3
BuildRequires: gem(tty-prompt) >= 0.21 gem(tty-prompt) < 1
BuildRequires: gem(tty-screen) >= 0.6 gem(tty-screen) < 1
BuildRequires: gem(tty-table) >= 0.11 gem(tty-table) < 1
BuildRequires: gem(pastel) >= 0
BuildRequires: gem(erubis) >= 2.7 gem(erubis) < 3
BuildRequires: gem(diff-lcs) >= 1.4.3 gem(diff-lcs) < 2
BuildRequires: gem(ffi-libarchive) >= 1.0.3 gem(ffi-libarchive) < 2
BuildRequires: gem(chef-zero) >= 14.0.11
BuildRequires: gem(chef-vault) >= 0
BuildRequires: gem(plist) >= 3.2 gem(plist) < 4
BuildRequires: gem(iniparse) >= 1.4 gem(iniparse) < 2
BuildRequires: gem(syslog-logger) >= 1.6 gem(syslog-logger) < 2
BuildRequires: gem(uuidtools) >= 2.1.5 gem(uuidtools) < 3.0
BuildRequires: gem(proxifier) >= 1.0 gem(proxifier) < 2
BuildRequires: gem(bundler) >= 1.10 gem(bundler) < 3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(fauxhai-ng) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency tomlrb >= 2.0.1,tomlrb < 3
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency net-ssh >= 6.1.0,net-ssh < 7
%ruby_use_gem_dependency diff-lcs >= 1.4.3,diff-lcs < 2
%ruby_ignore_names standalone_cookbook,omnibus,kitchen-tests,win32-eventlog
Requires:      gem(chef-config) = 16.13.16
Requires:      gem(chef-utils) = 16.13.16
Requires:      gem(train-core) >= 3.2.28 gem(train-core) < 4
Requires:      gem(train-winrm) >= 0.2.5
Requires:      gem(license-acceptance) >= 1.0.5 gem(license-acceptance) < 3
Requires:      gem(mixlib-cli) >= 2.1.1 gem(mixlib-cli) < 3.0
Requires:      gem(mixlib-log) >= 2.0.3 gem(mixlib-log) < 4.0
Requires:      gem(mixlib-authentication) >= 2.1 gem(mixlib-authentication) < 4
Requires:      gem(mixlib-shellout) >= 3.1.1 gem(mixlib-shellout) < 4.0
Requires:      gem(mixlib-archive) >= 0.4 gem(mixlib-archive) < 2.0
Requires:      gem(ohai) >= 16.0 gem(ohai) < 17
Requires:      gem(inspec-core) >= 4.23 gem(inspec-core) < 5
Requires:      gem(ffi) >= 1.9.25
Requires:      gem(ffi-yajl) >= 2.2 gem(ffi-yajl) < 3
Requires:      gem(net-ssh) >= 5.1 gem(net-ssh) < 7
Requires:      gem(net-ssh-multi) >= 1.2.1 gem(net-ssh-multi) < 2
Requires:      gem(net-sftp) >= 2.1.2 gem(net-sftp) < 4.0
Requires:      gem(ed25519) >= 1.2 gem(ed25519) < 2
Requires:      gem(bcrypt_pbkdf) >= 1.1 gem(bcrypt_pbkdf) < 2
Requires:      gem(highline) >= 1.6.9 gem(highline) < 3
Requires:      gem(tty-prompt) >= 0.21 gem(tty-prompt) < 1
Requires:      gem(tty-screen) >= 0.6 gem(tty-screen) < 1
Requires:      gem(tty-table) >= 0.11 gem(tty-table) < 1
Requires:      gem(pastel) >= 0
Requires:      gem(erubis) >= 2.7 gem(erubis) < 3
Requires:      gem(diff-lcs) >= 1.4.3 gem(diff-lcs) < 2
Requires:      gem(ffi-libarchive) >= 1.0.3 gem(ffi-libarchive) < 2
Requires:      gem(chef-zero) >= 14.0.11
Requires:      gem(chef-vault) >= 0
Requires:      gem(plist) >= 3.2 gem(plist) < 4
Requires:      gem(iniparse) >= 1.4 gem(iniparse) < 2
Requires:      gem(addressable) >= 0
Requires:      gem(syslog-logger) >= 1.6 gem(syslog-logger) < 2
Requires:      gem(uuidtools) >= 2.1.5 gem(uuidtools) < 3.0
Requires:      gem(proxifier) >= 1.0 gem(proxifier) < 2
Requires:      gem(bundler) >= 1.10 gem(bundler) < 3
Obsoletes:     chef-doc < %EVR
Provides:      chef-doc = %EVR
Provides:      gem(chef) = 16.13.16


%description
Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.


%package       -n gem-chef-config
Version:       16.13.16
Release:       alt1
Summary:       Chef's default configuration and config loading
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) = 16.13.16
Requires:      gem(mixlib-shellout) >= 2.0 gem(mixlib-shellout) < 4.0
Requires:      gem(mixlib-config) >= 2.2.12 gem(mixlib-config) < 4.0
Requires:      gem(fuzzyurl) >= 0
Requires:      gem(addressable) >= 0
Requires:      gem(tomlrb) >= 1.2 gem(tomlrb) < 3
Provides:      gem(chef-config) = 16.13.16

%description   -n gem-chef-config
Chef's default configuration and config loading.


%package       -n gem-chef-config-doc
Version:       16.13.16
Release:       alt1
Summary:       Chef's default configuration and config loading documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-config) = 16.13.16

%description   -n gem-chef-config-doc
Chef's default configuration and config loading documentation files.

Chef's default configuration and config loading.

%description   -n gem-chef-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-config.


%package       -n gem-chef-config-devel
Version:       16.13.16
Release:       alt1
Summary:       Chef's default configuration and config loading development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-config
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-config) = 16.13.16
Requires:      gem(bcrypt_pbkdf) >= 1.1.0 gem(bcrypt_pbkdf) < 1.2

%description   -n gem-chef-config-devel
Chef's default configuration and config loading development package.

Chef's default configuration and config loading.

%description   -n gem-chef-config-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-config.


%package       -n gem-chef-bin
Version:       16.13.16
Release:       alt1
Summary:       Chef-branded binstubs for chef-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 16.13.16
Provides:      gem(chef-bin) = 16.13.16

%description   -n gem-chef-bin
Chef-branded binstubs for chef-client.

%description   -n gem-chef-bin -l ru_RU.UTF8
Исполняемые заглушки для самоцвета chef.


%package       -n gem-chef-bin-doc
Version:       16.13.16
Release:       alt1
Summary:       Chef-branded binstubs for chef-client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-bin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef-bin) = 16.13.16

%description   -n gem-chef-bin-doc
Chef-branded binstubs for chef-client documentation files.

%description   -n gem-chef-bin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-bin.


%package       -n gem-chef-bin-devel
Version:       16.13.16
Release:       alt1
Summary:       Chef-branded binstubs for chef-client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-bin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-bin) = 16.13.16
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(bcrypt_pbkdf) >= 1.1.0 gem(bcrypt_pbkdf) < 1.2

%description   -n gem-chef-bin-devel
Chef-branded binstubs for chef-client development package.

Chef-branded binstubs for chef-client.

%description   -n gem-chef-bin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-bin.


%package       -n gem-chef-utils
Version:       16.13.16
Release:       alt1
Summary:       Basic utility functions for Core Chef Infra development
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef-utils) >= 0
Requires:      gem(fauxhai-ng) >= 0
Requires:      gem(rake) >= 0 gem(rake) < 14
Requires:      gem(rspec) >= 0 gem(rspec) < 4
Provides:      ruby-gem-chef-utils

%description   -n gem-chef-utils
Basic utility functions for Core Chef development.

%description   -n gem-chef-utils -l ru_RU.UTF8
Утилиты для самоцвета chef-utils.


%package       -n gem-chef-utils-doc
Version:       16.13.16
Release:       alt1
Summary:       Basic utility functions for Core Chef Infra development documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-utils
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-chef-utils-doc
Documentation files for chef-utils gem documentation files

%description   -n gem-chef-utils-doc -l ru_RU.UTF8
Файлы сведений для самоцвета chef-utils.


%package       -n gem-chef-utils-devel
Version:       16.13.16
Release:       alt1
Summary:       Basic utility functions for Core Chef Infra development development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-utils
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bcrypt_pbkdf) >= 1.1.0 gem(bcrypt_pbkdf) < 1.2

%description   -n gem-chef-utils-devel
Basic utility functions for Core Chef Infra development development package.

%description   -n gem-chef-utils-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-utils.


%package       -n gem-chef-doc
Version:       16.13.16
Release:       alt1
Summary:       Clients for the chef systems integration framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chef) = 16.13.16

%description   -n gem-chef-doc
Clients for the chef systems integration framework documentation files.

Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.

%description   -n gem-chef-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef.


%package       -n gem-chef-devel
Version:       16.13.16
Release:       alt1
Summary:       Clients for the chef systems integration framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 16.13.16
Requires:      gem(bcrypt_pbkdf) >= 1.1.0 gem(bcrypt_pbkdf) < 1.2

%description   -n gem-chef-devel
Clients for the chef systems integration framework development package.

Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.

%description   -n gem-chef-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef.


%package       -n chef
Version:       16.13.16
Release:       alt1
Summary:       Clients for the chef systems integration framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета chef
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chef) = 16.13.16

%description   -n chef
Clients for the chef systems integration framework executable(s).

Chef is a systems integration framework and configuration management library
written in Ruby. Chef provides a Ruby library and API that can be used to bring
the benefits of configuration management to an entire infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a standalone
tool (chef-solo). Configuration recipes are written in a pure Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as well as
the chef library.

%description   -n chef -l ru_RU.UTF8
Настройки для самоцвета chef.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

# Install init scripts
install -Dm 0755 %SOURCE1 %buildroot%_initdir/chef-client
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/chef-client.service
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/chef-client
install -Dm 0640 %SOURCE4 %buildroot%_sysconfdir/chef/client.rb

mkdir -p %buildroot%_var/log/chef
mkdir -p %buildroot%_var/lib/chef
mkdir -p %buildroot%_var/cache/chef
mkdir -p %buildroot/run/chef

%check
%ruby_test

%pre           -n chef
getent group _chef  >/dev/null || groupadd -r _chef
getent passwd _chef >/dev/null || useradd  -r -g _chef -d %_var/lib/chef -s /sbin/nologin -c "Opscode Chef Daemon" _chef

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-chef-config
%ruby_gemspecdir/chef-config-16.13.16.gemspec
%ruby_gemslibdir/chef-config-16.13.16

%files         -n gem-chef-config-doc
%ruby_gemsdocdir/chef-config-16.13.16

%files         -n gem-chef-config-devel

%files         -n gem-chef-bin
%ruby_gemspecdir/chef-bin-16.13.16.gemspec
%ruby_gemslibdir/chef-bin-16.13.16

%files         -n chef
%doc README.md
%_bindir/knife
%_bindir/chef-apply
%_bindir/chef-client
%_bindir/chef-resource-inspector
%_bindir/chef-service-manager
%_bindir/chef-shell
%_bindir/chef-solo
%_bindir/chef-windows-service
%_initdir/chef-client
%_unitdir/chef-client.service
%_sysconfdir/sysconfig/chef-client
%config(noreplace) %attr(0640, root, _chef) %_sysconfdir/chef/client.rb
%dir %attr(0750, root, _chef) %_sysconfdir/chef
%dir %attr(0750, _chef, _chef) %_var/log/chef
%dir %attr(0750, _chef, _chef) %_var/lib/chef
%dir %attr(0750, _chef, _chef) %_var/cache/chef

%files         -n gem-chef-bin-doc
%ruby_gemsdocdir/chef-bin-16.13.16

%files         -n gem-chef-bin-devel

%files         -n gem-chef-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chef-devel
%doc README.md

%files         -n gem-chef-utils
%ruby_gemspecdir/chef-utils-16.13.16.gemspec
%ruby_gemslibdir/chef-utils-16.13.16

%files         -n gem-chef-utils-doc
%ruby_gemsdocdir/chef-utils-16.13.16

%files         -n gem-chef-utils-devel


%changelog
* Sun Jul 11 2021 Pavel Skrylev <majioa@altlinux.org> 16.13.16-alt1
- ^ 16.5.32 -> 16.13.16

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 16.5.32-alt1
- ^ 16.2.89 -> 16.5.32
- ! build

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 16.2.89-alt1
- ^ 15.2.19 -> 16.2.89
- + chef-utils gem package

* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 15.2.19-alt1
- ^ 15.0.201 -> 15.2.19

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.201-alt1
- ^ 15.0.167 -> 15.0.201

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.167-alt2
- > setup gem's dependency detection

* Wed Feb 20 2019 Pavel Skrylev <majioa@altlinux.org> 15.0.167-alt1
- > Ruby Policy 2.0
- ^ 15.0.120 -> 15.0.167

* Fri Jan 04 2019 Andrey Cherepanov <cas@altlinux.org> 15.0.120-alt1
- New version.

* Mon Dec 10 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.102-alt1
- New version.

* Wed Dec 05 2018 Andrey Cherepanov <cas@altlinux.org> 15.0.98-alt1
- New version.

* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 14.6.47-alt1
- Bump to 14.6.47.

* Thu Oct 04 2018 Pavel Skrylev <majioa@altlinux.org> 14.6.11-alt2
- Fix to files storing procedure.

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 14.6.11-alt1
- New version.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.28-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 14.5.21-alt1
- New version.

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 14.4.63-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.20-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 22 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.20-alt1
- New version.

* Thu Jun 21 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.18-alt1
- New version.

* Tue Jun 19 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.17-alt1
- New version.

* Mon Jun 18 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.16-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.10-alt1
- New version.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.3.5-alt1
- New version.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.2-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 14.2.0-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.1.21-alt1
- New version.

* Tue Mar 20 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.142-alt1
- New version.

* Thu Sep 07 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.15-alt1
- New version

* Mon Sep 04 2017 Andrey Cherepanov <cas@altlinux.org> 13.4.11-alt1
- New version

* Sun Aug 27 2017 Andrey Cherepanov <cas@altlinux.org> 13.3.52-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 13.1.0-alt1
- New version

* Sat Jan 28 2017 Andrey Cherepanov <cas@altlinux.org> 12.19.2-alt1
- new version 12.19.2

* Wed Oct 05 2016 Andrey Cherepanov <cas@altlinux.org> 12.15.11-alt1
- new version 12.15.11

* Fri Jun 03 2016 Andrey Cherepanov <cas@altlinux.org> 12.11.18-alt1
- New version

* Mon Jan 18 2016 Andrey Cherepanov <cas@altlinux.org> 12.6.0-alt1
- New version

* Mon Oct 19 2015 Andrey Cherepanov <cas@altlinux.org> 12.5.1-alt1
- New version
- Package chef-config as separate package (need ro build ohai)

* Fri Oct 02 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.4-alt1
- New version

* Sun Sep 20 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.2-alt1
- New version
- Check for component versions according chef.gemspec

* Mon Aug 03 2015 Andrey Cherepanov <cas@altlinux.org> 12.4.1-alt1
- New version

* Wed May 20 2015 Andrey Cherepanov <cas@altlinux.org> 12.3.0-alt1
- New version

* Sat Jan 24 2015 Andrey Cherepanov <cas@altlinux.org> 12.0.6-alt1
- Initial build in Sisyphus
