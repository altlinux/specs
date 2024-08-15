%def_enable snapshot
%define _libexecsir %_prefix/libexec
%define ver_major 0.41
%define api_ver 0
%define beta %nil
%define rdn_name sm.puri.Phoc
%define xdg_name mobi.phosh.Phoc

%define dev_uid 500
%define wlroots_ver 0.17.4
%define gmobile_ver 0.1.0

# since 0.30 system 0.16 may be used but patched version required
%def_enable embed_wlroots
%{?_enable_embed_wlroots:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%def_disable embed_gmobile
%def_enable gtk_doc
%def_enable man
%def_disable check

Name: phoc
Version: %ver_major.0
Release: alt1%beta

Summary: Display compositor designed for mobile devices
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/World/Phosh/phoc

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/World/Phosh/phoc.git
Source: %name-%version%beta.tar
%endif
%{?_enable_embed_gmobile:Source1: gmobile-%gmobile_ver.tar}
%{?_enable_embed_wlroots:Source2: wlroots-%wlroots_ver.tar}

%define glib_ver 2.74
%define gmobile_ver 0.1.0
%define wayland_proto_ver 1.15
%define gnome_desktop_ver 43

BuildRequires(pre): rpm-macros-meson rpm-build-systemd
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(gnome-desktop-3.0) >= %gnome_desktop_ver
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libdisplay-info)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols) >= %wayland_proto_ver
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(xcb-icccm)
%{?_disable_embed_gmobile:BuildRequires: pkgconfig(gmobile) >= %gmobile_ver}
%{?_disable_embed_wlroots:BuildRequires: pkgconfig(wlroots) >= 0.17.1}
%{?_enable_embed_wlroots:BuildRequires: libgbm-devel libseat1-devel
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-errors)
BuildRequires: pkgconfig(hwdata)
BuildRequires: xorg-xwayland-devel libglvnd-devel libvulkan-devel
BuildRequires: pkgconfig(libliftoff)}
%{?_enable_gtk_doc:BuildRequires: gi-docgen pkgconfig(gobject-introspection-1.0) /usr/bin/g-ir-scanner}
%{?_enable_man:BuildRequires: /usr/bin/rst2man}
%{?_enable_check:BuildRequires: libgtest-devel xvfb-run mutter-gnome /usr/bin/Xwayland}

%description
Phoc is a wlroots based mobile devices compositor. Phoc is pronounced
like the English word fog.

%package devel-doc
Summary: Development documentation for Phoc
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package provides development documentation for Phoc wayland
compositor.

%prep
%setup -n %name-%version%beta %{?_enable_embed_gmobile:-a1} %{?_enable_embed_wlroots:-a2}
%{?_enable_embed_gmobile:mv gmobile-%gmobile_ver subprojects/gmobile}
%{?_enable_embed_wlroots:mv wlroots-%wlroots_ver subprojects/wlroots
pushd subprojects/wlroots
patch -p1 < ../packagefiles/wlroots/0001-Revert-layer-shell-error-on-0-dimension-without-anch.patch
popd}

%build
%meson \
    %{?_disable_embed_wlroots:-Dembed-wlroots=disabled} \
    %{?_enable_embed_wlroots:--default-library=static} \
    -Ddev-uid=%dev_uid \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_enable_man:-Dman=true}
%nil
%meson_build

%install
%meson_install

%{?_enable_embed_wlroots:
rm -r %buildroot%_includedir/wlr
rm %buildroot%_libdir/libwlroots.a
rm %buildroot%_pkgconfigdir/wlroots.pc}

%{?_enable_embed_gmobile:
rm %buildroot%_libdir/libgmobile.*
rm %buildroot%_pkgconfigdir/gmobile.pc}

%check
WLR_RENDERER=pixman xvfb-run %__meson_test

%files
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/sm.puri.phoc.gschema.xml
%_iconsdir/hicolor/symbolic/apps/%xdg_name.svg
%{?_enable_man:%_man1dir/%name.1*
%_man5dir/%name.ini.5*
%_man5dir/%name.gsettings.5*}
%doc README.md NEWS

%files devel-doc
%_datadir/doc/%name-%api_ver/

%changelog
* Thu Aug 15 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt1
- 0.41.0

* Thu Aug 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.41.0-alt0.9.rc1
- 0.41.0.rc1

* Sat Jul 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.1-alt1
- 0.40.1

* Sun Jun 30 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt1
- 0.40.0

* Wed Jun 26 2024 Yuri N. Sedunov <aris@altlinux.org> 0.40.0-alt0.9.rc1
- 0.40.0.rc1

* Tue May 14 2024 Yuri N. Sedunov <aris@altlinux.org> 0.39.0-alt1
- updated to v0.39.0-2-g5666185
- build against shared gmobile-0.2.0 library

* Sat Apr 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.38.0-alt1
- 0.38.0

* Sat Mar 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1.1
- fixed BR

* Fri Mar 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.37.0-alt1
- 0.37.0

* Sat Feb 03 2024 Yuri N. Sedunov <aris@altlinux.org> 0.36.0-alt1
- 0.36.0

* Sat Jan 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.35.0-alt1
- 0.35.0
- built with patched wlroots-0.17.1, gmobile-0.0.4

* Wed Dec 06 2023 Yuri N. Sedunov <aris@altlinux.org> 0.34.0-alt0.5.beta1
- 0.34.0.beta1

* Sat Oct 28 2023 Yuri N. Sedunov <aris@altlinux.org> 0.33.0-alt1
- 0.33.0

* Thu Oct 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.32.0-alt1
- 0.32.0

* Mon Sep 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.31.0-alt1
- 0.31.0

* Thu Aug 03 2023 Yuri N. Sedunov <aris@altlinux.org> 0.30.0-alt1
- 0.30.0 (ported to wlroots-0.16)
- built with patched wlroots-0.16.2
- enabled man and docs builds, new devel-doc subpackage

* Tue Jul 04 2023 Yuri N. Sedunov <aris@altlinux.org> 0.29.0-alt1
- 0.29.0

* Wed May 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.28.0-alt1
- updated to v0.28.0-1-gf707185

* Mon May 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.27.0-alt1
- 0.27.0

* Fri Mar 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.26.0-alt1
- 0.26.0

* Sun Mar 12 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.2-alt1
- 0.25.2

* Wed Mar 01 2023 Yuri N. Sedunov <aris@altlinux.org> 0.25.0-alt1
- 0.25.0

* Thu Feb 02 2023 Yuri N. Sedunov <aris@altlinux.org> 0.24.0-alt1
- 0.24.0

* Mon Jan 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.23.0-alt1
- 0.23.0

* Sat Sep 03 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.1-alt1
- v0.21.1-1-gc25d237

* Sun Jul 31 2022 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt0.5%beta
- first build for Sisyphus (v0.21.0_beta1-21-ge367874)


