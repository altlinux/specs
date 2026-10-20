%define commit ca9cf5102ad012a3dd4e7b7765a7b1329e3489a6

Name: ubztopdf
Version: 0.20260314
Release: alt1

Summary: Convert OpenBoard .ubz documents to PDF

License: GPL-3.0-only
Group: Office
Url: https://github.com/Pesc0/ubztopdf

# Source-url: https://github.com/Pesc0/ubztopdf/archive/%commit.tar.gz?/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%description
ubztopdf extracts the SVG pages from OpenBoard (.ubz) archives and compiles
them into a single multi-page PDF document, one file per input.

%prep
%setup

%build

%install
install -Dpm755 ubztopdf.py %buildroot%_bindir/%name
subst '1s|.*|#!%__python3|' %buildroot%_bindir/%name

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.20260314-alt1
- initial build for Sisyphus

