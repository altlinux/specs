# SPEC file for CutyCapt
#

%define real_name    CutyCapt

Name:     cutycapt
Version:  0.0
Release:  alt3

Summary: utility to capture WebKit's rendering of a web page

Group:    Networking/WWW
License:  %gpl2only %lgpl21plus
URL:      http://cutycapt.sourceforge.net/
# URL: https://github.com/hoehrmann/CutyCapt
# URL: https://github.com/DannyT/CutyCapt
# URL: https://github.com/oracle/infinity-cutycapt

Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %real_name-%version.tar
Patch0:  %real_name-%version-%release.patch

Patch1:  %real_name-bea8c782-debian-01-assume_http_as_default.patch
Patch2:  %real_name-bea8c782-alt-ignore_ssl_errors.patch
Patch3:  %real_name-bea8c782-alt-fix_build.patch

Patch4:  %real_name-bea8c782-alt-method.patch
Patch5:  %real_name-bea8c782-alt-image-save-quality.patch

Source1: README
Source2: README.alt

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Jun 20 2021
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 kf5-attica-devel kf5-kauth-devel kf5-kbookmarks-devel kf5-kcodecs-devel kf5-kcompletion-devel kf5-kconfig-devel kf5-kconfigwidgets-devel kf5-kcoreaddons-devel kf5-kitemviews-devel kf5-kjobwidgets-devel kf5-kservice-devel kf5-kwidgetsaddons-devel kf5-kwindowsystem-devel kf5-kxmlgui-devel kf5-solid-devel libglvnd-devel libqt5-core libqt5-gui libqt5-network libqt5-printsupport libqt5-qml libqt5-qmlmodels libqt5-quick libqt5-svg libqt5-webchannel libqt5-webkit libqt5-webkitwidgets libqt5-widgets libstdc++-devel python-modules python2-base python3 python3-base python3-module-paste qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-webchannel-devel ruby ruby-stdlibs sh4
BuildRequires: kf5-kguiaddons-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kio-devel kf5-kwallet-devel qt5-multimedia-devel qt5-phonon-devel qt5-script-devel qt5-svg-devel qt5-tools-devel qt5-webengine-devel qt5-webkit-devel qt5-websockets-devel qt5-x11extras-devel

%description
CutyCapt is a small cross-platform command-line utility to
capture WebKit's rendering of a web page into a variety of
vector and bitmap formats, including SVG, PDF, PS, PNG,
JPEG, TIFF, GIF, and BMP.

%prep
%setup  -n %real_name-%version
%patch0 -p1

%patch1
%patch2
%patch3

%patch4
%patch5

install -m 0644 %SOURCE1 .
install -m 0644 %SOURCE2 .

%build
qmake-qt5 PREFIX=%buildroot%prefix
%make

%install
install -d %buildroot%_bindir
install -m 0755 %real_name %buildroot%_bindir/%real_name

%files
%doc README README.alt
%_bindir/%real_name

%changelog
* Sun Jun 20 2021 Nikolay A. Fetisov <naf@altlinux.org> 0.0-alt3
- Rebuild with QT5
- Add support for Cookies

* Sat Dec 05 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.0-alt2
- Fix build with QT5

* Thu Apr 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.0-alt1.svn20111130
- Initial build for ALT Linux Sisyphus

