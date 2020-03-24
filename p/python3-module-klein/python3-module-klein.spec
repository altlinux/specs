%define  modulename klein

Name:    python3-module-%modulename
Version: 19.6.0
Release: alt1

Summary: werkzeug + twisted.web
License: MIT
Group:   Development/Python3
URL:     https://github.com/twisted/klein

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-incremental

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
%doc README.rst

%changelog
* Tue Mar 24 2020 Mikhail Gordeev <obirvalger@altlinux.org> 19.6.0-alt1
- Initial build for Sisyphus
