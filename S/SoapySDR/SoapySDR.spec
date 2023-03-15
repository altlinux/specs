# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define maj_ver 0.8

Name: SoapySDR
Version: %maj_ver.1
Release: alt3
Summary: A Vendor Neutral and Platform Independent SDR Support Library
Group: Engineering
License: BSL
Url: https://github.com/pothosware/%name

Source: soapy-sdr-%version.tar
# Source-url: https://github.com/pothosware/%name/archive/refs/tags/soapy-sdr-%version.tar.gz

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: ctest cmake
BuildRequires: gcc-c++
BuildRequires: swig
BuildRequires: doxygen
BuildRequires: python3-devel
BuildRequires: python3-module-numpy python3-module-numpy-testing

%description
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n python3-module-SoapySDR
Group: Development/Python3
Summary: Python3 Bindings for SoapySDR

%description -n python3-module-SoapySDR
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n %name-devel
Group: Development/Other
Summary: Development Files for SoapySDR
Requires: %name = %EVR

%description -n %name-devel
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices.

%package -n %name-doc
Group: Documentation
Summary: Development Files for SoapySDR
BuildArch: noarch

%description -n %name-doc
SoapySDR is an open-source generalized C/C++ API and runtime library
for interfacing with Software-Defined Radio (SDR) devices. This package includes
library header file documentation.

%prep
%setup -n soapy-sdr-%version

%build
export Python_ADDITIONAL_VERSIONS="%__python3_version"
%cmake -DUSE_PYTHON_CONFIG=ON -DPYTHON3_EXECUTABLE=%__python3
%cmake_build

%install
%cmake_install
mkdir -p %buildroot%_libdir/%name/modules%maj_ver
# install docs
mkdir -p %buildroot%_docdir/%name
cp -a %_cmake__builddir/docs/html/* %buildroot%_docdir/%name

%check
pushd %_cmake__builddir
ctest -V %optflags
popd

%files
%_bindir/SoapySDRUtil
%_libdir/libSoapySDR.so.%version
%_libdir/libSoapySDR.so.%maj_ver
%_man1dir/*
%doc README.md
# for hardware support modules
%dir %_libdir/%name
%dir %_libdir/%name/modules%maj_ver

%files -n python3-module-SoapySDR
%python3_sitelibdir/SoapySDR.py
%python3_sitelibdir/_SoapySDR.so
%python3_sitelibdir/__pycache__/SoapySDR.cpython-*.pyc

%files -n %name-devel
%_includedir/%name
%_libdir/libSoapySDR.so
%_pkgconfigdir/*
%dir %_datadir/cmake/%name
%_datadir/cmake/%name/*

%files -n %name-doc
%_docdir/%name/*

%changelog
* Mon Jun 27 2022 Anton Midyukov <antohami@altlinux.org> 0.8.1-alt3
- Initial build in Sisyphus

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt2_3
- update to new release by fcimport

* Wed Feb 02 2022 Cronbuild Service <cronbuild@altlinux.org> 0.8.1-alt2_1
- rebuild to get rid of unmets

* Mon Sep 20 2021 Igor Vlasenko <viy@altlinux.org> 0.8.1-alt1_1
- update to new release by fcimport
