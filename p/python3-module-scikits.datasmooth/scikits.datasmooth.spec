%define mname scikits
%define oname %mname.datasmooth

Name: python3-module-%oname
Version: 0.61
Release: alt3

Summary: Scikits data smoothing package
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/scikits.datasmooth/

# https://github.com/jjstickel/scikit-datasmooth.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-numpy
BuildRequires: python3-module-scipy

%py3_provides %oname
%py3_requires %mname numpy scipy cvxopt


%description
This is a scikit intended to include numerical methods for smoothing
data.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
%__python3 setup.py test

%files
%doc *.txt docs/* examples
%python3_sitelibdir/%mname/*
%python3_sitelibdir/*.egg-info


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.61-alt3
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.61-alt2.git20140303.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.61-alt2.git20140303.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.61-alt2.git20140303.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.61-alt2.git20140303.1
- NMU: Use buildreq for BR.

* Sun Apr 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.61-alt2.git20140303
- Rebuilt with updated NumPy

* Sat Mar 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.61-alt1.git20140303
- Initial build for Sisyphus

