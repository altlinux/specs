%define oname sphinx-settings
Name: python3-module-%oname
Version: 0.1.1
Release: alt1.git20141130.1.1
Summary: Class-based settings for Sphinx
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sphinx-settings/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/respect31/sphinx-settings.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-sphinx python3-module-sugarbowl
BuildPreReq: python3-module-nose python3-module-coverage

%py3_provides sphinx_settings
%py3_requires sphinx sugarbowl

%description
Class-based settings for Sphinx.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.git20141130.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20141130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141130
- Initial build for Sisyphus

