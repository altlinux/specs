%define dir		var/lib/clamav-db
%define sys_clamav 	/var/lib/clamav
%define sys_db		/var/lib/clamav-db

Name: clamav-db
Version: 20120521
Release: alt1

Summary: Antivirus database for ClamAV
Summary(ru-RU.UTF-8): Антивирусная база для ClamAV
License: distributable
Group: File tools
Url: http://www.clamav.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source1: main.cvd
Source2: daily.cvd
Source3: bytecode.cvd
Source4: safebrowsing.cvd

Requires: clamav

%description
Database for ClamAV virus scanner.
Last update: May 21, 2012

%description -l ru_RU.UTF-8
База для антивирусного сканера ClamAV
Последнее обновление: 21.05.2012

%prep

%install
%__install -pD %SOURCE1 %buildroot/%dir/main.cvd
%__install -pD %SOURCE2 %buildroot/%dir/daily.cvd
%__install -pD %SOURCE3 %buildroot/%dir/bytecode.cvd
%__install -pD %SOURCE4 %buildroot/%dir/safebrowsing.cvd

%post
for base in main daily bytecode
do
    if test ! -e %sys_clamav/$base.cvd -o %sys_db/$base.cvd -nt %sys_clamav/$base.cvd 
    then
    	yes | cp -fp %sys_db/$base.cvd %sys_clamav/$base.cvd 2>/dev/null
	chmod 0664 %sys_clamav/$base.cvd 2>/dev/null
    fi
done

%files
%attr(664,mail,root) %config(noreplace) /%dir/main.cvd
%attr(664,mail,root) %config(noreplace) /%dir/daily.cvd
%attr(664,mail,root) %config(noreplace) /%dir/bytecode.cvd
%attr(664,mail,root) %config(noreplace) /%dir/safebrowsing.cvd

%changelog
* Mon May 21 2012 Andrey Cherepanov <cas@altlinux.org> 20120521-alt1
- Update database

* Tue Mar 15 2011 Andrey Cherepanov <cas@altlinux.org> 20110315-alt1
- Update database
- Fix permission on database files to update via freshclam

* Mon Dec 06 2010 Andrey Cherepanov <cas@altlinux.org> 20101206-alt1
- update database
- add bytecode.cvd and safebrowsing.cvd databases
- disable safebrowsing.cvd

* Wed Dec 01 2010 Andrey Cherepanov <cas@altlinux.org> 20101201-alt1
- update database
- fix owner and group for correct update

* Fri Feb 26 2010 Andrey Cherepanov <cas@altlinux.org> 20100226-alt1
- Update database

* Sat Oct 24 2009 Andrey Cherepanov <cas@altlinux.org> 20091024-alt2
- Update database

* Fri Apr 17 2009 Andrey Cherepanov <cas@altlinux.org> 20090410-alt2
- Remove data from package summary 

* Fri Apr 10 2009 Andrey Cherepanov <cas@altlinux.org> 20090410-alt1
- Update database

* Mon May 19 2008 Andrey Cherepanov <cas@altlinux.ru> 20080519-alt1
- Update database

* Fri Apr 18 2008 Andrey Cherepanov <cas@altlinux.ru> 20080418-alt2
- Fix old database

* Fri Apr 18 2008 Andrey Cherepanov <cas@altlinux.ru> 20080418-alt1
- Update database
- Add copy database files if they are newer than files in /var/lib/clamav

* Fri Feb 08 2008 Andrey Cherepanov <cas@altlinux.ru> 20080207-alt1
- Fix build number for branch

* Thu Feb 07 2008 Andrey Cherepanov <cas@altlinux.ru> 20080207-alt0
- Update database
- Fix permission
- Add noreplace behaviour (does not replace freshen database)

* Wed Feb 06 2008 Andrey Cherepanov <cas@altlinux.ru> 20080206-alt0
- Place database into /var/lib/clamav-db for avoid conflicts with freshen database in /var/lib/clamav
- Fix permission to update database from KlamAV

* Thu Jan 31 2008 Andrey Cherepanov <cas@altlinux.ru> 20080131-alt0
- initial release for ALT Linux Sysyphus
