Name: checkmake
Version: 0.3.2
Release: alt1

Summary: Linter and analyzer for Makefiles

Group: Development/Tools
License: MIT
Url: https://github.com/mrtazz/checkmake

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mrtazz/checkmake/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang

BuildRequires: rpm-build-golang

%description
Checkmake is a tool for linting and checking Makefiles.
It scans Makefiles for potential issues based on configurable rules.

%prep
%setup -a1

%build
%gobuild -mod=vendor ./cmd/checkmake

%install
install -D -p -m 755 %name %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- new version 0.3.2

* Wed Jan 08 2025 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for ALT Sisyphus
