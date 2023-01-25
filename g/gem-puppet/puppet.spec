%define        gemname puppet
%define        _unpackaged_files_terminate_build 1
%define        confdir ext/redhat

Name:          gem-puppet
Version:       7.22.0
Release:       alt1
Summary:       A network tool for managing many disparate systems
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://puppet.com/
Vcs:           https://github.com/puppetlabs/puppet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source5:       puppet.conf
Source4:       auth.conf
Source3:       puppet-nm-dispatcher
Source2:       puppet.service
Source1:       client.init
Source:        %name-%version.tar
Patch4:        fix_yaml.patch
Patch3:        puppet-alt-aptrpm-osfamily.patch
Patch2:        puppet-fix-locale-loading.patch
Patch1:        puppet-alt-adjust-default-paths.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(facter) >= 2.4.0 gem(facter) < 5
BuildRequires: gem(hiera) >= 3.2.1 gem(hiera) < 4
BuildRequires: gem(semantic_puppet) >= 1.0 gem(semantic_puppet) < 2
BuildRequires: gem(fast_gettext) >= 1.1 gem(fast_gettext) < 3
BuildRequires: gem(locale) >= 2.1 gem(locale) < 3
BuildRequires: gem(multi_json) >= 1.13 gem(multi_json) < 2
BuildRequires: gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
BuildRequires: gem(deep_merge) >= 1.0 gem(deep_merge) < 2
BuildRequires: gem(scanf) >= 1.0 gem(scanf) < 2
BuildRequires: gem(CFPropertyList) >= 2.2 gem(CFPropertyList) < 4
BuildRequires: gem(gettext-setup) >= 1.0.1 gem(gettext-setup) < 1.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency CFPropertyList >= 2.2,CFPropertyList < 4
%ruby_use_gem_dependency gettext-setup >= 1.1,gettext-setup < 2
Requires:      gem(facter) >= 2.4.0 gem(facter) < 5
Requires:      gem(hiera) >= 3.2.1 gem(hiera) < 4
Requires:      gem(semantic_puppet) >= 1.0 gem(semantic_puppet) < 2
Requires:      gem(fast_gettext) >= 1.1 gem(fast_gettext) < 3
Requires:      gem(locale) >= 2.1 gem(locale) < 3
Requires:      gem(multi_json) >= 1.13 gem(multi_json) < 2
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(deep_merge) >= 1.0 gem(deep_merge) < 2
Requires:      gem(scanf) >= 1.0 gem(scanf) < 2
Requires:      gem(CFPropertyList) >= 2.2 gem(CFPropertyList) < 4
Requires:      puppet = %EVR
Provides:      gem(puppet) = %EVR

%ruby_use_gem_version puppet:%version

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts, along
with obviously discrete elements like packages, services, and files.


%package       -n puppet
Summary:       A network tool for managing many disparate systems executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета puppet
Group:         System/Servers
BuildArch:     noarch

Requires:      gem(puppet) = %EVR
Requires:      shadow-change
Requires(preun,post): %name = %EVR

%description   -n puppet
A network tool for managing many disparate systems executable(s).

Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts, along
with obviously discrete elements like packages, services, and files.

%description   -n puppet -l ru_RU.UTF-8
Исполнямка для самоцвета puppet.


%package       -n gem-puppet-doc
Summary:       A network tool for managing many disparate systems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета puppet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(puppet) = %EVR

%description   -n gem-puppet-doc
A network tool for managing many disparate systems documentation files.

Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts, along
with obviously discrete elements like packages, services, and files.

%description   -n gem-puppet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета puppet.


%package       -n gem-puppet-devel
Summary:       A network tool for managing many disparate systems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета puppet
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(puppet) = %EVR
Requires:      gem(gettext-setup) >= 1.0.1 gem(gettext-setup) < 1.1
Requires:      gem(CFPropertyList) >= 3.0 gem(CFPropertyList) < 4

%description   -n gem-puppet-devel
A network tool for managing many disparate systems development package.

Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts, along
with obviously discrete elements like packages, services, and files.

%description   -n gem-puppet-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета puppet.


%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install

# SysVInit files
install -Dp -m0644 %confdir/client.sysconfig %buildroot%_sysconfdir/sysconfig/puppet
install -Dp -m0755 %SOURCE1 %buildroot%_initrddir/puppet
# Systemd files
install -Dp -m0644 %SOURCE2 %buildroot%_unitdir/puppet.service
ln -s %_unitdir/puppet.service %buildroot%_unitdir/puppetagent.service

