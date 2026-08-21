Name: rdfind
Version: 1.8.0
Release: alt1
Summary: Program that finds duplicate files
Group: File tools
License: GPL-2.0-or-later
Url: https://rdfind.pauldreik.se
Vcs: https://github.com/pauldreik/rdfind
BuildRequires: libnettle-devel
BuildRequires: gcc-c++
Source0: %name-%version.tar

%description
Rdfind is a program that finds duplicate files.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc COPYING AUTHORS ChangeLog README.* TODO
%_bindir/*
%_man1dir/%{name}*

%changelog
* Sat Aug 22 2026 Aleksandr Shamaraev <shad@altlinux.org> 1.8.0-alt1
- 1.3.4 -> 1.8.0
- changed license

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.3.4-alt2
- NMU: remove %ubt from release

* Fri Dec 30 2016 Sergey Novikov <sotor@altlinux.org> 1.3.4-alt1%ubt
- Added ubt tag for simplifying backporting process

* Fri Dec 23 2016 Sergey Novikov <sotor@altlinux.org> 1.3.4-alt1
- initial packaging
