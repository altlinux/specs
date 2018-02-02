%def_with python3

%define modname typing

Name: python-module-%modname
Version: 3.6.4
Release: alt1

Summary: This is a backport of the standard library typing module to Python versions older than 3.6
License: PSF
Group: Development/Python

Url: https://pypi.python.org/pypi/%modname/
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.io/packages/source/t/%modname/%modname-%version.tar.gz

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
#-tests python3-module-setuptools_scm
%endif
BuildRequires: python-module-setuptools
#python-devel python-module-setuptools-tests python-module-setuptools_scm

%description
Typing defines a standard notation for Python function and variable type
annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and
runtime type checkers, static analyzers, IDEs and other tools.

%package -n python3-module-%modname
Summary: This is a backport of the standard library typing module to Python versions older than 3.6
Group: Development/Python3

%description -n python3-module-%modname
Typing defines a standard notation for Python function and variable type
annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and
runtime type checkers, static analyzers, IDEs and other tools.

%prep
%setup -n %modname-%version
%if_with python3
rm -fR ../python3-module-%modname-%version
cp -fR . ../python3-module-%modname-%version
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3-module-%modname-%version
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%modname-%version
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%modname
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.6.4-alt1
- 3.6.4

* Thu Jul 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Jan 23 2017 Anton Midyukov <antohami@altlinux.org> 3.5.3-alt1
- Initial build for ALT Linux Sisyphus.