install -Dp -m0644 conf/fileserver.conf %buildroot%_sysconfdir/puppet/fileserver.conf

# Create other configuration directories
mkdir -p %buildroot%_sysconfdir/puppet/ssl/{public_keys,certificate_requests,certs,ca/requests,ca/private,ca/signed,private,private_keys}
mkdir -p %buildroot%_sysconfdir/puppet/code/environments/production/manifests

# Setup tmpfiles.d config
mkdir -p %buildroot%_tmpfilesdir
echo "D /run/%gemname 0755 _%gemname %gemname -" > \
    %buildroot%_tmpfilesdir/%gemname.conf

# Create puppet modules directory for puppet module tool
mkdir -p %buildroot%_sysconfdir/%gemname/code/modules
touch %buildroot%_sysconfdir/puppet/code/modules/.dir

# Create service directory
mkdir -p %buildroot{%_cachedir,%_logdir,/run}/puppet

# Create puppet modules link
ln -s %_libexecdir/puppet-modules %buildroot%ruby_gemlibdir/vendor_modules

# Install NetworkManager dispatcher
install -Dpv %SOURCE3 \
    %buildroot%_sysconfdir/NetworkManager/dispatcher.d/98-%{name}

touch %buildroot%_sysconfdir/puppet/autosign.conf
install -Dm644 %SOURCE4 %buildroot%_sysconfdir/puppet/auto.conf
install -Dm644 %SOURCE5 %buildroot%_sysconfdir/puppet/puppet.conf

# link to gem library code base
ln -s %ruby_gemlibdir %buildroot%_datadir/%gemname

# TODO fix backward link to a foreman ? from theforeman-foreman
ln -s %_libexecdir/puppet-modules/theforeman-foreman/files/foreman-report_v2.rb %buildroot%ruby_gemlibdir/lib/puppet/reports/foreman.rb

# Create public subdirectory
mkdir -p %buildroot%ruby_gemlibdir/public
touch %buildroot%ruby_gemlibdir/public/.dir

# Create locale and modules directories
mkdir -p %buildroot%_datadir/puppet-locale %buildroot%_libexecdir/puppet-modules
touch %buildroot%_datadir/puppet-locale/.dir %buildroot%_libexecdir/puppet-modules/.dir

# Remove demo files
rm -rf %buildroot%_libexecdir/demo %buildroot%_datadir/ri/demo

%check
%ruby_test

%pre           -n puppet
[ ! -d %_sysconfdir/puppetlabs/puppet/ssl ] || (
   cp -rf %_sysconfdir/puppetlabs/puppet/ssl %_sysconfdir/puppet &&
   rm -rf %_sysconfdir/puppetlabs/puppet/ssl)
getent group foreman >/dev/null || %_sbindir/groupadd -r foreman
getent group puppet >/dev/null || %_sbindir/groupadd -r puppet
%_sbindir/useradd -r -N -G puppet,foreman -d %_cachedir/puppet -s /dev/null -c Puppet _puppet >/dev/null 2>&1 ||:

%post          -n puppet
%post_service puppet
sed -e "s,sample.server.name,$(hostname)," \
    -i %_sysconfdir/puppet/puppet.conf

%preun         -n puppet
%preun_service puppet

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_libexecdir/puppet-modules

