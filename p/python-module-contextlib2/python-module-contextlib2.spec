%define modulename contextlib2

%def_with python3

Name: python-module-contextlib2
Version: 0.4.0
Release: alt1.1.1

Summary: Backports and enhancements for the contextlib module

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pypi.python.org/packages/source/c/%modulename/%modulename-%version.tar

%setup_python_module %modulename

BuildArch: noarch

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-module-mwlib rpm-build-python3

%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-paste
%endif

%description
contextlib2 is a backport of the standard library's contextlib
module to earlier Python versions.

It also serves as a real world proving ground for possible
future enhancements to the standard library version.

%package -n python3-module-%modulename
Summary: Backports and enhancements for the contextlib module
Group: Development/Python3

%description -n python3-module-%modulename
contextlib2 is a backport of the standard library's contextlib
module to earlier Python versions.

It also serves as a real world proving ground for possible
future enhancements to the standard library version.

%prep
%setup -n %modulename-%version

%if_with python3
cp -fR . ../python3
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
%python_sitelibdir/%modulename.*
%python_sitelibdir/%modulename-%version-*.egg-info

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/%modulename.*
%python3_sitelibdir/__pycache__/%modulename.*
%python3_sitelibdir/%modulename-%version-*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1.1
- NMU: Use buildreq for BR.

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.1
- Added module for Python 3

* Mon Apr 08 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4.0-alt1
- initial build for ALT Linux Sisyphus
