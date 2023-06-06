Name: conspy
Version: 1.16
Release: alt1

Summary: Remote control for text mode virtual consoles

Group: Terminals
License: AGPL-3.0+
Url: https://conspy.sourceforge.net/

# Source-url: http://prdownloads.sourceforge.net/%name/%name-%version-1/conspy-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Sat Jan 21 2006
BuildRequires: libncurses-devel libtinfo-devel

%description
Conspy takes over a text mode Linux virtual console in much
the same manner as VNC allows a remote user to take over a GUI.

%prep
%setup

%build
touch NEWS
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/conspy
%_man1dir/*

%changelog
* Tue Jun 06 2023 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- new version 1.16 (with rpmrb script) (ALT bug 46377)
- license changed to AGPL-3.0+

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- new version 1.8 (with rpmrb script)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.7-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Oct 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- new version 1.7 (with rpmrb script)

* Mon Jan 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Sat Jan 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt0.1
- initial build for ALT Linux Sisyphus

* Sun Jan 19 2006 Russell Stuart <russell-rpm@stuart.id.au>
- New upstream release.
* Sun Jan  9 2006 Russell Stuart <russell-rpm@stuart.id.au>
- New upstream release.
* Sun Jan  1 2006 Russell Stuart <russell-rpm@stuart.id.au>
- New upstream release.
* Wed May 21 2003 Russell Stuart <russell-rpm@stuart.id.au>
- Initial RPM
