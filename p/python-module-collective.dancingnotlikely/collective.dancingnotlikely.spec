%define mname collective
%define oname %mname.dancingnotlikely
Name: python-module-%oname
Version: 1.0.3
Release: alt1.dev0.git20141205
Summary: A plugin that add more elements to ignore-list in the composer
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dancingnotlikely/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/collective.dancingnotlikely.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-unittest2 python-module-argparse
BuildPreReq: python-module-collective.dancing

%py_provides %oname
%py_requires collective.dancing

%description
This product patches the elements that shouldn't been show in newsletter
with Singing and Dancing.

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
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.dev0.git20141205
- Initial build for Sisyphus

