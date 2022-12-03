%define soversion 11

Name: libwlroots%soversion
Version: 0.16.0
Release: alt1

Summary: Modular Wayland compositor library
License: MIT
Group: System/Libraries
Url: https://gitlab.freedesktop.org/wlroots/wlroots

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Source: wlroots.tar

Patch0001: 0001-Avoid-duplicate-case-values.patch

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ctags
BuildRequires: glslang
BuildRequires: hwdatabase

BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(freerdp2)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libseat)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(vulkan)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(x11-xcb)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-composite)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xcb-xinput)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xwayland)

%description
%summary

%package -n libwlroots-devel
Summary: Development files for libwlroots
Group: Development/C
Requires: %name = %version-%release

%description -n libwlroots-devel
This package provides development files for libwlroots library.

%prep
%setup -n wlroots
%autopatch -p1

if ! grep -qs '^soversion[[:space:]]*=[[:space:]]*%soversion[[:space:]]*$' meson.build; then
	echo >&2 "Outdated %%soversion value in spec"
	exit 1
fi

%build
%meson
%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files
%_libdir/libwlroots.so.*
%doc README.md LICENSE

%files -n libwlroots-devel
%_includedir/wlr
%_libdir/libwlroots.so
%_pkgconfigdir/wlroots.pc

%changelog
* Sat Dec 03 2022 Alexey Gladkov <legion@altlinux.ru> 0.16.0-alt1
- New version (0.16.0)
- Soversion change.

* Sat Dec 03 2022 Alexey Gladkov <legion@altlinux.ru> 0.15.1-alt2
- Renamed the source package to allow multiple versions of the library in the
  repository.

* Tue Feb 08 2022 Alexey Gladkov <legion@altlinux.ru> 0.15.1-alt1
- New version (0.15.1)

* Sat Dec 25 2021 Alexey Gladkov <legion@altlinux.ru> 0.15.0-alt1
- New version (0.15.0)

* Sat Jul 17 2021 Alexey Gladkov <legion@altlinux.ru> 0.14.1-alt1
- New version (0.14.1)

* Mon Apr 26 2021 Alexey Gladkov <legion@altlinux.ru> 0.13.0-alt1
- New version (0.13.0)
- Rebased to upstream git history.
- Soversion added to the package name.

* Thu Mar 25 2021 Alexey Gladkov <legion@altlinux.ru> 0.12.0-alt1
- New version (0.12.0)
- Add libseat backend.
- Drop libdrmhelper backend.

* Sun Jul 26 2020 Alexey Gladkov <legion@altlinux.ru> 0.11.0-alt1
- New version (0.11.0)

* Fri Mar 27 2020 Alexey Gladkov <legion@altlinux.ru> 0.10.1-alt2
- Add drm backend based on libdrmhelper library.

* Wed Mar 25 2020 Alexey Gladkov <legion@altlinux.ru> 0.10.1-alt1
- New version (0.10.1)

* Mon Nov 18 2019 Alexey Gladkov <legion@altlinux.ru> 0.8.1-alt1
- New version (0.8.1)

* Fri Aug 09 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.0-alt2
- Add freerdp support
- Fix build error

* Fri May 24 2019 Alexey Gladkov <legion@altlinux.ru> 0.6.0-alt1
- New version (0.6.0)

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

