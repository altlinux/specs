Name: rdfind
Version: 1.3.4
Release: alt1%ubt
Summary: Program that finds duplicate files
Group: File tools
License: GPLv2
Url: https://rdfind.pauldreik.se/
BuildRequires(pre): rpm-build-ubt
BuildRequires: libnettle-devel
BuildRequires: gcc-c++
Source0: %name-%version.tar

%description
Rdfind is a program that finds duplicate files.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall

%files
%doc COPYING
%_bindir/*
%_man1dir/%{name}*

%changelog
* Fri Dec 30 2016 Sergey Novikov <sotor@altlinux.org> 1.3.4-alt1%ubt
- Added ubt tag for simplifying backporting process

* Fri Dec 23 2016 Sergey Novikov <sotor@altlinux.org> 1.3.4-alt1
- initial packaging
