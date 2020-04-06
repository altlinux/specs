%define oname js.d3

Name: python3-module-%oname
Version: 3.4.14
Release: alt2
Summary: Fanstatic package for D3.js
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/js.d3/

# https://github.com/mgood/js.d3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-fanstatic

%py3_provides %oname
%py3_requires js

%description
Fanstatic package for D3.js.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

cp -fR js/d3/resources %buildroot%python3_sitelibdir/js/d3/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/js/*
%python3_sitelibdir/*.egg-info

%changelog
* Mon Apr 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.4.14-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.4.14-alt1.dev0.git20141112.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.14-alt1.dev0.git20141112.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.4.14-alt1.dev0.git20141112.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.4.14-alt1.dev0.git20141112.1
- NMU: Use buildreq for BR.

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.14-alt1.dev0.git20141112
- Version 3.4.14.dev0

* Tue Nov 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.13-alt1.git20140104
- Initial build for Sisyphus

