Name:   python3-module-itemadapter
Version:0.9.0
Release:alt1

Summary:Wrapper for data container objects
License:BSD-3-Clause
Group:  Development/Python
URL:    https://github.com/scrapy/itemadapter

BuildArch: noarch
Source0:https://github.com/scrapy/itemadapter/archive/v%version.tar.gz#/%name-%version.tar

BuildRequires:  rpm-build-python3
BuildRequires:  python3-devel python3-module-setuptools python3-module-wheel
BuildRequires:  fdupes

%description
The ItemAdapter class is a wrapper for data container objects, providing
a common interface to handle objects of different types in an uniform
manner, regardless of their underlying implementation.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%python3_sitelibdir/itemadapter
%python3_sitelibdir/itemadapter-%version-py*.egg-info

%changelog
* Thu Aug 08 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.9.0-alt1
- new version

* Tue Apr 02 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux

