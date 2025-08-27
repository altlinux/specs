%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: nedit-ng
Version: 2025.2
Release: alt0.1.rc1
Summary: Qt port of the NEdit using modern C++
Group: Editors
License: GPLv2+
Url: https://github.com/eteran/nedit-ng
Vcs: https://github.com/eteran/nedit-ng.git
Source: %name-%version.tar
Patch: %name-alt-unbundle-yaml-cpp.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ boost-devel qt6-base-devel qt6-tools-devel libyaml-cpp-devel

%description
%name is a Qt port of the Nirvana Editor (NEdit) version 5.6. It is intended
to be a drop in replacement for nedit in every practical way, just as on many
systems /usr/bin/vi is now a symlink to /usr/bin/vim.

Because it is a true port of the original code, it (at least for now) inherits
some (but not all) of the limitations of the original. On the other hand, some
aspects have been improved simply by the fact that it is now a Qt application.

%prep
%setup
%patch -p1
rm -rf libs/yaml-cpp-0.8.0

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  %nil
%cmake_build

%install
%cmake_install
subst 's,Exec=nedit\ \%U,Exec=%name \%U,' %name.desktop
subst 's,Icon=nedit,Icon=%name,' %name.desktop
install -m644 -pD %name.desktop %buildroot%_desktopdir/%name.desktop
install -m644 -pD src/res/%name.png %buildroot%_liconsdir/%name.png

%files
%doc LICENSE.md README.md
%_bindir/%name
%_bindir/nc-ng
%_bindir/nedit-import
%_desktopdir/%name.desktop
%_liconsdir/%name.png

%changelog
* Fri May 30 2025 L.A. Kostis <lakostis@altlinux.ru> 2025.2-alt0.1.rc1
- 2025.2_rc1.
- Switch to qt6.

* Thu May 29 2025 L.A. Kostis <lakostis@altlinux.ru> 2025.1-alt1.1
- Unbundle yaml-cpp.

* Wed May 28 2025 L.A. Kostis <lakostis@altlinux.ru> 2025.1-alt1
- Initial build for ALTLinux.

