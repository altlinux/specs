# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict


Name: neomutt
Version: 20260616
Release: alt1
Summary: A version of Mutt with added features
License: GPL-2.0-or-later
Group: Networking/Mail
Url: https://www.neomutt.org/
Vcs: https://github.com/neomutt/neomutt

Requires: mailcap
AutoReqProv: nopython nopython3

Source: %name-%version.tar
Source1: neomutt.desktop
Source2: neomutt.xpm

BuildRequires: docbook-style-xsl
BuildRequires: elinks
BuildRequires: libdb5.3-devel
BuildRequires: libgpgme-devel
BuildRequires: libidn2-devel
BuildRequires: liblua5-devel
BuildRequires: libncursesw-devel
BuildRequires: libnotmuch-devel
BuildRequires: libsasl2-devel
BuildRequires: libsqlite3-devel
BuildRequires: libssl-devel
BuildRequires: libzstd-devel
BuildRequires: tcl
BuildRequires: xsltproc
BuildRequires: zlib-devel

%description
Neomutt is a small but powerful text based program for reading and
sending electronic mail under UNIX operating systems, including support
for color terminals, MIME, OpenPGP, and a threaded sorting mode.

                      ==
                    ++
                   +..@@
                  +.,.+
       +          +.,.+  +++
      +          @+.,.+ +@@
    @+           +....+++.@
    +.@         @+.......+
    +.+         +@....+.+
    +.+        @+.....+.+
    +.+@       +@........++++
    +.@+      @+.........+;;>
    +..+++++++%%@$#.......+.--
    @@.@+&%%&+@%%@@.......+>->
     +..@+++@.@%%@$@......+++
     +.........@%%+@$$....+
    @@$.........@%%++@$..$+
    +@@..........*%%++@@$+
    +@@...........@%%++++
    +@$............@+
    +@@...#.......@+
    @+@.#$+@@@...$++
     +..$+@*@+..$+@+
    @@.@++++++$.+@*+
   @+..+*@@+=+@.+@.+
   +@..+++@+++@..++@@+@
   +@.....+@@+@.....+@.@
   +$.....+@*+$.....+@.+
   +@@.$..+@@+@@.$..+@.+
   @++++++@++@++++++@++@


%prep
%setup
%autopatch -p1
%ifarch %e2k
# can't find BerkeleyDB due to silly warning from LCC
sed -i 's/-E | tail -1/-w &/' auto.def
# error: expression must have a constant value
sed -i -E 's/.*struct ExpandoDefinition \*const (.*NoPadding) =(.*);/#define \1\2/' mutt_config.c send/config.c
%endif

%build
%define optflags_lto %nil
%add_optflags -ftrivial-auto-var-init=zero
%define docdir %_docdir/%name
%undefine _configure_gettext
%configure \
	--autocrypt \
	--bdb \
	--docdir=%docdir \
	--gpgme \
	--idn2 --disable-idn \
	--lua \
	--notmuch \
	--pkgconf \
	--sasl \
	--sqlite \
	--ssl \
	--zlib \
	--zstd \
	%nil
%make_build

%install
%makeinstall_std
install -Dpm0544 %SOURCE1 %buildroot%_desktopdir/neomutt.desktop
install -Dpm0544 %SOURCE2 %buildroot%_pixmapsdir/neomutt.xpm

%find_lang %name

%check
# Simplest test
%buildroot%_bindir/neomutt -v
# Great tests
export NEOMUTT_TEST_DIR=$PWD/test-files
pushd test-files
./setup.sh
popd
make -s test

