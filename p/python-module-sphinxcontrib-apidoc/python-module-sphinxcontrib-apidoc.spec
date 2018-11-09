%define  oname sphinxcontrib-apidoc
%def_with python3

Name:    python-module-%oname
Version: 0.3.0
Release: alt1

Summary: A Sphinx extension for running sphinx-apidoc on each build

License: BSD-2-Clause
Group:   Development/Python
URL:     https://pypi.org/project/sphinxcontrib-apidoc
# https://github.com/sphinx-contrib/apidoc

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools python-module-pbr

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools python3-module-pbr

BuildArch: noarch

Source:  %name-%version.tar

%description
sphinx-apidoc is a tool for automatic generation of Sphinx sources that,
using the autodoc extension, documents a whole package in the style of
other automatic API documentation tools. sphinx-apidoc does not actually build
documentation - rather it simply generates it.
As a result, it must be run before sphinx-build.

%package -n python3-module-%oname
Summary: A Sphinx extension for running sphinx-apidoc on each build
Group: Development/Python3

%description -n python3-module-%oname
sphinx-apidoc is a tool for automatic generation of Sphinx sources that,
using the autodoc extension, documents a whole package in the style of
other automatic API documentation tools. sphinx-apidoc does not actually build
documentation - rather it simply generates it.
As a result, it must be run before sphinx-build.

%prep
%setup

%if_with python3
cp -a . ../python3
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
%python_sitelibdir/sphinxcontrib/apidoc/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/sphinxcontrib/apidoc/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Fri Nov 09 2018 Grigory Ustinov <grenka@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus
