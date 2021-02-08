%define _unpackaged_files_terminate_build 1
%def_with check

Name: jsl
Version: 0.3.0
Release: alt4

Summary: Check JavaScript code for common mistakes
License: MPL-1.1 or GPL-2.0+ or LGPL-2.1+
Group: Development/Tools

Url: http://javascriptlint.com

Source: %name-%version.tar
Patch0: jsl-0.3.0-smash.patch
Patch1: jsl-0.3.0-tests.patch
Patch2: 0001-Disable-support-for-READLINE-and-EDITLINE.patch
Patch3: 0002-Fix-build-for-aarch64.patch
Patch4: 0003-Fix-build-against-GCC10.patch

BuildRequires: perl-devel

%if_with check
BuildRequires: perl-base
%endif

%description
With JavaScript Lint, you can check all your JavaScript source code for
common mistakes without actually running the script or opening the web page.

JavaScript Lint holds an advantage over competing lints because it is based
on the JavaScript engine for the Firefox browser. This provides a robust
framework that can not only check JavaScript syntax but also examine the
coding techniques used in the script and warn against questionable
practices.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build

JS_PERLCONNECT=1 %make -C src -f Makefile.ref OBJDIR=../BUILD

%install
install -d %buildroot%_bindir
install BUILD/jsl %buildroot%_bindir

%check
cd tests
perl run_tests.pl ../BUILD/jsl

%files
%_bindir/jsl

%changelog
* Mon Feb 08 2021 Stanislav Levin <slev@altlinux.org> 0.3.0-alt4
- Fixed FTBFS(GCC10).

* Wed Mar 13 2019 Ivan A. Melnikov <iv@altlinux.org> 0.3.0-alt3
- Fix build on mipsel.

* Sun Sep 09 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2
- Build for aarch64.

* Wed Feb 21 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1
- Initial build

