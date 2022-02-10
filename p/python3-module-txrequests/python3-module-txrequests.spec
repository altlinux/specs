%define  modulename txrequests

Name:    python3-module-%modulename
Version: 0.9.6
Release: alt1

Summary: Asynchronous Python HTTP Requests for Humans using twisted
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/tardyp/txrequests

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Feb 10 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus
