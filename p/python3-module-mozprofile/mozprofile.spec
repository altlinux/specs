%define _unpackaged_files_terminate_build 1
%define oname mozprofile

%def_without check

Name: python3-module-%oname
Version: 0.28
Release: alt2

Summary: Library to create and modify Mozilla application profiles
License: MPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozprofile/
BuildArch: noarch

Source0: https://pypi.python.org/packages/64/8d/6812c090cf072ec3689c0c5f78d75936eebfec7108783b23230844770d51/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

Conflicts: python-module-%oname


%description
Library to create and modify Mozilla application profiles.

%prep
%setup -q -n %{oname}-%{version}

sed -i '/assert/s/^/#/' setup.py

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
%__python3 setup.py test
%endif

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*

%changelog
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.28-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.28-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.22-alt1
- Initial build for Sisyphus

