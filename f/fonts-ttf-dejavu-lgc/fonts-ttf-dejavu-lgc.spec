%define _name dejavu-lgc-fonts-ttf
%define fname dejavu-lgc

Name: fonts-ttf-%fname
Version: 2.33
Release: alt1

Summary: A font family based on the Bitstream Vera Fonts (Latin, Greek, Cyrillic)
License: %gpl2plus
Group: System/Fonts/True type

Url: http://dejavu.sourceforge.net
Source0: http://downloads.sourceforge.net/dejavu/%_name-%version.tar.bz2
Source1: 59-dejavu-lgc-minimal.conf
Source2: 20-unhint-small-dejavu-lgc-minimal.conf
Source3: dejavu-lgc-minimal-README.ALT
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

Summary(ru_RU.UTF-8): Шрифты, основанные на Bitstream Vera (латиница, кириллица и греческий)

%description
The DejaVu fonts are a font family based on the Bitstream Vera Fonts
release 1.10. Its purpose is to provide a wider range of characters
(see Current status page for more information) while maintaining the
original look and feel.

This package contains only Latin, Greek, Cyrillic glyphs subset.
If you need full range of glyphs, install fonts-ttf-dejavu.

%description -l ru_RU.UTF-8
DejaVu - это набор шрифтов, основанных на Bitstream Vera release 1.10.
Цель проекта DejaVu - предоставить более широкий набор символов,
сохраняя при этом первоначальный облик шрифта.

Этот пакет содержит только латинские, греческие и кириллические глифы.
Если требуется полный диапазон, установите fonts-ttf-dejavu.

%package minimal
Summary: Minimal set of Dejavu LGC fonts
Group: System/Fonts/True type
# there's no file conflict but duplication if both are installed
Conflicts: %name

%description minimal
%summary for use in ALT Linux installer

%prep
%setup -n %_name-%version

