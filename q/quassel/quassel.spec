%ifarch %qt5_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

Version:	0.13.1
Name:		quassel
Release:	alt4
Summary:	Quassel - IRC client
License: 	GPLv3
Group: 		Networking/IRC
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://www.quassel-irc.org/
Source0:	http://www.quassel-irc.org/pub/%name-%version.tar.bz2

Patch0:		quassel-0.13.1-qt5.14.patch

# Automatically added by buildreq on Sat Jun 26 2021 (-bi)
# optimized out: cmake cmake-modules elfutils fontconfig gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libdbusmenu-qt52 libgdk-pixbuf libglvnd-devel libgpg-error libopencore-amrnb0 libopencore-amrwb0 libp11-kit libqca-qt5 libqt5-core libqt5-dbus libqt5-gui libqt5-multimedia libqt5-network libqt5-positioning libqt5-printsupport libqt5-qml libqt5-quick libqt5-quickwidgets libqt5-script libqt5-sql libqt5-webchannel libqt5-webengine libqt5-webenginecore libqt5-webenginewidgets libqt5-widgets libqt5-xml librabbitmq-c libsasl2-3 libstdc++-devel libx265-160 perl python-base python-modules qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel sh4
BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: cmake libdbusmenu-qt5-devel libqca-qt5-devel libssl-devel qt5-multimedia-devel qt5-script-devel qt5-tools-devel zlib-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif

%description
Quassel IRC is a modern, cross-platform, distributed IRC client based on the Qt4 framework.
Distributed means that one (or multiple) client(s) can attach to and detach from a central
core that stays permanently online -- much like the popular combination of screen and a
text-based IRC client such as WeeChat, and similar to (but much more featureful than) so-called BNCs.
Re-attaching your client will show your IRC session in the same state as you left it in
(plus whatever happened while you were gone), and this even when you re-attach from a different
location. In addition, Quassel IRC can be used like a traditional client, with providing both
client and core functionality in one binary. An optional Beginner's Mode completely hides
this feature, so Quassel IRC can be setup very easily.

%prep
%setup -q
%patch0 -p1

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%_prefix \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DUSE_QT5=ON \
%if_enabled qtwebengine
	-DWITH_WEBENGINE=ON \
%else
	-DWITH_WEBKIT=ON \
%endif
	-DWITH_KDE=OFF \
	-DWITH_OPENSSL=ON
%cmake_build

%install
%cmake_install

%files
%dir %_datadir/%name
%_bindir/*
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/%name.png

%changelog
* Mon Nov 27 2023 Sergey V Turchin <zerg@altlinux.org> 0.13.1-alt4
- using rpm-macros-qt5-webengine

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 0.13.1-alt3
- build with qtwebkit instead of qtwebengine on e2k and ppc64le

* Mon Jun 28 2021 Motsyo Gennadi <drool@altlinux.ru> 0.13.1-alt2
- add patch for Qt >= 5.14 from Gentoo
 (https://raw.githubusercontent.com/gentoo/gentoo/master/net-irc/quassel/files/quassel-0.13.1-qt5.14.patch)

* Sat Jun 26 2021 Motsyo Gennadi <drool@altlinux.ru> 0.13.1-alt1
- 0.13.1 (#40259)

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.5.2-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sat Apr 10 2010 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Wed Nov 18 2009 Motsyo Gennadi <drool@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Wed May 20 2009 Motsyo Gennadi <drool@altlinux.ru> 0.4.1-alt1
- initial build for ALT Linux
