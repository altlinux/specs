%define gitversion c097d85

Name: rstudio
Version: 0.98.501
Release: alt2
Summary: RStudio IDE is a powerful and productive user interface for R
Group: Sciences/Mathematics
License: GPLv3
Url: http://www.rstudio.com/
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-v%version.tgz
Source1: https://s3.amazonaws.com/rstudio-buildtools/core-dictionaries.zip
Source2: https://s3.amazonaws.com/rstudio-buildtools/mathjax-20.zip
Source3: https://s3.amazonaws.com/rstudio-buildtools/gin-1.5.zip

BuildRequires: unzip
BuildRequires: cmake
BuildRequires: gcc5 gcc5-c++
BuildRequires: boost-program_options-devel boost-devel boost-devel-static boost-log-devel
BuildRequires: boost-interprocess-devel boost-asio-devel boost-devel-headers
BuildRequires: libicu-devel
BuildRequires: java-devel
BuildRequires: libpam0-devel
BuildRequires: libqt4-devel
BuildRequires: R-base
BuildRequires: R-devel
BuildRequires: ant
BuildRequires: pkgconfig(QtWebKit)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(uuid)
BuildRequires: gwt
Requires: R-base
Requires: rstudio-common

%description
RStudio is a free and open source integrated development environment for R.

%package server
Summary: RStudio IDE - server part
Group: Sciences/Mathematics
License: GPLv3
Url: http://www.rstudio.com/
Requires: R-base
Requires: rstudio-common

%description server
RStudio is a free and open source integrated development environment for R.

%package common
Summary: RStudio IDE - common files
Group: Sciences/Mathematics
License: GPLv3
Url: http://www.rstudio.com/
BuildArch: noarch
Requires: R-base

%description common
RStudio is a free and open source integrated development environment for R.

%prep
#%%setup -n rstudio-rstudio-%%gitversion
%setup -n rstudio-v%version
mkdir -p dependencies/common/dictionaries
unzip -qd dependencies/common/dictionaries %SOURCE1
mkdir -p dependencies/common/mathjax
unzip -qd dependencies/common/mathjax %SOURCE2
mkdir -p src/gwt/lib/gwt
pushd src/gwt/lib/gwt
ln -s %_datadir/java/gwt/ 2.5.1
popd
mkdir -p src/gwt/lib/gin/1.5
unzip -qd src/gwt/lib/gin/1.5 %SOURCE3

%build
pushd .
#fix 'boost::core::log' bug - http://stackoverflow.com/questions/25866378/cant-build-rstudio-ide-with-boost-1-56-0
echo " *** Attention : fixing boost::core::log bug *** "
find . \( -name *.cpp -or -name *.hpp \) -exec sed \
        -e 's@<core::@< ::core::@g' -e 's@\([^:]\)core::@\1::core::@g' -i {} \;
echo " *** Attention : finish fix  *** "

#build desktop
%cmake \
-DRSTUDIO_TARGET=Desktop \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name \
-DCMAKE_BUILD_TYPE=Release
%cmake_build

#build server
%cmake \
-DRSTUDIO_TARGET=Server \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name-server \
-DCMAKE_BUILD_TYPE=Release

%cmake_build
popd

%install
# I don't know why it's build twice
# It's from rosa spec
pushd .
%cmake \
-DRSTUDIO_TARGET=Desktop \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name \
-DCMAKE_BUILD_TYPE=Release
%cmakeinstall_std

mkdir -p %buildroot%_bindir
ln -s %_libdir/%name-server/bin/%name-server %buildroot%_bindir/%name-server
ln -s %_libdir/%name/bin/%name %buildroot%_bindir/%name

# The default one is too ugly
rm -f %buildroot%_desktopdir/%name.desktop
cat > %buildroot%_desktopdir/altlinux-%name.desktop << EOF
[Desktop Entry]
Name=RStudio
Comment=IDE for R
Exec=%_bindir/rstudio
Icon=rstudio
Type=Application
Terminal=false
Categories=Science;Math;X-ALTLinux-MoreApplications-Sciences-Mathematics;
MimeType=text/x-r-source;text/x-r;text/x-R;text/x-r-doc;text/x-r-sweave;text/x-r-markdown;text/x-r-html;application/x-r-data;application/x-r-project;text/x-r-history;text/x-r-profile;text/x-tex;text/x-markdown;text/html;text/css;text/javascript;
EOF
popd

%cmake \
-DRSTUDIO_TARGET=Server \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name-server

%cmakeinstall_std
ln -s %_libdir/%name-server/bin/rserver %buildroot%_bindir/rserver
# remove suse server specific files becouse girar fail
rm -fr %buildroot/%_libdir/%name-server/extras/init.d/suse
# remove debian initscripts specific files becouse girar fail
rm -fr %buildroot/%_libdir/%name-server/extras/init.d/debian

%files
%doc README.md COPYING
%_bindir/%name
%_libdir/%name
%_desktopdir/altlinux-%name.desktop

%files server
%_bindir/%name-server
%_bindir/rserver
%_libdir/%name-server

%files common
%_datadir/mime/packages/%name.xml
%_pixmapsdir/%name.png
%_iconsdir/hicolor/*/apps/%name.png
%_iconsdir/hicolor/*/mimetypes/application-x-r-*.png

%changelog
* Sun Oct 11 2015 Konstantin Artyushkin <akv@altlinux.org> 0.98.501-alt2
- initial build for ALT Linux Sisyphus

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.98.501-2
+ Revision: 149dcfd
- MassBuild#464: Increase release tag


