%define _unpackaged_files_terminate_build 1

%define oname optimus

Name: python3-module-%oname
Version: 0.0.2
Release: alt2

Summary: Python web framework project constructor
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/py-optimus/
BuildArch: noarch

# https://github.com/johndeng/optimus.git
Source0: https://pypi.python.org/packages/8e/38/c49f6c9f639e259f0558a517303fc821cc6a25ada43ea0f6bda389cd42c7/py-%{oname}-%{version}.tar.gz
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-click python3-module-jinja2

%py3_provides %oname

%add_findreq_skiplist %python3_sitelibdir/%oname/templates/*
%add_python3_compile_exclude %python3_sitelibdir/%oname/templates/*


%description
Optimus is a Python web framework project constructor.

Now optimus support create Tornado project structure.

%prep
%setup -q -n py-%{oname}-%{version}
%patch0 -p2

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
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.2-alt1
- automated PyPI update

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt2.git20141126
- Fixed build

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141126
- Initial build for Sisyphus

