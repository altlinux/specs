%define module_name proxmoxer
Name: python-module-%module_name
Version: 1.0.2
Release: alt2%ubt

Summary: Wrapper around Proxmox REST API v2
License: %mit
Group: Development/Python
Url: https://github.com/swayf/proxmoxer
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-ubt

BuildPreReq: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-requests
BuildRequires: python-module-paramiko

Requires: python-module-requests
Requires: python-module-paramiko

%description
Pythonic API for a Proxmox cluster manipulation.

%prep
%setup -q -n %name-%version

%build
%python_build

%install
%python_install
# don't include unit tests into the package
rm -rf %buildroot%python_sitelibdir/tests

%files
%python_sitelibdir/*

%changelog
* Fri Jun 08 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt2%ubt
- Fixed the dependencies and a bogus `Provides: python2.7(tests)`.

* Tue May 29 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt1%ubt
- Initial build for ALTLinux Sisyphus
