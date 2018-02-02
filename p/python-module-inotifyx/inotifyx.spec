%define oname inotifyx
Name: python-module-%oname
Version: 0.2.2
Release: alt1.bzr20140825.1
Summary: Simple Linux inotify bindings
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/inotifyx/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:inotifyx
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
inotifyx is a simple Python binding to the Linux inotify file system
event monitoring API.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc AUTHORS NEWS README
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.2-alt1.bzr20140825.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.bzr20140825
- Initial build for Sisyphus

