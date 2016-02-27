Name: phantomjs
Version: 2.0.0
Release: alt2

Summary: headless WebKit with JavaScript API
License: BSD
Group: Networking/WWW
Url: http://phantomjs.org

# git://github.com/ariya/phantomjs.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: /proc
BuildRequires: gcc-c++ libharfbuzz-devel gperf ruby ruby-tools flex perl-Term-ANSIColor fontconfig-devel libssl-devel libjpeg-devel libpng-devel zlib-devel chrpath libsqlite3-devel libicu-devel libX11-devel libpcre-devel python-module-simplejson python-modules-xml

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
MAKEFLAGS='' ./build.sh --confirm --qtdeps=system --qt-config -I/usr/include/pcre

%install
mkdir -p %buildroot%_bindir
cp bin/%name %buildroot%_bindir/%name
chrpath -d %buildroot%_bindir/%name

%files
%_bindir/%name
%doc ChangeLog LICENSE.BSD examples

%changelog
* Sat Feb 27 2016 Vladimir Lettiev <crux@altlinux.ru> 2.0.0-alt2
- Rebuild with libicu56

* Mon Nov 02 2015 Vladimir Lettiev <crux@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Nov 07 2012 Vladimir Lettiev <crux@altlinux.ru> 1.7.0-alt1
- 1.7.0
- Statical build with bundled Qt

* Tue Jun 26 2012 Vladimir Lettiev <crux@altlinux.ru> 1.6.0-alt1
- 1.6.0

* Fri Mar 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt2
- build with system libjpeg, libpng, zlib

* Fri Mar 23 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- initial build for Sisyphus

