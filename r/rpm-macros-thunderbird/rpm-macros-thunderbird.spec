%define _unpackaged_files_terminate_build 1

Name: rpm-macros-thunderbird
Version: 0.0.2
Release: alt1

Summary: Set of RPM macros for packaging applications that requires thunderbird
License: GPL-3.0-only
Group: Development/Other
BuildArch: noarch

Source0: thunderbird.macros

%description
%summary.

%install
mkdir -pv %buildroot/%_rpmmacrosdir
install -m644 %SOURCE0 %buildroot/%_rpmmacrosdir/thunderbird

%files
%_rpmmacrosdir/thunderbird

%changelog
* Wed Jan 21 2026 Michael Shigorin <mike@altlinux.org> 0.0.2-alt1
- Added %%e2k.

* Wed Jun 04 2025 Ajrat Makhmutov <rauty@altlinux.org> 0.0.1-alt1
- Initial build.
