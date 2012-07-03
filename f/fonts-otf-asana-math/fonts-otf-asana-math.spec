%define PName Asana-Math
Name:		fonts-otf-asana-math
Version:	000.926
Release:	alt1
License:	OFL
Group:		System/Fonts/True type
Summary:	OpenType MATH-enabled Asana font
URL:		http://www.ctan.org/tex-archive/fonts/Asana-Math/
Source:		ftp://indian.cse.msu.edu/pub/mirrors/CTAN/fonts/%PName.zip
BuildArch:	noarch

# Automatically added by buildreq on Thu Jun 03 2010
BuildRequires: unzip

%description
The Asana-Math OpenType font includes almost all mathematical symbols
included in the latest version of Unicode. In addition, it includes
a MATH OpenType table so as to be useful for the typesetting of
mathematical text. It has beeb tested with XeTeX 0.997 and the
output is comparable to the output produced with Cambria-Math.
The font is not finished yet, but it is released as beta software
in the hope that people will use it, diccover bugs and report
them back to me. Last but certainly least, I used the pxfonts as
a basis for the design of most glyphs.

%package -n fonts-ttf-asana-math
Summary:	TrueType ATH-enabled Asana font
Group:		System/Fonts/True type

%description -n fonts-ttf-asana-math
The Asana-Math OpenType font includes almost all mathematical symbols
included in the latest version of Unicode. In addition, it includes
a MATH OpenType table so as to be useful for the typesetting of
mathematical text. It has beeb tested with XeTeX 0.997 and the
output is comparable to the output produced with Cambria-Math.
The font is not finished yet, but it is released as beta software
in the hope that people will use it, diccover bugs and report
them back to me. Last but certainly least, I used the pxfonts as
a basis for the design of most glyphs.

%prep
%setup -n %PName

%build

%install
install -D %PName.otf %buildroot%_datadir/fonts/otf/%PName/%PName.otf
install -D %PName.otf %buildroot%_datadir/fonts/ttf/%PName/%PName.ttf
( cd %buildroot%_datadir/fonts/%PName
mkfontscale 
mkfontdir )

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s ../../..%_datadir/fonts/otf/%PName %buildroot%_sysconfdir/X11/fontpath.d/otf-%PName:pri=50
ln -s ../../..%_datadir/fonts/ttf/%PName %buildroot%_sysconfdir/X11/fontpath.d/ttf-%PName:pri=50

%post
%_bindir/fc-cache %_datadir/fonts/otf/%PName ||:
%_bindir/fc-cache %_datadir/fonts/ftf/%PName ||:

%files
%doc README
%_sysconfdir/X11/fontpath.d/otf-%PName:pri=50
%_datadir/fonts/otf/%PName

%files -n fonts-ttf-asana-math
%doc README.1ST
%_sysconfdir/X11/fontpath.d/ttf-%PName:pri=50
%_datadir/fonts/ttf/%PName

%changelog
* Fri Jun 04 2010 Fr. Br. George <george@altlinux.ru> 000.926-alt1
- Initial build from scratch

