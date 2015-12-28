%define dbname		daily
%define dir		var/lib/clamav-db
%define sys_clamav 	/var/lib/clamav
%define sys_db		/var/lib/clamav-db
%define checksum	1669087ad25cd3d49e047bbe59b95b8b

Name:    clamav-db-%dbname
Version: 20151030
Release: alt1

Summary: Antivirus database for ClamAV (%dbname)
Summary(ru): Антивирусная база для ClamAV (%dbname)
License: distributable
Group:   File tools
Url:     http://www.clamav.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source: %dbname.cvd

Requires: clamav

%description
Database %dbname.cvd for ClamAV virus scanner.

%description -l ru_RU.UTF-8
База для антивирусного сканера ClamAV %dbname.cvd

%prep

%install
install -pD %SOURCE0 %buildroot/%dir/%dbname.cvd

%post
for base in %dbname
do
    if test ! -e %sys_clamav/$base.cvd -o %sys_db/$base.cvd -nt %sys_clamav/$base.cvd 
    then
    	yes | cp -fp %sys_db/$base.cvd %sys_clamav/$base.cvd 2>/dev/null
	chmod 0664 %sys_clamav/$base.cvd 2>/dev/null
    fi
done

%files
%attr(664,mail,root) %config(noreplace) /%dir/%dbname.cvd

%changelog
* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 20151030-alt1
- Update database

* Tue Jan 27 2015 Andrey Cherepanov <cas@altlinux.org> 20150106-alt1
- Update database

* Wed Dec 24 2014 Andrey Cherepanov <cas@altlinux.org> 20141224-alt1
- Update database

* Sun Nov 30 2014 Andrey Cherepanov <cas@altlinux.org> 20141130-alt1
- Split clamav-db into undepended packages

