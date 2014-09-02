%define modulename dbfpy

%def_without python3

Name: python-module-%modulename
Version: 2.3.0
Release: alt1

%setup_python_module %modulename

Summary: Python module for accessing .dbf (xBase) files
License: Public domain
Group: Development/Python
Url: http://dbfpy.sourceforge.net/
Source: %name-%version.tar
BuildArch: noarch
BuildPreReq: python-module-setuptools
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
dbfpy can read and write simple DBF-files. The DBF-format
was developed about 30 years ago and was used by a number
of simple database applications (dBase, Foxpro, Clipper, ...).
The basic datatypes numbers, short text, and dates are available.
Many different extensions have been used; dbfpy can read and write
only simple DBF-files.

%package -n python3-module-%modulename
Summary: Python module for accessing .dbf (xBase) files
Group: Development/Python3

%description -n python3-module-%modulename
dbfpy can read and write simple DBF-files. The DBF-format
was developed about 30 years ago and was used by a number
of simple database applications (dBase, Foxpro, Clipper, ...).
The basic datatypes numbers, short text, and dates are available.
Many different extensions have been used; dbfpy can read and write
only simple DBF-files.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc README CHANGES
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%doc README CHANGES
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1
- Version 2.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.5-alt1.1
- Rebuild with Python-2.7

* Wed Oct 27 2010 Egor Glukhov <kaman@altlinux.org> 2.2.5-alt1
- Initial build for Sisyphus

