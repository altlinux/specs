# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1

Name: girar-summary
Version: 1.10
Release: alt1
Summary: Summarize task build in a table
License: GPL-2.0-only
Group: Development/Other

Source: %name-%version.tar
BuildRequires: banner
BuildRequires: gcc-c++
BuildRequires: libre2-devel

%description
%summary

%prep
%setup

%build
make

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
* Tue Apr 30 2024 Vitaly Chikunov <vt@altlinux.org> 1.10-alt1
- Fix FTBFS with newer libre2.

* Sat Mar 20 2021 Vitaly Chikunov <vt@altlinux.org> 1.9-alt1
- Only account widths for non-empty tasks.

* Sat Mar 20 2021 Vitaly Chikunov <vt@altlinux.org> 1.8-alt1
- Fix warning if stdin is a tty.

* Wed Mar 17 2021 Vitaly Chikunov <vt@altlinux.org> 1.7-alt1
- Switch to c++20.
- Bug fixes, code robustification, and rearrangements.

* Tue Mar 09 2021 Vitaly Chikunov <vt@altlinux.org> 1.6-alt1
- C++ version of girar-summary.
- Extract kernel-modules name from a tag.
- Fix test-only and resumed tasks detection for NNRs.
- Detect and mark removed subtasks.

* Wed Feb 24 2021 Vitaly Chikunov <vt@altlinux.org> 1.5-alt1
- Fix treat "build OK (cached)" as NNR for src.rpm.

* Sun Dec 27 2020 Vitaly Chikunov <vt@altlinux.org> 1.4-alt1
- Treat "build OK (cached)" as NNR.

* Sun Aug 02 2020 Vitaly Chikunov <vt@altlinux.org> 1.3-alt1
- Rename 'repo' column to 'name'.

* Fri Jul 31 2020 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- Fix SRPMs processing.
- Process 'build swiftly' sub-tasks as NNRs.
- Show skipped, swiftly [skipped], and NNR sub-tasks with a dash.
- Do not output lines w/o any builds.

* Fri Jul 24 2020 Vitaly Chikunov <vt@altlinux.org> 1.1-alt1
- Support SRPM builds.
- Add tests.

* Thu Jul 23 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt2
- Fix executable perms.

* Wed Jul 22 2020 Vitaly Chikunov <vt@altlinux.org> 1.0-alt1
- Version 1.0.
