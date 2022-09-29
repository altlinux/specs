%define  modulename deprecation

Name:    python3-module-%modulename
Version: 2.1.0
Release: alt1

Summary: A library to handle automated deprecations
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/briancurtin/deprecation

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
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/*.egg-info

%changelog
* Thu Sep 29 2022 Anton Zhukharev <ancieg@altlinux.org> 2.1.0-alt1
- 2.0.6 -> 2.1.0

* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.6-alt1
- Initial build for Sisyphus
