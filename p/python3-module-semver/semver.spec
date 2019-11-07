%define oname semver

Name: python3-module-%oname
Summary: Python package to work with Semantic Versioning
Version: 2.9.0
Release: alt1

Group: Development/Python3
License: BSD 3-Clause
Url: https://github.com/python-semver/python-semver
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


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

%files
%doc *.rst LICENSE.txt
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Nov 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.9.0-alt1
- Initial build

