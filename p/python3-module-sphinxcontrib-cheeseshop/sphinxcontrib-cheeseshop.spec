%define mname sphinxcontrib
%define oname %mname-cheeseshop

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: Sphinx extension cheeseshop
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinxcontrib-cheeseshop/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %mname.cheeseshop
%py3_requires %mname


%description
This extension adds directives for easy linking to Cheese Shop (Python
Package Index) packages.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|file|open|' setup.py

%build
%python3_build_debug

%install
%python3_install

%files
%doc README
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- python2 -> python3

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt1.2
- (NMU) rebuild with python3.6

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

