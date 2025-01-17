%define oname compsize

Name: btrfs-compsize
Version: 1.5
Release: alt2.gitd79eacf

Summary: Utility for measuring compression ratio of files on btrfs
License: GPLv2+
Group: File tools

Url: https://github.com/kilobyte/compsize

Source: %name-%version.tar

BuildRequires: libbtrfs-devel

%description
compsize takes a list of files (given as arguments) on a btrfs filesystem and
measures used compression types and effective compression ratio, producing
a report.

%prep
%setup

%build
%make_build

%install
%makeinstall_std

%files
%doc README.md
%_bindir/%oname
%_man8dir/%oname.8*

%changelog
* Sat Jan 18 2025 Andrey Limachko <liannnix@altlinux.org> 1.5-alt2.gitd79eacf
- Resurrected in sisyphus from removed packages

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- initial build for ALT Sisyphus
