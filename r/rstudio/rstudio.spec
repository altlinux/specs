%define _unpackaged_files_terminate_build 1

# update from scripts in dependencies/common
# egrep '(GWT_SDK_VER=|GIN_VER=|SELENIUM_VER=|CHROMEDRIVER_VER=)' dependencies/common/install-gwt
%define GWT_VER 2.7.0
%define GIN_VER 1.5
%define SELENIUM_VER 2.37.0
%define CHROMEDRIVER_VER 2.7

Name: rstudio
Version: 1.1.383
Release: alt1
Summary: RStudio IDE is a powerful and productive user interface for R
Group: Sciences/Mathematics
License: GPLv3
Url: http://www.rstudio.com/

# https://github.com/rstudio/rstudio.git
Source: %name-%version.tar
# https://s3.amazonaws.com/rstudio-dictionaries/core-dictionaries.zip
Source1: core-dictionaries.tar
# https://s3.amazonaws.com/rstudio-buildtools/gin-1.5.zip
Source2: gin.tar
# https://s3.amazonaws.com/rstudio-buildtools/gwt-2.7.0.zip
Source3: gwt.tar
# https://s3.amazonaws.com/rstudio-buildtools/selenium-java-2.37.0.zip
Source4: selenium-java.tar
# https://s3.amazonaws.com/rstudio-buildtools/selenium-server-standalone-2.37.0.jar
Source5: selenium-server-standalone-%{SELENIUM_VER}.jar
# https://s3.amazonaws.com/rstudio-buildtools/chromedriver-linux
Source6: chromedriver-linux
# https://github.com/rstudio/packrat.git
Source7: packrat.tar
# https://github.com/rstudio/rmarkdown.git
Source8: rmarkdown.tar
# https://github.com/rstudio/shinyapps.git
Source9: shinyapps.tar
# https://github.com/rstudio/rsconnect.git
Source10: rsconnect.tar

Source11: mathjax.tar

Patch1: rstudio-1.1.357-gentoo-clang-pandoc.patch
Patch2: rstudio-upstream-boost-compat.patch
Patch3: rstudio-alt-boost-compat.patch
Patch4: rstudio-alt-dialog-buttons.patch

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: clang
BuildRequires: boost-program_options-devel boost-devel boost-devel-static boost-log-devel
BuildRequires: boost-interprocess-devel boost-asio-devel boost-devel-headers
BuildRequires: libicu-devel
BuildRequires: java-devel
BuildRequires: libpam0-devel
BuildRequires: qt5-base-devel qt5-webchannel-devel qt5-quick1-devel qt5-location-devel qt5-sensors-devel qt5-svg-devel qt5-xmlpatterns-devel
BuildRequires: qt5-declarative-devel qt5-quickcontrols2-devel qt5-webkit-devel
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
%setup -b1 -b2 -b3 -b4 -b7 -b8 -b9 -b10 -b11
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

mkdir -p src/gwt/lib/{gin,gwt} \
	dependencies/common/dictionaries \
	src/gwt/lib/selenium/%{SELENIUM_VER} \
	src/gwt/lib/selenium/chromedriver/%{CHROMEDRIVER_VER}


mv ../gwt src/gwt/lib/gwt/%{GWT_VER}
mv ../gin src/gwt/lib/gin/%{GIN_VER}
mv ../core-dictionaries dependencies/common/dictionaries
mv ../selenium-java src/gwt/lib/selenium/%{SELENIUM_VER}
cp %{SOURCE5} src/gwt/lib/selenium/%{SELENIUM_VER}/
cp %{SOURCE6} src/gwt/lib/selenium/chromedriver/%{CHROMEDRIVER_VER}/
mv ../packrat dependencies/common/packrat
mv ../rmarkdown dependencies/common/rmarkdown
mv ../shinyapps dependencies/common/shinyapps
mv ../rsconnect dependencies/common/rsconnect
mv ../mathjax dependencies/common/mathjax-26

%build
#build desktop
%cmake \
-DRSTUDIO_TARGET=Desktop \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name \
-DQT_QMAKE_EXECUTABLE=%_bindir/qmake-qt5 \
-DCMAKE_BUILD_TYPE=Release
%cmake_build

#build server
%cmake \
-DRSTUDIO_TARGET=Server \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name-server \
-DQT_QMAKE_EXECUTABLE=%_bindir/qmake-qt5 \
-DCMAKE_BUILD_TYPE=Release

%cmake_build

%install
# I don't know why it's build twice
# It's from rosa spec
%cmake \
-DRSTUDIO_TARGET=Desktop \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name \
-DQT_QMAKE_EXECUTABLE=%_bindir/qmake-qt5 \
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

%cmake \
-DRSTUDIO_TARGET=Server \
-DCMAKE_INSTALL_PREFIX=%_libdir/%name-server \
-DQT_QMAKE_EXECUTABLE=%_bindir/qmake-qt5 \
-DCMAKE_BUILD_TYPE=Release

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
* Fri Jun 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.383-alt1
- Updated to upstream version 1.1.383.

* Sun Oct 11 2015 Konstantin Artyushkin <akv@altlinux.org> 0.98.501-alt2
- initial build for ALT Linux Sisyphus

* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.98.501-2
+ Revision: 149dcfd
- MassBuild#464: Increase release tag


