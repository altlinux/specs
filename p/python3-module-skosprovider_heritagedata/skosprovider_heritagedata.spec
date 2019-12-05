%define oname skosprovider_heritagedata

%def_disable check

Name: python3-module-%oname
Version: 0.2.0
Release: alt2

Summary: A skosprovider for the services at heritagedata.org
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/skosprovider_heritagedata/
BuildArch: noarch

# https://github.com/OnroerendErfgoed/skosprovider_heritagedata.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires skosprovider requests rdflib


%description
Skosprovider implementation of the heritagedata.org Vocabularies.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Skosprovider implementation of the heritagedata.org Vocabularies.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Skosprovider implementation of the heritagedata.org Vocabularies.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')


%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt1.git20141223.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20141223.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20141223.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20141223
- Initial build for Sisyphus

