%define  oname furl

%def_with check

Name:    python3-module-%oname
Version: 2.1.3
Release: alt2

Summary: URL parsing and manipulation made easy

License: Unlicense
Group:   Development/Python3
URL:     https://github.com/gruns/furl

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

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
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%doc *.md

%changelog
* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt2
- Fixed FTBFS.

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.3-alt1
- Automatically updated to 2.1.3.

* Fri Jun 24 2022 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus.
