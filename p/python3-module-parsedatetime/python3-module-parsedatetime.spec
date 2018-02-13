%define  modulename parsedatetime

Name:    python3-module-%modulename
Version: 2.4
Release: alt1

Summary: Parse human-readable date/time strings
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/bear/parsedatetime

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

%changelog
* Thu Feb 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 2.4-alt1
- Separate build for Sisyphus
