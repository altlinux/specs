%def_with check

Name: broot
Version: 1.57.0
Release: alt1
Summary: A new way to see and navigate directory trees
License: MIT
Group: File tools
Url: https://dystroy.org/broot
VCS: https://github.com/Canop/broot

Source: %name-%version.tar
Source1: vendor.tar
Patch: alt-fix-build-nix-on-loongarch64.patch

ExcludeArch: i586

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: diffstat

%description
%summary.

%prep
%setup -a 1
%patch -p1
diffstat -p1 -l < %PATCH0 | sed -re 's@vendor/@@' | xargs -r cargo-vendor-checksum -f
%rust_prep

%build
%rust_build

%install
%rust_install
install -Dm 0644 man/page %buildroot%_man1dir/%name.1

%check
%rust_test

%files
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Fri Jun 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.57.0-alt1
- Updated to version 1.57.0.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.56.4-alt1
- Updated to version 1.56.4.

* Sun Apr 12 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.56.2-alt1
- Updated to version 1.56.2.

* Sun Feb 15 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.55.0-alt1
- Updated to version 1.55.0.

* Sun Jan 18 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.54.0-alt1
- Updated to version 1.54.0.

* Sun Nov 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.53.0-alt1
- Updated to version 1.53.0.

* Sat Nov 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.52.0-alt1
- Updated to version 1.52.0.

* Fri Jun 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.47.0-alt1
- Updated to version 1.47.0.

* Sun Jun 01 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.46.5-alt1
- Updated to version 1.46.5.

* Tue Jan 07 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.44.5-alt1
- Updated to version 1.44.5.

* Sat Sep 21 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.44.0-alt1
- Updated to version 1.44.0.

* Fri Apr 26 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.36.1-alt1
- Updated to version 1.36.1.

* Sun Jan 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.32.0-alt2
- NMU: fixed FTBFS on LoongArch.

* Sat Jan 06 2024 Alexander Makeenkov <amakeenk@altlinux.org> 1.32.0-alt1
- Updated to version 1.32.0.

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.17.1-alt1
- Updated to version 1.17.1

* Sat Nov 19 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.2-alt1
- Updated to version 1.16.2

* Sun Oct 30 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.1-alt1
- Initial build for ALT
