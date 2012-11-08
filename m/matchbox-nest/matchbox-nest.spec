# BEGIN SourceDeps(oneline):
BuildRequires: libexpat-devel
# END SourceDeps(oneline)
%define name 	matchbox-nest
%define version 0.3
%define release %mkrel 5

Summary: 	X nesting for the Matchbox Desktop
Name: 		%name
Version: 	%version
Release: 	alt1_5
Url: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/matchbox-nest/0.3/%{name}-%{version}.tar.bz2

BuildRequires:	libmatchbox-devel libXtst-devel expat-devel
Source44: import.info

%description
X nesting for the panel from Matchbox.

%prep
%setup -q

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
* Thu Nov 08 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_5
- mageia import

