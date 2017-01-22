%def_with python3

%define oname typing

Name: python-module-%oname
Version: 3.5.3
Release: alt1

Summary: This is a backport of the standard library typing module to Python versions older than 3.5
License: PSF
Group: Development/Python

Url: https://pypi.python.org/pypi/%oname/
Packager: Python Development Team <python at packages.altlinux.org>

Source: https://pypi.python.org/packages/b6/0c/53c42edca789378b8c05a5496e689f44e5dd82bc6861d1ae5a926ee51b84/%oname-%version.tar.gz

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

%package -n python3-module-%oname
Summary: This is a backport of the standard library typing module to Python versions older than 3.5
Group: Development/Python3

%description -n python3-module-%oname
Typing defines a standard notation for Python function and variable type
annotations. The notation can be used for documenting code in a concise,
standard format, and it has been designed to also be used by static and
runtime type checkers, static analyzers, IDEs and other tools.

%prep
%setup -n %oname-%version
%if_with python3
rm -fR ../python3-module-%oname-%version
cp -fR . ../python3-module-%oname-%version
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3-module-%oname-%version
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3-module-%oname-%version
%python3_install
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Mon Jan 23 2017 Anton Midyukov <antohami@altlinux.org> 3.5.3-alt1
- Initial build for ALT Linux Sisyphus.
