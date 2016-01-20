%define rname poxml

Name: kde5-%rname
Version: 15.12.1
Release: alt1
%K5init

Group: Graphical desktop/KDE
Summary: Conversions between PO and XML
Url: http://www.kde.org
License: GPLv2+ / LGPLv2+

Source: %rname-%version.tar

# Automatically added by buildreq on Thu Jan 14 2016 (-bi)
# optimized out: cmake cmake-modules docbook-dtds docbook-style-xsl elfutils gcc-c++ kf5-kdoctools-devel libgpg-error libqt5-core libqt5-xml libstdc++-devel python-base python3 python3-base xml-common xml-utils xz
#BuildRequires: extra-cmake-modules kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static qt5-base-devel rpm-build-python3 ruby ruby-stdlibs
BuildRequires(pre): rpm-build-kf5
BuildRequires: extra-cmake-modules qt5-base-devel
BuildRequires: kf5-kdelibs4support kf5-kdoctools kf5-kdoctools-devel-static

%description
%summary.

%prep
%setup -n %rname-%version

%build
%K5build

%install
%K5install
%find_lang %name --with-kde --all-name

%files -f %name.lang
%doc COPYING*
%_K5bin/*

%changelog
* Wed Jan 20 2016 Sergey V Turchin <zerg@altlinux.org> 15.12.1-alt1
- new version

* Wed Sep 30 2015 Sergey V Turchin <zerg@altlinux.org> 15.12.0-alt1
- initial build
