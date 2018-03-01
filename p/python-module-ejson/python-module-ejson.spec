%define  modulename ejson

Name:    python-module-%modulename
Version: 0.1.5
Release: alt1

Summary: Extensible JSON serializers and deserializers
License: LGPL-3.0
Group:   Development/Python
URL:     https://github.com/Yipit/ejson

Packager: Andrey Cherepanov <cas@altlinux.org>

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
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%changelog
* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- Initial build for Sisyphus
