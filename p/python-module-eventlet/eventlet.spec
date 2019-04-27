%define _unpackaged_files_terminate_build 1
%define oname eventlet

%def_with check
%def_with docs

Name: python-module-%oname
Version: 0.24.1
Release: alt1
Summary: Highly concurrent networking library
License: MIT
Group: Development/Python
Url: https://pypi.org/project/eventlet/

# https://github.com/eventlet/eventlet.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python2.7(dns)
BuildRequires: python2.7(greenlet)
BuildRequires: python2.7(monotonic)
BuildRequires: python2.7(sphinx)
BuildRequires: python2.7(zmq)
%endif

%if_with check
BuildRequires: python2.7(dns)
BuildRequires: python2.7(enum34)
BuildRequires: python2.7(greenlet)
BuildRequires: python2.7(nose)
BuildRequires: python2.7(json)
BuildRequires: python2.7(monotonic)
BuildRequires: python2.7(zmq)
BuildRequires: python2.7(six)
BuildRequires: python2.7(subprocess32)
BuildRequires: python3(dns)
BuildRequires: python3(greenlet)
BuildRequires: python3(nose)
BuildRequires: python3(monotonic)
BuildRequires: python3(zmq)
BuildRequires: python3(tox)
%endif

%py_requires dns
%py_requires enum34

%add_python_req_skip stackless

%description
Eventlet is a concurrent networking library for Python that allows you
to change how you run your code, not how you write it.

It uses epoll or libevent for highly scalable non-blocking I/O.
Coroutines ensure that the developer uses a blocking style of
programming that is similar to threading, but provide the benefits of
non-blocking I/O. The event dispatch is implicit, which means you can
easily use Eventlet from the Python interpreter, or as a small part of a
larger application.

%package -n python3-module-%oname
Summary: Highly concurrent networking library
Group: Development/Python3

%py3_requires dns
%add_python3_req_skip stackless

%description -n python3-module-%oname
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
%patch -p1

cp -fR . ../python3

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%python_build

pushd ../python3
%python3_build
popd

%if_with docs
%make -C doc pickle
%make -C doc html
%endif

%install
%python_install

pushd ../python3
%python3_install
popd

%if_with docs
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
# raise timeouts
grep -qsrF 'TEST_TIMEOUT =' || exit 1
grep -srlF 'TEST_TIMEOUT =' | xargs \
sed -i 's/TEST_TIMEOUT[[:space:]]*=[[:space:]]*[0-9]\+$/TEST_TIMEOUT = 20/g'
# don't freeze versions
sed -i \
-e '/psycopg2-binary/d' \
-e '/coverage xml -i/d' \
-e '/coverage=/d' \
-e 's/==/>=/g' \
-e  '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/nosetests \{envbindir\}\/nosetests\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/nosetests\
    \/bin\/sed -i \x27s/nosetests-[0-9]\.[0-9]/nosetests/g\x27 \{envbindir\}\/nosetests' tox.ini

export PIP_NO_INDEX=YES
export TOX_TESTENV_PASSENV='RPM_BUILD_DIR'
export TOXENV=py%{python_version_nodots python},\
py%{python_version_nodots python3}-selects,\
py%{python_version_nodots python3}-poll,\
py%{python_version_nodots python3}-epolls

tox.py3 --sitepackages -p auto -o -vr

%files
%doc AUTHORS NEWS README.rst
%python_sitelibdir/eventlet-%version-py%_python_version.egg-info/
%python_sitelibdir/eventlet/
%if_with docs
%exclude %python_sitelibdir/*/pickle

%files docs
%doc examples doc/_build/html

%files pickles
%python_sitelibdir/*/pickle
%endif

%files -n python3-module-%oname
%doc AUTHORS NEWS README.rst
%python3_sitelibdir/eventlet-%version-py%_python3_version.egg-info/
%python3_sitelibdir/eventlet/

%changelog
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

