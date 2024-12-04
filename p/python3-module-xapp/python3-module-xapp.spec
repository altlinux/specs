# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define oname xapp

Name: python3-module-%oname
Version: 2.4.2
Release: alt2

Summary: Python Xapp Library

License: LGPL-2.0
Group: Development/Python
Url: https://github.com/linuxmint/python-xapp

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 rpm-build-gir
BuildRequires: meson

%description
%summary.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%python3_sitelibdir/%oname/

%changelog
* Mon Dec 02 2024 Anton Midyukov <antohami@altlinux.org> 2.4.2-alt2
- build from git tag

* Sat Jun 08 2024 Anton Midyukov <antohami@altlinux.org> 2.4.2-alt1
- New version

* Fri Dec 01 2023 Anton Midyukov <antohami@altlinux.org> 2.4.1-alt1
- New version

* Fri Nov 18 2022 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- New version

* Fri Jun 10 2022 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- New version

* Wed Jun 16 2021 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- New version

* Fri May 28 2021 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- New version

* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- New version

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- New version

* Mon Dec 2 2019 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt2
- Add rpm-build-gir to build requires

* Mon Dec 2 2019 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- New version

* Tue Nov 19 2019 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- New version
- Remove Python 2 subpackage

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 1.6.0-alt1
- New version

* Thu Nov 1 2018 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- New version

* Thu Jun 29 2017 Vladimir Didenko <cow@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
