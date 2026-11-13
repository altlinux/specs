%define _unpackaged_files_terminate_build 1
%define fontname fontawesome-web

Name: fonts-font-awesome-web
Version: 7.3.1
Release: alt1

Summary: Iconic font set, web files
License: OFL-1.1 and MIT and CC-BY-4.0
Group: System/Fonts/True type
URL: https://fontawesome.com
VCS: https://github.com/FortAwesome/Font-Awesome.git
BuildArch: noarch

Source: %fontname-%version.tar

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node

Provides: fonts-ttf-%fontname = %EVR
Obsoletes: fonts-ttf-%fontname < %EVR
Provides: fonts-web-%fontname = %EVR
Obsoletes: fonts-web-%fontname = %EVR

%description
Font Awesome provides scalable vector icons with CSS, SCSS and web fonts.

%package compat
Summary: Iconic font set, v4/v5 compatible files
Group: System/Fonts/True type
Requires: %name = %EVR

%description compat
Compatibility CSS, SCSS and web fonts for older Font Awesome styles.

%package -n fonts-svg-%fontname
Summary: Iconic font set, SVG files
Group: System/Fonts/True type

%description -n fonts-svg-%fontname
SVG icons, sprites and SVG object definitions from Font Awesome Free.

%package -n javascript-%fontname
Summary: Font Awesome JavaScript and npm modules
Group: Development/Other
Provides: fonts-js-%fontname = %EVR
Obsoletes: fonts-js-%fontname < %EVR

%description -n javascript-%fontname
Font Awesome browser JavaScript and the complete official npm modules,
including SVG core, common types and the free icon definitions.

%prep
%setup -q -n %fontname-%version

%install
install -d %buildroot%_datadir/%name
for d in webfonts js css scss svgs svgs-full sprites sprites-full \
    svg-objects svg-full-objects; do
    cp -a "$d" %buildroot%_datadir/%name/
done
install -d %buildroot%nodejs_sitelib/@fortawesome
cp -a js-packages/@fortawesome/* %buildroot%nodejs_sitelib/@fortawesome/
# The complete license is installed once in the main package.
rm %buildroot%nodejs_sitelib/@fortawesome/*/LICENSE.txt
rm %buildroot%nodejs_sitelib/@fortawesome/*/README.md

%files
%doc LICENSE.txt
%dir %_datadir/%name
%_datadir/%name/css
%_datadir/%name/scss
%_datadir/%name/webfonts
%exclude %_datadir/%name/css/v4-*
%exclude %_datadir/%name/css/v5-*
%exclude %_datadir/%name/scss/v4-*
%exclude %_datadir/%name/webfonts/fa-v4*

%files compat
%_datadir/%name/css/v4-*
%_datadir/%name/css/v5-*
%_datadir/%name/scss/v4-*
%_datadir/%name/webfonts/fa-v4*

%files -n fonts-svg-%fontname
%dir %_datadir/%name
%_datadir/%name/svgs
%_datadir/%name/svgs-full
%_datadir/%name/sprites
%_datadir/%name/sprites-full
%_datadir/%name/svg-objects
%_datadir/%name/svg-full-objects

%files -n javascript-%fontname
%dir %_datadir/%name
%dir %nodejs_sitelib
%_datadir/%name/js
%dir %nodejs_sitelib/@fortawesome
%nodejs_sitelib/@fortawesome/*

%changelog
* Wed Nov 11 2026 Ivan Khanas <xeno@altlinux.org> 7.3.1-alt1
- New version.

* Tue Apr 21 2026 L.A. Kostis <lakostis@altlinux.ru> 6.7.2-alt1
- 6.7.2.

* Thu Aug 08 2024 L.A. Kostis <lakostis@altlinux.ru> 6.6.0-alt1
- 6.6.0.

* Fri Feb 16 2024 L.A. Kostis <lakostis@altlinux.ru> 6.5.1-alt1
- 6.5.1.

* Fri Sep 15 2023 L.A. Kostis <lakostis@altlinux.ru> 6.4.2-alt1
- 6.4.2.

* Sat Jun 03 2023 L.A. Kostis <lakostis@altlinux.ru> 6.4.0-alt1
- initial build for ALTLinux.

