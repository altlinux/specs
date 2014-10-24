%define oname ez_setup
Name: python3-module-%oname
Version: 0.1
Release: alt1.dev.git20101122
Summary: ez_setup.py and distribute_setup.py
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/ez_setup/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ActiveState/ez_setup.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests

%py3_provides %oname

%description
ez_setup.py and distribute_setup.py.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.dev.git20101122
- Initial build for Sisyphus

