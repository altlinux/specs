%global _unpackaged_files_terminate_build 1
%def_with check

Name: rpi
Version: 0.21.2
Release: alt1
Summary: Coding-agent runtime and terminal CLI inspired by Pi
License: MIT
Group: Development/Tools
URL: https://rpi.laofu.online
VCS: https://github.com/bigfish1913/pi-rust

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-disable-self-update.patch

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
Rust-native, library-first coding-agent runtime and terminal CLI
inspired by Pi, with composable LLM providers, tools, sessions,
and plugin ABI.
Ready-to-install extensions live in the online catalog
https://rpi.bigfisharc.cn/packages.html.

%prep
%setup -a1
%autopatch -p1
%rust_prep

%build
%rust_build -p rpi-cli

%install
%rust_install rpi

%check
%rust_test -p rpi-cli -- --test-threads=1

%files
%_bindir/rpi

%changelog
* Mon Nov 09 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.21.2-alt1
- Updated to version 0.21.2.

* Sun Nov 08 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.21.1-alt1
- Updated to version 0.21.1.

* Fri Nov 06 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.21.0-alt1
- Updated to version 0.21.0.

* Thu Nov 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.20.0-alt1
- Updated to version 0.20.0.

* Wed Nov 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.17.1-alt1
- Updated to version 0.17.1.

* Sun Nov 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.16.0-alt1
- Updated to version 0.16.0.

* Wed Oct 28 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.0-alt1
- Updated to version 0.12.0.

* Tue Oct 27 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.11.0-alt1
- Initial build for ALT.
