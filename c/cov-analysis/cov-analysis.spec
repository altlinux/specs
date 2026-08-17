%define _unpackaged_files_terminate_build 1

Name: cov-analysis
Version: 1.2
Release: alt1

Summary: afl-cov successor - simpler and using modern llvm tools
License: AGPL-3.0-or-later
Group: Development/Tools
VCS: https://github.com/AFLplusplus/cov-analysis
Url: https://github.com/AFLplusplus/cov-analysis

BuildArch: noarch

BuildRequires: python3
BuildRequires: /proc

Source: %name-%version.tar

%description
Replacing afl-cov and libfuzzer-cov with modern coverage gathering and great
features!

%prep
%setup

%install
mkdir -p %buildroot%_bindir
%makeinstall_std PREFIX=%prefix

%check
%make_build test

%files
%doc README.md LICENSE
%_bindir/cov-analysis

%changelog
* Mon Aug 17 2026 Egor Ignatov <egori@altlinux.org> 1.2-alt1
- New version 1.2.

* Thu Jul 16 2026 Egor Ignatov <egori@altlinux.org> 1.1-alt1
- New version 1.1.

* Mon Jun 29 2026 Egor Ignatov <egori@altlinux.org> 1.0-alt1
- New version 1.0.

* Thu Jun 04 2026 Egor Ignatov <egori@altlinux.org> 0.0.0.32.gita161e6d-alt1
- First build for ALT.
