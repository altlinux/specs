%define mname ecreall.helpers
%define oname %mname.upgrade
Name: python-module-%oname
Version: 1.3
Release: alt1.dev0.git20140203
Summary: Adapter tool with helpers for upgrade often used at ecreall
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ecreall.helpers.upgrade/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tdesvenain/ecreall.helpers.upgrade.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests

%py_provides %oname
%py_requires %mname

%description
A set of helpful helpers for upgrade steps.

IUpgradeTool adapts a plone site, a site setup tool or a directory
import context, and provides method to make common upgrade configuration
and data upgrades.

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
%doc *.txt docs/*
%python_sitelibdir/ecreall/helpers/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.dev0.git20140203
- Initial build for Sisyphus

