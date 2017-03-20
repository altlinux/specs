%define confdir ext/redhat

Name:    puppet3
Version: 3.8.7
Release: alt1

Summary: A network tool for managing many disparate systems
Group:   System/Servers
License: ASL 2.0
URL:     https://puppetlabs.com/

BuildArch: noarch

Source:  %name-%version.tar
Patch:  %name-%version-%release.patch
Patch1: %name-%version-%release-ext-alt.diff
Patch2: puppet-3.8.7-ext-puppetlisten-rotten.patch
Patch5: puppet-3.8.7-aptrpm-defaultfor-alt.patch

BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-em-http-request
BuildRequires: ruby-eventmachine
BuildRequires: ruby-facter
BuildRequires: ruby-hashie
BuildRequires: ruby-heredoc_unindent
BuildRequires: ruby-hiera
BuildRequires: ruby-pathspec
BuildRequires: ruby-rgen
BuildRequires(pre): rpm-macros-kde-common-devel
%_K_if_ver_gteq %version 4
# commit 9147c43327383d24927d2070f3ff0a6ba9909c0f preceding 4.0.0-rc1
# (PUP-3272) Remove vendored safe_yaml and related patches
#
# safe_yaml is no longer needed since YAML on the network is no longer
# supported (slow because of safe_yaml, and unsecure without it).
%global no_safe_yaml 1
%else
%def_with ruby_safe_yaml
%endif
%{!?no_safe_yaml:%{?with_ruby_safe_yaml:BuildRequires: ruby-safe_yaml}}

Provides: puppet = %EVR
Conflicts: puppet
Requires: shadow-change
Conflicts: ruby-semantic

%filter_from_requires /^ruby(.*\(win32\|windows\|wmi-lite\|semantic\|spec_helper\).*)/d
# workaround unmet reqs on Ruby Rails:
%filter_from_requires /^ruby(active_\(record\|support\)\(\|\/.*\))/d

%description
Puppet lets you centrally manage every important aspect of your
system using a cross-platform specification language that manages
all the separate elements normally aggregated in different files,
like users, cron jobs, and hosts, along with obviously discrete
elements like packages, services, and files.

%package  server
Summary:  Server for the puppet system management tool
Group:    System/Servers
Requires: %name = %version-%release
Provides: puppet-server = %EVR
Conflicts: puppet-server

%description server
Provides the central puppet server daemon which provides manifests
to clients.  The server can also function as a certificate authority
and file server.

%prep
%setup
%patch5 -p1
%patch2 -p1
%patch1 -p1
%patch -p1
chmod +x ext/puppet-load.rb ext/regexp_nodes/regexp_nodes.rb
# remove vendor copy of libraries and support non-Linux platforms
subst 's/require /#require /' \
       lib/puppet/util/windows.rb
#      lib/puppet/vendor/require_vendored.rb \

rm -r \
       lib/puppet/feature/cfacter.rb \
       lib/puppet/util/rdoc \
       lib/puppet/util/windows \
       %{!?no_safe_yaml:lib/puppet/vendor/safe_yaml/spec} \
       lib/puppet/module_tool/skeleton/templates/generator/spec

echo "require 'rdoc'" > lib/puppet/util/rdoc.rb

