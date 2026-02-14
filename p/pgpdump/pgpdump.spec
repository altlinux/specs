%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: pgpdump
Version: 0.37
Release: alt1

Summary: A PGP packet visualizer
License: BSD-3-Clause
Group: File tools
Url: https://www.mew.org/~kazu/proj/pgpdump/
Vcs: https://github.com/kazu-yamamoto/pgpdump

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-valgrind
BuildRequires: bzlib-devel
BuildRequires: zlib-devel
%{?!_without_check:%{?!_disable_check:
%ifarch %valgrind_arches
BuildRequires: valgrind
%endif
}}

%description
pgpdump is a PGP packet visualizer which displays the packet format of
OpenPGP (RFC 4880) and PGP version 2 (RFC 1991).

The output of this command is similar to the one of GnuPG's `list
packets' command, however, pgpdump produces a more detailed and easier
to understand.

%prep
%setup

%build
%if 0%{?fanalyzer}
%define optflags_lto %nil
%add_optflags -fanalyzer -Werror
%endif
%autoreconf
%configure
%make

%install
install -D pgpdump %buildroot%_bindir/pgpdump
install -D pgpdump.1 %buildroot%_man1dir/pgpdump.1

%check
./pgpdump -v |& grep -P '^pgpdump version \Q%version,'
%ifarch %valgrind_arches
%define valgrind valgrind -q --error-exitcode=2 --track-origins=yes
sed -Ei.bak '/got=/s/"\$\{PGPDUMP\}"/%valgrind &/' test/test
! diff -u test/test test/test.bak || exit 3
%endif
%make_build check

%files
%doc ChangeLog.md COPYRIGHT README.md
%_bindir/pgpdump
%_man1dir/pgpdump.*

%changelog
* Fri Feb 13 2026 Vitaly Chikunov <vt@altlinux.org> 0.37-alt1
- Update to v0.37 (2026-02-12).

* Mon Jan 29 2024 Vitaly Chikunov <vt@altlinux.org> 0.36-alt1
- Update to v0.36 (2024-01-29).

* Sun May 22 2022 Vitaly Chikunov <vt@altlinux.org> 0.35-alt1
- Updated to v0.35 (2022-02-28).

* Mon Apr 13 2020 Pavel Vasenkov <pav@altlinux.org> 0.33-alt1
- New version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.26-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun May 24 2009 Yury Yurevich <anarresti@altlinux.org> 0.26-alt1
- initial build
