%define  oname bidi

%def_with check

Name:    python3-module-%oname
Version: 0.4.2
Release: alt1

Summary: BIDI algorithm related functions

License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/MeirKriheli/python-bidi

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-six
%endif

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test-3 -v

%files
%doc *.rst
%_bindir/py%oname
%python3_sitelibdir/%oname
%python3_sitelibdir/*.egg-info

%changelog
* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus.
