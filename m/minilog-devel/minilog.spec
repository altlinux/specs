%define        _name minilog

Name:          %_name-devel
Version:       0.1
Release:       alt0.1
Summary:       A minimal header only C++ logger system
License:       BSD-2-Clause
Group:         Development/C
Url:           https://github.com/dominikschnitzer/minilog
Vcs:           https://github.com/dominikschnitzer/minilog.log
BuildArch:     noarch

Source:        %name-%version.tar

%description
%summary.


%prep
%setup

%install
install -Dm644 %_name.h %buildroot%_includedir/%_name/%_name.h


%files
%doc README*
%_includedir/%_name


%changelog
* Mon Sep 28 2020 Pavel Skrylev <majioa@altlinux.org> 0.1-alt0.1
- initial build for Sisyphus
