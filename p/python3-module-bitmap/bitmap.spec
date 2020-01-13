%define oname bitmap

Name: python3-module-%oname
Version: 0.0.6
Release: alt2

Summary: BitMap for python
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/bitmap/
BuildArch: noarch

Source0: https://pypi.python.org/packages/da/10/bb92da21d7472d8a3befad8785c917f2bf099bdf326edebcba2abf57d09a/%{oname}-%{version}.tar.gz
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
This package provides a `BitMap` class which is an array of bits stored
in compact format.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p2

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
export PYTHONPATH=$PWD/src
py.test-%_python3_version -vv
%endif

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.6-alt2
- porting for python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.6-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.6-alt1
- automated PyPI update

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt2
- Fixed build

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1
- Initial build for Sisyphus

