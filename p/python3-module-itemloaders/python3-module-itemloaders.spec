Name:   python3-module-itemloaders
Version:1.1.0
Release:alt1

Summary:Base library for scrapy's ItemLoader
License:BSD-3-Clause
Group:  Development/Python
URL:    https://github.com/scrapy/itemloaders

BuildArch: noarch
Source0:https://github.com/scrapy/itemloaders/archive/refs/tags/v%version.tar.gz#/%name-%version.tar

BuildRequires:  rpm-build-python3
BuildRequires:  python3-devel python3-module-setuptools python3-module-wheel python3-module-jmespath
BuildRequires:  fdupes

%description
Library to populate items using XPath and CSS with a convenient API

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst
%python3_sitelibdir/itemloaders
%python3_sitelibdir/itemloaders-%{version}.dist-info

%changelog
* Tue Apr 02 2024 Daniil-Viktor Ratkin <krf10@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

