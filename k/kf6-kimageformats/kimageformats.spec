%define rname kimageformats
%def_enable heif

Name: kf6-%rname
Version: 6.4.0
Release: alt1
%K6init altplace

Group: System/Libraries
Summary: KDE Frameworks 6 plugins to allow QImage to support extra file formats
Url: http://www.kde.org
License: LGPL-2.1-or-later


Source: %rname-%version.tar

BuildRequires(pre): rpm-build-kf6
BuildRequires: extra-cmake-modules openexr-devel qt6-base-devel
BuildRequires: zlib-devel
BuildRequires: libavif-devel
BuildRequires: libraw-devel
%if_enabled heif
BuildRequires: libheif-devel
%endif
%ifnarch %arm
BuildRequires: libjxl-devel
%endif
# JXR disabled by default
#BuildRequires: libjxr-devel
BuildRequires: kf6-karchive-devel

%description
This framework provides additional image format plugins for QtGui.  As
such it is not required for the compilation of any other software, but
may be a runtime requirement for Qt-based software to support certain
image formats.

%package common
Summary: %name common package
Group: System/Configuration/Other
BuildArch: noarch
Requires: kde-common
%description common
%name common package


%prep
%setup -n %rname-%version

%build
%K6build \
%if_enabled heif
    -DKIMAGEFORMATS_HEIF=ON \
%endif
    -DBUILD_TESTING=ON \
    #

%install
%K6install
%find_lang %name --all-name
%K6find_qtlang %name --all-name

%files
%doc LICENSES/* README.md
%_K6plug/imageformats/kimg_*.so
#%_K6srv/qimageioplugins/

%changelog
* Tue Aug 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.4.0-alt1
- new version

* Tue Jun 11 2024 Sergey V Turchin <zerg@altlinux.org> 6.3.0-alt1
- new version

* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 6.2.0-alt1
- new version

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt1
- bump release

* Mon Apr 15 2024 Sergey V Turchin <zerg@altlinux.org> 6.1.0-alt0
- initial build

