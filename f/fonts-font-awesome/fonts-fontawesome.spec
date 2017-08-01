%define _fontsdir %_datadir/fonts

%define oldname fontawesome-fonts
%global fontname fontawesome
%global fontconf 60-%fontname.conf

Name: fonts-font-awesome
Version: 4.7.0
Release: alt1
Summary: Iconic font set, web files
Group: System/Fonts/True type
License: OFL and MIT
URL: http://fontawesome.io

Provides: fonts-ttf-fontawesome-web = %version-%release
Obsoletes: fonts-ttf-fontawesome-web < %version-%release

Source0: http://fontawesome.io/assets/font-awesome-%version.zip
Source1: %oldname-fontconfig.conf
Source2: README-Trademarks.txt

BuildArch: noarch
BuildRequires: mkfontscale unzip

%description
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format versions 1 and 2, Embedded OpenType and SVG font files which are
typically used on the web.

%package -n fonts-otf-fontawesome
Summary: Iconic font set
Group: System/Fonts/True type
License: OFL

Provides: fonts-ttf-fontawesome = %version-%release
Obsoletes: fonts-ttf-fontawesome < %version-%release

%description -n fonts-otf-fontawesome
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains OpenType and TrueType font files which are typically used
locally.

%prep
%setup -q -n font-awesome-%version
cp -p %SOURCE2 .

%install
mkdir -p %buildroot%_datadir/%name/{fonts,css,less,scss}
install -m0644 css/* %buildroot%_datadir/%name/css/
install -m0644 scss/* %buildroot%_datadir/%name/scss/
install -m0644 less/* %buildroot%_datadir/%name/less/
install -m0644 fonts/* %buildroot%_datadir/%name/fonts/

mkdir -p %buildroot%_fontsdir/otf/fontawesome
mv %buildroot%_datadir/%name/fonts/*.otf %buildroot%_fontsdir/otf/fontawesome/
mkfontscale %buildroot%_fontsdir/otf/fontawesome/
ln -s fonts.scale %buildroot%_fontsdir/otf/fontawesome/fonts.dir

mkdir -p %buildroot%_sysconfdir/X11/fontpath.d
ln -s %_fontsdir/otf/fontawesome %buildroot%_sysconfdir/X11/fontpath.d/otf-fontawesome:pri=50

mkdir -p %buildroot%_sysconfdir/fonts/conf.d
install -pD -m 0644 %SOURCE1 %buildroot%_datadir/fontconfig/conf.avail/%fontconf
ln -s %_datadir/fontconfig/conf.avail/%fontconf %buildroot%_sysconfdir/fonts/conf.d/%fontconf

%files
%doc README-Trademarks.txt
%_datadir/%name

%files -n fonts-otf-fontawesome
%_sysconfdir/X11/fontpath.d/otf-fontawesome:pri=50
%config(noreplace) %_sysconfdir/fonts/conf.d/%fontconf
%_datadir/fontconfig/conf.avail/%fontconf
%_fontsdir/otf/fontawesome

%changelog
* Tue Aug 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.7.0-alt1
- 4.7.0
