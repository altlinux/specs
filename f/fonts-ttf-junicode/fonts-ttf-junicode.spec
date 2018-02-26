%define fname junicode

Name: fonts-ttf-%fname
Version: 0.6.15
Release: alt2

Summary: TrueType Unicode font for medievalists

License: GPL
Group: System/Fonts/True type
Url: http://junicode.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%fname/%fname-%version.tar.bz2

BuildArch: noarch

BuildRequires: unzip rpm-build-fonts >= 0.3
PreReq: fontconfig >= 2.4.2

%description
A font family especially for medieval scholars, but containing an
extensive enough selection of Unicode characters to be widely useful.

%prep
%setup -q -c %name

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc Junicode.pdf License.pdf aelfric_job.pdf

%changelog
* Wed Sep 05 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.15-alt2
- rebuild with new rpm-build-fonts 0.3
- add require fontconfig 2.4.2

* Sat Jul 28 2007 Vitaly Lipatov <lav@altlinux.ru> 0.6.15-alt1
- initial build for ALT Linux Sisyphus
