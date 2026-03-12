%define   modulename sphinx-basic-ng
%define   pypi_name sphinx_basic_ng
%define   stage .beta2
%def_without docs

Name:      python3-module-%modulename
Version:   1.0.0
Release:   alt0.2%stage

Summary:   A modernised skeleton for Sphinx themes

License:   MIT
Group:     Development/Python3
URL:       https://pypi.org/project/sphinx-basic-ng
VCS:       https://github.com/pradyunsg/sphinx-basic-ng

BuildArch: noarch

Source:    %name-%version.tar

BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-myst-parser
BuildRequires: python3-module-sphinx-copybutton
BuildRequires: python3-module-sphinx-inline-tabs
BuildRequires: python3-module-furo
%endif

Provides: python3-module-%pypi_name
Provides: python3-module-basic-ng

%description
%summary.

%if_with docs
%package doc
Summary: Documentation for %modulename
Group: Development/Documentation

%description doc
This package contains documentation for %modulename.
%endif

%prep
%setup

%build
%pyproject_build

%if_with docs
export PYTHONPATH="$PWD"
# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%files
%doc LICENSE README.md
%python3_sitelibdir_noarch/%pypi_name
%python3_sitelibdir_noarch/%pypi_name-%{version}b2.dist-info

%if_with docs
%files doc
%doc LICENSE README.md html
%endif

%changelog
* Wed Mar 11 2026 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt0.2.beta2
- Built package according to generally accepted norms.

* Thu Mar 28 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.beta2
- Initial build for ALTLinux.
