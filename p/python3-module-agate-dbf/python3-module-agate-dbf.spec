%define  modulename agate-dbf

Name:    python3-module-%modulename
Version: 0.2.0
Release: alt1

Summary: Adds read support for DBF files to agate.
License: MIT
Group:   Development/Python3
URL:     https://github.com/wireservice/agate-dbf

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
%python3_sitelibdir/agatedbf/
%python3_sitelibdir/*.egg-info

%changelog
* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
