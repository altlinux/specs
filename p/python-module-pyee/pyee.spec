%define oname pyee
Name: python-module-%oname
Version: 0.0.8
Release: alt1.git20130806.1
Summary: A port of node.js's EventEmitter to python
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyee/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jesusabdullah/pyee.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-nose

%py_provides %oname

%description
pyee supplies an event_emitter object that acts similar to the
EventEmitter that comes with node.js.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
%make tests

%files
%doc *.rst
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.8-alt1.git20130806.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1.git20130806
- Initial build for Sisyphus

