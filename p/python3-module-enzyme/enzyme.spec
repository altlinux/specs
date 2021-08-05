%define oname enzyme

%def_disable check
%def_disable doc

Name: python3-module-%oname
Version: 0.4.2
Release: alt2.dev.git20131128.1.3
Summary: Python video metadata parser
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/enzyme/

# https://github.com/Diaoul/enzyme.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

BuildRequires(pre): rpm-macros-sphinx3 python3-module-sphinx
BuildRequires: python3-module-chardet python3-module-pytest python3-module-urllib3 python3-module-yaml
%if_with doc
BuildRequires: diaoul-sphinx-themes
%endif

%description
Enzyme is a Python module to parse video metadata.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Enzyme is a Python module to parse video metadata.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Enzyme is a Python module to parse video metadata.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Enzyme is a Python module to parse video metadata.

This package contains documentation for %oname.

%prep
%setup

%if_with doc
rm -fR docs/_themes
cp -fR %_datadir/diaoul-sphinx-themes docs/_themes
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build

%install
%python3_install

%if_with doc
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
python3 setup.py test
exit 1

%files
%doc *.rst
%python3_sitelibdir/*
%if_with doc
%exclude %python3_sitelibdir/*/pickle
%endif
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%if_with doc
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*
%endif

%changelog
* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.4.2-alt2.dev.git20131128.1.3
- temp. disable doc subpackages (firstly update the package)

* Sun Jul 25 2021 Grigory Ustinov <grenka@altlinux.org> 0.4.2-alt2.dev.git20131128.1.2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt1.dev.git20131128.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.dev.git20131128.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.dev.git20131128.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.dev.git20131128
- Initial build for Sisyphus

