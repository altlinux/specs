%define oname sphinxcontrib
%define pname python3-module-sphinxcontrib

Name: python3-module-sphinx-contrib
Version: 0.2.1
Release: alt2

Summary: A collection of Sphinx extensions
License: BSD
Group: Development/Python3
Url: https://bitbucket.org/birkenfeld/sphinx-contrib/
# hg clone https://bitbucket.org/birkenfeld/sphinx-contrib/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx


%description
This repository contains a collection of Sphinx extensions maintained by
their respective authors. It is not an official part of Sphinx.

%package -n %pname.traclinks
Summary: Adds a docutils role to create links to a Trac instance
License: MIT
Group: Development/Python3
%py3_provides %oname.traclinks
%py3_requires %oname

%description -n %pname.traclinks
This Sphinx extension adds a docutils role to create links to a Trac
instance.

%prep
%setup

%build
pushd traclinks
%python3_build
popd

%install
pushd traclinks
%python3_install
popd

%files -n %pname.traclinks
%doc traclinks/*.rst
%python3_sitelibdir/%oname/traclinks.*
%python3_sitelibdir/traclinks-*.egg-info
%python3_sitelibdir/%oname/__pycache__/


%changelog
* Thu Nov 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- python2 -> python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.1-alt1.hg20150829.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.hg20150829
- Initial build for Sisyphus

