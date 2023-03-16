Name: conmon
Version: 2.1.7
Release: alt1
# due to typo in version :(
Epoch: 1

Summary: OCI container runtime monitor
License: Apache-2.0
Group: System/Configuration/Other

Url: https://github.com/containers/conmon
Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires: go-md2man
BuildRequires: glibc-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(libseccomp) >= 2.5.2

%description
%summary.

%prep
%setup
%patch -p1

%build
export GIT_COMMIT=%release
%make_build CFLAGS+="%(getconf LFS_CFLAGS) -Wno-error=deprecated-declarations"

%install
%makeinstall_std PREFIX=%_usr

%files
%doc README.md
%_bindir/conmon
%_man8dir/conmon.*

%changelog
* Thu Mar 16 2023 Alexey Shabalin <shaba@altlinux.org> 1:2.1.7-alt1
- New version 2.1.7.

* Tue Jan 10 2023 Alexey Shabalin <shaba@altlinux.org> 1:2.1.5-alt1
- new version 2.1.5

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.4-alt1
- new version 2.1.4

* Wed Jun 15 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.2-alt1
- new version 2.1.2

* Fri Jun 03 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.1-alt1
- new version 2.1.1

* Fri Apr 08 2022 Alexey Shabalin <shaba@altlinux.org> 1:2.1.0-alt1
- new version 2.1.0

* Thu Dec 09 2021 Alexey Shabalin <shaba@altlinux.org> 1:2.0.31-alt1
- new version 2.0.31

* Sat Nov 06 2021 Alexey Shabalin <shaba@altlinux.org> 1:2.0.30-alt1
- new version 2.0.30
- build with seccomp support

* Thu Apr 22 2021 Alexey Shabalin <shaba@altlinux.org> 1:2.0.27-alt1
- new version 2.0.27

* Thu Sep 10 2020 Alexey Shabalin <shaba@altlinux.org> 1:2.0.21-alt1
- new version 2.0.21

* Thu Jul 09 2020 Michael Shigorin <mike@altlinux.org> 1:2.0.18-alt2
- E2K: ftbfs workaround (might be the new glib2)
- i586: LFS fix (thx aris@ either)
- minor spec cleanup

* Thu Jun 18 2020 Alexey Shabalin <shaba@altlinux.org> 1:2.0.18-alt1
- new version 2.0.18

* Fri May 15 2020 Alexey Shabalin <shaba@altlinux.org> 1:2.0.16-alt1
- new version 2.0.16

* Tue Apr 21 2020 Mikhail Gordeev <obirvalger@altlinux.org> 1:2.0.15-alt1
- Update to 2.0.15

* Fri Sep 20 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.1-alt1
- Update to 2.1

* Tue Jan 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0-alt1.8fba2062.1
- Initial build for Sisyphus
