Name: xCAT-server
Summary: Server and configuration utilities of the xCAT management project
Version: 2.5.1
Release: alt0.4.2
License: EPL
Group: System/Servers
Source: xCAT-server-%{version}.tar
Source1: xcat-sysconfig
Source2: xcatd-init
Source3: sources.list_x86_64
Source4: sources.list_x86
Packager: Andriy Stepanov <stanv@altlinux.ru>
BuildArch: noarch

# XXX@stanv:
Provides: perl(imgutils.pm)

Requires: perl-xCAT   >= %{version}
Requires: xCAT-client >= %{version}
Requires: squashfsprogs3
Requires: bind-utils
Requires: perl-Template
Requires: perl-File-Copy-Recursive
Requires: perl-DBD-SQLite
BuildRequires: perl-Curses perl-xCAT perl-Net-SSLeay perl-Template perl-DBD-SQLite
BuildRequires: perl-Net-DNS

%description
xCAT-server provides the core server and configuration management
components of xCAT.  This package should be installed on your management
server.

%add_findreq_skiplist %_datadir/xcat/netboot/add-on/*/*
%add_findreq_skiplist %_datadir/xcat/netboot/*/*
%add_findreq_skiplist %_datadir/xcat/install/*/*
%add_findreq_skiplist %_datadir/xcat/rollupdate/LL_setup
%add_findreq_skiplist %{perl_vendor_privlib}/xCAT_plugin/aixinstall.pm

%add_findreq_skiplist %{perl_vendor_privlib}/xCAT_plugin/AAsn.pm

# XXX@stanv: remove, when hpoa.pm issues will be solved. See perl-xCAT spec for `include'
# %add_findreq_skiplist %{perl_vendor_privlib}/xCAT_plugin/hpblade.pm

%prep
%setup -q

%build

%install

# Binaries.
install -d -pm 755 %{buildroot}%{_bindir}
install -d -pm 755 %{buildroot}%{_sbindir}

install -D -pm 755 bin/* %{buildroot}%{_bindir}
install -D -pm 755 sbin/* %{buildroot}%{_sbindir}

ln -sf ../sbin/stopstartxcatd %{buildroot}%{_sbindir}/xcatstart
ln -sf ../sbin/stopstartxcatd %{buildroot}%{_sbindir}/xcatstop

for i in ca rollupdate installp_bundles; do
  install -d -pm 755 %{buildroot}%{_datadir}/xcat/$i
  install -D -pm 644 share/xcat/$i/* %{buildroot}%{_datadir}/xcat/$i
done

# XXX: use install instead cp
cp -r share/xcat/install %{buildroot}%{_datadir}/xcat/

# Skip genimage for other foreign distros.
# "This command should be run on a system matching the architecture and distribution of the intended image."
# So, we don't need them on ALT Linux systems.
install -d -pm 755 %{buildroot}%{_datadir}/xcat/netboot
cp -r share/xcat/netboot/add-on %{buildroot}%{_datadir}/xcat/netboot/
cp -r share/xcat/netboot/imgutils %{buildroot}%{_datadir}/xcat/netboot/

for i in scripts tools cons "ib/scripts"; do
  install -d -pm 755 %{buildroot}%{_datadir}/xcat/$i
  install -D -pm 755 share/xcat/$i/* %{buildroot}%{_datadir}/xcat/$i
done

ln -sf %{_datadir}/xcat/cons/hmc %{buildroot}/%{_datadir}/xcat/cons/ivm

# Perl libs.
install -d -pm 755 %{buildroot}%{perl_vendor_privlib}/{xCAT,xCAT_plugin}
install -d -pm 755 %{buildroot}%{perl_vendor_privlib}/xCAT_monitoring/{samples,pcp}
install -d -pm 755 %{buildroot}%{perl_vendor_privlib}/xCAT_schema/samples

install -D -pm 644 lib/xcat/plugins/*      %{buildroot}%{perl_vendor_privlib}/xCAT_plugin
install -D -pm 644 lib/perl/xCAT/*      %{buildroot}%{perl_vendor_privlib}/xCAT

install -D -pm 644 lib/xcat/monitoring/samples/*  %{buildroot}%{perl_vendor_privlib}/xCAT_monitoring/samples
install -D -pm 644 lib/xcat/monitoring/pcp/*  %{buildroot}%{perl_vendor_privlib}/xCAT_monitoring/pcp
install -D -pm 644 lib/xcat/monitoring/*.pm  %{buildroot}%{perl_vendor_privlib}/xCAT_monitoring

install -D -pm 644 lib/xcat/schema/samples/* %{buildroot}%{perl_vendor_privlib}/xCAT_schema/samples

# !!!!
# OPT ?????
install -d -pm 755 %{buildroot}%{_datadir}/xcat/xdsh/Context
install -D -pm 644 lib/xcat/dsh/Context/* %{buildroot}%{_datadir}/xcat/xdsh/Context

install -d -pm 755 %{buildroot}%{_datadir}/xcat/lib
install -D -pm 644 lib/xcat/shfunctions %{buildroot}/%{_datadir}/xcat/lib

# Init scrips.
install -d -pm 755 %{buildroot}%{_initdir}
install -D -pm 755 %{S:2} %{buildroot}%{_initdir}/xcatd

# Configuration files.
install -d -pm 755 %{buildroot}%{_sysconfdir}/xcat
install -D -pm 644 etc/xcat/postscripts.rules %{buildroot}%{_sysconfdir}/xcat

# Sysconfig
install -m 755 -d %{buildroot}%_sysconfdir/sysconfig
install -D -pm 644 %{S:1} %{buildroot}%{_sysconfdir}/sysconfig/xcat

# Directory with ALT Linux config files
install -m 755 -d %{buildroot}%_sysconfdir/xcat/alt
install -m 755 -d %{buildroot}%_sysconfdir/xcat/alt/nodes

# sources.list example files
install -D -pm 644 %{S:3} %{buildroot}%{_sysconfdir}/xcat/alt
install -D -pm 644 %{S:4} %{buildroot}%{_sysconfdir}/xcat/alt
install -D -pm 644 %{S:3} %{buildroot}%{_sysconfdir}/xcat/alt/nodes
install -D -pm 644 %{S:4} %{buildroot}%{_sysconfdir}/xcat/alt/nodes

%post
if [ -f /etc/profile.d/xcat.sh ]; then
  . /etc/profile.d/xcat.sh
fi
%post_service xcatd
if [ "$1" -gt "1" ]; then #only on upgrade...
  # Migration issue for monitoring
  %{_sbindir}/chtab filename=monitorctrl.pm notification -d
fi

if [ "$1" = "1" ]; then #Only if installing for the first time..
  # Default path to sources.list config files:
  XCATBYBASS=1 chtab key=aptsrclist_x86_64 site.value="/etc/xcat/alt/sources.list_x86_64"
  XCATBYBASS=1 chtab key=aptsrclist_x86 site.value="/etc/xcat/alt/sources.list_x86"
  # In ALT Linux BIND runned in chroot environment
  XCATBYBASS=1 chtab key=binddir site.value="/var/lib/bind/zone/"
  XCATBYBASS=1 chtab key=bindzones site.value="/zone/"
  XCATBYBASS=1 chtab key=bindconf site.value="/var/lib/bind/etc/named.conf"
fi



%preun
%preun_service xcatd

%files
%{_bindir}/*
%{_sbindir}/*
%{perl_vendor_privlib}/xCAT
%{perl_vendor_privlib}/xCAT_plugin
%{perl_vendor_privlib}/xCAT_schema
%{perl_vendor_privlib}/xCAT_monitoring
%{_datadir}/xcat
%{_sysconfdir}/xcat
%{_initdir}/*
%{_sysconfdir}/sysconfig/xcat

%changelog
* Thu Mar 10 2011 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4.2
- Fix rebuild pass through for Sisyphus.

* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4.1
- patch from madmax@ for ibswitch.pm.

* Wed Nov 24 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.4
- Update from upstream SVN: trunk@8256.

* Mon Nov 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.3
- Update from upstream SVN: trunk@8225.

* Mon Nov 15 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.2
- Update from upstream SVN: trunk@8159.

* Thu Oct 28 2010 Andriy Stepanov <stanv@altlinux.ru> 2.5.1-alt0.1
- Update from upstream SVN: trunk@7954.

* Fri Oct 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.4
- Update from upstream SVN: trunk@7904.

* Wed Oct 06 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.3
- Update from upstream SVN: trunk@7760.

* Fri Sep 17 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.2
- Update from upstream SVN: trunk@7490.

* Sat Sep 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.4-alt0.1
- Update from upstream SVN: trunk@7385.

* Sun Jun 27 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.3-alt0.1
- Update from upstream SVN: trunk@6611.

* Mon Jun 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.2
- Update from upstream SVN: trunk@6560.

* Wed Jun 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.4.2-alt0.1
- Update from upstream SVN: trunk@6312.

* Tue May 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.8
- Update from upstream SVN: trunk@6208.

* Thu Apr 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.7
- Update from upstream SVN: trunk@5831.

* Thu Mar 25 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.6
- merge patches branch.

* Tue Mar 23 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.5
- fix typos.

* Tue Mar 23 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.4
- Add requires to perl-File-Copy-Recursive for ALT genimage.

* Mon Mar 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.3
- dns.pm adaptation

* Mon Mar 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.2
- Update from upstream SVN: trunk@5541.

* Thu Mar 18 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.5-alt0.1
- Update from upstream SVN: trunk@5517.

* Tue Mar 02 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.8
- Update from upstream SVN: trunk@5320.

* Tue Feb 09 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.7
- Move to standard directories

* Mon Feb 08 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.6
- Update from upstream SVN.

* Fri Jan 22 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.5
- Skip findreq for install scripts.

* Thu Jan 21 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.4
- Update from upstream SVN: trunk@5004.

* Tue Jan 19 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.3
- Update from upstream SVN: trunk@4978.

* Mon Jan 11 2010 Andriy Stepanov <stanv@altlinux.ru> 2.3.3-alt0.2
- Update from upstream SVN.

* Mon Dec 14 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.2
- Add patches.

* Fri Dec 11 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3.2-alt0.1
- Update from upstream SVN.

* Thu Nov 12 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.3
- Update from upstream SVN.

* Tue Nov 03 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.2
- Update from upstream SVN.

* Thu Oct 29 2009 Andriy Stepanov <stanv@altlinux.ru> 2.3-alt0.1
- Package for ALT Linux.

