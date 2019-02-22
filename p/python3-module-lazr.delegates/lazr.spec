%define _unpackaged_files_terminate_build 1
%define oname lazr.delegates

Name: python3-module-%oname
Version: 2.0.4
Release: alt2

Summary: Easily write objects that delegate behavior.
License: LGPLv3
Group: Development/Python3
Url: https://launchpad.net/lazr.delegates
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel
BuildRequires: python3-module-nose
BuildRequires: python3-module-zope.interface

Requires: python3-module-zope.interface
%py3_requires zope.interface.advice zope.interface.interfaces
%add_python3_req_skip lazr zope


%description
The lazr.delegates package makes it easy to write objects that delegate behavior
to another object. The new object adds some property or behavior on to the other
object, while still providing the underlying interface, and delegating behavior.

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
* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.4-alt2
- Broken reqs for p8 branch fixed

* Fri Feb 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.4-alt1
- Initial build for Sisyphus
