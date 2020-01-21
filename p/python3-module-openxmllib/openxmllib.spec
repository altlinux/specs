%define _unpackaged_files_terminate_build 1

%define oname openxmllib

Name: python3-module-%oname
Version: 1.1.1
Release: alt2

Summary: Provides resources to handle OpenXML documents
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/openxmllib/
BuildArch: noarch

Source0: https://pypi.python.org/packages/3c/df/cdb840bad7bfd3148a972313403463c6fb5e7eb5a540ae9d2c8acac54b88/%{oname}-%{version}.zip
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lxml python3-module-urllib3
BuildRequires: python3-module-nose
BuildRequires: python-tools-2to3 unzip

%py3_provides %oname
%py3_requires lxml


%description
openxmllib is a set of tools that deals with the new ECMA 376 office
file formats known as OpenXML.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc README.rst PKG-INFO COPYING doc
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.1-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.1-alt1
- automated PyPI update

* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt1
- Initial build for Sisyphus

