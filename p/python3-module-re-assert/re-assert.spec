Name:    python3-module-re-assert
Version: 1.1.0
Release: alt1

Summary: show where your regex match assertion failed!

License: MIT
Group:   Development/Python3
URL:     https://github.com/asottile/re-assert

Source:  %name-%version.tar

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/re_assert.py
%python3_sitelibdir/__pycache__/re_assert.*.pyc
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus.
