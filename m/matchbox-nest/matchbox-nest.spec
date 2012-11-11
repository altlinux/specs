# BEGIN SourceDeps(oneline):
BuildRequires: libexpat-devel
# END SourceDeps(oneline)
Requires: xorg-xnest
%define name 	matchbox-nest
%define version 0.3
%define release 5

Summary: 	X nesting for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	alt2_5
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/matchbox-nest/0.3/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel libXtst-devel expat-devel
Source44: import.info
Patch33: matchbox-nest-0.3-alt-Xnest-path.patch

%description
X nesting for the panel from Matchbox.

%prep
%setup -q
%patch33 -p1

%build
%configure
%make

%install
%makeinstall

%files
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/%name




%changelog
* Sun Nov 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt2_5
- bugfix release

* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_5
- mageia import

