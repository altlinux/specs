%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,unresolved=relaxed

Summary: A popular and easy to use graphical IRC (chat) client
Name: hexchat
Version: 2.16.2
Release: alt1
License: GPLv2+
Group: Networking/IRC
Url: https://hexchat.github.io
VCS: https://github.com/hexchat/hexchat.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: meson
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(libproxy-1.0)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(lua)
BuildRequires: perl-devel perl(ExtUtils/Embed.pm)
BuildRequires: python3(cffi)
BuildRequires: python3(setuptools)

Requires: enchant2

Provides: xchat = %EVR
Obsoletes: xchat
Provides: xchat2 = %EVR
Obsoletes: xchat2

%add_python3_path %_libdir/hexchat/python

%add_python3_req_skip _hexchat_embedded

%description
HexChat is an easy to use graphical IRC chat client for the X Window System.
It allows you to join multiple IRC channels (chat rooms) at the same time,
talk publicly, private one-on-one conversations etc. Even file transfers
are possible.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description devel
This package contains the development files for %name.

%prep
%setup

%build
%meson -Dwith-lua=lua
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc COPYING readme.md
%_bindir/hexchat
%dir %_libdir/hexchat
%dir %_libdir/hexchat/plugins
%_libdir/hexchat/plugins/checksum.so
%_libdir/hexchat/plugins/fishlim.so
%_libdir/hexchat/plugins/lua.so
%_libdir/hexchat/plugins/sysinfo.so
%_libdir/hexchat/plugins/perl.so
%_libdir/hexchat/plugins/python.so
%_libdir/hexchat/python
%_desktopdir/*.desktop
%_iconsdir//hicolor/*/apps/*
%_datadir/metainfo/*.appdata.xml
%_datadir/dbus-1/services/org.hexchat.service.service
%_man1dir/*

%files devel
%_includedir/*
%_pkgconfigdir/*

%changelog
* Sun Apr 28 2024 Anton Farygin <rider@altlinux.ru> 2.16.2-alt1
- 2.16.2

* Wed Feb 16 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2.16.1-alt1
- Updated to upstream version 2.16.1.

* Mon Oct 04 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.16.0-alt1
- Updated to upstream version 2.16.0.

* Fri Apr 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.14.3-alt1
- Updated to version 2.14.3.

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2.14.2-alt1.1
- rebuild with new perl 5.28.1

* Fri Sep 21 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.14.2-alt1
- Initial build for ALT.
