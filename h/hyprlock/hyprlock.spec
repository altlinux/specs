%define _unpackaged_files_terminate_build 1

Name:    hyprlock
Version: 0.9.5
Release: alt1

Summary: Hyprland's GPU-accelerated screen locking utility
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/hyprwm/hyprlock

ExcludeArch: i586

Source: %name-%version.tar
Patch1: hyprlock-alt-tcb-check.patch
Patch2: hyprlock-fix-config-files-destination-path.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: libGL-devel
BuildRequires: libGLU-devel
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(hyprlang)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libwebp)
BuildRequires: pkgconfig(libmagic)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(sdbus-c++)
BuildRequires: pkgconfig(hyprwayland-scanner)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(gbm)
BuildRequires: libpam-devel

%description
%summary

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake -GNinja -Wno-dev
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
echo 'auth            include         system-auth' > %buildroot%_sysconfdir/pam.d/%name

%files
%doc *.md
%attr(2711, root, chkpwd) %_bindir/%name
%config(noreplace) %_sysconfdir/pam.d/%name
%config(noreplace) %_sysconfdir/xdg/hypr/hyprlock.conf

%changelog
* Sat Apr 25 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.9.5-alt1
- new version 0.9.5

* Wed Apr 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.9.4-alt1
- new version 0.9.4
- fix changelog (ALT #55486)

* Wed Nov 05 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.2-alt1
- New version (ALT #56712).

* Fri Jul 18 2025 Andrey Cherepanov <cas@altlinux.org> 0.9.0-alt1
- New version.

* Mon Jun 30 2025 Andrey Cherepanov <cas@altlinux.org> 0.8.2-alt1
- New version.
- Exclude i586 from build due to missing hyprwayland-scanner for this arch.
- Fix config files destination (thanks Nikita <sc4.nick@yandex.ru>)
- Set sgid bit to executable (ALT #51014).

* Thu Nov 14 2024 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- New version.

* Thu Aug 01 2024 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt2
- Adapt to check password stored in tcb (ALT #51014).

* Fri Jul 05 2024 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Build to Sisyphus (ALT #50649) (thanks to Timofey Krymskiy).
- Adapt PAM module to ALT PAM stack.
