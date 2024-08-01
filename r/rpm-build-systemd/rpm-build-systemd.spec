%define oname systemd

Name: rpm-build-%oname
Version: 6
Release: alt2

Summary: RPM helper macros to build packages with systemd support
License: LGPL-2.1-or-later
Group: Development/Other
BuildArch: noarch
Source1: systemd.macros
Requires: rpm-macros-%oname >= %EVR
Requires: libsystemd-devel

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
* Thu Aug 01 2024 Alexey Shabalin <shaba@altlinux.org> 6-alt2
- fixed %%systemd_post_with_restart.

* Thu Jun 20 2024 Alexey Shabalin <shaba@altlinux.org> 6-alt1
- add all macros with systemd path.

* Thu May 25 2023 Alexey Gladkov <legion@altlinux.ru> 5-alt4
- Hide systemd-specific utilities to avoid adding a dependency on systemd.

* Mon Oct 18 2021 Alexey Shabalin <shaba@altlinux.org> 5-alt3
- Fixed typo in bash script.

* Mon Oct 18 2021 Alexey Shabalin <shaba@altlinux.org> 5-alt2
- Drop requires on systemd from package with macros

* Mon Oct 11 2021 Alexey Shabalin <shaba@altlinux.org> 5-alt1
- Rename macros post_systemd_restart_later to post_systemd_postponed

* Sun Sep 05 2021 Alexey Shabalin <shaba@altlinux.org> 4-alt1
- Fixed %%post_systemd_restart_later macros.

* Thu Sep 02 2021 Alexey Shabalin <shaba@altlinux.org> 3-alt1
- Used systemd-update-helper in macroses.

* Fri Aug 27 2021 Alexey Shabalin <shaba@altlinux.org> 2-alt2
- Fixed rpm changelog for 2-alt1.

* Thu Aug 26 2021 Alexey Shabalin <shaba@altlinux.org> 2-alt1
- Added macroses:
  %%post_systemd, %%preun_systemd, %%post_systemd_restart_later

* Mon Aug 23 2021 Alexey Shabalin <shaba@altlinux.org> 1-alt1
- Initial build.

