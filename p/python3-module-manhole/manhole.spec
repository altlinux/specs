%define _unpackaged_files_terminate_build 1
%define oname manhole

%def_without docs
%def_without check

Name: python3-module-%oname
Version: 1.6.0
Release: alt5
Summary: Debugging manhole for python applications 
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/manhole/

# https://github.com/ionelmc/python-manhole.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)
BuildRequires: python3(sphinx_py3doc_enhanced_theme)
%endif

%if_with check
BuildRequires: /proc
BuildRequires: /dev/pts
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

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

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

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build_debug

%install
%python3_install

%if_with docs
export PYTHONPATH=$PWD/src
pushd docs
sphinx-build-3 -b pickle -d _build/doctrees . _build/pickle
sphinx-build-3 -b html -d _build/doctrees . _build/html
popd

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
# python uwsgi is not packaged yet
rm tests/wsgi.py
sed -i -e '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    \/bin\/cp {env:_PYTEST_BIN:} \{envbindir\}\/pytest\
    \/bin\/sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/pytest' \
-e '/setenv =/a\
    py%{python_version_nodots python3}: _PYTEST_BIN=%_bindir\/py.test3' \
-e '/pytest-travis-fold/d' \
tox.ini
export PIP_NO_INDEX=YES
export MANHOLE_TEST_TIMEOUT=30
export TOX_TESTENV_PASSENV='MANHOLE_TEST_TIMEOUT'
%define py3_nodot py%{python_version_nodots python3}
export TOXENV=%py3_nodot-normal-normal-nocov
%_bindir/tox.py3 --sitepackages -v

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif


%changelog
* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt5
- s/rpm-macros-sphinx/rpm-macros/sphinx3/

* Tue Feb 04 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.6.0-alt4
- Porting on Python3.

* Thu Aug 08 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt3
- Fixed testing against Pytest 5.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.6.0-alt2
- Added missing dep on Pytest.

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

