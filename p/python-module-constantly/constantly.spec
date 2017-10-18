%def_with python3
%def_without check

%define oname constantly
Name: python-module-%oname
Version: 15.1.0
Release: alt3

Summary: Symbolic constants in Python

Url: http://github.com/twisted/constantly
License: X11
Group: Development/Python
BuildArch: noarch

# https://github.com/twisted/constantly.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: git-core

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

#setup_python_module %oname

%description
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.


%package -n python3-module-%oname
Summary: Symbolic constants in Python
Group: Development/Python3

%description -n python3-module-%oname
A library that provides symbolic constant support.
It includes collections and constants with text, numeric, and bit flag values.
Originally ``twisted.python.constants`` from the `Twisted <https://twistedmatrix.com/>`_ project.


%prep
%setup

git config --global user.email "<python@packages.altlinux.org>"
git config --global user.name "Python Development Team"
git init-db
git add . -A
git commit -a -m "REL: v%version"
git tag -m "v%version" v%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test

%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-constantly
%python3_sitelibdir/*
%endif

%changelog
* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt3
- Fixed egg-info version.

* Wed Aug 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 15.1.0-alt2
- Enabled build for python-3.

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 15.1.0-alt1
- initial build for ALT Sisyphus

