# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
# Cannot be enabled due to librrpage.so:
# %%define _stripped_files_terminate_build 1
# Workaround for https://github.com/rr-debugger/rr/issues/2977
%filter_from_requires /^libc.so.6(GLIBC_PRIVATE)/d

Name:		rr
Version:	5.5.0
Release:	alt2
Summary:	Record and Replay Framework
Group:		Development/Debuggers
License:	MIT and BSD and Apache-2.0
URL:		https://rr-project.org/
Vcs:		https://github.com/mozilla/rr.git
# Upstream issue tracker: https://github.com/mozilla/rr/issues/

Provides:	rr-project = %EVR
Obsoletes:	rr-project <= 5.3.0-alt1

Source:		%name-%version.tar
ExclusiveArch:	x86_64
Requires:	gdb

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-python3
BuildRequires:	cmake
BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	capnproto-devel

%description
rr is a lightweight tool for recording, replaying and debugging execution of
applications (trees of processes and threads). Debugging extends gdb with very
efficient reverse-execution, which in combination with standard gdb/x86
features like hardware data watchpoints, makes debugging much more fun.

Supported microarchitectures are Intel Nehalem (2010) or later.

%prep
%setup -q
subst "s!/bin/!/lib/rr/!" src/replay_syscall.cc
subst "s!/bin/rr_page_!lib/rr/rr_page_!" src/AddressSpace.cc

%build
%add_optflags -Wno-error=class-memaccess -Wno-error=unused-result
%cmake -Ddisable32bit=ON -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install
mv %buildroot/%_bindir/rr_* %buildroot%_libdir/rr/
subst '1s:/usr/bin/bash:/bin/bash:' %buildroot%_bindir/signal-rr-recording.sh
rm -f %buildroot%_bindir/rr_page*
# Workaround for https://github.com/rr-debugger/rr/issues/2977
rm -f %buildroot%_libdir/rr/librraudit.so

%files
%doc LICENSE README.md
%_bindir/rr
%_bindir/signal-rr-recording.sh
%_bindir/rr-collect-symbols.py
%_datadir/rr
%_datadir/bash-completion/completions/rr
%_libdir/rr

%changelog
* Wed Oct 13 2021 Vitaly Chikunov <vt@altlinux.org> 5.5.0-alt2
- Do not install librraudit.so (fixes build for glibc-2.34).

* Sat Oct 09 2021 Vitaly Chikunov <vt@altlinux.org> 5.5.0-alt1
- Update to 5.5.0 (2021-09-20).

* Sat Jun 12 2021 Arseny Maslennikov <arseny@altlinux.org> 5.4.0-alt3
- NMU: spec: adapt to new cmake macros.

* Sun Dec 27 2020 Vitaly Chikunov <vt@altlinux.org> 5.4.0-alt2
- spec: Temporary disable '-Werror=class-memaccess'.
- spec: Update licenses.

* Thu Oct 29 2020 Vitaly Chikunov <vt@altlinux.org> 5.4.0-alt1
- Update to 5.4.0 (2020-10-29).
- spec: Rename from rr-project to rr.

* Fri Mar 27 2020 Vitaly Chikunov <vt@altlinux.org> 5.3.0-alt1
- Update to 5.3.0.

* Sat Nov 30 2019 Vitaly Chikunov <vt@altlinux.org> 5.2.0.0.253.g4c734005-alt1
- Update to 5.2.0-253-g4c734005.

* Thu Jun 14 2018 Vitaly Chikunov <vt@altlinux.ru> 5.2.0-alt1
- First build of rr for ALT.

