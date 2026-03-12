%define _unpackaged_files_terminate_build 1

Name: rpm-macros-ml
Version: 1.0
Release: alt1

Summary: RPM macros to package software that depends on ML frameworks
License: GPL-3.0-only
Group: Development/Other
BuildArch: noarch

Source0: ml.macros

%description
%summary.

%install
install -pD -m644 %SOURCE0 %buildroot/%_rpmmacrosdir/ml

%files
%_rpmmacrosdir/ml

%changelog
* Thu Feb 26 2026 Nikita Shmatko <nash@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
