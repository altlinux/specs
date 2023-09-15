%define _fontsdir %_datadir/fonts

%global fontname fontawesome-web

Name: fonts-font-awesome-web
Version: 6.4.2
Release: alt1
Summary: Iconic font set, web files
Group: System/Fonts/True type
License: OFL-1.1 and MIT and CC-BY-4.0
URL: https://fontawesome.com

Provides: fonts-ttf-%fontname = %EVR
Obsoletes: fonts-ttf-%fontname < %EVR

Provides: fonts-web-%fontname = %EVR
Obsoletes: fonts-web-%fontname = %EVR

# https://use.fontawesome.com/releases/v%version/fontawesome-free-%version-web.zip
Source0: %fontname-%version.tar

BuildArch: noarch

%description
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format version 2, Embedded OpenType and SVG font files which are
typically used on the web.

%package compat
Summary: Iconic font set, v4/v5 compatible files
Group: System/Fonts/True type
Requires: %name = %EVR

%description compat
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains v4/v5 compatible shims to ease upgrade from previous
versions.

%package -n fonts-svg-%fontname
Summary: Iconic font set, svg files
Group: System/Fonts/True type
Requires: %name = %EVR

%description -n fonts-svg-%fontname
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains CSS, SCSS and LESS style files as well as Web Open Font
Format version 2, Embedded OpenType and SVG font files which are
typically used on the web.

%package -n javascript-%fontname
Summary: Iconic font set, js files
Group: System/Fonts/True type
Requires: fonts-svg-%fontname = %EVR

Provides: fonts-js-%fontname = %EVR
Obsoletes: fonts-js-%fontname < %EVR

%description -n javascript-%fontname
Font Awesome gives you scalable vector icons that can instantly be
customized a.. size, color, drop shadow, and anything that can be done with the
power of CSS.

This package contains JS which can be used together with SVG for people who
prefer to use SVGs to display icons. People who want to use advanced features
like Power Transforms.

%prep
%setup -q -n %fontname-%version

%install
mkdir -p %buildroot%_datadir/%name/{webfonts,js,css,less,scss,sprites}
mkdir -p %buildroot%_datadir/%name/svgs/{brands,regular,solid}
for d in webfonts js css less scss svgs/brands svgs/regular svgs/solid sprites; do
install -m0644 $d/* %buildroot%_datadir/%name/$d/
done

%files
%doc LICENSE.txt
%_datadir/%name
%exclude %_datadir/%name/css/v4-*
%exclude %_datadir/%name/css/v5-*
%exclude %_datadir/%name/less/v4-*
%exclude %_datadir/%name/scss/v4-*
%exclude %_datadir/%name/webfonts/fa-v4*
%exclude %_datadir/%name/js
%exclude %_datadir/%name/svgs
%exclude %_datadir/%name/sprites

%files compat
%_datadir/%name/css/v4-*
%_datadir/%name/css/v5-*
%_datadir/%name/less/v4-*
%_datadir/%name/scss/v4-*
%_datadir/%name/webfonts/fa-v4*

%files -n fonts-svg-%fontname
%_datadir/%name/svgs
%_datadir/%name/sprites

%files -n javascript-%fontname
%_datadir/%name/js

%changelog
* Fri Sep 15 2023 L.A. Kostis <lakostis@altlinux.ru> 6.4.2-alt1
- 6.4.2.

* Sat Jun 03 2023 L.A. Kostis <lakostis@altlinux.ru> 6.4.0-alt1
- initial build for ALTLinux.

