Name: timewarrior
Version: 1.10.0
Release: alt1

Summary: Timewarrior is a command line time tracking application
License: MIT
Group: Office

Url: https://github.com/GothenburgBitFactory/timewarrior
Vcs: https://github.com/GothenburgBitFactory/timewarrior

Source: %name-%version.tar
Source1: libshared.tar

BuildPreReq: cmake rpm-macros-cmake
BuildRequires: gcc-c++ asciidoctor

%description
Timewarrior is a time tracking utility that offers simple stopwatch features as
well as sophisticated calendar-base backfill, along with flexible reporting. It
is a portable, well supported and very active Open Source project.

%prep
%setup
tar -xf %SOURCE1 -C src/ 

%build
%cmake -DCMAKE_BUILD_TYPE=release
%cmake_build

%install
%cmake_install
mv %buildroot/%_docdir/timew %buildroot/%_docdir/%name-%version
#removed static library and include files
#this dont needed for packing
rm -rv %buildroot/usr/lib
rm -rv %buildroot/usr/include

%files
%doc AUTHORS ChangeLog *.md ext/
%_bindir/*
%_mandir/man1/*
%_mandir/man7/*

%changelog
* Mon Aug 03 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.10.0-alt1
- 1.2.0 -> 1.10.0
- changed URL & added VCS

* Sun Mar 08 2020 Kirill Maslinsky <kirill@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Feb 28 2019 Kirill Maslinsky <kirill@altlinux.org> 1.1.1-alt1
- initial build