%install
pushd ttf
%ttf_fonts_install %fname
popd
mkdir -p %buildroot%_sysconfdir/fonts/conf.avail
# wonder if I broke things by using all upstream configs now...
install -pm644 fontconfig/*.conf %buildroot%_sysconfdir/fonts/conf.avail/
# minimal subpackage
mkdir ttf-minimal
cp -al ttf/DejaVuLGCSans{,Mono}{,-Bold,-Oblique,-BoldOblique}.ttf ttf-minimal/
pushd ttf-minimal
%ttf_fonts_install %fname-minimal
popd
install -pm644 %SOURCE1 %SOURCE2 %buildroot%_sysconfdir/fonts/conf.avail/
install -pm644 %SOURCE3 README.ALT

%post
%post_fonts

%postun
%postun_fonts

%post minimal
%post_fonts

%postun minimal
%postun_fonts

%files -f ttf/%fname.files
%_sysconfdir/fonts/conf.avail/*.conf
%exclude %_sysconfdir/fonts/conf.avail/??-%fname-minimal.conf
%exclude %_sysconfdir/fonts/conf.avail/??-unhint-small-%fname-minimal.conf
%doc AUTHORS BUGS LICENSE NEWS README langcover-lgc.txt unicover-lgc.txt

%files minimal -f ttf-minimal/%fname-minimal.files
%_sysconfdir/fonts/conf.avail/??-%fname-minimal.conf
%_sysconfdir/fonts/conf.avail/??-unhint-small-%fname-minimal.conf
%doc LICENSE README.ALT

%changelog
* Thu Jul 21 2011 Michael Shigorin <mike@altlinux.org> 2.33-alt1
- 2.33
- clarified description (thanks sem@)

* Fri Jan 21 2011 Michael Shigorin <mike@altlinux.org> 2.32-alt1
- 2.32 (thanks force@)

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 2.30-alt1
- 2.30
- packaged all upstream fontconfig snippets

* Mon Sep 08 2008 Michael Shigorin <mike@altlinux.org> 2.26-alt1
- built for ALT Linux
- based on fonts-ttf-dejavu-2.25-alt1
- updated to 2.26
- fixed License: (see also #17052)
- introduced minimal subpackage with basic Sans and Mono variations

* Tue May 20 2008 Alexey Rusakov <ktirf@altlinux.org> 2.25-alt1
- New version (2.25).
- Fixed ALT Bug 15408 (no more forcing DejaVu as sans-serif).

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24-alt1
- new version 2.24 (with rpmrb script)

* Sat Feb 02 2008 Alexey Rusakov <ktirf@altlinux.org> 2.23-alt2
- Fixed fontconfig files location (conf.avail instead of conf.d; only
  symlinks in conf.d).
- Use rpm-build-licenses.

* Sun Jan 20 2008 Alexey Rusakov <ktirf@altlinux.org> 2.23-alt1
- New version 2.23.
- Changed the tarball name and installation procedure according to upstream changes.

* Tue Oct 30 2007 Alexey Rusakov <ktirf@altlinux.org> 2.21-alt1
- new version 2.21 (with rpmrb script)

* Mon Sep 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.20-alt1
- new version (2.20)

* Fri Sep 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.19-alt2
- updated according to the new fonts policy

* Tue Aug 07 2007 Alexey Rusakov <ktirf@altlinux.org> 2.19-alt1
- new version 2.19 (with rpmrb script)
- updated the download link on SourceForge to be mirror-agnostic.

* Sun Jul 01 2007 Alexey Rusakov <ktirf@altlinux.org> 2.18-alt1
- new version 2.18 (with rpmrb script)

* Mon May 14 2007 Alexey Rusakov <ktirf@altlinux.org> 2.17-alt1
- new version 2.17 (with rpmrb script)

* Tue Apr 03 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16-alt1
- new version 2.16 (with rpmrb script)

* Mon Feb 19 2007 Alexey Rusakov <ktirf@altlinux.org> 2.15-alt1
- new version 2.15 (with rpmrb script)

* Wed Jan 17 2007 Alexey Rusakov <ktirf@altlinux.org> 2.14-alt1
- new version (2.14)
- using macros from rpm-build-fonts. The specfile somehow squeezed.

* Tue Dec 19 2006 Alexey Rusakov <ktirf@altlinux.org> 2.13-alt1
- new version 2.13 (with rpmrb script)

* Sun Oct 22 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.11-alt1
- new version 2.11 (with rpmrb script)

* Mon Sep 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.10-alt1
- new version 2.10 (with rpmrb script)

* Sun Jul 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.8-alt1
- new version 2.8 (with rpmrb script)

* Sun Jun 18 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.7-alt1
- new version 2.7 (with rpmrb script)

* Tue May 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6-alt1
- new version 2.6 (with rpmrb script)

* Mon May 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.5-alt1
- new version 2.5 (with rpmrb script)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.5.0-alt1
- new version 2.5.0 (with rpmrb script)

* Tue Mar 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.4-alt1
- new version

* Tue Feb 21 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.3-alt1
- new version

* Mon Jan 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.2-alt1
- new version

* Sat Nov 26 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0-alt2
- changes according to the draft of a font packages policy:
- - moved the fonts from .../fonts/default/TrueType-dejavu to .../fonts/ttf/dejavu.
- - renamed the package to fonts-ttf-dejavu.

* Sat Nov 12 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.0-alt1
- new version

* Mon Oct 17 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.15-alt1
- new version

* Sun Sep 18 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.14-alt1
- New upstream version.

* Mon Aug 22 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.13-alt2
- A quickfix for Mono fonts that were broken in original 1.13.

* Mon Aug 15 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.13-alt1
- New upstream version.

* Wed Aug 03 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.12-alt1
- New upstream version.

* Mon Jun 20 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.11-alt1
- New upstream version.

* Tue May 24 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.10-alt1
- New upstream version.

* Mon Apr 18 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.9-alt1
- New upstream version.

* Fri Apr 01 2005 Alexey Rusakov <ktirf@altlinux.ru> 1.8-alt1
- Initial Sisyphus package.

