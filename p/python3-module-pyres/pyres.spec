%define oname pyres

%def_disable check

Name: python3-module-%oname
Version: 1.5
Release: alt3

Summary: Python resque clone
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyres/

BuildArch: noarch

# https://github.com/binarydud/pyres.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires redis

%description
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Resque is a great implementation of a job queue by the people at github.
It's written in ruby, which is great, but I primarily work in python. So
I took on the task of porting over the code to python and PyRes was the
result.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|&-3|' docs/Makefile

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.md *.markdown LICENSE CHANGES.txt
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%changelog
* Fri Apr 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt3
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.5-alt2.git20140901.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Dec 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5-alt2.git20140901
- Updated runtime dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5-alt1.git20140901.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5-alt1.git20140901.1
- NMU: Use buildreq for BR.

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.git20140901
- Initial build for Sisyphus

