BuildRequires: desktop-file-utils
Name: krb5-ticket-watcher
Version: 1.0.3
Release: alt1.1
Summary: A Tray Applet for Watching, Renewing, and Reinitializing Kerberos Tickets
Url: http://sourceforge.net/projects/krb5ticketwatch
License: %gpl2plus
Group: System/X11

Packager: Andriy Stepanov <stanv@altlinux.ru>

Source: %name-%version.tar
Patch1: 0001-made-default-realm-the-first-one-in-list.patch
Patch2: krb5-ticket-watcher-1.0-alt-date-fix.patch
Patch3: krb5-ticket-watcher-1.0.3-alt-fix-includes.patch

BuildRequires: kde-common-devel rpm-build-licenses libkrb5-devel libkeyutils-devel
BuildRequires: cmake gcc-c++ libcom_err-devel libqt4-devel

%description
A tray applet for watching, renewing, and reinitializing Kerberos
tickets.

%prep
%setup
%patch1 -p2
%patch2 -p1
%patch3 -p2

%build
%add_optflags -I%_includedir/krb5
%K4build

%install
%K4install
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Security \
	%buildroot%_desktopdir/krb5-ticket-watcher.desktop

%files
%_bindir/krb5-ticket-watcher
%_pixmapsdir/krb5-ticket-watcher.png
%_desktopdir/krb5-ticket-watcher.desktop
%{_datadir}/locale/*/*/*.mo
%doc COPYING Changes News TODO

%changelog
* Sat Jan 05 2013 Ivan A. Melnikov <iv@altlinux.org> 1.0.3-alt1.1
- Fixed build with new krb5;
- Minor packaging improvements.

* Thu Sep 27 2012 Andriy Stepanov <stanv@altlinux.ru> 1.0.3-alt1
- New version

* Thu Jul 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3.qa2
- Fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.2-alt3.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for krb5-ticket-watcher

* Wed Apr 08 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt3
- #19536 (fix: convert valid/expires info to local charset)

* Mon Mar 30 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt2
- Add patch: Fetch default REALM name from DNS records.

* Sun Mar 22 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.2-alt1
- New version.

* Fri Mar 20 2009 Andriy Stepanov <stanv@altlinux.ru> 1.0.1-alt1
- Initial import to Sisyphus
