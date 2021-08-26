%define oname systemd

Name: rpm-build-%oname
Version: 2
Release: alt1

Summary: RPM helper macros to build packages with systemd support
License: LGPL-2.1-or-later
Group: Development/Other
BuildArch: noarch
Source1: systemd.macros
Requires: rpm-macros-%oname >= %EVR
Requires: systemd-utils >= 1:248 udev libsystemd-devel

%description
%summary.

%package -n rpm-macros-%oname
Group: Development/Other
BuildArch: noarch
Summary: Macros that define paths and scriptlets related to systemd

%description -n rpm-macros-%oname
%summary.

%prep

%build
%install
mkdir -p %buildroot%_rpmmacrosdir
install -D -m644 %SOURCE1 -p %buildroot%_rpmmacrosdir/%oname

%files
%files -n rpm-macros-%oname
%_rpmmacrosdir/*

%changelog
* Thu Aug 26 2021 Alexey Shabalin <shaba@altlinux.org> 2-alt1
- Added macroses:
  %post_systemd, %preun_systemd, %post_systemd_restart_late

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 1-alt1
- Initial build.

