%define _unpackaged_files_terminate_build 1
%define oname mozprocess

Name: python3-module-%oname
Version: 0.8
Release: alt1

Summary: Mozilla-authored process handling
License: MPLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/mozprocess/
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-mozinfo python-tools-2to3
BuildRequires: python3-module-six


%description
Mozilla-authored process handling.

%prep
%setup

sed -i 's|file(|open(|' setup.py

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
%doc PKG-INFO
%python3_sitelibdir/*


%changelog
* Wed Jan 22 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt1
- Version updated to 0.8
- porting on python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.24-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated PyPI update

* Tue Dec 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.21-alt1
- Initial build for Sisyphus

