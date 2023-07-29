# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fossology-nomos
Version: 4.3.0
Release: alt1
Summary: Nomos detects licenses and copyrights in a file
License: GPL-2.0-or-later
Group: Development/Other
Url: https://github.com/fossology/fossology

Provides: nomos
Provides: nomossa

Source: %name-%version.tar

BuildRequires: glib2-devel
BuildRequires: libjson-c-devel

%description
%summary.

This is only handy standalone nomos agent CLI, excluding other parts of full
FOSSology open source license compliance software system and toolkit.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
make -C src/nomos/agent -f Makefile.nomossa.altlinux \
       CFLAGS='%optflags -DVERSION_S=\"%version\" -DCOMMIT_HASH_S=\"%release\"'

%install
install -Dm0755 -p src/nomos/agent/nomossa %buildroot%_bindir/nomossa

%check
PATH=%buildroot%_bindir:$PATH
nomossa -V | grep '%version.*%release'
cp -a LICENSE /tmp
pushd /tmp
  date > no_lice
  time nomossa LICENSE | grep -xF 'File LICENSE contains license(s) GPL-2.0-only,LGPL-2.1-only'
  time nomossa no_lice | grep -xF 'File no_lice contains license(s) No_license_found'
popd
# Crash test.
nomossa -d .gear
nomossa -d LICENSES

%files
%doc README.md LICENSE src/nomos/agent/README src/nomos/agent/Notes
%_bindir/nomossa

%changelog
* Sun Jul 16 2023 Vitaly Chikunov <vt@altlinux.org> 4.3.0-alt1
- Update to 4.3.0 (2023-06-28).
- Note that upstream did controversial change of some GPL license shortnames,
  like GPL-2.0 => GPL-2.0-only, LGPL-2.1+ => LGPL-2.1-or-later.
- Do not basename(3) filenames when printing licenses.

* Mon Nov 14 2022 Vitaly Chikunov <vt@altlinux.org> 4.2.0-alt3
- spec: Remove needless BR on postgresql-devel and php.

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
