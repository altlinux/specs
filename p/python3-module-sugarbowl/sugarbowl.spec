%define oname sugarbowl
Name: python3-module-%oname
Version: 0.52.1
Release: alt1.git20141130
Summary: Sugarbowl provides cachedproperty, import_object and more
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sugarbowl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sugarbowl/sugarbowl.py.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-coverage

%description
Sugarbowl provides cachedproperty, import_object and more.

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
* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.52.1-alt1.git20141130
- Initial build for Sisyphus

