# FIXME: init-script!
# TODO: xinetd

Name: p910nd
Version: 0.97
Release: alt1

Summary: Tiny non-spooling printer daemon

License: GPL
Group: System/Servers
Url: http://p910nd.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/p910nd/%name-%version.tar
Source1: %name.init
Patch: %name-open.patch

BuildRequires: libwrap-devel

%description
Tiny non-spooling printer daemon for Linux hosts. Accepts data over a
TCP network connection from a spooling host. Useful on diskless X
terminals with local printer.

%prep
%setup

%build
%make_build USE_WRAP=1

%install
%makeinstall_std
install -d %buildroot%_initdir %buildroot%_datadir/%name
#install %SOURCE1 %buildroot/%_initdir/p910nd
install %SOURCE1 %name.init1
#install -m755 p910nd %buildroot%_sbindir
install *.pl %buildroot%_datadir/%name/
#install p910nd.8 %buildroot%_man8dir
rm -rf %buildroot/etc/init.d/p910nd

%post
#%%post_service %name

%preun
#%%preun_service %name

%files
#_initddir/%name
%doc %name.init %name.init1
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sbindir/%name
%_datadir/%name/
%_man8dir/*


%changelog
* Sun Jun 24 2018 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt1
- new version 0.97 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.92-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- new version 0.92 (with rpmrb script)

* Mon Jan 30 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt0.1
- initial build for ALT Linux Sisyphus (spec from PLD)

