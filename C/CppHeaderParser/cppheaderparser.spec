%global pypi_name CppHeaderParser
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 2.7.4
Release: alt0.1
Summary: Parse C++ header files and generate a data structure representing the class
Group: Development/Python

License: BSD
Url: https://sourceforge.net/projects/cppheaderparser/
Source0: %name-%version.tar

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python

%description
%summary

%description -n python3-module-%{pypi_name}
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files -n python3-module-%{pypi_name}
%python3_sitelibdir_noarch/%{pypi_name}
%python3_sitelibdir_noarch/%{pypi_name}-%{version}.dist-info/

%changelog
* Tue Jun 13 2023 L.A. Kostis <lakostis@altlinux.ru> 2.7.4-alt0.1
- Initial build for ALTLinux.

