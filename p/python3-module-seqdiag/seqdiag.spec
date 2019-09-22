%define oname seqdiag

Name:       python3-module-%oname
Version:    0.9.6
Release:    alt1

Summary:    seqkdiag generate sequence-diagram image file from spec-text file

License:    ASLv2
Group:      Development/Python3
URL:        https://pypi.org/project/seqdiag

Packager:   Grigory Ustinov <grenka@altlinux.org>

Source:     %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools

BuildArch:  noarch

%description
seqdiag generates sequence-diagram image file from spec-text files.

Features:
- Generate sequence-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
%if "3"=="3"
mv %buildroot%_bindir/seqdiag %buildroot%_bindir/seqdiag3
%endif


%files
%doc *.rst
%_bindir/seqdiag3
%python3_sitelibdir/seqdiag_sphinxhelper.py
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info

%changelog
* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus.
