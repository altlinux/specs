
Name:    puppet
Version: 2.7.21
Release: alt2

Summary: System administration - Automated
Group:   System/Servers
License: MIT
Url:     https://puppetlabs.com/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

#AutoReq: yes,noruby
BuildRequires: rpm-build-ruby ruby-facter

%description
Puppet lets you centrally manage every important aspect of your
system using a cross-platform specification language that manages
all the separate elements normally aggregated in different files,
like users, cron jobs, and hosts, along with obviously discrete
elements like packages, services, and files.

%package http_server-mongrel
Summary: Mongrel HTTP server for Puppet
Group: System/Servers
PreReq: %name = %version-%release

%description http_server-mongrel
Mongrel HTTP server for Puppet.

%package server
Summary: Server for the puppet system management tool
Group: System/Servers
Requires: %name = %version-%release

%description server
Provides the central puppet server daemon which provides manifests
to clients.  The server can also function as a certificate authority
and file server.

You may need to install appropriate %name-http_server-XXX.

%prep
%setup
%patch -p1

%build
# MacOS X crap
rm -f lib/puppet/provider/service/launchd.rb \
      lib/puppet/provider/macauthorization/macauthorization.rb \
      lib/puppet/provider/package/appdmg.rb \
      lib/puppet/provider/package/pkgdmg.rb \
      lib/puppet/provider/nameservice/directoryservice.rb \
      lib/puppet/provider/group/directoryservice.rb \
      lib/puppet/provider/user/directoryservice.rb \
      lib/puppet/provider/computer/computer.rb
# Only used by (non-packaged) puppetdoc
rm -rf lib/puppet/util/rdoc*

%install
mkdir -p %buildroot{%_sysconfdir/{logrotate.d,sysconfig,puppet/manifests},%_localstatedir/puppet,%_logdir/puppet,%_var/run/puppet,%_initdir}

%ruby_vendor install.rb --destdir=%buildroot
install -p -m644 conf/altlinux/*.conf %buildroot%_sysconfdir/puppet
install -p -m755 conf/altlinux/puppetd.init %buildroot%_initdir/puppetd
install -p -m755 conf/altlinux/puppetmasterd.init %buildroot%_initdir/puppetmasterd
install -p -m644 conf/altlinux/puppet.sysconfig %buildroot%_sysconfdir/sysconfig/puppet
install -p -m644 conf/altlinux/puppetmaster.sysconfig %buildroot%_sysconfdir/sysconfig/puppetmaster
install -p -m644 conf/altlinux/logrotate %buildroot%_sysconfdir/logrotate.d/puppet

rm -rf %buildroot/usr/lib/ruby/site_ruby/puppet/util/windows*
rm -rf %buildroot/usr/lib/ruby/site_ruby/puppet/module_tool/skeleton/templates/generator/spec

%pre
%_sbindir/groupadd -r -f puppet
%_sbindir/useradd -r -n -g puppet -d %_localstatedir/puppet -s /dev/null -c Puppet _puppet >/dev/null 2>&1 ||:

%post
%post_service puppetd

%preun
%preun_service puppetd

%post server
%post_service puppetmasterd

%preun server
%preun_service puppetmasterd

%files
%config %_initdir/puppetd
%dir %_sysconfdir/puppet
%config(noreplace) %_sysconfdir/puppet/puppet.conf
%config(noreplace) %_sysconfdir/puppet/auth.conf
%config(noreplace) %_sysconfdir/sysconfig/puppet
%config(noreplace) %_sysconfdir/logrotate.d/puppet
%_bindir/pi
%_bindir/puppet
%_bindir/puppetdoc
%_bindir/ralsh
%_bindir/filebucket
%_sbindir/puppetd
%_sbindir/puppetqd
%ruby_sitelibdir/*
%exclude %ruby_sitelibdir/puppet/network/http/mongrel*
%exclude %ruby_sitelibdir/puppet/network/http_server/*
%_man8dir/pi.8*
%_man8dir/puppet.8*
%_man5dir/puppet.conf.5*
%_man8dir/ralsh.8*
%_man8dir/filebucket.8*
%_man8dir/puppetd.8*
%_man8dir/puppetqd.8*
%_man8dir/puppetdoc.8*
%_man8dir/puppet-*.8*

%attr(1770,_puppet,puppet) %dir %_localstatedir/puppet
%attr(1770,root,puppet) %dir %_logdir/puppet
%attr(1770,root,puppet) %dir %_var/run/puppet

%files http_server-mongrel
%ruby_sitelibdir/puppet/network/http/mongrel*
%ruby_sitelibdir/puppet/network/http_server/mongrel.rb 

%files server
%config %_initdir/puppetmasterd
%dir %_sysconfdir/puppet
%config(noreplace) %_sysconfdir/puppet/fileserver.conf
%config(noreplace) %_sysconfdir/sysconfig/puppetmaster
%_sbindir/puppetrun
%_sbindir/puppetmasterd
%_sbindir/puppetca
%_man8dir/puppetrun.8*
%_man8dir/puppetmasterd.8*
%_man8dir/puppetca.8*
%attr(1770,root,puppet) %dir %_logdir/puppet
%attr(1770,root,puppet) %dir %_var/run/puppet

%changelog
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

