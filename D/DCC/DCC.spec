%def_disable dccm

%define home_dir %_localstatedir/dcc
%define mylibexec_dir %_libexecdir/dcc

# set to spamd because spamassassin is the primary user
%define default_user  spamd
%define default_group spamd

Summary: A clients-server system for collecting checksums of mail messages
Name: DCC
Version: 2.3.169
Release: alt0.1
License: MIT-0
Group: System/Servers
Url: http://www.rhyolite.com/anti-spam/dcc/
Source0: http://www.rhyolite.com/anti-spam/dcc/source/dcc-%version.tar
Source1: dcc.service
Source2: dccifd.socket
Requires: spamassassin-spamd

%if_enabled dccm
BuildRequires: sendmail-devel
%endif

%description
The DCC or Distributed Checksum Clearinghouse is currently a system of
many clients and more than 120 servers that collects and count
checksums related to several million mail messages per day, most as
seen by Internet Service Providers. The counts can be used by SMTP
servers and mail user agents to detect and reject or filter spam or
unsolicited bulk mail. DCC servers exchange or "flood" common
checksums. The checksums include values that are constant across
common variations in bulk messages, including "personalizations."

%prep
%setup -n dcc-%version
find . -name Makefile.in | xargs subst 's/chown/:/g'

%build
export CFLAGS="%optflags"
PERL=%_bindir/perl ./configure \
  --with-installroot=%buildroot \
  %{subst_enable dccm} \
  --homedir=%home_dir \
  --libexecdir=%mylibexec_dir \
  --bindir=%_bindir \
  --mandir=%_mandir \
  --disable-sys-inst
%make_build

%install
make install
#make install \
#  SET_BINOWN= SET_MANOWN= SET_DCCOWN=
%_bindir/perl -pi -e 's,%buildroot,,gi' %buildroot%home_dir/map.txt
mkdir -p %buildroot%_man8dir
cp -a *.8 %buildroot%_man8dir
install -pD -m644 %SOURCE1 %buildroot%_unitdir/dcc.service
install -pD -m644 %SOURCE2 %buildroot%_unitdir/dccifd.socket
mkdir -p %buildroot{%_initdir,%_sysconfdir/cron.daily}
ln -s %mylibexec_dir/rcDCC %buildroot%_initdir/rcDCC
ln -s %mylibexec_dir/cron-dccd %buildroot%_sysconfdir/cron.daily/cron-dcc

%files
%doc LICENSE FAQ* CHANGES
%attr(43770,root,%default_group) %dir %home_dir
%attr(640,root,%default_group) %config(noreplace) %home_dir/dcc_conf
%attr(640,root,%default_group) %config(noreplace) %home_dir/flod
%attr(640,root,%default_group) %config(noreplace) %home_dir/grey_flod
%attr(640,root,%default_group) %config(noreplace) %home_dir/grey_whitelist
%attr(600,%default_user,%default_group) %config(noreplace) %home_dir/ids
%attr(710,%default_user,%default_group) %config(noreplace) %home_dir/log
%attr(600,%default_user,%default_group) %config(noreplace) %home_dir/map
%attr(600,%default_user,%default_group) %config(noreplace) %home_dir/map.txt
%attr(640,root,%default_group) %config(noreplace) %home_dir/whiteclnt
%attr(640,root,%default_group) %config(noreplace) %home_dir/whitecommon
%attr(640,root,%default_group) %config(noreplace) %home_dir/whitelist
%config %_unitdir/dcc.service
%config %_unitdir/*.socket
%_sysconfdir/cron.daily/*
%_initdir/*
%_bindir/cdcc
%_bindir/dccproc
%_bindir/dccif-test
%mylibexec_dir
%_man8dir/*

%changelog
* Mon May 06 2024 L.A. Kostis <lakostis@altlinux.ru> 2.3.169-alt0.1
- 3.1.169.

* Sat Feb 19 2022 L.A. Kostis <lakostis@altlinux.ru> 2.3.168-alt0.1
- 2.3.168.
- systemd: fix stale socket.

* Fri Mar 12 2021 L.A. Kostis <lakostis@altlinux.ru> 2.3.167-alt0.2
- Added systemd units and sockets.
- Added sysv init link.
- Added cleanup cron script link.
- Fix compilation with recent gcc.

* Mon Jul 22 2019 L.A. Kostis <lakostis@altlinux.ru> 2.3.167-alt0.1
- Version 2.3.167.

* Mon Mar 27 2017 L.A. Kostis <lakostis@altlinux.ru> 1.3.159-alt0.1
- Version 1.3.159.

* Wed Nov 04 2015 L.A. Kostis <lakostis@altlinux.ru> 1.3.158-alt0.1
- initial build for ALTLinux.

* Mon Jun 10 2013 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.145-24
- Update to 1.3.145.

* Sun Mar  1 2009 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.103-23
- Update to 1.3.103.

* Wed Apr 30 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.90-22
- Update to 1.3.90.

* Wed Oct 17 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.66-20
- Update to 1.3.66.

* Sat Oct 13 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.64-19
- Update to 1.3.64.

* Wed Jun 13 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.57-18
- Update to 1.3.57.

* Wed May 23 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.56-17
- Update to 1.3.56.

* Mon Feb 12 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.50-16
- update to 1.3.50.

* Sun Oct 22 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.3.42-15
- Update to 1.3.42.

* Wed May 31 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.3.31.

* Sat Nov 26 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.3.21.

* Sun Apr  3 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.3.0.

* Sun Mar  6 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.71.

* Mon Jan 17 2005 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.67.

* Fri Dec 17 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.64.

* Tue Nov  2 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.58.

* Fri Oct 22 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.57.

* Thu Sep 16 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.53.

* Mon May 31 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.49.

* Mon May  3 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Updated to 1.2.47.

* Sat Apr  3 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Update to 1.2.39.

* Fri May  2 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

