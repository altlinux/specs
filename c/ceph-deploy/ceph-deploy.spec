%define modname ceph-deploy

Name: ceph-deploy
Version: 2.0.1
Release: alt1.g86943fc.1

Summary: Deploy Ceph with minimal infrastructure
Group: System/Base
License: MIT
Url: https://github.com/ceph/ceph-deploy
BuildArch: noarch

Source: %name-%version.tar
Patch1: change-version.patch

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

Requires: python3-module-%name = %EVR


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

# Use only for version after release, delete when updating to a new version
%patch1 -p1

%build
%python3_build_debug -b build3
%python_build_debug -b build2

export PYTHONPATH=$PWD
%make -C docs man

%install
ln -snf build2 build
%python_install -O1
mv %buildroot%_bindir/{%name,%name.py2}
ln -snf build3 build
%python3_install

install -pDm644 docs/build/man/%name.1 %buildroot%_man1dir/%name.1

%files
%doc LICENSE README.rst
%_bindir/%name
%_man1dir/*

%files -n python-module-%name
%_bindir/%name.py2
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests/

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests/

%files -n python-module-%name-tests
%python_sitelibdir/*/tests/

%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests/


%changelog
* Thu Jul 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 2.0.1-alt1.g86943fc.1
- Update to v2.0.1-30-g86943fc
- Disable useless (it ran 0 tests) check

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
