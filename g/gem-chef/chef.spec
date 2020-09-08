# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname chef

Name:          gem-%pkgname
Version:       16.5.32
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

%gem_replace_version bcrypt_pbkdf ~> 1.1.0
%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %pkgname-doc < %EVR
Provides:      %pkgname-doc = %EVR

%description
Chef is a systems integration framework and configuration management
library written in Ruby. Chef provides a Ruby library and API that can
be used to bring the benefits of configuration management to an entire
infrastructure.

Chef can be run as a client (chef-client) to a server, or run as a
standalone tool (chef-solo). Configuration recipes are written in a pure
Ruby DSL.

This package contains the chef-client, chef-solo and knife binaries as
well as the chef library.


%package       -n %pkgname
Summary:       Chef's default configuration and config loading
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Chef's default configuration and config loading.

%description   -n %pkgname -l ru_RU.UTF8
Настройки для самоцвета %gemname.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       config
Summary:       Chef's default configuration and config loading
Group:         Development/Ruby
BuildArch:     noarch

%description   config
Chef's default configuration and config loading.

%description   config -l ru_RU.UTF8
Настройки для самоцвета %gemname.


%package       config-doc
Summary:       Documentation files for %gemname-config gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   config-doc
Documentation files for %gemname-config gem.

%description   config-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname-config.


%package       utils
Summary:       Basic utility functions for Core Chef development
Group:         Development/Ruby
BuildArch:     noarch

%description   utils
%summary.

%description   utils -l ru_RU.UTF8
Утилиты для самоцвета %gemname.


%package       utils-doc
Summary:       Documentation files for %gemname-utils gem
Group:         Development/Ruby
BuildArch:     noarch

%description   utils-doc
%summary.

%description   utils-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname-utils.


%package       bin
Summary:       Chef-branded binstubs for chef-client
Group:         Development/Ruby
BuildArch:     noarch

%description   bin
Chef-branded binstubs for chef-client.

%description   bin -l ru_RU.UTF8
Исполняемые заглушки для самоцвета %gemname.


%package       bin-doc
Summary:       Documentation files for %gemname-bin gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   bin-doc
Documentation files for %gemname-bin gem.

%description   bin-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname-bin.


%prep
%setup
rm -rf $(find -name "*.py")

%build
%ruby_build --ignore=standalone_cookbook,omnibus,kitchen-tests,win32-eventlog

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

%files
%ruby_gemspecdir/chef-%version.gemspec
%ruby_gemslibdir/chef-%version

%files         config
%ruby_gemspecdir/chef-config-%version.gemspec
%ruby_gemslibdir/chef-config-%version

%files         utils
%ruby_gemspecdir/chef-utils-%version.gemspec
%ruby_gemslibdir/chef-utils-%version

%files         bin
%ruby_gemspecdir/chef-bin-%version.gemspec
%ruby_gemslibdir/chef-bin-%version

%files         doc
%ruby_gemsdocdir/chef-%version

%files         config-doc
%ruby_gemsdocdir/chef-config-%version

%files         utils-doc
%ruby_gemsdocdir/chef-utils-%version

%files         bin-doc
%ruby_gemsdocdir/chef-bin-%version

%files         -n %pkgname
%doc README*
%_bindir/*
%_initdir/chef-client
%_unitdir/chef-client.service
%_sysconfdir/sysconfig/chef-client
%config(noreplace) %attr(0640, root, _chef) %_sysconfdir/chef/client.rb
%dir %attr(0750, root, _chef) %_sysconfdir/chef
%dir %attr(0750, _chef, _chef) %_var/log/chef
%dir %attr(0750, _chef, _chef) %_var/lib/chef
%dir %attr(0750, _chef, _chef) %_var/cache/chef

%pre           -n %pkgname
getent group _chef  >/dev/null || groupadd -r _chef
getent passwd _chef >/dev/null || useradd  -r -g _chef -d %_var/lib/chef -s /sbin/nologin -c "Opscode Chef Daemon" _chef

%changelog
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

