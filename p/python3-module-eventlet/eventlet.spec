%define oname eventlet

%ifnarch armh
%def_with check
%else
%def_without check
%endif

%def_without docs

Name: python3-module-%oname
Version: 0.37.0
Release: alt1

Summary: Highly concurrent networking library
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/eventlet/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

Requires: python3-module-dns
Requires: python3-module-greenlet

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
BuildRequires: python3-module-hatch-vcs
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-six
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-dns
%endif
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-dns
BuildRequires: python3-module-psycopg2
BuildRequires: python3-module-zmq
%endif

%add_python3_req_skip stackless

# required by strange pylib.py:
%add_python3_req_skip py.magic

%description
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

%if_with docs
%package pickles
Summary: Pickles for Eventlet
Group: Development/Python

%description pickles
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

This package contains pickles for Eventlet.

%package docs
Summary: Documentation for Eventlet
Group: Development/Documentation
BuildArch: noarch

%description docs
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

This package contains documentation for Eventlet.
%endif

%prep
%setup

# requires thrift, python 2.7 only
rm -rv eventlet/zipkin

# remove obsoleted tsafe (ALT bug 45443)
rm -v eventlet/green/OpenSSL/tsafe.py

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv doc/
%endif

%build
%pyproject_build

%install
%pyproject_install

%if_with docs
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc html SPHINXBUILD=sphinx-build-3
%endif

%check
%pyproject_run_pytest -v -k "\
not test_dns_methods_are_green \
and not test_noraise_dns_tcp \
and not test_clear \
and not test_raise_dns_tcp"

%files
%doc AUTHORS NEWS README.rst
%python3_sitelibdir/eventlet-%version.dist-info
%python3_sitelibdir/eventlet/

%if_with doc
%files docs
%doc examples doc/_build/html
%endif

%changelog
* Thu Sep 12 2024 Anton Vyatkin <toni@altlinux.org> 0.37.0-alt1
- new version 0.37.0

* Sat Apr 13 2024 Anton Vyatkin <toni@altlinux.org> 0.36.1-alt1
- new version 0.36.1

* Fri Feb 23 2024 Anton Vyatkin <toni@altlinux.org> 0.35.2-alt1
- new version 0.35.2

* Wed Jan 31 2024 Anton Vyatkin <toni@altlinux.org> 0.35.1-alt1
- new version 0.35.1

* Wed Jan 24 2024 Anton Vyatkin <toni@altlinux.org> 0.35.0-alt1
- new version 0.35.0

* Mon Jan 22 2024 Anton Vyatkin <toni@altlinux.org> 0.34.3-alt1
- new version 0.34.3

* Fri Dec 29 2023 Anton Vyatkin <toni@altlinux.org> 0.34.2-alt1
- new version 0.34.2

* Fri Oct 13 2023 Anton Vyatkin <toni@altlinux.org> 0.33.3-alt3
- Dropped dependency on distutils.

* Wed Apr 12 2023 Anton Vyatkin <toni@altlinux.org> 0.33.3-alt2
- Fix BuildRequires

* Fri Mar 17 2023 Vitaly Lipatov <lav@altlinux.ru> 0.33.3-alt1
- new version 0.33.3 (with rpmrb script)
- remove obsoleted OpenSSL.tsafe using (ALT bug 45443)

* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 0.33.1-alt1
- new version 0.33.1 (with rpmrb script)

* Sat Feb 12 2022 Anton Midyukov <antohami@altlinux.org> 0.33.0-alt1
- new version (0.33.0) with rpmgs script
- enable check

* Fri Nov 13 2020 Vitaly Lipatov <lav@altlinux.ru> 0.29.1-alt2
- make docs (tests still be disabled due python2 reqs)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.29.1-alt1
- new version 0.29.1 (with rpmrb script)
- update buildrequires

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 0.25.1-alt3
- build python3 package separately, cleanup spec

* Fri Oct 09 2020 Igor Vlasenko <viy@altlinux.ru> 0.25.1-alt2
- NMU: removed deprecated python2 zipkin due to thrift dependency

* Tue Jun 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.25.1-alt1
- Automatically updated to 0.25.1.
- Build without check (for openstack update).

* Fri Apr 26 2019 Stanislav Levin <slev@altlinux.org> 0.24.1-alt1
- 0.18.4 -> 0.24.1.
- Enabled testing.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.18.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.18.4-alt1
- 0.18.4

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.17.4-alt1.git20150722.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.17.4-alt1.git20150722.1
- NMU: Use buildreq for BR.

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.4-alt1.git20150722
- Version 0.17.4

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17.1-alt1.git20150225
- Version 0.17.1

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.1-alt1.git20150114
- Version 0.16.1

* Tue Dec 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.git20141230
- Version 0.16.0
- Added module for Python 3

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.16.0-alt1.dev.git20141106
- Version 0.16.0.dev

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15.0-alt1
- Version 0.15.0

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.1-alt1
- Version 0.12.1

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.16-alt1
- Initial build for Sisyphus

