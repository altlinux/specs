%define _unpackaged_files_terminate_build 1
%define oname manhole

%def_with docs
%def_with check

Name: python-module-%oname
Version: 1.6.0
Release: alt1
Summary: Debugging manhole for python applications 
License: BSD
Group: Development/Python
Url: https://pypi.org/project/manhole/

# https://github.com/ionelmc/python-manhole.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python2.7(sphinx)
BuildRequires: python2.7(sphinx_rtd_theme)
BuildRequires: python2.7(sphinx_py3doc_enhanced_theme)
%endif

%if_with check
BuildRequires: /proc
BuildRequires: /dev/pts
BuildRequires: python2.7(process_tests)
BuildRequires: python2.7(requests)
BuildRequires: python2.7(subprocess32)
BuildRequires: python3(process_tests)
BuildRequires: python3(requests)
BuildRequires: python3(tox)
%endif

%description
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

%package -n python3-module-%oname
Summary: Debugging manhole for python applications 
Group: Development/Python3

%description -n python3-module-%oname
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Manhole is in-process service that will accept unix domain socket
connections and present the stacktraces for all threads and an
interactive prompt. It can either work as a python daemon thread waiting
for connections at all times or a signal handler (stopping your
application and waiting for a connection).

Access to the socket is restricted to the application's effective user
id or root.

This package contains documentation for %oname.
%endif

%prep
%setup
%patch -p1

cp -fR . ../python3

%if_with docs
%prepare_sphinx .
ln -s ../objects.inv docs/
%endif

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%python_install

%if_with docs
export PYTHONPATH=$PWD/src
pushd docs
sphinx-build -b pickle -d _build/doctrees . _build/pickle
sphinx-build -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

%check
# python uwsgi is not packaged yet
rm tests/wsgi.py
sed -i -e '/\[testenv\]/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp %_bindir\/py.test3 \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
-e '/pytest-travis-fold/d' \
tox.ini
export PIP_NO_INDEX=YES
export MANHOLE_TEST_TIMEOUT=30
export TOX_TESTENV_PASSENV='MANHOLE_TEST_TIMEOUT'
%define py_nodot py%{python_version_nodots python}
%define py3_nodot py%{python_version_nodots python3}
export TOXENV=%py_nodot-normal-normal-nocov,%py3_nodot-normal-normal-nocov
%_bindir/tox.py3 --sitepackages -p auto -o -v

%files
%doc *.rst
%_bindir/*
%exclude %_bindir/*.py3
%python_sitelibdir/*
%if_with docs
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%files -n python3-module-%oname
%doc *.rst
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
* Mon Feb 18 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1
- 1.0.0 -> 1.6.0.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.0-alt2.git20150419.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt2.git20150419.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt2.git20150419.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt2.git20150419
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20150419
- New snapshot

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141223
- Initial build for Sisyphus

