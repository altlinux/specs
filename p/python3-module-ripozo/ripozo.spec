%define oname ripozo

%def_without check

Name: python3-module-%oname
Version: 0.1.27
Release: alt2

Summary: An tool for easily making RESTful interfaces
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/ripozo/
BuildArch: noarch

# https://github.com/vertical-knowledge/ripozo.git
Source: %name-%version.tar
Patch0: fix-doc-build.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx 


%description
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A pluggable tool for quickly and efficiently creating web apis. In the
modern day, your server is no longer just interacting with a web
browser. Instead it's interfacing with desktop and mobile web browsers,
multiple native applications, and maybe even being exposed as an API to
other developers. Ripozo is designed to solve this problem. It allows
you to easily build Hypermedia/HATEOAS/REST APIs quickly and
efficiently.

This package contains documentation for %oname.

%prep
%setup
%patch0 -p1

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.1.27-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.27-alt1.dev0.git20150423.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.27-alt1.dev0.git20150423.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.27-alt1.dev0.git20150423.1
- NMU: Use buildreq for BR.

* Fri Apr 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.27-alt1.dev0.git20150423
- Version 0.1.27.dev0

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.20-alt1.dev0.git20150324
- Initial build for Sisyphus

