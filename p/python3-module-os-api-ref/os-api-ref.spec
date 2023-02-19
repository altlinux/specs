%define oname os-api-ref
%def_without check
%def_with docs

Name: python3-module-%oname
Version: 2.3.0
Release: alt1.1

Summary: Sphinx Extensions to support API reference sites in OpenStack

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/os-api-ref

Source: %oname-%version.tar
Source1: %oname.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-pbr >= 2.0.0
BuildRequires: python3-module-yaml >= 3.12

%if_with check
BuildRequires: python3-module-hacking >= 3.0.1
BuildRequires: python3-module-coverage >= 4.0
BuildRequires: python3-module-testtools >= 2.2.0
BuildRequires: python3-module-sphinx-testing >= 1.0.1
BuildRequires: python3-module-beautifulsoup4 >= 4.6.0
BuildRequires: python3-module-stestr >= 2.0.0
BuildRequires: python3-module-pre-commit >= 2.6.0
%endif

%if_with docs
BuildRequires: python3-module-sphinx >= 4.0.0
BuildRequires: python3-module-openstackdocstheme >= 2.2.1
%endif

%description
This project is a collection of sphinx stanzas that assist in building
an API Reference site for an OpenStack project in RST. RST is great
for unstructured English, but displaying semi structured (and
repetitive) data in tables is not its strength. This provides tooling
to insert semi-structured data describing request and response
parameters and status or error messages, and turn those into nice tables.

The project also includes a set of styling (and javascript) that is
expected to layer on top of a Sphinx theme base. This addition
provides a nice set of collapsing sections for REST methods and
javascript controls to expand / collapse all sections.

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
install -pDm 644 man/%oname.1 %buildroot%_man1dir/%oname.1
%endif

%check
%__python3 -m stestr run

%files
%doc LICENSE AUTHORS ChangeLog *.rst
%python3_sitelibdir/os_api_ref
%python3_sitelibdir/os_api_ref-%version.dist-info
%exclude %python3_sitelibdir/os_api_ref/tests

%files tests
%python3_sitelibdir/os_api_ref/tests

%if_with docs
%files doc
%doc LICENSE *.rst html
%_man1dir/%oname.1.xz
%endif

%changelog
* Sun Feb 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1.1
- Moved on modern pyproject macros.

* Tue Oct 18 2022 Grigory Ustinov <grenka@altlinux.org> 2.3.0-alt1
- Automatically updated to 2.3.0.
- Renamed spec file.

* Thu Jul 30 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.0-alt2
- Transfer on python3.
- Fix license.

* Wed Dec 12 2018 Alexey Shabalin <shaba@altlinux.org> 1.6.0-alt1
- Initial packaging
