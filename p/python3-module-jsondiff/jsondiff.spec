%define oname jsondiff

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: Diff JSON and JSON-like structures in Python

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsondiff

# Source-url: https://pypi.io/packages/source/j/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

Conflicts: jdiff

%description
Diff JSON and JSON-like structures in Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%_bindir/jdiff
%python3_sitelibdir/*

%changelog
* Mon May 22 2023 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- new version 2.0.0 (with rpmrb script)
- add conflicts: jdiff (ALT bug 41297)

* Wed Apr 12 2023 Anton Vyatkin <toni@altlinux.org> 1.3.0-alt2
- Fix BuildRequires

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1.3.0-alt1
- new version 1.3.0 (with rpmrb script)

* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus
