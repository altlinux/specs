%define _unpackaged_files_terminate_build 1

Name: wlc
Version: 2.1.1
Release: alt1

Summary: Weblate commandline client

License: GPL-3.0-or-later
Group: Development/Tools
Url: https://github.com/WeblateOrg/wlc

# Source-url: https://github.com/WeblateOrg/wlc/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE README.md
%_bindir/wlc
%python3_sitelibdir/wlc/
%python3_sitelibdir/%{pyproject_distinfo wlc}/

%changelog
* Mon Jul 27 2026 Boris Yumankulov <boria138@altlinux.org> 2.1.1-alt1
- initial build for ALT Sisyphus

