%define oname initgroups
Name: python-module-%oname
Version: 2.13.1
Release: alt1.dev.git20130313
Summary: Convenience uid/gid helper function used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/initgroups/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/initgroups.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests

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
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

