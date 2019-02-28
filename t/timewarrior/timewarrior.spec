Name: timewarrior
Version: 1.1.1
Release: alt1

Summary: Timewarrior is a command line time tracking application
License: MIT
Group: Office

Url: https://taskwarrior.org/docs/timewarrior/
Source: %name-%version.tar
Packager: Kirill Maslinsky <kirill@altlinux.org>
Patch0:                %name-%version-%release.patch

BuildPreReq: cmake rpm-macros-cmake
BuildRequires: gcc-c++

%description
Timewarrior is a time tracking utility that offers simple stopwatch features as
well as sophisticated calendar-base backfill, along with flexible reporting. It
is a portable, well supported and very active Open Source project.

%prep
%setup

%build
%cmake_insource
%make_build # VERBOSE=1

%install
%makeinstall_std
%find_lang %name
mv %buildroot/%_docdir/timew %buildroot/%_docdir/%name-%version

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README.md CONTRIBUTING.md
%_bindir/*
%_man1dir/*


%changelog
* Thu Feb 28 2019 Kirill Maslinsky <kirill@altlinux.org> 1.1.1-alt1
- initial build

