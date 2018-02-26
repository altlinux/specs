%define oname greenlet

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt1.hg20111215
Summary: Lightweight in-process concurrent programming
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/greenlet
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://bitbucket.org/ambroff/greenlet
Source: %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of
micro- thread with no implicit scheduling; coroutines, in other words.
This is useful when you want to control exactly when your code runs. You
can build custom scheduled micro-threads on top of greenlet; however, it
seems that greenlets are useful on their own as a way to make advanced
control flow structures. For example, we can recreate generators; the
difference with Python's own generators is that our generators can call
nested functions and the nested functions can yield values too.
Additionally, you don't need a "yield" keyword. See the example in
tests/test_generator.py.

Greenlets are provided as a C extension module for the regular
unmodified interpreter.

%if_with python3
%package -n python3-module-%oname
Summary: Lightweight in-process concurrent programming (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of
micro- thread with no implicit scheduling; coroutines, in other words.
This is useful when you want to control exactly when your code runs. You
can build custom scheduled micro-threads on top of greenlet; however, it
seems that greenlets are useful on their own as a way to make advanced
control flow structures. For example, we can recreate generators; the
difference with Python's own generators is that our generators can call
nested functions and the nested functions can yield values too.
Additionally, you don't need a "yield" keyword. See the example in
tests/test_generator.py.

Greenlets are provided as a C extension module for the regular
unmodified interpreter.
%endif

%package tests
Summary: Tests for greenlet
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description tests
The greenlet package is a spin-off of Stackless, a version of CPython
that supports micro-threads called "tasklets". Tasklets run
pseudo-concurrently (typically in a single or a few OS-level threads)
and are synchronized with data exchanges on "channels".

This package contains tests for greenlet.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
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

%files
%doc AUTHORS LICENSE NEWS README doc/greenlet.txt
%python_sitelibdir/*
%_includedir/python%_python_version/greenlet

%files tests
%doc tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS LICENSE NEWS README doc/greenlet.txt
%python3_sitelibdir/*
%_includedir/python%{_python3_version}mu/greenlet
%endif

%changelog
* Mon Jun 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.hg20111215
- Version 0.3.2
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.hg20110903.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20110903
- New snapshot

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.hg20110326.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20110326
- New snapshot

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20100606.1
- Rebuilt for debuginfo

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.hg20100606
- Initial build for Sisyphus (ALT #23646)

