# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: girar-summary
Version: 1.1
Release: alt1
Summary: Summarize task build in a table
License: GPL-2.0-only
Group: Development/Other
BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build

%check
make test

%install
mkdir -p %buildroot%_bindir
install -p -m755 girar-summary      %buildroot%_bindir
install -p -m755 girar-summary-task %buildroot%_bindir

%files
%_bindir/girar-summary
%_bindir/girar-summary-task

%changelog
* Fri Jul 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Support SRPM builds.
- Add tests.

* Thu Jul 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt2
- Fix executable perms.

* Wed Jul 22 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- Version 1.0.
