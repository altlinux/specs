%define   modulename agate-dbf
%def_with check
%def_with docs

Name:      python3-module-%modulename
Version:   0.2.4
Release:   alt2

Summary:   Adds read support for DBF files to agate

License:   MIT
Group:     Development/Python3
URL:       https://pypi.org/project/agate-dbf
VCS:       https://github.com/wireservice/agate-dbf

BuildArch: noarch

Packager:  Mikhail Gordeev <obirvalger@altlinux.org>

Source:    %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-agate
BuildRequires: python3-module-dbfread
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-furo
BuildRequires: python3-module-accessible-pygments
%endif

%description
%summary

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
# generate man page
sphinx-build-3 -b man docs man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%if_with docs
# install man page
install -pDm 644 man/%modulename.1 %buildroot%_man1dir/%modulename.1
%endif

%check
%pyproject_run_pytest

%files
%doc COPYING README.rst CHANGELOG.rst AUTHORS.rst
%python3_sitelibdir/agatedbf
%python3_sitelibdir/agate_dbf-%version.dist-info

%if_with docs
%files doc
%doc COPYING README.rst CHANGELOG.rst AUTHORS.rst html
%_man1dir/%modulename.1.*
%endif

%changelog
* Fri Mar 13 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt2
- Built with check.
- Built with docs.

* Tue Jan 13 2026 Grigory Ustinov <grenka@altlinux.org> 0.2.4-alt1
- Automatically updated to 0.2.4.

* Thu Jun 05 2025 Grigory Ustinov <grenka@altlinux.org> 0.2.3-alt1
- Automatically updated to 0.2.3.

* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus
