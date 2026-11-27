%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict,lint=relaxed

%global _zig_cache_dir %_builddir/zig-cache

%define luajit_ver 2.1
%define luajit_flags -fsys=lua -Dzlua_additional_system_headers="%_datadir/luajit-%luajit_ver"

Name: ly
Version: 1.5.0
Release: alt1

Summary: The Ly display manager
License: WTFPL
Group: Graphical desktop/Other
Url: https://codeberg.org/fairyglade/ly
Vcs: https://codeberg.org/fairyglade/ly

ExclusiveArch: %zig_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

Patch0: ly-1.5.0-zlua-system-lua.patch
Patch1: ly-1.5.0-zlua-headers-flag.patch

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(pam)
# Not pkgconfig because it's version different from sisyphus (see luajit.pc)
BuildRequires: libluajit-devel = %luajit_ver

%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD,
designed with portability in mind (e.g. it does not require systemd to run).

%prep
%setup -a1
mv -f ./vendor %_zig_vendor_dir
%patch0 -p1 -d %_zig_vendor_dir/zlua-*
%patch1 -p1

# agetty provides only /sbin/agetty and not /usr/sbin/agetty
sed -i 's|\$PREFIX_DIRECTORY/sbin/agetty|/sbin/agetty|' res/ly@.service

%build
%zig_build %luajit_flags

%install
%zig_install installexe -Ddest_directory=%buildroot %luajit_flags

%files
%_bindir/%name
%_unitdir/%name@.service
%_unitdir/%name-kmsconvt@.service
%config(noreplace) %_sysconfdir/%name
%_sysconfdir/pam.d/%name
%_sysconfdir/pam.d/%name-autologin

%changelog
* Fri Nov 27 2026 Ilya Sorochan <k0tran@altlinux.org> 1.5.0-alt1
- Updated to 1.5.0.
- Build with system luajit.

* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- NMU: Updated to 1.4.1 (fixes FTBFS with zig 0.16)
- Use zig-pkg as the vendor directory
- Packaged ly-kmsconvt@.service, languages, example files and custom-sessions

* Thu Mar 12 2026 Anton Zhukharev <ancieg@altlinux.org> 1.3.2-alt1
- Updated to 1.3.2.

* Mon Dec 22 2025 Anton Zhukharev <ancieg@altlinux.org> 1.3.0-alt1
- Updated to 1.3.0.

* Tue Nov 18 2025 Anton Zhukharev <ancieg@altlinux.org> 1.2.0-alt1
- Updated to 1.2.0.

* Mon Jun 26 2023 Roman Alifanov <ximper@altlinux.org> 0.6.0-alt0.g2ca870c
- Initial build for Sisyphus
