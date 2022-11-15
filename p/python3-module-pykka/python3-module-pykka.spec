%define _unpackaged_files_terminate_build 1
%define mname pykka

Name: python3-module-%mname
Version: 2.0.2
Release: alt1.1
Summary: Python implementation of the actor model
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/jodal/pykka
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme

%description
Pykka is a Python implementation of the actor model.
The actor model introduces some simple rules to control
the sharing of state and cooperation between execution units,
which makes it easier to build concurrent applications.

%package -n %name-tests
Summary: Python implementation of the actor model
Group: Development/Python3
BuildArch: noarch
Requires: %name

%description -n %name-tests
This package contains tests for %name.

%package -n %name-docs
Summary: Python implementation of the actor model
Group: Development/Python3
BuildArch: noarch

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%mname/tests

%description -n %name-docs
This package contains docs for %name.

%prep
%setup
sed -i "s/sphinx-build/sphinx-build-3/" docs/Makefile

%build
%python3_build
pushd docs
make html

%install
%python3_install
mkdir -p %buildroot%python3_sitelibdir/%mname/docs
cp -pr tests %buildroot%python3_sitelibdir/%mname
cp -pr docs/_build/html/* %buildroot%python3_sitelibdir/%mname/docs

%files
%python3_sitelibdir/%mname
%python3_sitelibdir/Pykka-%version-py%_python3_version.egg-info
%exclude %python3_sitelibdir/%mname/docs
%exclude %python3_sitelibdir/%mname/tests
%doc LICENSE

%files -n %name-tests
%python3_sitelibdir/%mname/tests

%files -n %name-docs
%python3_sitelibdir/%mname/docs

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 2.0.2-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Mon Jan 27 2020 Alexander Makeenkov <amakeenk@altlinux.org> 2.0.2-alt1
- Initial build for ALT
