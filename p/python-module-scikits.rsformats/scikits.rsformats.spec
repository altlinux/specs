# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt2.1.1.1
%define mname scikits
%define oname %mname.rsformats

%def_with python3

Name: python-module-%oname
Epoch: 1
Version: 0.1
#Release: alt2.1
Summary: Tools for reading remote sensing formats
License: BSD
Group: Development/Python
Url: http://scikits.scipy.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# from git://git.altlinux.org/people/real/packages/scikits.git
# which from http://svn.scipy.org/svn/scikits/trunk (don't work now)
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pyparsing libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pyparsing libnumpy-py3-devel
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires %mname pyparsing numpy

%description
This package provides tools for reading remote sensing formats.

%package -n python3-module-%oname
Summary: Tools for reading remote sensing formats
Group: Development/Python3
%py3_provides %oname
%py3_requires %mname pyparsing numpy

%description -n python3-module-%oname
This package provides tools for reading remote sensing formats.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc scikits/rsformats/examples
%python_sitelibdir/%mname/rsformats
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc scikits/rsformats/examples
%python3_sitelibdir/%mname/rsformats
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1:0.1-alt2.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1-alt2.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:0.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Apr 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1-alt2
- Rebuilt with updated NumPy

* Sun Mar 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.1-alt1
- Initial build for Sisyphus

