%define oname aiohttp

%def_with python3
# def_with docs needed package python3-modile-sphinxcontrib-blockdiag (missing in Sisyphus)
%def_without docs
%def_without check

Name: python3-module-%oname
Version: 3.8.3
Release: alt1
Summary: http client/server for asyncio
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/KeepSafe/aiohttp.git
Source: %name-%version.tar
# submodule part from pypi archive with pregenerated c sources
Source1: llhttp.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(wheel)
BuildRequires: python3-devel python3-module-setuptools python3-module-Cython
BuildRequires: python3-module-multidict
%if_with check
BuildRequires: python3-module-yarl python3-module-async-timeout python3-module-pytest-mock
%endif
%if_with docs
BuildRequires(pre): python3-module-sphinx-devel
BuildRequires: python3-module-sphinxcontrib-asyncio python3-module-sphinxcontrib-newsfeed
%endif

# conditional imports
%py3_requires charset_normalizer idna_ssl

%description
http client/server for asyncio (PEP-3156).

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
http client/server for asyncio (PEP-3156).

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
http client/server for asyncio (PEP-3156).

This package contains documentation for %oname.

%prep
%setup -a1
# gen.py expects to find .git in project root, cheat a bit
sed -i 's,".git",".gitmodules",' tools/gen.py
# use system cython
sed -i '/^cythonize:/ s,.install-cython,,' Makefile
find tools -type f -name \*.py | xargs sed -ri '/env python$/ s,$,3,'
%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
make cythonize
%pyproject_build

%if_with docs
%make_build -C docs html SPHINXBUILD=py3_sphinx-build
%endif

%install
%pyproject_install

%if_with check
%check
python3 setup.py test
%endif

%if_with docs
%files docs
%doc docs/_build/html/*
%endif

%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/*test*
%exclude %python3_sitelibdir/%oname/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/*test*
%python3_sitelibdir/%oname/*/*test*

%changelog
* Mon Jan 02 2023 Anton Midyukov <antohami@altlinux.org> 3.8.3-alt1
- new version 3.8.3

* Fri Feb 11 2022 Stanislav Levin <slev@altlinux.org> 3.8.1-alt2
- Added missing mandatory runtime dependency on charset_normalizer.

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.8.1-alt1
- 3.8.1 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.4-alt1
- 3.7.4 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.3-alt1
- 3.7.3 released

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.7.1-alt1
- 3.7.1 released

* Sun May 10 2020 Anton Midyukov <antohami@altlinux.org> 3.6.2-alt1
- 3.6.2 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.6.1-alt1
- 3.6.1 released

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 3.5.4-alt1
- New version 3.5.4
- Disable check
- Cleanup spec

* Thu Mar 14 2019 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt2
- Added py3_requires chardet (Closes: 36270)
- Cleanup spec

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.5-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.2.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt1
- New version 2.2.5

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.5-alt2
- Updated build dependencies.

* Thu May 04 2017 Anton Midyukov <antohami@altlinux.org> 1.3.5-alt1
- New version 1.3.5

* Fri Jan 13 2017 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- New version 1.2.0
- Disabled build documentation

* Sun Aug 07 2016 Anton Midyukov <antohami@altlinux.org> 0.21.5-alt1
- New version 0.21.5 (Closes: 32363)
- Disable tests (girar not support IPv6)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz at altlinux.org> 0.15.3-alt7.git20150425.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Mar  5 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt7.git20150425
- (.spec) cleanup unneeded BuildRequires(pre): rpm-macros-sphinx
  (and other BuildReq cleanups)

* Fri Mar 04 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt6.git20150425
- Removed dependence to python-module-gunicorn, which created selfdeps.

* Thu Mar  3 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.15.3-alt5.git20150425
- (.spec) Safer build: cleanup ../python3/ before use.
  (Nevertheless, beware: using ../python3/ for the build is very dirty
  because it is not cleaned up automatically afterwards and can cause
  side-effects in other unsafe specs, similar to this one. This dirty
  use of ../python3/ is very wide-spread in Sisyphus packages.)
- (.spec) Fail if the maintainer's intentions are not fulfilled
  (because the sources or the build environment have changed since the
  spec was written): rm/cp without -f

* Thu Mar 03 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt4.git20150425.2
- Remove self dependence.

* Wed Mar 02 2016 Denis Medvedev <nbr@altlinux.org>  0.15.3-alt3.git20150425.2
- File "inv"  for sphynx is in python-sphinx-objects.inv. 

* Mon Feb 08 2016 Denis Medvedev <nbr@altlinux.org> 0.15.3-alt2.git20150425.2
- NMU: manual build

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 0.15.3-alt2.git20150425.1
- NMU: Use buildreq for BR.

* Fri Jan 29 2016 Sergey Alembekov <rt@altlinux.ru> 0.15.3-alt2.git20150425
- rebuild with cleaned build requires

* Mon Apr 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.3-alt1.git20150425
- Version 0.15.3

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.4-alt1.git20150217
- Version 0.14.4

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.2-alt1.git20150123
- Version 0.14.2

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt2.git20141231
- Version 0.13.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.1-alt1.a0.git20141229
- Version 0.13.1a0

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.0-alt1.git20141129
- Version 0.11.0

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.3-alt1.a.git20141125
- Initial build for Sisyphus

