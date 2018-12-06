%define  modulename deprecation

Name:    python-module-%modulename
Version: 2.0.6
Release: alt1

Summary: A library to handle automated deprecations
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/briancurtin/deprecation

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Fri Dec 07 2018 Alexey Shabalin <shaba@altlinux.org> 2.0.6-alt1
- Initial build for Sisyphus
