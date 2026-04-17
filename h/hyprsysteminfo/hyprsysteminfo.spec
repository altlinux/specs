Name: hyprsysteminfo
Version: 0.1.3.6abb64f
Release: alt1
License: BSD-3-Clause

Summary: A tiny hyprtoolkit application to display information about the running system
Summary(ru_RU.UTF-8): Крошечное приложение hyprtoolkit для отображения информации о запущенной системе

Group: Graphical desktop/Other

Url: https://github.com/hyprwm/hyprsysteminfo
Vcs: https://github.com/hyprwm/hyprsysteminfo.git

ExcludeArch: %ix86
Source: %name-%version.tar

BuildRequires: cmake

BuildRequires: clang libstdc++-devel

BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(hyprutils)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: pkgconfig(aquamarine)

BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpci)

BuildRequires: glaze-devel

%description
A tiny hyprtoolkit application to display information about
the running system, or copy diagnostics data, without the terminal.

%description -l ru_RU.UTF-8
Небольшое приложение hyprtoolkit для отображения информации о запущенной
системе или копирования диагностических данных без терминала.

%prep
%setup

%build
%cmake -DCMAKE_CXX_COMPILER=clang++
%cmake_build

%install
%cmake_install

%files
%_bindir/hyprsysteminfo
%_desktopdir/hyprsysteminfo.desktop

%changelog
* Fri Mar 20 2026 Kirill Unitsaev <fiersik@altlinux.org> 0.1.3.6abb64f-alt1
- new version 0.1.3.6abb64f
- rewrite entire app in hyprtoolkit
- build with clang

* Thu Jan 23 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.3-alt2
- drop manual dependencies

* Fri Jan 10 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.3-alt1
- new version 0.1.3 (with rpmrb script)

* Sat Jan 04 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.1.2-alt1
- Initial build
