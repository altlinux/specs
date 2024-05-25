%define soversion 12

Name: libwlroots
Version: 0.17.3
Release: alt1

Summary: Modular Wayland compositor library
License: MIT
Group: System/Libraries
Url: https://gitlab.freedesktop.org/wlroots/wlroots

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# Source-url: https://gitlab.freedesktop.org/wlroots/wlroots/-/releases/%version/downloads/wlroots-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ctags
BuildRequires: glslang
BuildRequires: pkgconfig(hwdata)

BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(freerdp2)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(glesv2)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libdisplay-info)
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
BuildRequires: pkgconfig(xcb-errors)

BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xwayland)

%description
%summary.

%package -n libwlroots%soversion
Summary: Modular Wayland compositor library
Group: System/Libraries

%description -n libwlroots%soversion
%summary.

%package -n libwlroots-devel
Summary: Development files for libwlroots
Group: Development/C
Requires: libwlroots%soversion = %EVR

%description -n libwlroots-devel
This package provides development files for libwlroots library.

%prep
%setup

if ! grep -qs '^soversion[[:space:]]*=[[:space:]]*%soversion[[:space:]]*$' meson.build; then
	echo >&2 "Outdated %%soversion value in spec"
	exit 1
fi

%build
%meson \
  "-Dbackends=[
    'drm',
	'libinput',
    'x11',
  ]" \
  -Dxwayland=enabled \
  -Dxcb-errors=enabled

%meson_build

%install
%meson_install

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
%meson_test

%files -n libwlroots%soversion
%_libdir/libwlroots.so.*
%doc README.md LICENSE

%files -n libwlroots-devel
%_includedir/wlr
%_libdir/libwlroots.so
%_pkgconfigdir/wlroots.pc

%changelog
* Sat May 25 2024 Roman Alifanov <ximper@altlinux.org> 0.17.3-alt1
- new version 0.17.3 (with rpmrb script)

* Tue Feb 27 2024 Roman Alifanov <ximper@altlinux.org> 0.17.1-alt2
- reworking package to save history of tasks in the future

* Sat Feb 24 2024 Roman Alifanov <ximper@altlinux.org> 0.17.1-alt1
- new version 0.17.1 (with rpmrb script)
- move to tarball

* Sun Oct 01 2023 Alexey Gladkov <legion@altlinux.ru> 0.16.2-alt2
- Fix frame_number deprecated in FFmpeg 6.0

* Fri Mar 10 2023 Alexey Gladkov <legion@altlinux.ru> 0.16.2-alt1
- New version (0.16.2)

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

