%define _fontsdir %_datadir/fonts

%define oldname fontawesome-fonts
%global fontname fontawesome
%global fontconf 60-%fontname.conf

Name: fonts-font-awesome
Version: 4.7.0
Release: alt3
Summary: Iconic font set, web files
Group: System/Fonts/True type
License: OFL-1.1 and MIT
URL: http://fontawesome.io

Source0: http://fontawesome.io/assets/font-awesome-%version.zip
Source1: %oldname-fontconfig.conf
Source2: README-Trademarks.txt

BuildArch: noarch
BuildRequires: unzip

Provides: fonts-ttf-fontawesome-web = %version-%release
Obsoletes: fonts-ttf-fontawesome-web < %version-%release

%description
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as True Type,
Web Open Font Format versions 1 and 2, Embedded OpenType and SVG font files
which are typically used on the web.

%package -n fonts-otf-fontawesome
Summary: Iconic font set
Group: System/Fonts/True type
License: OFL-1.1

%description -n fonts-otf-fontawesome
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains OpenType font files which are typically used locally.

%prep
%setup -q -n font-awesome-%version
cp -p %SOURCE2 .

%install
mkdir -p %buildroot%_datadir/%name/{fonts,css,less,scss}
install -m0644 css/* %buildroot%_datadir/%name/css/
install -m0644 scss/* %buildroot%_datadir/%name/scss/
install -m0644 less/* %buildroot%_datadir/%name/less/
install -m0644 fonts/* %buildroot%_datadir/%name/fonts/

mkdir -p %buildroot%_fontsdir/otf/%fontname
mv %buildroot%_datadir/%name/fonts/*.otf %buildroot%_fontsdir/otf/%fontname/

mkdir -p %buildroot%_fontsdir/ttf/%fontname
mv %buildroot%_datadir/%name/fonts/*.ttf %buildroot%_fontsdir/ttf/%fontname/

# Save symlinks to fonts in original directory (expected by Proxmox sources)
ln -s %_fontsdir/otf/%fontname/FontAwesome.otf %buildroot%_datadir/%name/fonts/FontAwesome.otf
ln -s %_fontsdir/ttf/%fontname/fontawesome-webfont.ttf %buildroot%_datadir/%name/fonts/fontawesome-webfont.ttf

mkdir -p %buildroot%_sysconfdir/fonts/conf.d
install -pD -m 0644 %SOURCE1 %buildroot%_datadir/fontconfig/conf.avail/%fontconf
ln -s %_datadir/fontconfig/conf.avail/%fontconf %buildroot%_sysconfdir/fonts/conf.d/%fontconf

%files
%doc README-Trademarks.txt
%_datadir/%name
%_fontsdir/ttf/%fontname
%_datadir/%name/fonts/*.ttf
# We don't need empty symlinks here
%exclude %_datadir/%name/fonts/*.otf

%files -n fonts-otf-fontawesome
%config(noreplace) %_sysconfdir/fonts/conf.d/%fontconf
%_datadir/fontconfig/conf.avail/%fontconf
%_fontsdir/otf/%fontname
# Put symlinks in package with otfs
%_datadir/%name/fonts/*.otf


%changelog
* Mon Feb 24 2025 Sergey Konev <darisishe@altlinux.org> 4.7.0-alt3
- More Policy-Friendly packaging approach

* Sat Feb 08 2025 Sergey Konev <darisishe@altlinux.org> 4.7.0-alt2
- Added Proxmox-compatible symlink to fonts

* Tue Aug 01 2017 Valery Inozemtsev <shrek@altlinux.ru> 4.7.0-alt1
- 4.7.0
