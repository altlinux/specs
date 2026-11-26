%define _unpackaged_files_terminate_build 1

Name: avd-fw
Version: 0.2
Release: alt1
ExclusiveArch: aarch64

Summary: Video codec firmware loader Apple Sillicon
License: MIT
Group: System/Configuration/Hardware
URL: https://github.com/AsahiLinux/avd-fw
VCS: https://github.com/AsahiLinux/avd-fw

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: clang
BuildRequires: llvm
BuildRequires: lld

%description
%summary.

%prep
%setup
%autopatch -p1

sed -i "s|run_command('version.sh', 'get-vcs', check: true).stdout().strip()|'v%{version}'|" meson.build

%build
%meson --cross-file=./llvm.ini --libdir=%_libexecdir
%meson_build

%install
%meson_install

%files
%_libexecdir/firmware/apple/avd-fw-v2-t0.bin
%_libexecdir/firmware/apple/avd-fw-v3-t0.bin
%_libexecdir/firmware/apple/avd-fw-v3-t1.bin
%_libexecdir/firmware/apple/avd-fw-v4-t0.bin
%_libexecdir/firmware/apple/avd-fw-v5-t1.bin
%_libexecdir/firmware/apple/avd-fw-v5-t0.bin

%changelog
* Thu Nov 26 2026 Anton Osipov <radiolamp@altlinux.org> 0.2-alt1
- 0.2.
- Use %{version} from spec instead of git describe in meson.build
  to build without .git / network access.

* Thu Sep 10 2026 Anton Osipov <radiolamp@altlinux.org> 0.1-alt1
- Initial build for ALT.
