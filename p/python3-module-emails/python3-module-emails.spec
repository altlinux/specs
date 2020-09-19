%define _unpackaged_files_terminate_build 1
%define oname emails

Name: python3-module-%oname
Version: 0.6
Release: alt2
Summary: Modern python library for emails
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/lavr/python-emails
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
%add_python3_req_skip tests

%description
Features
- HTML-email message abstraction
- Method to transform html body:
- css inlining (using peterbe's premailer)
- image inlining
- DKIM signature
- Message loaders
- Send directly or via django email backend


%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/make_rfc822.py
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%doc LICENSE README.rst

%changelog
* Sat Sep 19 2020 Alexander Makeenkov <amakeenk@altlinux.org> 0.6-alt2
- Fixed requires
- Fixed license name
- Fixed %files section

* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6-alt1
- New version

* Sat Mar 30 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.15-alt1
- Initial build for ALT

