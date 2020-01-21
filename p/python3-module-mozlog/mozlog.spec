%define _unpackaged_files_terminate_build 1
%define oname mozlog

Name: python3-module-%oname
Version: 3.3
Release: alt2

Summary: Robust log handling specialized for logging in the Mozilla universe
License: MPL 1.1/GPL 2.0/LGPL 2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozlog/
BuildArch: noarch

Source0: https://pypi.python.org/packages/ce/ce/85ce01843e2deea5b93d457a54f0246288256c2358fd30311eadef184bf7/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3 python3-module-mozfile

Conflicts: python-module-%oname


%description
Robust log handling specialized for logging in the Mozilla universe.

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
* Tue Jan 21 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.3-alt2
- Porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1
- automated PyPI update

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10-alt1
- Version 2.10

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.9-alt1
- Version 2.9

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8-alt1
- Initial build for Sisyphus

