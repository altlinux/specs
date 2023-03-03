%define oname fanstatic

%def_with check

Name: python3-module-%oname
Version: 1.3
Release: alt1
Summary: Flexible static resources for web applications
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/fanstatic/
VCS: https://github.com/fanstatic/fanstatic/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
%if_with check
BuildRequires: python3-module-webob
%endif

%description
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

%package docs
Summary: Documentation for fanstatic
Group: Development/Documentation

%description docs
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains documentation for fanstatic.

%package pickles
Summary: Pickles for fanstatic
Group: Development/Python3

%description pickles
Fanstatic is a smart static resource publisher for Python. For more
information on what it's about and how to use it, see:
http://fanstatic.org

This package contains pickles for fanstatic.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build

%install
%python3_install

%check
%tox_check -- -k "not test_library_registry"

export PYTHONPATH=%buildroot%python3_sitelibdir
%make SPHINXBUILD=sphinx-build-3 -C doc html
%make SPHINXBUILD=sphinx-build-3 -C doc pickle

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/fanstatic/

%files
%doc LICENSE.txt *.rst
%_bindir/fanstatic-compile
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/*/pickle

%changelog
* Fri Mar 03 2023 Anton Vyatkin <toni@altlinux.org> 1.3-alt1
- new version 1.3

* Mon Jun 07 2021 Grigory Ustinov <grenka@altlinux.org> 1.0-alt3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2.a5.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.a5.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0-alt2.a5.1
- NMU: Use buildreq for BR.

* Sun Feb 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2.a5
- Added necessary requirements

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a5
- Version 1.0a5

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a4
- Version 1.0a4

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a3
- Version 1.0a3

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.16-alt1.1
- Rebuild with Python-3.3

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16-alt1
- Version 0.16
- Added docs and pickles

* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.4-alt1
- Version 0.11.4
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.3-alt1
- Version 0.11.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.11.2-alt1.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1
- Initial build for Sisyphus

