%define  oname uritools

%def_with check

Name:    python3-module-%oname
Version: 4.0.1
Release: alt1

Summary: URI parsing, classification and composition

License: MIT
Group:   Development/Python3
URL:     https://github.com/tkem/uritools

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info

%changelog
* Mon Jan 09 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus.