%files         -n puppet
%doc README.md
%_bindir/puppet
%_initdir/puppet
%_unitdir/puppet.service
%_unitdir/puppetagent.service
%config(noreplace) %_tmpfilesdir/%gemname.conf
%dir %_sysconfdir/puppet
%attr(0771,_puppet,puppet) %dir %_sysconfdir/puppet/ssl
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/public_keys
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/certificate_requests
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/certs
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/requests
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/private
%attr(0755,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/ca/signed
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/private
%attr(0750,_puppet,puppet) %dir %_sysconfdir/puppet/ssl/private_keys
%dir %_sysconfdir/puppet/code/environments
%dir %_sysconfdir/puppet/code/environments/production
%dir %_sysconfdir/puppet/code/environments/production/manifests
%dir %_sysconfdir/puppet/code
%_sysconfdir/puppet/code
%attr(0664,_puppet,puppet) %config(noreplace) %_sysconfdir/puppet/autosign.conf
%config(noreplace) %_sysconfdir/puppet/auto.conf
%config(noreplace) %_sysconfdir/puppet/puppet.conf
%config(noreplace) %_sysconfdir/sysconfig/puppet
%config(noreplace) %_sysconfdir/puppet/fileserver.conf
%_sysconfdir/NetworkManager/dispatcher.d/98-%{name}
%_datadir/puppet
%_datadir/puppet-locale
%attr(1770,_puppet,puppet) %dir %_cachedir/puppet
%_cachedir/puppet/
%attr(1770,_puppet,puppet) %dir %_logdir/puppet
%attr(1770,_puppet,puppet) %dir /run/puppet
%doc %_man8dir/*
%doc %_man5dir/puppet.conf.5*

%files         -n gem-puppet-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-puppet-devel
%doc README.md


%changelog
* Wed Jan 25 2023 Andrey Cherepanov <cas@altlinux.org> 7.22.0-alt1
- New version.

* Fri Dec 09 2022 Andrey Cherepanov <cas@altlinux.org> 7.21.0-alt1
- New version.

* Sun Oct 09 2022 Andrey Cherepanov <cas@altlinux.org> 7.20.0-alt1
- New version.

* Wed Sep 14 2022 Andrey Cherepanov <cas@altlinux.org> 7.19.0-alt1
- New version.

* Sat Jul 23 2022 Andrey Cherepanov <cas@altlinux.org> 7.18.0-alt1
- New version.

* Tue May 31 2022 Pavel Skrylev <majioa@altlinux.org> 7.17.0.1-alt1
- ^ 7.17.0 -> 7.17.0.1

* Sun May 29 2022 Andrey Cherepanov <cas@altlinux.org> 7.17.0-alt1
- New version.

* Fri Apr 15 2022 Andrey Cherepanov <cas@altlinux.org> 7.16.0-alt1
- New version.

* Fri Mar 18 2022 Andrey Cherepanov <cas@altlinux.org> 7.15.0-alt1
- New version.

* Fri Feb 18 2022 Andrey Cherepanov <cas@altlinux.org> 7.14.0-alt4
- Removed requires of puppet-puppetserver-foreman.

* Mon Jan 31 2022 Pavel Skrylev <majioa@altlinux.org> 7.14.0-alt3
- !fixed osfamily for apt rpm to altlinux (closes #41622)
- !conf to support newer puppetserver-foreman puppet module

* Fri Jan 28 2022 Andrey Cherepanov <cas@altlinux.org> 7.14.0-alt2
- Requires gem-puppet same version for preun/post scripts.

* Wed Jan 19 2022 Andrey Cherepanov <cas@altlinux.org> 7.14.0-alt1
- New version.

* Fri Dec 10 2021 Andrey Cherepanov <cas@altlinux.org> 7.13.1-alt1
- New version.

* Wed Nov 10 2021 Andrey Cherepanov <cas@altlinux.org> 7.12.1-alt1
- New version.

* Mon Oct 11 2021 Andrey Cherepanov <cas@altlinux.org> 7.12.0-alt1
- New version.

* Wed Sep 15 2021 Andrey Cherepanov <cas@altlinux.org> 7.11.0-alt1
- New version.

* Mon Aug 16 2021 Andrey Cherepanov <cas@altlinux.org> 7.10.0-alt1
- New version.

* Mon Jul 19 2021 Andrey Cherepanov <cas@altlinux.org> 7.9.0-alt1
- New version.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 7.8.0-alt1
- New version.

* Tue May 25 2021 Andrey Cherepanov <cas@altlinux.org> 7.7.0-alt1
- New version.

* Wed Apr 28 2021 Andrey Cherepanov <cas@altlinux.org> 7.6.1-alt1
- New version.

* Fri Apr 16 2021 Andrey Cherepanov <cas@altlinux.org> 7.6.0-alt1
- New version.

* Mon Mar 15 2021 Andrey Cherepanov <cas@altlinux.org> 7.5.0-alt1
- New version.

* Fri Feb 12 2021 Andrey Cherepanov <cas@altlinux.org> 7.4.1-alt1
- New version.

* Sat Feb 06 2021 Andrey Cherepanov <cas@altlinux.org> 7.4.0-alt1
- New version.

* Mon Jan 25 2021 Andrey Cherepanov <cas@altlinux.org> 7.3.0-alt1
- New version.

* Mon Dec 28 2020 Pavel Skrylev <majioa@altlinux.org> 7.1.0-alt3
- + symlink to report for foreman
- ! owner for the facts folder and yaml reports

* Mon Dec 14 2020 Pavel Skrylev <majioa@altlinux.org> 7.1.0-alt2
- * default puppet.conf
- ! spec

* Mon Dec 14 2020 Pavel Skrylev <majioa@altlinux.org> 7.1.0-alt1
- ^ 7.0.0 -> 7.1.0
- + link to vendor modules for puppet gem

* Mon Nov 30 2020 Pavel Skrylev <majioa@altlinux.org> 7.0.0-alt2
- + default static config files for auth and authsign

* Sat Nov 14 2020 Andrey Cherepanov <cas@altlinux.org> 7.0.0-alt1
- New version.

* Thu Oct 22 2020 Andrey Cherepanov <cas@altlinux.org> 6.19.1-alt1
- New version.

* Tue Oct 20 2020 Andrey Cherepanov <cas@altlinux.org> 6.19.0-alt1
- New version.

* Mon Aug 24 2020 Andrey Cherepanov <cas@altlinux.org> 6.18.0-alt1
- New version.

* Sun Jul 19 2020 Andrey Cherepanov <cas@altlinux.org> 6.17.0-alt1
- New version.

* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 6.16.0-alt1.2
- ! groups creation proc in post section

* Thu Jul 09 2020 Pavel Skrylev <majioa@altlinux.org> 6.16.0-alt1.1
- + puppet user to foreman group
- ! spec tags
- ! lost keys placement from an elder versions of puppet to newer ones

* Sat May 30 2020 Andrey Cherepanov <cas@altlinux.org> 6.16.0-alt1
- New version.

* Fri May 22 2020 Andrey Cherepanov <cas@altlinux.org> 6.15.0-alt3
- Move environments/production/manifests to /etc/puppet/code (ALT #38520).

* Mon May 11 2020 Andrey Cherepanov <cas@altlinux.org> 6.15.0-alt2
- Apply useful part of old patch as actual patches and get patch from Debian.
- Modules are placed into /etc/puppet/code/modules instead of /etc/puppet/modules.
- Fix retrieving metainfo folders (ALT #38422).
- Make system-wide directories /usr/share/puppet-modules and /usr/share/puppet-locale.

* Wed Apr 29 2020 Andrey Cherepanov <cas@altlinux.org> 6.15.0-alt1
- New version.

* Tue Mar 10 2020 Andrey Cherepanov <cas@altlinux.org> 6.14.0-alt1
- New version.

* Tue Feb 18 2020 Andrey Cherepanov <cas@altlinux.org> 6.13.0-alt1
- New version.

* Tue Jan 21 2020 Andrey Cherepanov <cas@altlinux.org> 6.12.0-alt1
- New version.

* Fri Dec 06 2019 Pavel Skrylev <majioa@altlinux.org> 6.11.1-alt1
- updated (^) 6.10.1 -> 6.11.1
- removed (-) deep_merge gem out of spec
- fixed (!) version in spec

* Sun Oct 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.10.1-alt1
- New version.

* Tue Oct 01 2019 Andrey Cherepanov <cas@altlinux.org> 6.10.0-alt1
- New version.

* Mon Sep 09 2019 Pavel Skrylev <majioa@altlinux.org> 6.9.0-alt0.2
- fixed (!) spec according the changelog policy

* Mon Aug 19 2019 Pavel Skrylev <majioa@altlinux.org> 6.9.0-alt0.1
- updated (^) 6.8.0 -> 6.9.0
- added (+) links to required dirs in spec
- fixed (!) spec

* Fri Aug 16 2019 Andrey Cherepanov <cas@altlinux.org> 6.8.0-alt1
- New version.

* Sat Jul 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.2-alt1
- New version.

* Mon Jul 22 2019 Andrey Cherepanov <cas@altlinux.org> 6.7.0-alt1
- New version.

* Thu Jun 27 2019 Andrey Cherepanov <cas@altlinux.org> 6.6.0-alt1
- New version.

* Wed Jun 19 2019 Andrey Cherepanov <cas@altlinux.org> 6.5.0-alt1
- New version.

* Fri Apr 26 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.2-alt1
- New version.

* Thu Apr 11 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.1-alt1
- New version.

* Mon Apr 01 2019 Andrey Cherepanov <cas@altlinux.org> 6.4.0-alt1
- New version.

* Sat Mar 09 2019 Pavel Skrylev <majioa@altlinux.org> 6.3.0-alt1
- Bump to 6.3.0;
- Use Ruby Policy 2.0.

* Mon Mar 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 6.1.0-alt2
- Requires fixed.

* Tue Dec 18 2018 Andrey Cherepanov <cas@altlinux.org> 6.1.0-alt1
- New version.

* Mon Dec 03 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.4-alt2
- Repack to avoid unnecessary deps.

* Thu Nov 01 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.4-alt1
- New version.

* Mon Oct 29 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.3-alt1
- New version.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 6.0.2-alt1.qa1
- NMU: applied repocop patch

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.2-alt1
- New version.

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.1-alt1
- New version.

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 6.0.0-alt2
- Updated deps of fast-gettext to 1.7.

* Wed Sep 19 2018 Andrey Cherepanov <cas@altlinux.org> 6.0.0-alt1
- New version.
- Package ad gem.
- Use /run instead of /var/run in tmpfiles rules.
- puppet-server is deprecated. To run puppet as a server you must use puppetserver.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.6-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Jun 11 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.2-alt1
- New version.

* Fri Jun 01 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt3
- Fix "Cannot determine basic system flavour" (https://tickets.puppetlabs.com/browse/SERVER-14).

* Wed Apr 25 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt2
- Create and package all configuration directories.
- Add puppetdb example configuration to puppet.conf.

* Thu Apr 19 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version.

* Wed Apr 04 2018 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version.

* Thu Oct 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.2-alt1
- New version

* Sat Sep 30 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.1-alt1
- New version

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version

* Wed Sep 13 2017 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Thu Aug 17 2017 Andrey Cherepanov <cas@altlinux.org> 5.1.0-alt1
- New version

* Wed Jul 19 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.1-alt1
- New version

* Wed Jun 28 2017 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version

* Mon Jun 19 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.4-alt1
- New version

* Fri Jun 16 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.3-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.2-alt1
- New version

* Sun May 21 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.1-alt1
- New version

* Mon Apr 10 2017 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- New version

* Wed Feb 01 2017 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- new version 4.9.0

* Fri Jan 27 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.2-alt1
- new version 4.8.2

* Wed Jan 18 2017 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- new version 4.8.1
- aptrpm package provider is default for ALT operating system

* Fri Oct 21 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt2
- Fix build without bundled libraries
- Rebuild with fixed ruby autoreq (ALT #32601)

* Thu Oct 06 2016 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt1
- new version 4.7.0

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 4.3.1-alt1
- New version
- Package missing directories (ALT #30148)

* Sat Apr 25 2015 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version

* Tue Jan 13 2015 Andrey Cherepanov <cas@altlinux.org> 3.7.3-alt1
- New version

* Thu May 15 2014 Andrey Cherepanov <cas@altlinux.org> 3.5.1-alt1
- New version
- Rename services to puppet, puppetmaster
- Add NetworkManager dispatcher script to pickup changes to
  /etc/resolv.conf and such

* Fri Jul 26 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.21-alt2
- Set correct pid file name for services (ALT #29114)
- Set correct user name _puppet in configuration of puppetmasterd

* Fri Jun 07 2013 Andrey Cherepanov <cas@altlinux.org> 2.7.21-alt1
- New version 2.7.21 (ALT #28695)
- Use system group `puppet` instead `_puppet` (ALT #28273)
- New format of puppet.conf (ALT #28517)

* Fri Nov 30 2012 Led <led@altlinux.ru> 2.7.5-alt1.2
- Rebuilt with ruby-1.9.3-alt1

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.7.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 06 2011 Sergey Alembekov <rt@altlinux.ru> 2.7.5-alt1
- [2.7.5]

* Tue Sep 27 2011 Sergey Alembekov <rt@altlinux.ru> 2.7.3-alt1
- [2.7.3]

* Sun Jun 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.24.8-alt1
- [0.24.8]

* Sat Dec 20 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt3
- Fixed interpackage dependencies

* Sat Dec 20 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt2
- Cleaned up build deps

* Sat Nov 01 2008 Sir Raorn <raorn@altlinux.ru> 0.24.6-alt1
- [0.24.6]

* Tue Aug 26 2008 Sir Raorn <raorn@altlinux.ru> 0.24.5-alt1
- Built for Sisyphus
