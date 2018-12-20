%global oname sphinx-feature-classification

Name: python-module-%oname
Version: 0.3.1
Release: alt1
Summary: Generate a matrix of pluggable drivers and their support to an API in Sphinx.

Group: Development/Python
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname
Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 2.0.0
BuildRequires: python-module-docutils >= 0.11

BuildRequires: python-module-sphinx >= 1.5.1
BuildRequires: python-module-reno >= 1.8.0
BuildRequires: python-module-openstackdocstheme >= 1.17.0

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-docutils >= 0.11

BuildRequires: python3-module-sphinx >= 1.5.1
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme >= 1.17.0

%description
This is a Sphinx directive that allows creating matrices of drivers
a project contains and which features they support.
The directive takes an INI file with specific syntax explained
in the usage documentation to generate the matrices,
in which projects have the authority to say what is supported within their own repository.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Generate a matrix of pluggable drivers and their support to an API in Sphinx.
Group: Development/Python3

%description -n python3-module-%oname
This is a Sphinx directive that allows creating matrices of drivers
a project contains and which features they support.
The directive takes an INI file with specific syntax explained
in the usage documentation to generate the matrices,
in which projects have the authority to say what is supported within their own repository.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package contains tests for %oname.

%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
Documentation for %oname.

%prep
%setup -n %oname-%version
# Remove bundled egg-info
rm -rf %oname.egg-info

sed -i '/warning-is-error/d' setup.cfg

rm -rf ../python3
cp -a . ../python3


%build
%python_build
pushd ../python3
%python3_build
popd

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}


%install
%python_install

pushd ../python3
%python3_install
popd


%files
%doc README.rst LICENSE ChangeLog
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files -n python3-module-%oname
%doc README.rst LICENSE ChangeLog
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Thu Dec 20 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.1-alt1
- Initial build.
