%define oname seqdiag

Name:       python-module-%oname
Version:    0.9.6
Release:    alt1

Summary:    seqkdiag generate sequence-diagram image file from spec-text file

License:    ASLv2
Group:      Development/Python
URL:        https://pypi.org/project/seqdiag

Packager:   Grigory Ustinov <grenka@altlinux.org>

Source:     %oname-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools

BuildArch:  noarch

%description
seqdiag generates sequence-diagram image file from spec-text files.

Features:
- Generate sequence-diagram from dot like text (basic feature).
- Multilingualization for node-label (utf-8 only).

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install
%if ""=="3"
mv %buildroot%_bindir/seqdiag %buildroot%_bindir/seqdiag
%endif


%files
%doc *.rst
%_bindir/seqdiag
%python_sitelibdir/seqdiag_sphinxhelper.py
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%changelog
* Mon Sep 23 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.6-alt1
- Initial build for Sisyphus.
