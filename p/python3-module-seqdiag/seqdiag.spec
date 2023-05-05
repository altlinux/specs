%define oname seqdiag

Name:       python3-module-%oname
Version:    3.0.0
Release:    alt1

Summary:    seqkdiag generate sequence-diagram image file from spec-text file

License:    Apache-2.0
Group:      Development/Python3
URL:        https://pypi.org/project/seqdiag

Packager:   Grigory Ustinov <grenka@altlinux.org>

Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch:  noarch

%description
seqdiag generates sequence-diagram image file from spec-text files.

Features:
- Generate sequence-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst
%_bindir/seqdiag
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/tests

%changelog
* Fri Apr 28 2023 Anton Vyatkin <toni@altlinux.org> 3.0.0-alt1
- NMU: New version 3.0.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt1
- Build new version.

* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus.
