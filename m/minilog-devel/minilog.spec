%define        _name minilog

Name:          %_name-devel
Version:       0.1
Release:       alt0.2
Summary:       A minimal header only C++ logger system
License:       BSD-2-Clause
Group:         Development/C
Url:           https://github.com/dominikschnitzer/minilog
Vcs:           https://github.com/dominikschnitzer/minilog.log
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         fix.patch

%description
A minimal header only C++ logger system.


%prep
%setup
%autopatch

%install
install -Dm644 %_name.h %buildroot%_includedir/%_name/%_name.h


%files
%doc README*
%_includedir/%_name


%changelog
* Sat May 02 2026 Pavel Skrylev <majioa@altlinux.org> 0.1-alt0.2
- ! fixed call to class method of Log.

* Mon Sep 28 2020 Pavel Skrylev <majioa@altlinux.org> 0.1-alt0.1
- initial build for Sisyphus
