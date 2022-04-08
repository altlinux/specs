%define oname sigtools

%def_without check

Name: python3-module-%oname
Version: 2.0.3
Release: alt1

Summary: Python module to manipulate function signatures

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sigtools/

Packager: Python Development Team <python@packages.altlinux.org>

# https://github.com/epsy/sigtools.git
# Source-url: https://pypi.io/packages/source/s/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

Patch: 4838e84cbf5968910f282b41abf53769b34f0c1d.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-unittest python3-module-coverage python3-module-mock
%endif

%py3_provides %oname
%py3_requires six

BuildRequires: python3-module-html5lib python3-module-sphinx

%description
Utilities for working with 3.3's inspect.Signature objects.
The sigtools python library provides:

* Decorators to specify keyword-only parameters, annotations and
  positional-only parameters, even on python2: sigtools.modifiers
* Decorators to specify how *args, **kwargs are handled, in a way that
  can be introspected: sigtools.specifiers
* Function combination routines that preserve signatures:
  sigtools.wrappers
* Functions to manipulate signature objects likewise: sigtools.signatures

%prep
%setup
%patch -p1

%build
%python3_build

%install
%python3_install
rm -rf %buildroot%python3_sitelibdir/sigtools/tests/

%check
python3 setup.py test

%files
%doc *.rst docs/*.rst*
%python3_sitelibdir/*

%changelog
* Wed Apr 06 2022 Grigory Ustinov <grenka@altlinux.org> 2.0.3-alt1
- Build new version.

* Thu Jun 24 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.2-alt3
- drop excessive python3-module-jinja2-tests BR

* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.2-alt2
- Drop python2 support.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- new version 2.0.2 (with rpmrb script)
- switch to build from tarball
- disable check (module repeated-test is missed)
- build python3 module only

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt2.b2.git20150217.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.b2.git20150217.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt2.b2.git20150217
- NMU: added python-module-sphinx to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.b2.git20150217.1
- NMU: Use buildreq for BR.

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b2.git20150217
- Version 0.1b2

* Tue Jan 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b1.git20150111
- Initial build for Sisyphus

