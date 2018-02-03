%define _unpackaged_files_terminate_build 1
BuildRequires: unzip
%define oname openxmllib
Name: python-module-%oname
Version: 1.1.1
Release: alt1.1
Summary: Provides resources to handle OpenXML documents
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/openxmllib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/3c/df/cdb840bad7bfd3148a972313403463c6fb5e7eb5a540ae9d2c8acac54b88/%{oname}-%{version}.zip
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-lxml
BuildPreReq: python-module-nose

%py_provides %oname
%py_requires lxml

%description
openxmllib is a set of tools that deals with the new ECMA 376 office
file formats known as OpenXML.

%prep
%setup -q -n %{oname}-%{version}

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README.rst PKG-INFO COPYING doc
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus

