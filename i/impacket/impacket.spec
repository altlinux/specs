%global pypi_name impacket
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 0.12.0
Release: alt0.1
Summary: Collection of Python classes for working with network protocols
Group: Development/Python3

License: Apache-1.1
Url: https://github.com/fortra/impacket
Source0: %name-%version.tar

BuildRequires: python3-devel
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python3

%description
%summary

%description -n python3-module-%{pypi_name}
%summary

%package examples
Summary: %name tools and examples using %name python3 module
Group: Networking/Other
Requires: python3-module-%name = %EVR

%description examples
Impacket is a collection of Python classes for working with network
protocols. Impacket is focused on providing low-level
programmatic access to the packets and for some protocols (e.g.
SMB1-3 and MSRPC) the protocol implementation itself.
Packets can be constructed from scratch, as well as parsed from
raw data, and the object-oriented API makes it simple to work with
deep hierarchies of protocols. The library provides a set of tools
as examples of what can be done within the context of this library.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%_docdir/%name

%files -n python3-module-%{pypi_name}
%doc LICENSE README.md
%python3_sitelibdir_noarch/%{pypi_name}
%python3_sitelibdir_noarch/%{pypi_name}-%{version}.dist-info/

%files examples
%_bindir/*

%changelog
* Wed Feb 19 2025 L.A. Kostis <lakostis@altlinux.ru> 0.12.0-alt0.1
- Initial build for ALTLinux.

