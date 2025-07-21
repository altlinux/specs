%define        _unpackaged_files_terminate_build 1
%define        nomen quassel
%ifarch %qt5_qtwebengine_arches
%def_enable    qtwebengine
%else
%def_disable   qtwebengine
%endif

Version:       0.14.0.37
Name:          %nomen
Release:       alt0.1
Summary:       Quassel - IRC client
License:       GPLv3
Group:         Networking/IRC
Url:           https://www.quassel-irc.org/
Vcs:           https://github.com/quassel/quassel.git

Source:        %name-%version.tar

BuildRequires(pre): rpm-macros-qt5-webengine
BuildRequires: cmake
BuildRequires: libdbusmenu-qt5-devel
BuildRequires: libqca-qt5-devel
BuildRequires: libssl-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-script-devel
BuildRequires: qt5-tools-devel
BuildRequires: zlib-devel
BuildRequires: boost-devel
%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif

%description
Quassel IRC is a modern, cross-platform, distributed IRC client based on the Qt4
framework. Distributed means that one (or multiple) client(s) can attach to and
detach from a central core that stays permanently online -- much like the
popular combination of screen and a text-based IRC client such as WeeChat, and
similar to (but much more featureful than) so-called BNCs. Re-attaching your
client will show your IRC session in the same state as you left it in (plus
whatever happened while you were gone), and this even when you re-attach from a
different location. In addition, Quassel IRC can be used like a traditional
client, with providing both client and core functionality in one binary. An
optional Beginner's Mode completely hides this feature, so Quassel IRC can be
setup very easily.

%package       -n lib%{nomen}
Summary:       Quassel - IRC client library
Group:         System/Libraries

%description   -n lib%{nomen}
Quassel - IRC client library.

Quassel IRC is a modern, cross-platform, distributed IRC client based on the Qt4
framework. Distributed means that one (or multiple) client(s) can attach to and
detach from a central core that stays permanently online -- much like the
popular combination of screen and a text-based IRC client such as WeeChat, and
similar to (but much more featureful than) so-called BNCs. Re-attaching your
client will show your IRC session in the same state as you left it in (plus
whatever happened while you were gone), and this even when you re-attach from a
different location. In addition, Quassel IRC can be used like a traditional
client, with providing both client and core functionality in one binary. An
optional Beginner's Mode completely hides this feature, so Quassel IRC can be
setup very easily.


%package       -n lib%{nomen}-devel
Summary:       Quassel - IRC client development files
Group:         Development/C++

%description   -n lib%{nomen}-devel
Quassel - IRC client development files.

Quassel IRC is a modern, cross-platform, distributed IRC client based on the Qt4
framework. Distributed means that one (or multiple) client(s) can attach to and
detach from a central core that stays permanently online -- much like the
popular combination of screen and a text-based IRC client such as WeeChat, and
similar to (but much more featureful than) so-called BNCs. Re-attaching your
client will show your IRC session in the same state as you left it in (plus
whatever happened while you were gone), and this even when you re-attach from a
different location. In addition, Quassel IRC can be used like a traditional
client, with providing both client and core functionality in one binary. An
optional Beginner's Mode completely hides this feature, so Quassel IRC can be
setup very easily.


%prep
%setup -q

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
   -DWITH_OPENSSL=ON \
   %nil
%cmake_build

%install
%cmake_install

%files
%dir %_datadir/%name
%_bindir/*
%_datadir/%name
%_desktopdir/*.desktop
%_iconsdir/*/*/apps/%name.png

%files         -n lib%{nomen}
%_libdir/lib%{nomen}-*.so.*

%files         -n lib%{nomen}-devel
%_libdir/lib%{nomen}-*.so


%changelog
* Sun Jul 20 2025 Pavel Skrylev <majioa@altlinux.org> 0.14.0.37-alt0.1
- ^ 0.13.1 -> 0.14.0p37
- * rebased to git upstream

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
