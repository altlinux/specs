%define fname latex-xft

Name: fonts-ttf-%fname
Version: 0.1
Release: alt4

Summary: xft-compatible versions of some LaTeX fonts

License: distributable
Group: System/Fonts/True type
Url: http://apt.ling.li/rpms/latex-xft-fonts

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

Source: ftp://ftp.lyx.org/pub/lyx/bin/1.3.2/latex-xft-fonts-%version.tar.gz

Obsoletes: %fname-fonts
Provides: %fname-fonts
Provides: %fname-fonts-ttf
Obsoletes: %fname-fonts-ttf

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
Some xft-compatible versions of LaTeX fonts for use
with visual math symbol display in LyX. You will need
to install this package if your version of Qt is using
Xft for displaying fonts (most recent systems).

%prep
%setup -q -n %fname-fonts-%version

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc README

%changelog
* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt4
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Fri Jan 12 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt3
- rewrote spec with rpm-build-fonts

* Wed Jan 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt2
- cleanup spec according to policy
- build with ttmkfdir
- rename to latex-xft-fonts-ttf
- fix bug #5821

* Fri Jun 18 2004 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- first build for Sisyphus

* Fri Dec 20 2002  John Levon  <levon@movementarian.org>
- Initial version
