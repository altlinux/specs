%define modulename talib
%def_with python3

Name: python-module-%modulename
Version: 0.4.10
Release: alt1.1

%setup_python_module %modulename

Summary: This is a Python wrapper for TA-LIB
License: BSD2
Group: Development/Python

Url: https://github.com/mrjbq7/ta-lib
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %modulename-%version.tar

#BuildPreReq: %py_dependencies setuptools
BuildPreReq: libta-lib-devel
BuildRequires: python-module-numpy
BuildRequires: libnumpy-devel
%if_with python3
BuildPreReq: libta-lib-devel
BuildRequires: python3-module-numpy
BuildRequires: libnumpy-py3-devel
%endif

#-------------------------------------------------------------------------------
%if_with python3
%package -n python3-module-%modulename
Summary: This is a Python wrapper for TA-LIB
Group: Development/Python3

%description -n python3-module-%modulename 
%summary
%endif
#-------------------------------------------------------------------------------
%description
This is a Python wrapper for TA-LIB based on Cython instead of SWIG

%prep
%setup -n %modulename-%version

%if_with python3
rm -fr ../python3
cp -a ./ ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

#-------------------------------------------------------------------------------
%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif
#-------------------------------------------------------------------------------

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.10-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jun 21 2017 Konstantin Artyushkin <akv@altlinux.org> 0.4.10-alt1
- initial build

