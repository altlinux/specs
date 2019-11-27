%define oname zc.parse_addr

Name: python3-module-%oname
Version: 1.0.0
Release: alt2

Summary: Parse network addresses of the form: HOST:PORT
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/zc.parse_addr/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires zc


%description
Parse network addresses of the form: HOST:PORT.

%prep
%setup

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
%doc PKG-INFO
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info


%changelog
* Wed Nov 27 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

