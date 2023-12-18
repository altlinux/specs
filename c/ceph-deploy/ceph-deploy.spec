%define _unpackaged_files_terminate_build 1

%define modname ceph-deploy

Name: ceph-deploy
Version: 2.1.0
Release: alt3

Summary: Deploy Ceph with minimal infrastructure
License: MIT
Group: System/Base

Url: https://github.com/ceph/ceph-deploy
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildRequires: openssh-clients

BuildRequires: python3-module-remoto >= 1.1.4
BuildRequires: python3-module-sphinx

# Tox tests requirements
#BuildRequires: python3-module-pytest
#BuildRequires: python3-module-mock
#BuildRequires: python3-module-tox

Requires: python3-module-%name = %EVR


%description
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

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

sed -i 's/python-module/python3-module/g' ceph_deploy/hosts/alt/uninstall.py

%build
%python3_build

export PYTHONPATH=$PWD
%make -C docs man

%install
%python3_install

install -pDm644 docs/build/man/%name.1 %buildroot%_man1dir/%name.1

%files
%doc LICENSE README.rst
%_bindir/%name
%_man1dir/*

%files -n python3-module-%name
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests/

%files -n python3-module-%name-tests
%python3_sitelibdir/*/tests/


%changelog
* Mon Dec 18 2023 Michael Shigorin <mike@altlinux.org> 2.1.0-alt3
- make uninstall.py target python3 modules with removal
  (thx Andrey Firsov for the proposed fix)

* Fri Sep 10 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt2
- Revert "osd: decode output from remoto" (Closed: 40875)

* Sat Sep 04 2021 Alexey Shabalin <shaba@altlinux.org> 2.1.0-alt1
- 2.1.0

* Tue Feb 18 2020 Alexey Shabalin <shaba@altlinux.org> 2.0.1-alt3
- master snapshot bcb968a13e0f2643507b06aa8f6249e360e8e742

* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt2
- build for python2 disabled

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
