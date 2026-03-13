%define   modulename agate
%def_with check
%def_with docs

Name:      python3-module-%modulename
Version:   1.14.2
Release:   alt2

Summary:   A Python data analysis library that is optimized for humans instead of machines

License:   MIT
Group:     Development/Python3
URL:       https://pypi.org/project/agate
VCS:       https://github.com/wireservice/agate

BuildArch: noarch

Packager:  Mikhail Gordeev <obirvalger@altlinux.org>

Source:    %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-parsedatetime
BuildRequires: python3-module-isodate
BuildRequires: python3-module-pytimeparse
BuildRequires: python3-module-slugify
BuildRequires: python3-module-leather
%endif

%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-furo
BuildRequires: python3-module-accessible-pygments
%endif

%description
agate is a Python data analysis library that is optimized for humans instead of
machines. It is an alternative to numpy and pandas that solves real-world
problems with readable code.

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
%python3_sitelibdir/%modulename/
%python3_sitelibdir/%modulename-%version.dist-info

%if_with docs
%files doc
%doc COPYING README.rst CHANGELOG.rst AUTHORS.rst html
%_man1dir/%modulename.1.*
%endif

%changelog
* Fri Mar 13 2026 Grigory Ustinov <grenka@altlinux.org> 1.14.2-alt2
- Built with check.
- Built with docs.

* Sun Mar 01 2026 Grigory Ustinov <grenka@altlinux.org> 1.14.2-alt1
- Automatically updated to 1.14.2.

* Tue Jan 20 2026 Grigory Ustinov <grenka@altlinux.org> 1.14.1-alt1
- Automatically updated to 1.14.1.

* Tue Jan 13 2026 Grigory Ustinov <grenka@altlinux.org> 1.14.0-alt1
- Automatically updated to 1.14.0.

* Thu Jun 05 2025 Grigory Ustinov <grenka@altlinux.org> 1.13.0-alt1
- Automatically updated to 1.13.0.

* Tue Apr 25 2023 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.1-alt1
- New version 1.7.1.

* Wed Feb 07 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.0-alt1
- Initial build for Sisyphus
