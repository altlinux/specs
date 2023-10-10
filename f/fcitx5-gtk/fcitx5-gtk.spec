Group: Graphical desktop/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: libX11-devel libxkbcommon-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

Name:           fcitx5-gtk
Version:        5.1.0
Release:        alt1_1
Summary:        Gtk im module and glib based dbus client library
License:        LGPLv2+
URL:            https://github.com/fcitx/fcitx5-gtk
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:        https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        https://pgp.key-server.io/download/0x8E8B898CBF2412F9


BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  libfmt-devel
Source44: import.info

#Requires:       (%{name}2 if gtk2)
#Requires:       (%{name}3 if gtk3)
#Requires:       (%{name}4 if gtk4)

# not requiring fcitx5 due to that I want to make 
# im_modules be able to install seperately
# this will be helpful to those who are looking 
# forward to use upstream flatpak version.

%description
Gtk im module and glib based dbus client library.

%package devel
Group: Graphical desktop/Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description devel
Development files for fcitx5-gtk.

%package -n %{name}2
Group: Graphical desktop/Other
Summary:        fcitx5 gtk module for gtk2
Requires:       %{name} = %{version}-%{release}

%description -n %{name}2
fcitx5 gtk module for gtk2.

%package -n %{name}3
Group: Graphical desktop/Other
Summary:        fcitx5 gtk module for gtk3
Requires:       %{name} = %{version}-%{release}

%description -n %{name}3
fcitx5 gtk module for gtk3.

%package -n %{name}4
Group: Graphical desktop/Other
Summary:        fcitx5 gtk module for gtk4
Requires:       %{name} = %{version}-%{release}

%description -n %{name}4
fcitx5 gtk module for gtk4.

%prep
%setup -q


%build
%{fedora_v2_cmake} -GNinja
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install
sed -i 's,^Version: $,Version: %version,' %buildroot%_pkgconfigdir/Fcitx5GClient.pc

%files
%doc --no-dereference LICENSES/LGPL-2.1-or-later.txt
%doc README.md 
%{_libdir}/libFcitx5GClient.so.5.*
%{_libdir}/libFcitx5GClient.so.2
%{_libdir}/girepository-1.0/FcitxG-1.0.typelib

%files devel
%{_includedir}/Fcitx5/GClient/
%{_libdir}/cmake/Fcitx5GClient
%{_libdir}/libFcitx5GClient.so
%{_libdir}/pkgconfig/Fcitx5GClient.pc
%{_datadir}/gir-1.0/

%files -n %{name}2
%{_libdir}/gtk-2.0/*/immodules/im-fcitx5.so
%{_bindir}/fcitx5-gtk2-immodule-probing

%files -n %{name}3
%{_libdir}/gtk-3.0/*/immodules/im-fcitx5.so
%{_bindir}/fcitx5-gtk3-immodule-probing

%files -n %{name}4
%{_libdir}/gtk-4.0/*/immodules/libim-fcitx5.so
%{_bindir}/fcitx5-gtk4-immodule-probing

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 5.1.0-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 5.0.18-alt1_1
- new version

