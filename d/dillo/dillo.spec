# Spec file for Dillo

Name: dillo
Version: 3.0.5
Release: alt4

Summary: a small FLTK-based web browser
Group: Networking/WWW
License: %gpl2plus
Url: http://www.dillo.org

Packager: Nikolay A. Fetisov <naf@altlinux.org>

# Patch for i18n:  http://teki.jpn.ph/pc/software/index-e.shtml
Source0: %name-%version.tar
Source1: %name-16.png
Source2: %name-32.png
Source3: %name-48.png
Source4: %name.desktop

Patch1:  %name-3.0.5-debian-fix-OpenSSL-1.1-detection.patch
Patch2:  %name-3.0.5-alt-ca_location_fix.patch
Patch3:  %name-3.0.5-alt-fix_GCC.patch

BuildRequires(pre): rpm-build-licenses


# Automatically added by buildreq on Sun Aug 19 2018
# optimized out: fontconfig glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libX11-devel libcom_err-devel libkrb5-devel libstdc++-devel python-base python-modules python3 python3-base python3-dev ruby sh3 xorg-proto-devel zlib-devel
BuildRequires: gcc-c++ libfltk-devel libjpeg-devel libpng-devel libssl-devel
BuildRequires: libXrender-devel libXcursor-devel libXfixes-devel libXext-devel
BuildRequires: perl-libnet libXinerama-devel libXft-devel fontconfig-devel

%description
Dillo 3 is a graphical multi-platform web browser known for its
speed and small footprint. It is based on FLTK 1.3,
the Fast and Light Toolkit (FLTK).

Dillo aims to be small in resources, stable, developer-friendly,
usable, very fast, and extensible.

%prep
%setup -q

%patch1 -p1
%patch2
%patch3

%build
%autoreconf
%configure  --enable-ipv6 \
            --enable-ssl \
            %nil

%make_build

%install
%makeinstall

mkdir -p -- %buildroot%_sysconfdir/%name
mv -- %buildroot%_sysconfdir/*rc %buildroot/%_sysconfdir/%name/

mkdir -p -- %buildroot%_miconsdir %buildroot%_liconsdir %buildroot%_niconsdir
install -m0644 -- %SOURCE1 %buildroot%_miconsdir/%name.png
install -m0644 -- %SOURCE2 %buildroot%_niconsdir/%name.png
install -m0644 -- %SOURCE3 %buildroot%_liconsdir/%name.png

mkdir -p -- %buildroot%_desktopdir
install -m 0644 -- %SOURCE4 %buildroot%_desktopdir/%name.desktop

rm -f -- doc/Makefile*

%find_lang %name

%files -f %name.lang
%_bindir/dillo
%_bindir/dillo-install-hyphenation
%_bindir/dpid
%_bindir/dpidc
%_libdir/dillo*

%doc AUTHORS ChangeLog COPYING INSTALL NEWS README doc/
%doc %_defaultdocdir/%name/user_help.html

%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/domainrc
%config(noreplace) %_sysconfdir/%name/keysrc
%config(noreplace) %_sysconfdir/%name/dpidrc
%config(noreplace) %_sysconfdir/%name/dillorc

%_miconsdir/%{name}*
%_niconsdir/%{name}*
%_liconsdir/%{name}*
%_desktopdir/%name.desktop
%_man1dir/dillo.1*

%changelog
* Tue Mar 16 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.0.5-alt4
- Fix build with GCC 10.2

* Wed Feb 13 2019 Grigory Ustinov <grenka@altlinux.org> 3.0.5-alt3
- Rebuild with libfltk1.3.5rc1.

* Thu Sep 06 2018 Nikolay A. Fetisov <naf@altlinux.org> 3.0.5-alt2
- Rebuild with openssl 1.1.0i

* Sun Aug 19 2018 Nikolay A. Fetisov <naf@altlinux.org> 3.0.5-alt1
- New version
- Fix configuration error (Closes: 33289)

* Thu Apr 28 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.0.4.1-alt1.qa1
- Fixed build with libfltk13-1.3.3-alt1.

* Thu Jan 29 2015 Andrey Cherepanov <cas@altlinux.org> 3.0.4.1-alt1
- New version

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt7.1
- Rebuilt with libpng15

* Sat May 26 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt7
- Fix build with --no-copy-dt-needed-entries

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.8.6-alt6.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sun Jul 05 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt6
- Security fix (CVE-2009-2294) (Closes: 20680)

* Sat Nov 15 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt5
- Fix build with automake_1.9
- Remove obsolete update_menus/clean_menus calls

* Sun Jul 20 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt4
- Fix repocop issues on icon's dirs and desktop file

* Mon Feb 25 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt3
- Updating Dillo i18n patch to v. 20070916

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt2
- Fix typos in package description.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.6-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Jul 19 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.8.6-alt1
- Revives from orphaned
- New version 0.8.6
- Build with i18n-misc patch
- Localization for dillorc
- Adding desktop file and icon

* Wed Aug 27 2003 Alexey Tourbin <at@altlinux.ru> 0.7.3-alt1
- 0.7.3
- old toolbar icons kept, I don't like new ones
- new icons for menufile(5) from http://www.dillo.org/Icons/
- dillorc: changed default geometry 640x550 -> 720x600

* Tue Jul 08 2003 Alexey Tourbin <at@altlinux.ru> 0.7.2-alt2
- most of the CVS changes applied (0.7.3 to be)
- pld-gzip_fallback.patch updated
- optimization: -Os (the binary claims to be as small as 265Kb)

* Mon May 12 2003 Alexey Tourbin <at@altlinux.ru> 0.7.2-alt1
- 0.7.2
- patches updated; pld-gzip_fallback.patch disabled
- fixed libpng3 build

* Mon Feb 24 2003 Alexey Tourbin <at@altlinux.ru> 0.7.0-alt2
- menu entry added; large png icon added (PLD)
- double-free/endless loop in pld-gzip_fallback.patch fixed

* Mon Feb 20 2003 Alexey Tourbin <at@altlinux.ru> 0.7.0-alt1
- initial revision, various patches integrated
