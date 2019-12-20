%define oname jenkins

%def_without docs

Name: python3-module-py%oname
Version: 1.5.0
Release: alt1

Summary: Python bindings for the remote Jenkins API
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-jenkins/
BuildArch: noarch

# git://git.openstack.org/stackforge/python-jenkins
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: git-core python3-module-coverage
BuildRequires: python3-module-subunit-tests

%if_with docs
BuildRequires: python3-module-sphinx
%endif

%py3_requires pbr six
%add_python3_req_skip requests.packages.urllib3.exceptions

Conflicts: python3-module-%oname


%description
Python Jenkins is a python wrapper for the Jenkins REST API which aims
to provide a more conventionally pythonic way of controlling a Jenkins
server. It provides a higher-level API containing a number of
convenience functions.

%if_with docs
%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Python Jenkins is a python wrapper for the Jenkins REST API which aims
to provide a more conventionally pythonic way of controlling a Jenkins
server. It provides a higher-level API containing a number of
convenience functions.

This package contains pickles for %oname.
%endif

%prep
%setup

%if_with docs
sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile
%endif

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"
git init-db
git add . -A
git commit -a -m "%version"
git tag -m "%version" %version

%build
%python3_build_debug

%install
%python3_install

%if_with docs
%make -C doc pickle
%make -C doc html

cp -fR doc/build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
%if 0
%__python3 setup.py test -v
%__python3 setup.py testr -v --slowest
%endif

%files
%doc *.rst
%if_with docs
%doc doc/build/html
%endif
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle
%endif


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.5.0-alt1
- Version updated to 1.5.0
- build for python2 disabled

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 0.4.8-alt1.git20150810.2
- Rebuild with python-module-six

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.8-alt1.git20150810.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.8-alt1.git20150810.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.8-alt1.git20150810
- Initial build for Sisyphus

