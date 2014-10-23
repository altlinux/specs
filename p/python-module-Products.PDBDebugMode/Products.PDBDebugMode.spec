%define oname Products.PDBDebugMode
Name: python-module-%oname
Version: 1.3.1
Release: alt1.git20110724
Summary: Post-mortem debugging on Zope 2 excpetions
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PDBDebugMode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PDBDebugMode.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-ipdb

%py_provides %oname
Requires: python-module-Zope2
%py_requires collective.monkeypatcher

%description
Enable various PDB debugging when debug-mode=on

When Zope is running in debug mode this product hooks PDB debugging into
various parts of a Zope instance. Some additional Plone specific hooks
are also included.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc Products/PDBDebugMode/README.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20110724
- Initial build for Sisyphus

