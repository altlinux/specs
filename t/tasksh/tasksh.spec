Name: tasksh
Version: 1.0.0
Release: alt2

Summary: Shell for taswarrior
License: MIT
Group: Office
Url: https://git.tasktools.org/projects/EX/repos/tasksh/browse

Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake gcc5-c++

%description
%summary

%prep
%setup

%build
%cmake_insource
%make_build # VERBOSE=1

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc %_docdir/%name
%_bindir/tasksh
%_man1dir/tasksh.1.xz

%changelog
* Sun Dec 20 2015 Konstantin Artyushkin <akv@altlinux.org> 1.0.0-alt2
- initial build for ALT Linux Sisyphus

