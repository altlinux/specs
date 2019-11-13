%global oname sphinx-feature-classification

Name: python3-module-%oname
Version: 0.4.1
Release: alt1

Summary: Generate a matrix of pluggable drivers and their support to an API in Sphinx.

Group: Development/Python3
License: ASL 2.0
Url: http://docs.openstack.org/developer/%oname

Source: https://tarballs.openstack.org/%oname/%oname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 2.0
BuildRequires: python3-module-docutils >= 0.11

BuildRequires: python3-module-sphinx >= 1.5.1
BuildRequires: python3-module-reno >= 1.8.0
BuildRequires: python3-module-openstackdocstheme >= 1.17.0

%description
This is a Sphinx directive that allows creating matrices of drivers
a project contains and which features they support.
The directive takes an INI file with specific syntax explained
in the usage documentation to generate the matrices,
in which projects have the authority to say what is supported
within their own repository.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
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

%build
%python3_build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
python3 setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%python3_install

%files
%doc README.rst LICENSE ChangeLog
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files doc
%doc doc/build/html

%changelog
* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.1-alt1
- Automatically updated to 0.4.1.

* Tue Oct 29 2019 Grigory Ustinov <grenka@altlinux.org> 0.3.1-alt2
- Build without python2.

* Thu Dec 20 2018 Alexey Shabalin <shaba@altlinux.org> 0.3.1-alt1
- Initial build.
