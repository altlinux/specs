# SPEC file for CutyCapt
#

%define real_name    CutyCapt

Name:     cutycapt
Version:  0.0
Release:  alt1.svn20111130

Summary: utility to capture WebKit's rendering of a web page

Group:    Networking/WWW
License:  %gpl2only %lgpl21plus
URL:      http://cutycapt.sourceforge.net/
# URL: https://github.com/hoehrmann/CutyCapt
# URL: https://github.com/DannyT/CutyCapt

Packager: Nikolay Fetisov <naf@altlinux.ru>

Source0: %real_name-%version.tar
Patch0:  %real_name-%version-%release.patch

Patch1:  %real_name-svn20111130-debian-01-assume_http_as_default.patch
Patch2:  %real_name-svn20111130-alt-ignore_ssl_errors.patch

Source1: README
Source2: README.alt

AutoReqProv: yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Thu Apr 12 2012
# optimized out: fontconfig libgst-plugins libqt4-core libqt4-devel libqt4-gui libqt4-network libqt4-svg libqt4-webkit libstdc++-devel
BuildRequires: gcc-c++ phonon-devel

%description
CutyCapt is a small cross-platform command-line utility to
capture WebKit's rendering of a web page into a variety of
vector and bitmap formats, including SVG, PDF, PS, PNG,
JPEG, TIFF, GIF, and BMP.

%prep
%setup  -n %real_name-%version
%patch0 -p1

%patch1 -p1
%patch2

install -m 0644 %SOURCE1 .
install -m 0644 %SOURCE2 .

%build
%_qt4dir/bin/qmake PREFIX=%buildroot%prefix
%make

%install
install -d %buildroot%_bindir
install -m 0755 %real_name %buildroot%_bindir/%real_name

%files
%doc README README.alt
%_bindir/%real_name

%changelog
* Thu Apr 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.0-alt1.svn20111130
- Initial build for ALT Linux Sisyphus

