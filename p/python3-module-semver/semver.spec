%define oname semver
%def_with check

Name: python3-module-%oname
Version: 2.13.0
Release: alt1

Summary: Python package to work with Semantic Versioning

Group: Development/Python3
License: BSD 3-Clause
Url: https://pypi.org/project/semver/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python3-module-pytest-cov

%if_with check
%py3_buildrequires tox
%endif

Requires: python3 >= 3.6

%description
A Python module for semantic versioning. Simplifies comparing versions.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install
%python3_prune

%check
py.test3 -v .

%files
%doc *.rst LICENSE.txt
%_bindir/*
%python3_sitelibdir/*


%changelog
* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.13.0-alt1
- new version 2.13.0 (with rpmrb script)

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt2
- cleanup spec, enable tests

* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt1
- Initial build
