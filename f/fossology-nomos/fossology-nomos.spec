# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: fossology-nomos
Version: 4.2.0
Release: alt3
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

%prep
%setup

sed -i 's/egrep/grep -E/g' $(grep -rl egrep src/nomos/agent)
sed -i 's/fgrep/grep -F/g' $(grep -rl fgrep src/nomos/agent)

# Unhide building steps.
sed -i '/(MAKE).* -s /s/ -s / /g' $(grep -rl '\$(MAKE).* -s ' --include=Makefile'*' )

# Skip linking what is not needed for nomossa - libfossology with postgresql
# interface.
sed -i '/FO_LDFLAGS/s/-lfossology//' Makefile.conf
sed -i '/FO_LDFLAGS/s/-lpq//' Makefile.conf
# Without PG this creates empty `-I' option which consumes next option (where
# is by the luck glib-2.0 include dir).
sed -i '/FO_CFLAGS/s/-I\$(PG_INCLUDEDIR)//' Makefile.conf

%build
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
