%define _unpackaged_files_terminate_build 1

%define oname manifestparser

Name: python3-module-%oname
Version: 1.1
Release: alt2

Summary: Library to create and manage test manifests
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/manifestparser/
BuildArch: noarch

Source0: https://pypi.python.org/packages/53/4e/f621c25a2e0ef6e7a38987f291a88d06996e3f8bfe3ad6302b4abc45c9f8/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Library to create and manage test manifests.

%prep
%setup -q -n %{oname}-%{version}

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc PKG-INFO
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1-alt2
- Porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Initial build for Sisyphus

