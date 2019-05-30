%define _unpackaged_files_terminate_build 1
%define oname hamcrest

%def_with doc
%def_with check

Name: python-module-%oname
Version: 2.0.0
Release: alt3.a1.git20150729

Summary: Hamcrest framework for matcher objects
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/PyHamcrest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
# https://github.com/hamcrest/PyHamcrest.git
Source: %name-%version.tar
Patch: hamcrest-2.0.0-Silence-warnings-from-tests-due-to-use-of-old-pytest.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with doc
BuildRequires: python2.7(sphinx_rtd_theme)
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib
BuildRequires: python-module-sphinx-devel
%endif

%if_with check
BuildRequires: python2.7(mock)
BuildRequires: python2.7(numpy)
BuildRequires: python2.7(pytest_cov)
BuildRequires: python3(mock)
BuildRequires: python3(numpy)
BuildRequires: python3(pytest_cov)
BuildRequires: python3(tox)
%endif

%description
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

%package -n python3-module-%oname
Summary: Hamcrest framework for matcher objects
Group: Development/Python3

%description -n python3-module-%oname
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data filtering,
but it is in the area of writing flexible tests that matchers are most
commonly used.

This package contains documentation for %oname.

%prep
%setup
%patch -p1

cp -fR . ../python3

%if_with doc
%prepare_sphinx .
ln -s ../objects.inv doc/
%endif

%build
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%if_with doc
export PYTHONPATH=$PWD/src
%make -C doc pickle
%make -C doc html
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/
rm -f *requirements.txt
%endif

%check
sed -i '/\[testenv\]$/a whitelist_externals =\
    \/bin\/cp\
    \/bin\/sed\
commands_pre =\
    cp %_bindir\/py.test3 \{envbindir\}\/py.test\
    sed -i \x271c #!\{envpython\}\x27 \{envbindir\}\/py.test' tox.ini
export PIP_NO_INDEX=YES
export TOXENV=py%{python_version_nodots python},py%{python_version_nodots python3}
tox.py3 --sitepackages -p auto -o -rv

%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%if_with doc
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*
%endif

%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*

%changelog
* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 2.0.0-alt3.a1.git20150729
- Fixed Pytest4.x compatibility errors.
- Enabled testing for Python3 package.

* Tue Apr 23 2019 Michael Shigorin <mike@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1.1.1
- introduce doc knob (on by default)
- minor spec cleanup

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.git20150729.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt2.a1.git20150729.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 2.0.0-alt2.a1.git20150729
- cleanup buildreq

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20150729
- New snapshot

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1.git20141030
- Initial build for Sisyphus

