%define _unpackaged_files_terminate_build 1
%define oname lazr.config

Name: python3-module-%oname
Version: 2.2.1
Release: alt2

Summary: Create configuration schemas, and process and validate configurations.
License: LGPLv3
Group: Development/Python3
Url: https://launchpad.net/lazr.config
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildRequires: python3-module-lazr.delegates
BuildRequires: python3-module-zope.interface

Requires: python3-module-zope.interface
Requires: python3-module-lazr.delegates
%add_python3_req_skip lazr


%description
The LAZR config system is typically used to manage process configuration. Process
configuration is for saying how things change when we run systems on different 
machines, or under different circumstances.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.* COPYING.*
%python3_sitelibdir/*


%changelog
* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt2
- Broken reqs for p8 branch fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2.1-alt1
- Initial build for Sisyphus
