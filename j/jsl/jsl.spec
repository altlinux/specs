%define _unpackaged_files_terminate_build 1
%def_with check

Name: jsl
Version: 0.3.0
Release: alt1%ubt

Summary: Check JavaScript code for common mistakes
License: MPLv1.1
Group: Development/Tools

Url: http://javascriptlint.com

Source: %name-%version.tar
Patch0: jsl-0.3.0-smash.patch
Patch1: jsl-0.3.0-tests.patch
Patch2: 0001-Disable-support-for-READLINE-and-EDITLINE.patch

BuildRequires(pre): rpm-build-ubt
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
* Wed Feb 21 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt1%ubt
- Initial build

