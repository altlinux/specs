%define fname ubuntu-font-family

Name: fonts-ttf-%fname
Version: 0.71.2
Release: alt1

Summary: Ubuntu Font Family, sans-serif typeface hinted for clarity

License: Ubuntu Font Licence 1.0
Group: System/Fonts/True type
Url: http://font.ubuntu.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://archive.ubuntu.com/ubuntu/pool/main/u/ubuntu-font-family-sources/ubuntu-font-family-sources_%version.orig.tar.gz
Source: %fname-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-fonts

%description
The Ubuntu Font Family are a set of matching new libre/open
fonts in development during 2010--2011. The development is being funded
by Canonical Ltd on behalf the wider Free Software community and the
Ubuntu project. The technical font design work and implementation is
being undertaken by Dalton Maag. 

Both the final font Truetype/OpenType
files and the design files used to produce the font family are
distributed under an open licence and you are expressly encouraged to
experiment, modify, share and improve.

%prep
%setup -n %fname-%version

%install
%ttf_fonts_install %fname

%post
%post_fonts

%postun
%postun_fonts

%files -f %fname.files
%doc *.txt

%changelog
* Fri May 13 2011 Vitaly Lipatov <lav@altlinux.ru> 0.71.2-alt1
- new version 0.71.2 (with rpmrb script)

* Thu Sep 30 2010 Vitaly Lipatov <lav@altlinux.ru> 0.68-alt1
- initial build for ALT Linux Sisyphus
