%set_verify_elf_method rpath=relaxed

%define modulename talib

%def_without check

Name: python3-module-%modulename
Version: 0.4.26
Release: alt1

Summary: This is a Python wrapper for TA-LIB
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/TA-Lib

Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-numpy
BuildRequires: libta-lib-devel
BuildRequires: libnumpy-py3-devel
%if_with check
BuildRequires: python3-module-pytest
%endif

Requires: python3-module-numpy

%description
This is a Python wrapper for TA-LIB based on Cython instead of SWIG.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install
%python3_prune

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 talib --ignore=.talib/test_polars.py

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/TA_Lib-%version.dist-info
%exclude %python3_sitelibdir/%modulename/test_*


%changelog
* Wed Apr 19 2023 Anton Vyatkin <toni@altlinux.org> 0.4.26-alt1
- New version 0.4.26.

* Mon Mar 16 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.17-alt3
- Fixed build with numpy.

* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.17-alt2
- build for python2 disabled

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.17-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.10-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jun 21 2017 Konstantin Artyushkin <akv@altlinux.org> 0.4.10-alt1
- initial build

