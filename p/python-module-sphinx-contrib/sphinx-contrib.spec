%define oname sphinxcontrib
%define pname python-module-sphinxcontrib
Name: python-module-sphinx-contrib
Version: 0.2.1
Release: alt1.hg20150829.1
Summary: A collection of Sphinx extensions
License: BSD
Group: Development/Python
Url: https://bitbucket.org/birkenfeld/sphinx-contrib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/birkenfeld/sphinx-contrib/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx

%description
This repository contains a collection of Sphinx extensions maintained by
their respective authors. It is not an official part of Sphinx.

%package -n %pname.traclinks
Summary: Adds a docutils role to create links to a Trac instance
License: MIT
Group: Development/Python
%py_provides %oname.traclinks
%py_requires %oname

%description -n %pname.traclinks
This Sphinx extension adds a docutils role to create links to a Trac
instance.

%prep
%setup

%build
pushd traclinks
%python_build
popd

%install
pushd traclinks
%python_install
popd

%files -n %pname.traclinks
%doc traclinks/*.rst
%python_sitelibdir/%oname/traclinks.*
%python_sitelibdir/traclinks-*.egg-info

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.hg20150829.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.hg20150829
- Initial build for Sisyphus

