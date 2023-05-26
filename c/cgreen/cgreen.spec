Name: cgreen
Version: 1.6.2
Release: alt1

Summary: Framework for unit testing, written in C
License: ISC
Group: Development/C
Url: http://www.lastcraft.com/cgreen.php

Source0: %name-%version.tar

BuildRequires: cmake rpm-macros-cmake gcc gcc-c++

%define _unpackaged_files_terminate_build 1

%description 
What is it? It's a framework for unit testing, written in C. A tool
for C developers writing tests of their own code.

If you have used JUnit, or any of the xUnit clones, you will find
the concept familiar. In particular the tool supports a range of
assertions, composable test suites and setup/teardown facilities.
Because of the peculiarities of C programming, each test function
is normally run in it's own process.

NOTE: this package includes a slightly modified version of cgreen. Check
http://git.altlinux.ru/people/voins/packages/?p=cgreen.git for list of changes


%prep
%setup -q

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc README.md samples

%_bindir/%name-runner
%_bindir/%name-debug

%_includedir/*
%_libdir/*.so*

%_libdir/cmake/%name/*.cmake

%_man1dir/*
%_man5dir/*

%_datadir/bash-completion/completions/*


%changelog
* Tue May 09 2023 Vladimir Rubanov <august@altlinux.org> 1.6.2-alt1
- Upgrade version to 1.6.2
- Switch to standard packaging.

* Tue Mar 30 2021 Mikhail Efremov <sem@altlinux.org> 1.0-alt3
- Fix License tag.
- Use _unpackaged_files_terminate_build.
- Fix packaging on 32bit arches.

* Mon Jun 16 2014 Mikhail Efremov <sem@altlinux.org> 1.0-alt2
- Fix build.

* Mon Jan 07 2008 Alexey Voinov <voins@altlinux.ru> 1.0-alt1
- initial build