%files -f %name.lang
%config(noreplace) %_sysconfdir/neomuttrc
%_bindir/neomutt
%_mandir/man?/*
%_libexecdir/neomutt*
%docdir
%_desktopdir/neomutt.desktop
%_pixmapsdir/neomutt.xpm
%_datadir/neomutt

%changelog
* Tue Jun 30 2026 Daniel Zagaynov <kotopesutility@altlinux.org> 20260616-alt1
- Update to 20260616 (2026-06-16).

* Tue May 05 2026 Vitaly Chikunov <vt@altlinux.org> 20260504-alt1
- Update to 20260504 (2026-05-04).

* Fri Apr 10 2026 Vitaly Chikunov <vt@altlinux.org> 20260406-alt1
- Update to 20260406 (2026-04-06).

* Tue Jan 06 2026 Vitaly Chikunov <vt@altlinux.org> 20260105-alt1
- Update to 20260105 (2026-01-05). The same as 20251211 with a revert of the
  Browser fix.

* Mon Dec 15 2025 Vitaly Chikunov <vt@altlinux.org> 20251211-alt1
- Update to 20251211 (2025-12-11).

* Fri Sep 12 2025 Vitaly Chikunov <vt@altlinux.org> 20250905-alt1
- Update to 20250905 (2025-09-05).

* Sat Jun 14 2025 Vitaly Chikunov <vt@altlinux.org> 20250510-alt2
- Unrandomize the right side of the Message-ID, as recommended by RFC 5322.

* Mon May 12 2025 Daniel Zagaynov <kotopesutility@altlinux.org> 20250510-alt1
- Update to 20250510 (2025-05-10).

* Thu Apr 10 2025 Daniel Zagaynov <kotopesutility@altlinux.org> 20250404-alt1
- Update to 20250404 (2025-04-04).

* Thu Feb 13 2025 Constantin Sunzow <protvin@altlinux.org> 20250113-alt2
- Rebuild against libdb-5.3.

* Mon Jan 13 2025 Daniel Zagaynov <kotopesutility@altlinux.org> 20250113-alt1
- Update to 20250113 (2025-01-13).

* Thu Jan 09 2025 Daniel Zagaynov <kotopesutility@altlinux.org> 20250109-alt1
- Update to 20250109 (2025-01-09).

* Sun Dec 15 2024 Vitaly Chikunov <vt@altlinux.org> 20241212-alt1
- Update to 20241212 (2024-12-12).

* Sun Dec 15 2024 Vitaly Chikunov <vt@altlinux.org> 20241114-alt1
- Update to 20241114 (2024-11-14), (fixes: CVE-2024-49393, CVE-2024-49394).

* Mon May 06 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 20240425-alt1.1
- Fixed build for Elbrus.

* Wed May 01 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 20240425-alt1
- Update to 20240425 (2024-04-25).

* Sat Mar 30 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 20240329-alt1
- Update to 20240329

* Sun Mar 24 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 20240323-alt1
- Update to 20240323 (2024-03-23).
- Update test-files.

* Thu Feb 01 2024 Daniel Zagaynov <kotopesutility@altlinux.org> 20240201-alt1
- Update to 20240201 (2024-02-01).

* Fri Dec 22 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 20231221-alt1
- Update to 20231221(2023-12-21).

* Sun Nov 05 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 20231103-alt1.4.g992c7938e
- Update to 20231103-4-g992c7938e.

* Thu Oct 26 2023 Vitaly Chikunov <vt@altlinux.org> 20231023-alt1
- Update to 20231023 (2023-10-23).

* Wed Oct 11 2023 Vitaly Chikunov <vt@altlinux.org> 20231006-alt1
- Update to 20231006 (2023-10-06).

* Fri May 19 2023 Vitaly Chikunov <vt@altlinux.org> 20230517-alt1
- Update to 20230517 (2023-05-17).

* Sun May 14 2023 Vitaly Chikunov <vt@altlinux.org> 20230512-alt1
- Update to 20230512 (2023-05-12).

* Sat Apr 08 2023 Vitaly Chikunov <vt@altlinux.org> 20230407-alt1
- Update to 20230407 (2023-04-07).

* Thu Mar 23 2023 Vitaly Chikunov <vt@altlinux.org> 20230322-alt1
- Update to 20230322 (2023-03-22).

* Wed Nov 02 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 20220429-alt2.1
- Fixed build for Elbrus.

* Wed Oct 12 2022 Vitaly Chikunov <vt@altlinux.org> 20220429-alt2
- spec: Fix build with libgpg-error-1.46.

* Tue May 03 2022 Vitaly Chikunov <vt@altlinux.org> 20220429-alt1
- Update to 20220429.
- Enable Native Language Support (NLS).
- Enable Autocrypt support.
- Package documentation in non-versioned directory.
- Package desktop files.

* Wed Nov 03 2021 Vitaly Chikunov <vt@altlinux.org> 20211029-alt1
- Update to 20211029.

* Sun Oct 24 2021 Vitaly Chikunov <vt@altlinux.org> 20211022-alt1
- Update to 20211022-6-g4c9fa28537 (2021-10-24).
- Do not apply color groups patch.

* Mon Jul 05 2021 Alexey Gladkov <legion@altlinux.ru> 20210205-alt2.1
- Add color groups for header and body.

* Sun Jul 04 2021 Vitaly Chikunov <vt@altlinux.org> 20210205-alt2
- Fix CVE-2021-32055.

* Sun Feb 07 2021 Vitaly Chikunov <vt@altlinux.org> 20210205-alt1
- Update to 20210205.

* Mon Nov 30 2020 Vitaly Chikunov <vt@altlinux.org> 20201127-alt1
- Update to 20201127.

* Wed Nov 25 2020 Vitaly Chikunov <vt@altlinux.org> 20201120-alt1
- Update to 20201120.

* Sun Sep 27 2020 Vitaly Chikunov <vt@altlinux.org> 20200925-alt1
- Update to 20200925.

* Sat Sep 05 2020 Vitaly Chikunov <vt@altlinux.org> 20200821-alt2
- Fix alias parsing (closes: 38891).

* Mon Aug 24 2020 Vitaly Chikunov <vt@altlinux.org> 20200821-alt1
- Update to 20200821.

* Mon Aug 17 2020 Vitaly Chikunov <vt@altlinux.org> 20200814-alt1
- Update to 20200814.

* Tue Aug 11 2020 Vitaly Chikunov <vt@altlinux.org> 20200807-alt1
- Update to 20200807.

* Wed Jul 01 2020 Vitaly Chikunov <vt@altlinux.org> 20200626-alt1
- Update to 20200626.

* Tue May 05 2020 Vitaly Chikunov <vt@altlinux.org> 20200501-alt1
- Update to 20200501.

* Mon Apr 27 2020 Vitaly Chikunov <vt@altlinux.org> 20200424-alt1
- Update to 20200424.

* Sat Apr 18 2020 Vitaly Chikunov <vt@altlinux.org> 20200417-alt1
- Update to 20200417.
- Enable zlib, zstd, sqlite.
- spec: Add %%check section with tests.

* Thu Apr 09 2020 Vitaly Chikunov <vt@altlinux.org> 20200320-alt1
- Update to 20200320.

* Mon Nov 26 2018 Vitaly Chikunov <vt@altlinux.ru> 20180716-alt2
- Switch from libidn to libidn2

* Wed Aug 29 2018 Vitaly Chikunov <vt@altlinux.org> 20180716-alt1
- NeoMutt release 20180716

* Wed Feb 21 2018 Vitaly Chikunov <vt at altlinux.org> 20180221-alt1
- initial build for ALT Linux Sisyphus
