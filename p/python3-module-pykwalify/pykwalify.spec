%define _unpackaged_files_terminate_build 1
%define oname pykwalify

%def_disable check

Name: python3-module-%oname
Version: 1.7.0
Release: alt1
Epoch: 1
Summary: Python lib/cli for JSON/YAML schema validation
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pykwalify/
#Git: https://github.com/Grokzen/pykwalify.git

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-docopt python3-module-yaml
#BuildPreReq: python3-module-testfixtures python3-module-tox
#BuildPreReq: python3-module-coveralls
BuildRequires: python3-module-html5lib
BuildRequires: python3-module-nose
BuildRequires: python3-module-pbr
BuildRequires: python3-module-tox
BuildRequires: python3-module-unittest2
BuildRequires: python3-module-z4r-coveralls
BuildRequires: python3-module-zope.component

%py3_provides %oname
#%py3_requires json docopt yaml

%description
YAML/JSON validation library.

This framework is a port with alot added functionality of the java
version of the framework kwalify that can be found at:
http://www.kuwata-lab.com/kwalify/

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd

%check
python3 setup.py test
py.test-%_python3_version -vv

%files
%doc *.md docs/*
%_bindir/*.py3
%python3_sitelibdir/*

%changelog
* Wed Jan 15 2020 Nikolai Kostrigin <nickel@altlinux.org> 1:1.7.0-alt1
- NMU: 1.6.1 -> 1.7.0
- Remove python2 module build

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 1:1.6.1-alt1
- The version is synchronized with upstream (used Epoch)

* Fri Aug 17 2018 Pavel Vainerman <pv@altlinux.ru> 18.03-alt1.git20180314
- build new version

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 15.01-alt2.git20150117.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 15.01-alt2.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 15.01-alt2.git20150117
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 15.01-alt1.git20150117
- Initial build for Sisyphus
