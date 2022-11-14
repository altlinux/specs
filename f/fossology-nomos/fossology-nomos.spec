# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fossology-nomos
Version: 4.2.0
Release: alt2

Summary: Architecture for analyzing software, nomos standalone
License: GPL-2.0-or-later
Group: Other
Url: https://github.com/fossology/fossology

Source: %name-%version.tar

Provides: nomos
Provides: nomossa

BuildRequires: glib2-devel
BuildRequires: libicu-devel
BuildRequires: libjson-c-devel
BuildRequires: perl-Text-Template
BuildRequires: postgresql-devel
BuildRequires: gcc-c++
BuildRequires: /usr/bin/php

%description
The FOSSology project is a web based framework that allows you to
upload software to be picked apart and then analyzed by software
agents which produce results that are then browsable via the web
interface. Existing agents include license analysis, metadata
extraction, and MIME type identification.

This package contains the nomos agent programs and their resources.

%prep
%setup

sed -i 's/egrep/grep -E/g' $(grep -rl egrep src/nomos/agent)
sed -i 's/fgrep/grep -F/g' $(grep -rl fgrep src/nomos/agent)

%build
make build-lib
make -C src/nomos/agent -f Makefile.sa all \
       VERSION=%version COMMIT_HASH=%release

%install
install -Dm0755 -p src/nomos/agent/nomossa %buildroot%_bindir/nomossa

%check
PATH=%buildroot%_bindir:$PATH
cp -a LICENSE /tmp
pushd /tmp
  date > no_lice
  time nomossa LICENSE | grep ' GPL-2\.0,LGPL-2\.1$'
  time nomossa no_lice | grep ' No_license_found$'
popd
# Crash test.
nomossa -d .gear

%files
%doc README.md LICENSE src/nomos/agent/README src/nomos/agent/Notes
%_bindir/nomossa

%changelog
* Mon Nov 14 2022 Michael Shigorin <mike@altlinux.org> 4.2.0-alt2
- Explicit BR: gcc-c++.

* Sat Nov 12 2022 Vitaly Chikunov <vt@altlinux.org> 4.2.0-alt1
- Updated to 4.2.0 (2022-11-11).

* Thu May 26 2022 Vitaly Chikunov <vt@altlinux.org> 4.1.0-alt1
- Updated to 4.1.0 (2022-05-20).

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
