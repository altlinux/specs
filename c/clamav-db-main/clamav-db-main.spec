%define dbname		main
%define dir		var/lib/clamav-db
%define sys_clamav 	/var/lib/clamav
%define sys_db		/var/lib/clamav-db
%define checksum	a22e1b59c5e8b8eff166271b08b4ad72

Name:    clamav-db-%dbname
Version: 20170608
Release: alt1

Summary: Antivirus database for ClamAV (%dbname)
Summary(ru): Антивирусная база для ClamAV (%dbname)
License: distributable
Group:   File tools
Url:     http://www.clamav.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source: %dbname.cvd

Requires:  clamav
Provides:  clamav-db = %EVR
Obsoletes: clamav-db < %EVR

# Requires other databases
Requires:  clamav-db-daily
Requires:  clamav-db-bytecode

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

%check
test "$(md5sum "%buildroot%sys_db/%dbname.cvd" | cut -f1 -d' ')" = "%checksum"

%files
%attr(664,mail,root) %config(noreplace) /%dir/%dbname.cvd

%changelog
* Fri May 10 2019 Andrey Cherepanov <cas@altlinux.org> 20170608-alt1
- Update database.
- Remove clamav-db-safebrowsing requirement for clamav-db.

* Wed Apr 06 2016 Andrey Cherepanov <cas@altlinux.org> 20160317-alt1
- Update database
- Test checksum

* Sun Nov 30 2014 Andrey Cherepanov <cas@altlinux.org> 20130918-alt1
- Split clamav-db into undepended packages

