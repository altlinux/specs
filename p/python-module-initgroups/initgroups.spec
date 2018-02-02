%define oname initgroups
Name: python-module-%oname
Version: 2.14.0
Release: alt1.dev0.git20150618.1
Summary: Convenience uid/gid helper function used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/initgroups/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/initgroups.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
initgroups provides a convenience function to deal with user / group ids
on Unix-style systems.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.14.0-alt1.dev0.git20150618.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt1.dev0.git20150618
- Version 2.14.0.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

