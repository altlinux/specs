Name: binwalk
Version: 3.1.0
Release: alt1

Summary: Firmware Analysis Tool

License: MIT
Group: File tools
Url: https://github.com/ReFirmLabs/binwalk

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ReFirmLabs/binwalk/archive/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc
BuildRequires: bzlib-devel liblzma-devel libfreetype-devel fontconfig-devel

%description
Binwalk is a firmware analysis tool designed to assist in the analysis,
extraction, and reverse engineering of firmware images and other binary blobs.
It is simple to use, fully scriptable,
and can be easily extended via custom signatures, extraction rules, and plugin modules.

Binwalk supports various types of analysis useful
for inspecting and reverse engineering firmware, including:

* Embedded file identification and extraction
* Executable code identification
* Entropy analysis and graphing
* Heuristic data analysis

Binwalk's file signatures are (mostly) compatible with the magic signatures
used by the Unix file utility, and include customized/improved signatures
for files that are commonly found in firmware images such as compressed/archived files,
firmware headers, kernels, bootloaders, filesystems, etc.

%prep
%setup -a1

mkdir -p .cargo
cat >> .cargo/config <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- new version 3.1.0 (rewritten in Rust)

* Sat Feb 25 2023 Vitaly Lipatov <lav@altlinux.ru> 2.3.4-alt1
- new version 2.3.4 (with rpmrb script)

* Sat Dec 18 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- new version 2.3.3 (with rpmrb script)

* Thu Aug 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.2-alt1
- new version 2.3.2 (with rpmrb script)

* Mon Jun 07 2021 Vitaly Lipatov <lav@altlinux.ru> 2.3.1-alt1
- new version 2.3.1 (with rpmrb script)

* Mon Nov 11 2019 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt2
- Transfer on python3.

* Sat Oct 26 2019 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0 (with rpmrb script)

* Sat Feb 16 2019 Pavel Nakonechnyi <zorg@altlinux.org> 2.1.1-alt3.git2e0ccfbf
- new version based on Git commit 2e0ccfbf3eff09c310cf3c8cbff3a72e8b41a845
- update project URL

* Sat May 05 2018 Pavel Nakonechnyi <zorg@altlinux.org> 2.1.1-alt2.git298cc28d
- new Git version based on 298cc28d493df7fa71236aac4f2b71d79763a435

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- new version 2.1.1 (with rpmrb script)

* Sun Jul 12 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt2
- fix build

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- new version 2.0.1 (with rpmrb script)

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- initial build for ALT Linux Sisyphus
