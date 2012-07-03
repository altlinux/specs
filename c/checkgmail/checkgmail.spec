Name: checkgmail
Version: 1.13
Release: alt2.qa1

Summary: alternative Gmail Notifier

License: GPL
Group: Office
Url: http://checkgmail.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Source1: %name.desktop
Source2: %name.svg

Patch: %name.gtk.patch

Requires: perl-Crypt-Simple perl-Gtk2-Sexy 
# Automatically added by buildreq on Sat Dec 15 2007 (-bi)
BuildRequires: net-tools perl-Crypt-Simple perl-Encode perl-Gtk2-Sexy perl-Gtk2-TrayIcon perl-XML-Simple perl-libwww perl-threads perl-Crypt-SSLeay
BuildRequires: desktop-file-utils

%description
CheckGmail is a system tray application that checks a Gmail account for
new mail. When new mail is present the tray icon changes, an optional
animated popup is displayed and a tooltip displays the number and details
of new messages. Each message can be opened directly in a browser window,
and many common Gmail operations (marking as read, archiving, deleting
or reporting as spam) can be carried out on messages directly within
CheckGmail, without the need to use the Gmail web interface.

%prep
%setup -q
%patch

%install
install -m644 -D man/checkgmail.1.gz %buildroot%_man1dir/checkgmail.1.gz
install -m755 -D %name %buildroot%_bindir/%name
install -m644 -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -m644 -D %SOURCE2 %buildroot%_pixmapsdir/%name.svg
desktop-file-install --dir %buildroot%_desktopdir \
	--add-category=Email \
	%buildroot%_desktopdir/checkgmail.desktop

%files
%doc todo Readme ChangeLog
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/*
%_pixmapsdir/*

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.13-alt2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for checkgmail

* Mon Apr 18 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.13-alt2
- fix build

* Sat May 31 2008 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- new version 1.13 (with rpmrb script)

* Sat Dec 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- initial build for ALT Linux Sisyphus
