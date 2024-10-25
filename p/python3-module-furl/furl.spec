%define  oname furl

%def_with check

Name:    python3-module-%oname
Version: 2.1.3
Release: alt3

Summary: URL parsing and manipulation made easy

License: Unlicense
Group:   Development/Python3
URL:     https://pypi.org/project/furl
VCS:     https://github.com/gruns/furl

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
BuildRequires: python3-module-orderedmultidict
%endif

BuildArch: noarch

Source:  %name-%version.tar

Patch: furl-2.1.3-use-ipadress-library.patch

%description
%summary

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
# https://github.com/gruns/furl/issues/176
%pyproject_run_pytest -k'not test_odd_urls'

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%doc *.md

%changelog
* Fri Oct 25 2024 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt3
- Moved to modern pyproject macros.
- Disabled failing test.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt2
- Fixed FTBFS.

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt1
- Automatically updated to 2.1.3.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus.
