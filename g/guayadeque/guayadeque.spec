# wx-config
%global wxversion 3.2

Name: guayadeque
Version: 0.4.7
Release: alt1
Summary: Music player
License: GPLv3+ and BSD and LGPLv2+ and wxWidgets
URL: http://guayadeque.org/
Group: Sound
# Source-url: https://github.com/anonbeat/guayadeque/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
# https://github.com/anonbeat/guayadeque/issues/144
Patch0: guayadeque-wxwidgets-3.2.patch
# https://github.com/anonbeat/guayadeque/issues/155
Patch1: guayadeque-ambiguous-overload.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: libtag-devel
BuildRequires: libcurl-devel
BuildRequires: libgpod-devel
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libwxGTK3.2-devel
BuildRequires: libwxsqlite3-devel
BuildRequires: libdbus-devel

%description
Guayadeque is a music management program designed for all music enthusiasts. It
is Full Featured Linux media player that can easily manage large collections
and uses the Gstreamer media framework.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake \
 -DCMAKE_BUILD_TYPE='Release' \
 -DCMAKE_EXE_LINKER_FLAGS:STRING=-lwx_gtk3u_aui-%wxversion \
 -DCMAKE_CXX_FLAGS="%optflags"
 
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_datadir/applications
desktop-file-install --delete-original  \
        --dir %buildroot%_datadir/applications   \
        --remove-category Application \
        %buildroot%_datadir/applications/%name.desktop

%find_lang %name

%check
desktop-file-validate %buildroot%_datadir/applications/*.desktop
appstream-util validate-relax --nonet %buildroot%_datadir/appdata/*.appdata.xml

%files -f %name.lang
%doc README
%_bindir/%name
%_datadir/%name/*.conf
%_datadir/%name/*.xml
%dir %_datadir/%name
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop
%_datadir/appdata/%name.appdata.xml

%changelog
* Fri Mar 17 2023 Anton Midyukov <antohami@altlinux.org> 0.4.7-alt1
- Initial build
