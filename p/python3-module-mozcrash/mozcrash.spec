%define _unpackaged_files_terminate_build 1

%define oname mozcrash

Name: python3-module-%oname
Version: 1.0
Release: alt2

Summary: Library for printing stack traces from minidumps left behind by crashed processes
License: MPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozcrash/
BuildArch: noarch

Source0: https://pypi.python.org/packages/fa/a7/5caf82d2d44ac2bea78dbd6465ec11e692f408ed15dd65adad4438d49745/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mozfile python3-module-mozlog
BuildRequires: python-tools-2to3 python3-module-mozinfo
BuildRequires: python3-module-six


%description
Library for printing stack traces from minidumps left behind by crashed
processes.

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
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- Porting on Python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

