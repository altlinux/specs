Name: tasksh
Version: 1.0.0
Release: alt3

Summary: Shell for taskwarrior
License: MIT
Group: Office
Url: https://taskwarrior.org

Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake gcc-c++

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
* Fri Nov 30 2018 Grigory Ustinov <grenka@altlinux.org> 1.0.0-alt3
- Fixed build.
- Fixed summary.
- Fixed URL.

* Sun Dec 20 2015 Konstantin Artyushkin <akv@altlinux.org> 1.0.0-alt2
- initial build for ALT Linux Sisyphus

