%define fname DSEG

%define desc_common \
DSEG is a free font which imitate LCD Display (7SEG, 14SEG, Weather icons etc.).\
DSEG have special features:\
\
* Includes the roman-alphabet and symbol glyphs.\
* Many types(over 50) are available.\
* Licensed under SIL OPEN FONT LICENSE Version 1.1.\
  You can use DSEG for non-commercial and commercial purposes.

Name: fonts-ttf-%fname
Version: 0.46
Release: alt1

Summary: 7-segment and 14-segment LCD font

License: OFL-1.1
Group: System/Fonts/True type
URL: https://www.keshikan.net/fonts-e.html
VCS: https://github.com/keshikan/DSEG

Packager: Alexander Kovalev <alexvk@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-fonts

BuildRequires: fontforge woff2

%description
%desc_common

%package -n fonts-web-%fname
Summary: 7-segment and 14-segment LCD web font
Group: System/Fonts/True type
%description -n fonts-web-%fname
%desc_common

This package contains the DSEG web fonts.

%prep
%setup

%build
%make

%install
rm -v sample/*.psd
chmod -x ./*.{md,txt} sample/*
pushd fonts
for dir in *; do
    for ftype in ttf woff woff2; do
	mkdir -p %buildroot%_fontsdir/$ftype/$dir
	cp -a $dir/*.$ftype %buildroot%_fontsdir/$ftype/$dir
    done
done
popd

%files
%doc README.md DSEG-LICENSE.txt sample
%_fontsdir/ttf/%{fname}*

%files -n fonts-web-%fname
%doc README.md DSEG-LICENSE.txt sample
%_fontsdir/woff*/%{fname}*

%changelog
* Mon Sep 08 2025 Alexander Kovalev <alexvk@altlinux.org> 0.46-alt1
- Initial build for ALT.