# Unbundle
rm -r lib/puppet/vendor/*{pathspec,rgen%{!?no_safe_yaml:%{?with_ruby_safe_yaml:,safe_yaml}}}*

%build

%install
%ruby_vendor install.rb \
	     --destdir=%buildroot \
	     --configdir=%_sysconfdir/puppet \
	     --codedir=%_sysconfdir/puppet/code \
	     --vardir=%_localstatedir/puppet \
	     --rundir=%_runtimedir/puppet \
	     --logdir=%_logdir/puppet \
	     --no-rdoc \
	     --no-tests

# Systemd files
install -Dp -m0644 ext/systemd/puppet.service %buildroot%_unitdir/puppet.service
ln -s %_unitdir/puppet.service -T %buildroot%_unitdir/puppetagent.service
install -Dp -m0644 ext/systemd/puppetmaster.service %buildroot%_unitdir/puppetmaster.service
# SysVInit files
install -Dp -m0644 %confdir/client.sysconfig %buildroot%_sysconfdir/sysconfig/puppet
install -Dp -m0755 %confdir/client.init %buildroot%_initrddir/puppet
install -Dp -m0644 %confdir/server.sysconfig %buildroot%_sysconfdir/sysconfig/puppetmaster
install -Dp -m0755 %confdir/server.init %buildroot%_initrddir/puppetmaster

install -Dp -m0644 %confdir/fileserver.conf %buildroot%_sysconfdir/puppet/fileserver.conf
install -Dp -m0644 %confdir/puppet.conf %buildroot%_sysconfdir/puppet/puppet.conf
install -Dp -m0644 %confdir/logrotate %buildroot%_sysconfdir/logrotate.d/puppet

# Install the ext/ directory to %%_datadir/%%name
install -d %buildroot%_datadir/puppet
cp -a ext/ -t %buildroot%_datadir/puppet

# Install emacs mode files
emacsdir=%buildroot%_datadir/emacs/site-lisp
install -Dp -m0644 ext/emacs/puppet-mode.el $emacsdir/puppet-mode.el
install -Dp -m0644 ext/emacs/puppet-mode-init.el \
    $emacsdir/site-start.d/puppet-mode-init.el

# Install vim syntax files
vimdir=%buildroot%_datadir/vim/vimfiles
install -Dp -m0644 ext/vim/ftdetect/puppet.vim $vimdir/ftdetect/puppet.vim
install -Dp -m0644 ext/vim/syntax/puppet.vim $vimdir/syntax/puppet.vim

# TODO Install wrappers for SELinux
#install -Dp -m0755 %%SOURCE4 %buildroot%_bindir/start-puppet-agent
#sed -i 's/@@COMMAND@@/agent/g' %buildroot%_bindir/start-puppet-agent
#install -Dp -m0755 %%SOURCE4 %buildroot%_bindir/start-puppet-master
#sed -i 's/@@COMMAND@@/master/g' %buildroot%_bindir/start-puppet-agent

# Setup tmpfiles.d config
mkdir -p %buildroot%_sysconfdir/tmpfiles.d
echo "D /var/run/puppet 0755 _puppet puppet -" > \
    %buildroot%_sysconfdir/tmpfiles.d/%name.conf

# Create puppet modules directory for puppet module tool
mkdir -p %buildroot%_sysconfdir/puppet/modules

# Create service directory
mkdir -p %buildroot{%_localstatedir,%_logdir,%_runtimedir}/puppet

# emacs and vim bits are installed elsewhere
rm -r %buildroot%_datadir/puppet/ext/{emacs,vim}
# remove misc packaging artifacts in source not applicable to rpm
rm -r %buildroot%_datadir/puppet/ext/{gentoo,freebsd,solaris,suse,windows,osx,ips,debian}
rm -r %buildroot%_datadir/puppet/ext/{redhat,systemd}
rm %buildroot%_datadir/puppet/ext/{build_defaults.yaml,project_data.yaml}
# remove obsoleted checks
rm -r %buildroot%_datadir/puppet/ext/nagios

# Add missing directories
install -d %buildroot%_localstatedir/puppet/ssl/private_keys

%pre
%_sbindir/groupadd -r -f puppet
%_sbindir/useradd -r -n -g puppet -d %_localstatedir/puppet -s /dev/null -c Puppet _puppet >/dev/null 2>&1 ||:

%post
%post_service puppet

%preun
%preun_service puppet

%post server
%post_service puppetmaster

%preun server
%preun_service puppetmaster

%files
%_initdir/puppet
%_unitdir/puppet.service
%_unitdir/puppetagent.service
%config(noreplace) %_sysconfdir/tmpfiles.d/%name.conf
%dir %_sysconfdir/puppet
%config(noreplace) %_sysconfdir/puppet/puppet.conf
%config(noreplace) %_sysconfdir/puppet/auth.conf
%config(noreplace) %_sysconfdir/sysconfig/puppet
%config(noreplace) %_sysconfdir/logrotate.d/puppet
%_bindir/puppet
%_bindir/extlookup2hiera
%ruby_sitelibdir/*
%_datadir/puppet
%_man8dir/*
%_man5dir/puppet.conf.5*
%_datadir/emacs
%_datadir/vim
%attr(1770,_puppet,puppet) %dir %_localstatedir/puppet
%_localstatedir/puppet/*
%attr(1770,_puppet,puppet) %dir %_localstatedir/puppet/ssl/private_keys
%attr(1770,_puppet,puppet) %dir %_logdir/puppet
%attr(1770,_puppet,puppet) %dir %_runtimedir/puppet

%files server
%_initdir/puppetmaster
%_unitdir/puppetmaster.service
%config(noreplace) %_sysconfdir/puppet/fileserver.conf
%config(noreplace) %_sysconfdir/sysconfig/puppetmaster

%changelog
* Fri Mar 17 2017 Ivan Zakharyaschev <imz@altlinux.org> 3.8.7-alt1
- Latest Puppet3 built (3.8.7) for those who don't move to Puppet4
- NetworkManager dispatcher script removed (by Puppet in 3.8.7 & 4.4.1
  for (PUP-4545): Too many restarts on interface changes)
- ext/puppetlisten removed (as in Puppet4) because its SSL code is rotten
- Used all relevant ALT adaptions from 4.8.2-alt1

* Wed Feb 15 2017 Ivan Zakharyaschev <imz@altlinux.org> 4.8.2-alt2
- NetworkManager dispatcher script removed (by Puppet in 3.8.7 & 4.4.1
  for (PUP-4545): Too many restarts on interface changes)
- (.spec) cleanup
  (Prepare for other names, e.g., for packaging the previous puppet3.)

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

