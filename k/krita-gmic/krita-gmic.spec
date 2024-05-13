%ifarch %e2k
# it's impossible to use such a bad OpenMP implementation for such complex code
%def_disable openmp
%else
%def_enable openmp
%endif

Name: krita-gmic
Version: 3.2.4.1
Release: alt1

Group: Graphics
Summary: GREYC's Magic Image Converter for Krita
License: CECILL-2.0 and GPL-3.0
Url: https://files.kde.org/krita/build/dependencies/

Requires: gmic

Source: gmic-patched-%version.tar

BuildRequires: libGraphicsMagick-c++-devel libImageMagick-devel libXext-devel libXrandr-devel
BuildRequires: libavformat-devel libfftw3-devel libjpeg-devel libopencv-devel libpng-devel
BuildRequires: libswscale-devel libtiff-devel openexr-devel xorg-cf-files zlib-devel
%{?_enable_openmp:BuildRequires: libgomp-devel}
BuildRequires: libcurl-devel
BuildRequires(pre): rpm-macros-qt5
BuildRequires: rpm-build-kf5
BuildRequires: qt5-base-devel qt5-tools-devel
BuildRequires: extra-cmake-modules kf5-kcoreaddons-devel krita-devel

%description
G'MIC (GREYC's Magic Image Converter) is an interpreter of image processing
macros whose goal is to convert, manipulate and visualize generic 1D/2D/3D
multi-spectral image datasets.

%prep
%setup -n gmic-patched-%version

%build
pushd gmic-qt
%K5build \
    -DGMIC_QT_HOST=krita-plugin \
    -DENABLE_SYSTEM_GMIC=FALSE \
    #
popd

%install
pushd gmic-qt
%K5install
popd
%find_lang --with-man %name

%files -f %name.lang
%_K5lib/kritaplugins/krita_gmic_qt.so
%doc gmic-qt/README*

%changelog
* Mon May 13 2024 Sergey V Turchin <zerg@altlinux.org> 3.2.4.1-alt1
- initial build
