%define modname ceph-deploy

Name: ceph-deploy
Version: 2.0.0
Release: alt1

Summary: Deploy Ceph with minimal infrastructure
Group: System/Base
License: MIT
Url: https://github.com/ceph/ceph-deploy
BuildArch: noarch

Source: %name-%version.tar
Patch: 0001-altlinux-distro-added.patch

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
BuildRequires: python-module-sphinx
BuildRequires: python-module-virtualenv
BuildRequires: python-module-remoto
BuildRequires: openssh-clients
BuildRequires: git

# Tox tests requirements
BuildRequires: python-module-pytest
BuildRequires: python-module-mock
BuildRequires: python-module-tox
BuildRequires: python-module-urlparse3

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-module-virtualenv
BuildPreReq: python3-module-remoto

# Tox tests requirements
BuildPreReq: python3-module-pytest
BuildPreReq: python3-module-mock
BuildPreReq: python3-module-tox

Requires: python-module-%name = %EVR


%description
ceph-deploy is a way to deploy Ceph relying on just SSH access to the servers, sudo, 
and some Python. It runs fully on your workstation, requiring no servers, databases, 
or anything like that.

%package -n python-module-%name
Summary: Deploy Ceph with minimal infrastructure
Group: Development/Python
%py_requires remoto

%description -n python-module-%name
ceph-deploy is a way to deploy Ceph relying on just SSH access to the servers, sudo, 
and some Python. It runs fully on your workstation, requiring no servers, databases, 
or anything like that.

%package -n python3-module-%name
Summary: Deploy Ceph with minimal infrastructure
Group: Development/Python3
%py3_requires remoto
%add_python3_req_skip urlparse

%description -n python3-module-%name
ceph-deploy is a way to deploy Ceph relying on just SSH access to the servers, sudo, 
and some Python. It runs fully on your workstation, requiring no servers, databases, 
or anything like that.

%package docs
Summary: Documentation for %name
Group: Development/Documentation
Requires: %name = %version-%release

%description docs
ceph-deploy is a way to deploy Ceph relying on just SSH access to the servers, sudo, 
and some Python. It runs fully on your workstation, requiring no servers, databases, 
or anything like that.

This package contains documentation for %name

%package -n python-module-%name-tests
Summary: Tests for python-module-%name
Group: System/Base
Requires: python-module-%name = %version-%release

%description -n python-module-%name-tests
ceph-deploy is a way to deploy Ceph relying on just SSH access to the servers, sudo, 
and some Python. It runs fully on your workstation, requiring no servers, databases, 
or anything like that.

This package contains tests for python3-module-%name

%package -n python3-module-%name-tests
Summary: Tests for python3-module-%name
Group: System/Base
Requires: python3-module-%name = %version-%release

%description -n python3-module-%name-tests
ceph-deploy is a way to deploy Ceph relying on just SSH access to the servers, sudo, 
and some Python. It runs fully on your workstation, requiring no servers, databases, 
or anything like that.

This package contains tests for python3-module-%name

%prep
%setup
%patch -p1
sed -i 's/.*remoto.*//' setup.py 
sed -i 's/.*else:.*//' setup.py

pushd ceph_deploy/util
sed -i "s/0644/'0664'/" pkg_managers.py
sed -i "s/0600/'0600'/" pkg_managers.py
popd

rm -rf ../python3
cp -fR . ../python3

%build
export CEPH_DEPLOY_NO_VENDOR=1
%python_build_debug

pushd ../python3
%python3_build_debug
popd

export PYTHONPATH=$PWD
%make -C docs man

%install
pushd ../python3
%python3_install
popd
pushd %buildroot/%_bindir
mv %name %name.py3
popd

export CEPH_DEPLOY_NO_VENDOR=1
%python_install -O1

%check
python setup.py test

%files
%doc LICENSE README.rst
%_bindir/*

%files -n python-module-%name
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests/

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests/

%files docs
%doc docs/*/man/*

%files -n python-module-%name-tests
%python_sitelibdir/*/tests/

%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests/


%changelog
* Tue Apr 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt1
- Updated version to 2.0.0

* Thu Apr 05 2018 Lenar Shakirov <snejok@altlinux.ru> 1.5.39-alt2
- 0001-altlinux-distro-added.patch:
  * don't remove libcephfs{1,2} (ALT: #34729)

* Tue Dec 19 2017 Lenar Shakirov <snejok@altlinux.ru> 1.5.39-alt1
- 1.5.39

* Mon Jan 09 2017 Lenar Shakirov <snejok@altlinux.ru> 1.5.34-alt4
- Add all ALT distros with Simply and Regular
- Revert adding "Requires: ceph > 0.94.7-alt2":
  * ceph-deploy purge command remove ceph-deploy too

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 1.5.34-alt3
- Doesn't remove librados2 and librbd1 on purge: needed by qemu-img
- Req: ceph > 0.94.7-alt2 (because we want ceph-mds) (ALT: #32309)

* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 1.5.34-alt2
- Add 0001-altlinux-distro-added.patch

* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 1.5.34-alt1
- First build for Sisyphus (based on 1.5.32-1.fc25)
