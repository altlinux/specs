%define _unpackaged_files_terminate_build 1
%define oname emails

Name: python3-module-%oname
Version: 0.6
Release: alt1
Summary: Modern python library for emails
License: Apache 2.0
Group: Development/Python3
Url: https://github.com/lavr/python-emails
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
Requires: python3-module-premailer

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
%python3_sitelibdir/*
%doc LICENSE README.*

%changelog
* Thu Aug 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.6-alt1
- New version

* Sat Mar 30 2019 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.15-alt1
- Initial build for ALT

