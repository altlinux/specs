Name: rdesktop
Version: 1.6.0
Release: alt4.1

Summary: Powerful tool for remote desktop connection
License: GPL
Group: Networking/Remote access

Url: http://www.rdesktop.org/
Source0: %name-%version.tar.gz
Source1: ru.fixed
Patch0: rdesktop-1.5.0-rawkeyboard_nofreespace_kbswitch.patch
Patch1: rdesktop-1.6_auto_raw_keyboard.patch
Patch2: rdesktop-alt-man.patch
Patch3: rdesktop.long.names.on.redirect.drives.patch
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Automatically added by buildreq on Mon Jan 25 2010
BuildRequires: imake libICE-devel libX11-devel libalsa-devel libsamplerate-devel libssl-devel xorg-cf-files
# optimized out: glibc-pthread perl-threads pkg-config xorg-kbproto-devel xorg-xproto-devel

Summary(ru_RU.KOI8-R): Удалённое графическое подключение к Windows по протоколу RDP

%description
Powerful tool for remote desktop connection. It can be used to
access Windows NT and Windows 2000 terminal servers. Unlike Citrix ICA
it doesn't require any additional software to be setup on server.

%description -l ru_RU.KOI8-R
Программа для удалённого графического подключения к Windows по протоколу RDP.
Может быть использовано для доступа к Windows NT и Windows 2002
терминальным серверам, а также Windows XP PE. В отличие от Citrix ICA
эта программа не требует установки дополнительного ПО на сервер.

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%autoreconf
%add_optflags -DSAVE_LICENSE
%configure \
	--prefix=%prefix \
	--mandir=%prefix/share/man \
	--with-openssl=%prefix \
	--with-ipv6 \
	--with-sound=alsa
# --with-libvncserver
# --with-debug-kbd
%make_build

%install
%makeinstall_std
install -pm644 %SOURCE1 %buildroot%_datadir/%name/keymaps/

%files
%_bindir/*
%_man1dir/*
%_datadir/%name

%changelog
* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 1.6.0-alt4.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Tue Jan 26 2010 Michael Shigorin <mike@altlinux.org> 1.6.0-alt4
- fixed (historical/unused) patch0 compression, thanks ldv@

* Mon Jan 25 2010 Michael Shigorin <mike@altlinux.org> 1.6.0-alt3
- built for Sisyphus (closes: #19968)
- buildreq

* Sun Jan 24 2010 Michael A. Kangin <prividen@altlinux.org> 1.6.0-alt2.1.2
- New raw keyboard patch

* Thu Aug 27 2009 Michael A. Kangin <prividen@altlinux.org> 1.6.0-alt2.1.1
- remove '-y' patch due evdev incompatibility (#19968)
- fixed RU keymap (#5912)

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.6.0-alt2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Wed Jul 09 2008 Igor Zubkov <icesik@altlinux.org> 1.6.0-alt2
- fix crash with long filenames (closes #13495)

* Wed May 14 2008 Igor Zubkov <icesik@altlinux.org> 1.6.0-alt1
- 1.6.0 release

* Sat May 10 2008 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt7
- CVE-2008-1801
- CVE-2008-1802
- CVE-2008-1803

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt6
- add description of -y option to man page (closes #11447)

* Wed Sep 26 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt5
- remove menu file (closes #12794)

* Sat Apr 21 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt4
- update patch for raw input

* Sat Apr 21 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt3
- update from CVS (20070521) which fix random segfaults (#11441)
- build with alsa and without libao

* Thu Feb 22 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt2
- build with libao (closes #10741)
- buildreq

* Thu Feb 22 2007 Igor Zubkov <icesik@altlinux.org> 1.5.0-alt1
- enable IPv6 support (closes #10739)

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.5.0-alt0.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Mon Dec 04 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.5.0-alt0
- NMU: Fix (#6280)
- new version
- drop %name-1.4.1.20060218-rawkeyboard.patch
- add %name-1.5.0-rawkeyboard_nofreespace_kbswitch.tar.bz2

* Sat Feb 18 2006 Sergey Y. Afonin <asy@altlinux.ru> 1.4.1.20060218-alt0
- CVS 20060218 (utf8 support in clipboard)

* Wed Oct 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- add patch from Serge Ryabchun (sr@) for raw keyboard mode (-y option)

* Thu Jul 07 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt0.1
- new version
- dropped a patches as merged with mainstream

* Fri Apr 01 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt0.1
- new version

* Sat Oct 30 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt4
- add patch for KDE embedded (krdc)

* Sat Sep 04 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt3
- fix username encoding in command line options
  (add patch from Alexey V. Novikov (bug #5054))

* Wed Jul 28 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- remove menu entry (bug #3975)

* Sun May 02 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version

* Mon Jan 12 2004 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version
- spec cleanup

* Fri Feb 14 2003 Dmitry Malenko <maldim@altlinux.ru> 1.2.0-alt2
- Fixed to look for keymaps in proper place

* Thu Feb 06 2003 Dmitry Malenko <maldim@altlinux.ru> 1.2.0-alt1
- New version
- Spec cleanup

* Wed Jan 29 2003 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt4
- Spec cleanup

* Fri Jan 24 2003 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt3
- Added Mandrake patch:
    * fixed NumLock behavior
    * support for mouse wheel
- Added man to distribution

* Mon Jun 24 2002 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt2
- Changed rdesktop.menu to accept RDP_CONNECTION variable as a parameter

* Wed May 29 2002 Dmitry Malenko <maldim@altlinux.ru> 1.1.0-alt1
- Packaged for ALT Linux

