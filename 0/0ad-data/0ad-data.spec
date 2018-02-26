%define origversion r08832
%define gamename 0ad

Name:    	0ad-data
Version:        0.%origversion
Release:        alt1

Summary:        The Data Files for 0 A.D.
Summary(ru_RU.UTF-8): Файлы ресурсов для игры 0 A.D.

License:        CC-BY-SA
Group:          Games/Strategy
Url:            http://wildfiregames.com/0ad/

Packager: 	Anton Chernyshov <ach@altlinux.org>
Source0:        %gamename-%origversion-alpha-unix-data.tar

BuildArch:      noarch

BuildPreReq: 	perl-Spreadsheet-ParseExcel
BuildPreReq: 	perl-OLE-Storage_Lite

%description
Files that needed to play in 0 A.D.

%description -l ru_RU.UTF-8
Файлы ресурсов необходимые для игры 0 A.D.

%prep
%setup -n %gamename-%origversion-alpha

%install
mkdir -p %buildroot/%_gamesdatadir/%gamename
mv binaries/data/* %buildroot/%_gamesdatadir/%gamename/

%files
%_gamesdatadir/%gamename/*

%changelog
* Mon Dec 13 2010 Anton Chernyshov <ach@altlinux.org> 0.r08832-alt1
- new upstream release - r08832

* Thu Nov 4 2010 Anton Chernyshov <ach@altlinux.org> 0.r08413-alt1
- fix game version
- fix package changelog according to distribution rules

* Fri Oct 26 2010 Anton Chernyshov <ach@altlinux.org> r08413-alt1
- new upstream release - r08413

* Tue Oct 19 2010 Anton Chernyshov <ach@altlinux.org> r07970-alt1
- create spec file and first build
