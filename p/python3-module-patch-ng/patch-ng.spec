# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define oname patch-ng

Name: python3-module-%oname
Version: 1.18.1
Release: alt1

Summary: Library to parse and apply unified diffs

License: MIT
Group: Development/Python3
URL: https://github.com/conan-io/python-patch-ng
VCS: https://github.com/conan-io/python-patch-ng

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-intro >= 2.2.4
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Library to parse and apply unified diffs.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%python3_sitelibdir/patch_ng.py
%python3_sitelibdir/patch_ng-%version.dist-info
%python3_sitelibdir/__pycache__/*

%changelog
* Sat Aug 30 2025 Anton Midyukov <antohami@altlinux.org> 1.18.1-alt1
- new version (1.18.1) with rpmgs script

* Sun Nov 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1.17.4-alt1
- new version 1.17.4 (with rpmrb script)
- build from tarball

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.17.1-alt1
- Initial build

