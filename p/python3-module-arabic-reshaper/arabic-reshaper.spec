%define  modulename arabic-reshaper

%def_with check

Name:    python3-module-%modulename
Version: 3.0.0
Release: alt1

Summary: Python module for formatting Arabic sentences

License: MIT
Group:   Development/Python3
URL:     https://github.com/mpcabd/python-arabic-reshaper

Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-future
%endif

BuildArch: noarch

%description
A module for reconstructing Arabic sentences that are to be used in
applications that do not support Arabic.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%python3_sitelibdir/arabic_reshaper
%python3_sitelibdir/arabic_reshaper-%version.dist-info

%changelog
* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

* Thu Sep 22 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.4-alt1
- Automatically updated to 2.1.4.
- Build with check.

* Mon Jun 27 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt1
- Initial build for Sisyphus.
