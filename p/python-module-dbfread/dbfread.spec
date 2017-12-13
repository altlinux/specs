%define _unpackaged_files_terminate_build 1
%define oname dbfread

%def_with python3

Name: python-module-%oname
Version: 2.0.7
Release: alt2
Summary: Read DBF Files with Python
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/dbfread/

# https://github.com/olemb/dbfread.git
Source: %{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-devel python-module-setuptools-tests
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python-module-objects.inv
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Read DBF Files with Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
DBF is a file format used by databases such dBase, Visual FoxPro, and
FoxBase+. This library reads DBF files and returns the data as native
Python data types for further processing. It is primarily intended for
batch jobs and one-off scripts.

This package contains documentation for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
py.test -vv
%if_with python3
pushd ../python3
py.test3 -vv
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Dec 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.7-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.7-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.4-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Thu Apr 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1.git20150207
- Initial build for Sisyphus

