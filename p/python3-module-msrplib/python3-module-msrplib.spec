%define  modulename msrplib

Name:    python3-module-%modulename
Version: 0.21.0
Release: alt1

Summary: MSRP (RFC4975) client library
License: LGPL-2.1+
Group:   Development/Python3
URL:     https://github.com/AGProjects/python3-msrplib

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source: python3-%modulename-%version.tar

%description
This library implements Message Session Relay Protocol (MSRP). MSRP is
defined in RFC 4975.  The relay extension that can be used for NAT
traversal purposes is defined in RFC 4976.

%prep
%setup -n python3-%modulename-%version

%build
%python3_build

%install
%python3_install

%files
%doc README
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info

%changelog
* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 0.21.0-alt1
- Initial build for Sisyphus
