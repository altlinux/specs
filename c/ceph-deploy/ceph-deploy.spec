Name: ceph-deploy
Version: 1.5.34
Release: alt2
Summary: Admin and deploy tool for Ceph
Group: System/Base

License: MIT
Url: https://github.com/ceph/ceph-deploy

Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar
Patch: 0001-altlinux-distro-added.patch

BuildArch: noarch
BuildRequires: rpm-build-python
BuildRequires: python-module-setuptools

# Tox tests requirements
BuildRequires: openssh-clients
BuildRequires: python-module-pytest
BuildRequires: python-module-mock
BuildRequires: python-module-remoto
BuildRequires: python-module-tox

Requires: python-module-remoto

%description
An easy to use admin tool for deploy ceph storage clusters.

%prep
%setup
%patch -p1

%build
export CEPH_DEPLOY_NO_VENDOR=1
%python_build

%install
export CEPH_DEPLOY_NO_VENDOR=1
%python_install -O1

%check
# Tests are currently broken:
#   http://tracker.ceph.com/issues/8825
#CEPH_DEPLOY_NO_VENDOR=1 tox -e py27-novendor || :

%files
%doc LICENSE README.rst
%_bindir/ceph-deploy
%python_sitelibdir/*

%changelog
* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 1.5.34-alt2
- Add 0001-altlinux-distro-added.patch

* Mon Jun 20 2016 Lenar Shakirov <snejok@altlinux.ru> 1.5.34-alt1
- First build for Sisyphus (based on 1.5.32-1.fc25)

