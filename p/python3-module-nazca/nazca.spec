%define _unpackaged_files_terminate_build 1

%define oname nazca

Name: python3-module-%oname
Version: 0.9.5
Release: alt2

Summary: Python library for data alignment
License: LGPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/nazca/

BuildArch: noarch

Source: %{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six python3-module-scipy
BuildRequires: python3-module-lxml
BuildRequires: python3-module-numpy-testing

%description
Python library for data alignment.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Python library for data alignment.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

cp -fR test/ %buildroot%python3_sitelibdir/%oname/
cp -fR examples/ %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test
%exclude %python3_sitelibdir/*/examples

%files tests
%python3_sitelibdir/*/test
%python3_sitelibdir/*/examples

%changelog
* Mon Aug 24 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.5-alt2
- Build requires fixed.

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.9.5-alt1
- Version updated to 0.9.5
- porting to python3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Oct 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.7.2-alt2
- Updated dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.2-alt1
- automated PyPI update

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

