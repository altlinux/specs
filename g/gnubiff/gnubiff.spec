%define _name gnubiff

%def_with password

Name: %_name
Version: 2.2.11
Release: alt3.1

Summary: gnubiff is a mail notifier that displays headers when new mail has arrived.
License: %gpl3plus w/exception for OpenSSL
Group: Networking/Mail
Url: http://gnubiff.sourceforge.net

Source: http://downloads.sourceforge.net/%_name/%_name-%version.tar.gz
Source2: %name.desktop
Patch: %_name-2.2.9-alt-tls-support.patch
#Patch1: %_name-2.2.9-fix-build.patch
Patch3: %_name-2.2.11-fix-building.patch
Patch4: gnubiff-2.2.11-alt-DSO.patch

BuildPreReq: rpm-build-licenses

# From configure.ac
BuildPreReq: libgamin-devel >= 0.1.0
BuildPreReq: libgtk+2-devel >= 2.6
BuildPreReq: glib2-devel >= 2.4
BuildPreReq: libglade2-devel >= 2.3
BuildPreReq: libpopt-devel

BuildRequires: gcc-c++ libxml2-devel perl-XML-Parser

%description
gnubiff is a mail notification program that checks for mail and displays
headers when new mail has arrived. This package contains Gtk+ version that
does not need a GNOME panel to work.

gnubiff features include:

    * Multiple mailbox support
    * pop3, apop, imap4, mh, qmail and mailfile support
    * SSL & certificates support
    * GNOME support with complete integration to panel
    * GTK stand-alone support
    * Automatic detection of mailbox format
    * Mail header & content display
    * IDLE state support for imap4
    * FAM support for mh/qmail/mailfile
    * PNG animation support
    * Highly configurable
    * Spam filtering
    * HIG 2.0 compliance
    * Small memory usage

%prep
%setup -q -n %_name-%version
%patch -p1 -b .alt-tls-support
#patch1 -p0 -b .fix-build
%patch3 -p0 -b .fix-building
%patch4 -p2

%build
%configure \
    %{subst_with password} \
    %{?_with_password:--with-password-string="andthentherewere3"} \
    --enable-expert \
    --disable-gnome

%make_build

%install
%makeinstall_std
install -pD -m644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

%find_lang %_name

%files -f %_name.lang
%_bindir/%_name
%dir %_datadir/%_name
%_datadir/%_name/*
%_pixmapsdir/*
%_desktopdir/*.desktop
%_infodir/*.info*
%_man1dir/*
%doc README ChangeLog COPYING THANKS TODO NEWS AUTHORS

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.11-alt3.1
- Fixed build

* Tue Nov 10 2009 Alexey Rusakov <ktirf@altlinux.org> 2.2.11-alt3
- Removed obsolete (un)install_info invocations.

* Wed May 20 2009 Alexey Rusakov <ktirf@altlinux.org> 2.2.11-alt2
- Added a %_datadir/gnubiff directory to the files list.

* Fri May 15 2009 Alexey Rusakov <ktirf@altlinux.org> 2.2.11-alt1
- New version (2.2.11).

* Sun Mar 29 2009 Alexey Rusakov <ktirf@altlinux.org> 2.2.10-alt2
- Removed deprecated post/postun macros.
- Use makeinstall_std macro instead of makeinstall

* Fri Nov 07 2008 Alexey Rusakov <ktirf@altlinux.org> 2.2.10-alt1
- New version (2.2.10).
- Fixed building with the new toolchain.
- Added a .desktop file.

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.9-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat Feb 09 2008 Alexey Rusakov <ktirf@altlinux.org> 2.2.9-alt1
- New version (2.2.9).
- Added STARTTLS support (ALT Bug 14373, thanks to hiddenman@ for the
  patch).

* Wed Sep 12 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.8-alt1
- new version (2.2.8)
- upstream relicensed under %gpl3plus

* Fri Aug 24 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.7-alt1
- new version
- use a macro from rpm-build-licenses

* Tue Feb 20 2007 Alexey Rusakov <ktirf@altlinux.org> 2.2.5-alt1
- new version (2.2.5)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 2.2.3-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Oct 23 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Tue Aug 08 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.2.2-alt1
- new version (2.2.2)
- added passwords saving switch and turned it on by default (per
  hiddenman@'s request).

* Sun Jun 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.2.1-alt1
- new version (2.2.1)
- updated dependencies.

* Tue Aug 23 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.1.5-alt1
- New upstream version.

* Thu Jul 21 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.1.4-alt1
- New upstream version.

* Mon Apr 11 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.1.3-alt1
- Initial Sisyphus package.

