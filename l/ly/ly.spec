%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%global _zig_cache_dir %_builddir/zig-cache

Name: ly
Version: 1.3.2
Release: alt1

Summary: The Ly display manager
License: WTFPL
Group: Graphical desktop/Other
Url: https://codeberg.org/fairyglade/ly
Vcs: https://codeberg.org/fairyglade/ly

ExclusiveArch: %zig_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(pam)

%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD,
designed with portability in mind (e.g. it does not require systemd to run).

%prep
%setup -a1
mv -f ./vendor %_zig_cache_dir

%build
%zig_build

%install
%zig_install installexe -Ddest_directory=%buildroot

%files
%_bindir/%name
%_unitdir/%name@.service
%_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/config.ini
%_sysconfdir/pam.d/%name
%_sysconfdir/pam.d/%name-autologin

%changelog
* Thu Mar 12 2026 Anton Zhukharev <ancieg@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Mon Dec 22 2025 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Tue Nov 18 2025 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Jun 26 2023 Roman Alifanov <ximper@altlinux.org> 0.6.0-alt0.g2ca870c
- Initial build for Sisyphus
