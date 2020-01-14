%define modulename talib

Name: python3-module-%modulename
Version: 0.4.17
Release: alt2

Summary: This is a Python wrapper for TA-LIB
License: BSD2
Group: Development/Python3
Url: https://github.com/mrjbq7/ta-lib

Source: %modulename-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: libta-lib-devel
BuildRequires: python3-module-numpy
BuildRequires: libnumpy-py3-devel


%description
This is a Python wrapper for TA-LIB based on Cython instead of SWIG

%prep
%setup -n %modulename-%version
%patch -p2

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.17-alt2
- build for python2 disabled

* Mon Apr 08 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.17-alt1
- Build new version for python3.7.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.10-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jun 21 2017 Konstantin Artyushkin <akv@altlinux.org> 0.4.10-alt1
- initial build

