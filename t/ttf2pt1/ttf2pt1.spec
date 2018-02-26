Name: ttf2pt1
Version: 3.4.4
Release: alt1

Group: Publishing
Summary: True Type Font to Postscript Type 1 Converter
License: GPLv2+ and BSD with advertising
URL: http://ttf2pt1.sourceforge.net/
Packager: Michael A. Kangin <prividen@altlinux.org>

BuildRequires: libfreetype-devel t1lib-devel
Requires: t1utils

Source0: %name-%version.tar.gz



%description
Ttf2pt1 is a font converter from the True Type format (and some other formats
supported by the FreeType library as well) to the Adobe Type1 format.

%prep
%setup -q

%build
%make all

%install
sed -i	-e 's|TTF2PT1_SHAREDIR|%_docdir/%name-%version|' %name.1

mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
install %name %buildroot/%_bindir/
install %name.1 %buildroot%_man1dir/



%files
%_bindir/*
%_man1dir/*.1*
%doc CHANGES README FONTS FONTS.hpux 

%changelog
* Mon Aug 17 2009 Michael A. Kangin <prividen@altlinux.org> 3.4.4-alt1
- Initial build for Sisyphus




