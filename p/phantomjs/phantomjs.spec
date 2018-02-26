Name: phantomjs
Version: 1.6.0
Release: alt1

Summary: headless WebKit with JavaScript API
License: BSD
Group: Networking/WWW
Url: http://code.google.com/p/phantomjs/

# git://github.com/ariya/phantomjs.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ fontconfig-devel libssl-devel libjpeg-devel libpng-devel zlib-devel chrpath

%description
PhantomJS is a headless WebKit with JavaScript API.
It has fast and native support for DOM handling, CSS selector, JSON,
Canvas, and SVG.
PhantomJS is cross-platform, it can be compiled for Linux, Windows,
FreeBSD, and Mac OS X.

%prep
%setup -q
%patch -p1

%build
MAKEFLAGS=-j1 ./build.sh

%install
mkdir -p %buildroot{%_libdir/%name,%_bindir}
for lib in Core Gui Network WebKit; do
    cp -a src/qt/lib/libQt$lib.so.* %buildroot%_libdir/%name
    chrpath -r %_libdir/%name %buildroot%_libdir/%name/libQt$lib.so.?
done
cp bin/%name %buildroot%_bindir/%name
chrpath -r %_libdir/%name %buildroot%_bindir/%name

%files
%_bindir/%name
%_libdir/%name
%doc ChangeLog LICENSE.BSD examples

%changelog
* Tue Jun 26 2012 Vladimir Lettiev <crux@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Mar 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt2
- build with system libjpeg, libpng, zlib

* Fri Mar 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- initial build for Sisyphus

