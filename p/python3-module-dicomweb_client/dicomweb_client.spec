%define _unpackaged_files_terminate_build 1
# available online
%def_without docs
# no offline tests
%def_without tests
%define oname dicomweb_client

Name: python3-module-%oname
Version: 0.59.1
Release: alt1

Summary: Client intefaces for DICOMweb RESTful services QIDO-RS, WADO-RS and STOW-RS
License: MIT
Group: Development/Python3
URL: https://dicomweb-client.readthedocs.io/
VCS: https://github.com/ImagingDataCommons/dicomweb-client.git

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools
BuildRequires: libnumpy-py3-devel
BuildRequires: python3-module-retrying
BuildRequires: python3-module-requests
BuildRequires: python3-module-Pillow
BuildRequires: python3-module-pydicom
BuildRequires: python3-module-typing_extensions

%description
The dicomweb-client build distribution provides client intefaces
for DICOMweb RESTful services QIDO-RS, WADO-RS and STOW-RS to
search, retrieve and store DICOM objects over the web,
respectively. For more information about DICOMweb please refer
to the documentation of the DICOM standard, in particular PS3.18.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/%oname
%doc LICENSE README.md
%python3_sitelibdir/%oname/*
%python3_sitelibdir/%oname-%version.dist-info/*

%changelog
* Mon Feb 19 2024 Elizaveta Morozova <morozovaes@altlinux.org> 0.59.1-alt1
Initial build for ALT.

