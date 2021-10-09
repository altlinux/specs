Name: radiotray-ng
Version: 0.2.7
Release: alt2
Summary: Internet radio player

License: GPLv3+
Group: Sound
Url: https://github.com/ebruck/radiotray-ng

Source: %name-%version.tar
# Source-url: %url/archive/v%version/%name-%version.tar.gz

Patch1: %name-%version.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: libcurl-devel
BuildRequires: boost-program_options-devel
BuildRequires: boost-filesystem-devel
BuildRequires: boost-log-devel
BuildRequires: boost-locale-devel
BuildRequires: libwxGTK3.0-devel
BuildRequires: libpcre-devel
BuildRequires: jsoncpp-devel
BuildRequires: gstreamer-devel
BuildRequires: libxdg-basedir-devel
BuildRequires: libbsd-devel
BuildRequires: libappindicator-gtk3-devel
BuildRequires: libnotify-devel
BuildRequires: libglibmm-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: libffi-devel
BuildRequires: libfribidi-devel
BuildRequires: libthai-devel
BuildRequires: libdatrie-devel
BuildRequires: bzlib-devel
BuildRequires: libuuid-devel
BuildRequires: libexpat-devel
BuildRequires: libXdmcp-devel
BuildRequires: libpixman-devel
BuildRequires: libtiff-devel
BuildRequires: libmount-devel
BuildRequires: libblkid-devel
BuildRequires: libselinux-devel
BuildRequires: libXinerama-devel
BuildRequires: libXi-devel
BuildRequires: libXrandr-devel
BuildRequires: libXcursor-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXdamage-devel
BuildRequires: wayland-protocols
BuildRequires: libxkbcommon-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: libwayland-egl-devel
BuildRequires: libepoxy-devel
BuildRequires: at-spi2-atk-devel
BuildRequires: libat-spi2-core-devel
BuildRequires: libXtst-devel
BuildRequires: lsb-release

%description
Radio Tray is an online radio streaming player that runs on a Linux system
tray. Its goal is to have the minimum interface possible, making it very
straightforward to use.

Radiotray-NG is a rewrite of the classical radiotray application, but based
on modern technologies (gstreamer 1.0, python3 and c++).

%prep
%setup -q -n %name-%version
%patch1 -p1

# fix building on e2k 
# https://bugzilla.altlinux.org/40634
%ifarch %e2k
	# as of lcc 1.25.17 (glib2 induces warnings causing ftbfs)
	sed -i 's,-Werror,,' CMakeLists.txt
%endif

%build
%cmake_insource -DCONFIGURED_ONCE:BOOL=YES \
    -DLSB_RELEASE_EXECUTABLE="lsb_release" \
    -DDISTRIBUTOR_ID="alt"
%cmake_build

%install
%cmake_install

# fix .desktop file
desktop-file-edit %buildroot%_datadir/applications/radiotray-ng.desktop \
	--set-comment="Internet Radio Player" \
	--set-icon=radiotray-ng-on

# another .desktop file with bad icon
desktop-file-edit %buildroot%_datadir/applications/rtng-bookmark-editor.desktop \
	--set-icon=radiotray-ng-on

# Remove autostart
rm %buildroot%_sysconfdir/xdg/autostart/%name.desktop

# Remove themes
rm -rf %buildroot%_iconsdir/Yaru

# handle docs in files section
rm %buildroot%_datadir/doc/%name/*

# Remove self-installed license file
rm %buildroot%_datadir/licences/%name/COPYING

#Remove unneeded script
rm %buildroot%_bindir/rt2rtng

%check
appstream-util validate-relax --nonet %buildroot%_datadir/metainfo/%name.appdata.xml
desktop-file-validate %buildroot%_desktopdir/%name.desktop
desktop-file-validate %buildroot%_desktopdir/rtng-bookmark-editor.desktop

%files
%doc AUTHORS README.md
%_bindir/%name
%_bindir/rtng-bookmark-editor
%_desktopdir/%name.desktop
%_desktopdir/rtng-bookmark-editor.desktop
%_iconsdir/hicolor/*/apps/*
%_iconsdir/breeze/apps/*/radiotray-ng*.svg
%_datadir/metainfo/%name.appdata.xml
%_datadir/%name

%changelog
* Sat Oct 02 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 0.2.7-alt2
- Fix building on %%e2k, thanks to mike@ (closes: 40634)

* Wed Jul 07 2021 Evgeniy Kukhtinov <neurofreak@altlinux.org> 0.2.7-alt1
- initial build
