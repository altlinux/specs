%define  modulename requestbuilder

Name:    python-module-%modulename
Version: 0.7.1
Release: alt1

Summary: Command line-driven HTTP request builder
License: ISC
Group:   Development/Python
URL:     https://github.com/boto/requestbuilder

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

BuildArch: noarch

Source: %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Tue Jun 02 2020 Andrey Cherepanov <cas@altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus.
