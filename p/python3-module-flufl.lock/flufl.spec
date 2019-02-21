%define _unpackaged_files_terminate_build 1
%define oname flufl.lock

Name: python3-module-%oname
Version: 3.2
Release: alt1

Summary: An NFS-safe file lock.
License: Apache-2.0
Group: Development/Python3
Url: https://gitlab.com/warsaw/flufl.lock
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildRequires: python3-module-atpublic

Requires: python3-module-atpublic


%description
This package is called flufl.lock. It is an NFS-safe file-based lock with 
timeouts for POSIX systems.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.*
%python3_sitelibdir/*


%changelog
* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2-alt1
- Initial build for Sisyphus
