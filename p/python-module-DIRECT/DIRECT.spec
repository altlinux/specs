%define oname DIRECT

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt1

Summary: Python wrapper to the DIRECT algorithm
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/DIRECT

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%setup_python_module %oname

Source: %name-%version.tar

BuildPreReq: python-devel python-module-sphinx-devel libnumpy-devel
BuildPreReq: gcc-fortran
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel libnumpy-py3-devel
BuildPreReq: python-tools-2to3
%endif

%description
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

%package pickles
Summary: Pickles for DIRECT
Group: Development/Python

%description pickles
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

This package contains pickles for DIRECT.

%package docs
Summary: Documentation for DIRECT
Group: Development/Documentation
BuildArch: noarch

%description docs
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.

This package contains documentation for DIRECT.

%if_with python3
%package -n python3-module-%oname
Summary: Python wrapper to the DIRECT algorithm
Group: Development/Python3

%description -n python3-module-%oname
DIRECT is a method to solve global bound constraint optimization
problems and was originally developed by D. R. Jones, C. D. Perttunen
and B. E. Stuckmann.

The DIRECT package uses the fortan implementation of DIRECT written by
Joerg.M.Gablonsky, DIRECT Version 2.0.4.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
#find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
#find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%prepare_sphinx doc
ln -s ../objects.inv doc/source/

%build
%add_optflags %optflags_shared
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C doc pickle
%make -C doc html

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

