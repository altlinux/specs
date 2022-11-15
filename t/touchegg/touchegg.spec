%define _cmake__builddir BUILD

Name:     touchegg
Version:  2.0.15
Release:  alt1

Summary:  Linux multi-touch gesture recognizer
License:  GPL-3.0
Group:    Other
Url:      https://github.com/JoseExposito/touchegg

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch1:   touchegg-alt-remove-static.patch

BuildRequires(pre): rpm-build-ninja
BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libXdmcp-devel
BuildRequires: libXrandr-devel
BuildRequires: libXtst-devel
BuildRequires: libcairo-devel
BuildRequires: libgtk+3-devel
BuildRequires: libinput-devel
BuildRequires: libpcre-devel
BuildRequires: libpugixml-devel
BuildRequires: libudev-devel
BuildRequires: libffi-devel
BuildRequires: libsystemd-devel

%description
Touchegg is an app that runs in the background and transform the gestures you
make on your touchpad into visible actions in your desktop.

%prep
%setup
%ifarch %e2k
# because of "multiple definition of" errors at linking
%define lcc_fix() \
  sed -i "1i #define preferred_separator preferred_separator_$(echo %1 | tr /- __)" src/%1.cpp
%lcc_fix config/xml-config-loader
%lcc_fix utils/client-lock
%lcc_fix utils/paths
%lcc_fix main
%else
%patch1 -p1
%endif

%build
%cmake -GNinja -Wno-dev
%ninja_build -C BUILD

%install
%ninja_install -C BUILD

%preun
%preun_service %name

%post
%post_service %name

%files
%doc *.md
%_bindir/%name
%_sysconfdir/xdg/autostart/%name.desktop
%_datadir/%name
%_unitdir/%name.service

%changelog
* Tue Nov 15 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.15-alt1
- New version.

* Sat Apr 02 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.14-alt1
- New version.

* Mon Jan 10 2022 Andrey Cherepanov <cas@altlinux.org> 2.0.13-alt1
- New version.

* Fri Oct 22 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.12-alt1
- New version.

* Sat Sep 25 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.0.11-alt2
- Fixed build for Elbrus.

* Mon Jul 05 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.11-alt1
- New version.

* Tue Jun 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.10-alt1
- New version.

* Wed Apr 28 2021 Arseny Maslennikov <arseny@altlinux.org> 2.0.9-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue Apr 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.9-alt1
- New version.

* Thu Feb 25 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.8-alt1
- New version.

* Mon Feb 08 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.7-alt1
- New version.

* Tue Feb 02 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.6-alt1
- New version.

* Thu Jan 07 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.5-alt1
- New version.

* Sun Jan 03 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
