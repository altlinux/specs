%global pypi_name pcapy-ng
%define _unpackaged_files_terminate_build 1

Name: %pypi_name
Version: 1.0.9
Release: alt0.1
Summary: Python pcap extension
Group: Development/Python3

License: Apache-1.1
Url: https://github.com/stamparm/pcapy-ng/
Source0: pcapy-%version.tar

BuildRequires: python3-devel gcc-c++
BuildRequires: python3-module-setuptools python3-module-wheel python3-module-Cython libpcap-devel

%package -n python3-module-%{pypi_name}
Summary: %summary
Group: Development/Python3

%description
Pcapy-NG is a Python extension module that interfaces with the libpcap packet
capture library.

%description -n python3-module-%{pypi_name}
Pcapy-NG is a Python extension module that interfaces with the libpcap packet
capture library.

%prep
%setup -n pcapy-%version

%build
%pyproject_build

%install
%pyproject_install

rm -rf %buildroot%_docdir/%pypi_name

%files -n python3-module-%{pypi_name}
%doc LICENSE README pcapy.html
%python3_sitelibdir/*.so
%python3_sitelibdir/pcapy_ng-%{version}.dist-info/

%changelog
* Wed Feb 19 2025 L.A. Kostis <lakostis@altlinux.ru> 1.0.9-alt0.1
- Use -NG sources.

* Wed Feb 19 2025 L.A. Kostis <lakostis@altlinux.ru> 0.11.4-alt0.1
- Initial build for ALTLinux.

