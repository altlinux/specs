%define _unpackaged_files_terminate_build 1
%def_with check

Name: astroterm
Version: 1.1.0
Release: alt1

Summary: A planetarium for your terminal
License: MIT
Group: Games/Other
Url: https://github.com/da-luce/astroterm
Vcs: https://github.com/da-luce/astroterm

Source0: %name-%version.tar
# bsc5 - archived copy from the bright star catalog webpage
Source1: bsc5

BuildRequires(pre): rpm-macros-meson
BuildRequires: pkg-config
BuildRequires: ninja-build
BuildRequires: meson
BuildRequires: xxd
BuildRequires: libncurses++w-devel
BuildRequires: libargtable2-devel

%description
%summary

Explore stars, planets, constellations, and more, all rendered right
in the command line-no telescope required.

%prep
%setup
cp %SOURCE1 %_builddir/%name-%version/data

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_bindir/astroterm
%doc LICENSE README.md

%changelog
* Tue Mar 31 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.1.0-alt1
- Updated to 1.1.0 for ALT Sisyphus.

* Thu Jan 20 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.0.10-alt1
- Updated to 1.0.10 for ALT Sisyphus.

* Thu Oct 1 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.0.9-alt1
- Updated to 1.0.9 for ALT Sisyphus.

* Thu Aug 11 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.0.8-alt1
- Updated to 1.0.8 for ALT Sisyphus.

* Thu Mar 13 2025 Timofei Fedotov <sovtouch@altlinux.org> 1.0.7-alt1
- Initial build for ALT Sisyphus.
