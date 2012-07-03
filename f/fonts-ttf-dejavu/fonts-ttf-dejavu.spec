%define _name dejavu-fonts-ttf
%define fname dejavu

Name: fonts-ttf-%fname
Version: 2.33
Release: alt1

Summary: A font family based on the Bitstream Vera Fonts with a wider set of characters
Summary (ru_RU.UTF-8): Шрифты, основанные на Bitstream Vera, с более широким набором символов 
License: Freely distributable
Group: System/Fonts/True type
Url: http://dejavu.sourceforge.net
Source: http://downloads.sourceforge.net/%fname/%_name-%version.tar.bz2
BuildArch: noarch
Packager: Alexey Rusakov <ktirf@altlinux.ru>

BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

Obsoletes: %fname-fonts-ttf < 2.10
Provides: %fname-fonts-ttf = %version-%release
Provides: fonts-ttf-core

%description
The DejaVu fonts are a font family based on the Bitstream Vera Fonts
release 1.10. Its purpose is to provide a wider range of characters
(see Current status page for more information) while maintaining the
original look and feel.

%description -l ru_RU.UTF-8
DejaVu - это набор шрифтов, основанных на Bitstream Vera release 1.10.
Цель проекта DejaVu - предоставить более широкий набор символов,
сохраняя при этом первоначальный облик шрифта.

%prep
%setup -n %_name-%version

%install
pushd ttf
%ttf_fonts_install %fname
popd
mkdir -p %buildroot%_sysconfdir/fonts/conf.avail
install -m644 -pD fontconfig/{??-unhint-small-dejavu*.conf,??-dejavu*.conf} \
    %buildroot%_sysconfdir/fonts/conf.avail/

%post
%post_fonts

%postun
%postun_fonts

%files -f ttf/%fname.files
%_sysconfdir/fonts/conf.avail/*.conf
%doc AUTHORS BUGS LICENSE NEWS README status.txt unicover.txt

%changelog
* Thu Jul 21 2011 Michael Shigorin <mike@altlinux.org> 2.33-alt1
- 2.33

* Tue Dec 22 2009 Alexey Rusakov <ktirf@altlinux.org> 2.30-alt2
- Provide fonts-ttf-core (Closes: ALT#22588).

* Fri Aug 28 2009 Alexey Rusakov <ktirf@altlinux.org> 2.30-alt1
- New version 2.30 (with rpmrb script).

* Mon Mar 09 2009 Alexey Rusakov <ktirf@altlinux.org> 2.29-alt1
- New version 2.29 (with rpmrb script).

* Mon Dec 22 2008 Alexey Rusakov <ktirf@altlinux.org> 2.28-alt1
- New version (2.28).
- Added Packager tag.
- Updated installation sequence due to updates in fontconfig files.

* Mon Sep 08 2008 Alexey Rusakov <ktirf@altlinux.org> 2.26-alt1
- New version (2.26).
- Fixed the License tag (closing ALT Bug 17052).

* Tue May 20 2008 Alexey Rusakov <ktirf@altlinux.org> 2.25-alt1
- New version (2.25).
- Fixed ALT Bug 15408 (no more forcing DejaVu as sans-serif).

* Tue Mar 11 2008 Alexey Rusakov <ktirf@altlinux.org> 2.24-alt1
- New version 2.24 (with rpmrb script).

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

