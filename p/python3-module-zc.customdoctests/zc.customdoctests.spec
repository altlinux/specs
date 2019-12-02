%define oname zc.customdoctests

Name: python3-module-%oname
Version: 1.0.2
Release: alt2

Summary: Leverage doctest / manuel hooks to support other languages, such as JavaScript
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/zc.customdoctests/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/zc.customdoctests.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
%py3_requires zc manuel.testing zope.testing

BuildRequires: python3-module-manuel python3-module-zope.testing


%description
doctest (and recently manuel) provide hooks for using custom doctest
parsers. zc.customdoctests helps to leverage this to support other
languages, such as JavaScript.

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
%doc *.txt
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info


%changelog
* Mon Dec 02 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt1.dev0.git20140409.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20140409.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.dev0.git20140409.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.dev0.git20140409.1
- NMU: Use buildreq for BR.

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.dev0.git20140409
- Initial build for Sisyphus

