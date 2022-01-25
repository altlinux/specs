# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fossology-nomos
Version: 4.0.0
Release: alt1

Summary: Architecture for analyzing software, nomos standalone
License: GPL-2.0-or-later
Group: Other
Url: https://github.com/fossology/fossology

Source: %name-%version.tar

Provides: nomos
Provides: nomossa

BuildRequires: glib2-devel
BuildRequires: libjson-c-devel
BuildRequires: postgresql-devel

%description
The FOSSology project is a web based framework that allows you to
upload software to be picked apart and then analyzed by software
agents which produce results that are then browsable via the web
interface. Existing agents include license analysis, metadata
extraction, and MIME type identification.

This package contains the nomos agent programs and their resources.

%prep
%setup

%build
# Hackish way to build. Build nomos (required to fulfill all dependencies)
# and then rebuild agent in standalone way. `rm *.o` to rebuild, so there
# is no weird errors, such as `FATAL nomos_utils.c.803: "" is not a plain file'.
%make_build -C src/nomos
rm -f src/nomos/agent/*.o
%make_build -C src/nomos/agent -f Makefile.sa nomossa \
	VERSION=%version COMMIT_HASH=%release

%install
install -Dm0755 -p src/nomos/agent/nomossa %buildroot%_bindir/nomossa

%check
src/nomos/agent/nomossa LICENSE  | grep ' GPL-2\.0,LGPL-2\.1$'
src/nomos/agent/nomossa Makefile | grep ' No_license_found$'
# Crash test.
src/nomos/agent/nomossa -d .gear

%files
%doc README.md LICENSE src/nomos/agent/README src/nomos/agent/Notes
%_bindir/nomossa

%changelog
* Tue Jan 25 2022 Vitaly Chikunov <vt@altlinux.org> 4.0.0-alt1
- Updated to 4.0.0 (2022-01-21).

* Wed Aug 04 2021 Vitaly Chikunov <vt@altlinux.org> 3.11.0-alt1
- Update to 3.11.0 (2021-07-30).

* Mon May 10 2021 Vitaly Chikunov <vt@altlinux.org> 3.10.0-alt1
- Update to 3.10.0 (2021-05-07).

* Thu Dec 10 2020 Vitaly Chikunov <vt@altlinux.org> 3.9.0-alt2
- Fix build on gcc 10.2.1.

* Wed Dec 02 2020 Vitaly Chikunov <vt@altlinux.org> 3.9.0-alt1
- Update to 3.9.0 (2020-11-30).

* Tue May 05 2020 Vitaly Chikunov <vt@altlinux.org> 3.8.0-alt1
- Update to 3.8.0.
- Add %%check section to spec.

* Wed Dec 11 2019 Vitaly Chikunov <vt@altlinux.org> 3.6.0.0.89.g9cbe36ba0-alt2
- Rebuild to make directory scan actually work.

* Tue Dec 10 2019 Vitaly Chikunov <vt@altlinux.org> 3.6.0.0.89.g9cbe36ba0-alt1
- First release for ALT.
