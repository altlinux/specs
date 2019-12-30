%define oname loremipsum

%def_enable check

Name: python3-module-%oname
Version: 2.0.0
Release: alt2

Summary: A Lorem Ipsum text generator
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/loremipsum/
BuildArch: noarch

# https://github.com/monkeython/loremipsum.git
Source: %name-%version.tar


BuildRequires(pre): rpm-build-python3
BuildRequires: pylint-py3 python3-module-hacking python3-module-wheel
BuildRequires: python3-module-coverage python3-module-coveralls
BuildRequires: python3-module-flake8 python3-module-testrepository
BuildRequires: python3-tools-pep8 python3-module-sphinx

%py3_provides %oname


%description
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The purpose of this package is to generate random (plausible) text
sentences and paargraphs based on a dictionary and a sample text. By
default this package will generate Lorem Ipsum style text, but you can
customize the generator to effectively load any dictionary and any
sample text you like.

This package contains documentation for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

pushd %oname
cp -fR samples serialization tests \
    %buildroot%python3_sitelibdir/%oname/
popd

export PYTHONPATH=%buildroot%python3_sitelibdir
pushd docs
sphinx-build-3 -b pickle -d _build/doctrees . _build/pickle
sphinx-build-3 -b html -d _build/doctrees . _build/html
popd

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt2
- build for python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1.b2.git20141031.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt1.b2.git20141031.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Dec 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.b2.git20141031
- Initial build for Sisyphus

