%define oname dracclient
%def_with check
%def_with docs

Name: python3-module-%oname
Version: 8.0.0
Release: alt1.1

Summary: OpenStack Library for managing machines with Dell iDRAC cards

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/python-dracclient

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 1.6
BuildRequires: python3-module-lxml >= 2.3
BuildRequires: python3-module-requests >= 2.10.0

%if_with check
BuildRequires: python3-module-stestr
BuildRequires: python3-module-coverage >= 3.6
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-requests-mock >= 1.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-openstackdocstheme
%endif

%description
%summary.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package contains tests for %oname.

%if_with docs
%package doc
Summary: Documentation for %oname
Group: Development/Documentation

%description doc
This package contains documentation for %oname.
%endif

%prep
%setup -n %oname-%version

# Remove bundled egg-info
rm -rfv *.egg-info

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 doc/source html
# generate man page
sphinx-build-3 -b man doc/source man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/python-%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
# somehow it's missing
cat > .stestr.conf <<EOF
[DEFAULT]
test_path=${OS_TEST_PATH:-./dracclient/tests}
top_dir=./
EOF
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/python_dracclient-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 8.0.0-alt1.1
- Moved on modern pyproject macros.

* Wed Oct 19 2022 Grigory Ustinov <grenka@altlinux.org> 8.0.0-alt1
- Automatically updated to 8.0.0.

* Thu Oct 31 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus.
