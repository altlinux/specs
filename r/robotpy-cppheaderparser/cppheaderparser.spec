%global pypi_name robotpy-cppheaderparser
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 5.1.2
Release: alt0.1
Summary: Parse C++ header files and generate a data structure representing the class
Group: Development/Python3

License: BSD
Url: https://pypi.org/project/%pypi_name
Source0: %name-%version.tar

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python3
Provides: python3-module-CppHeaderParser = %EVR
Obsoletes: python3-module-CppHeaderParser < %version

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
%python3_sitelibdir_noarch/CppHeaderParser
%python3_sitelibdir_noarch/robotpy_cppheaderparser-%{version}.dist-info/

%changelog
* Mon Feb 17 2025 L.A. Kostis <lakostis@altlinux.ru> 5.1.2-alt0.1
- Initial build for ALTLinux.
- Use as alternative to unmaintained CppHeaderParser.
