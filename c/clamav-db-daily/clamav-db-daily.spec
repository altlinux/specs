%define dbname		daily
%define dir		var/lib/clamav-db
%define sys_clamav 	/var/lib/clamav
%define sys_db		/var/lib/clamav-db
%define checksum	e0d769d4bf4ba9749958051313d421f1

Name:    clamav-db-%dbname
Version: 20240531
Release: alt1

Summary: Antivirus database for ClamAV (%dbname)
Summary(ru): Антивирусная база для ClamAV (%dbname)
License: distributable
Group:   File tools
Url:     http://www.clamav.net/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

# https://packages.microsoft.com/clamav/daily.cvd
Source: %dbname.cvd

Requires: clamav

%description
Database %dbname.cvd for ClamAV virus scanner.

%description -l ru_RU.UTF-8
База для антивирусного сканера ClamAV %dbname.cvd

%prep

%install
install -pD %SOURCE0 %buildroot/%dir/%dbname.cvd

%check
test "$(md5sum "%buildroot%sys_db/%dbname.cvd" | cut -f1 -d' ')" = "%checksum"

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
* Fri May 31 2024 Kirill Izmestev <felixz@altlinux.org> 20240531-alt1
- Update database.

* Fri May 17 2024 Kirill Izmestev <felixz@altlinux.org> 20240517-alt1
- Update database.

* Fri Apr 19 2024 Kirill Izmestev <felixz@altlinux.org> 20240419-alt1
- Update database.

* Fri Apr 05 2024 Kirill Izmestev <felixz@altlinux.org> 20240405-alt1
- Update database.

* Thu Feb 21 2024 Kirill Izmestev <felixz@altlinux.org> 20240321-alt1
- Update database.

* Wed Feb 06 2024 Kirill Izmestev <felixz@altlinux.org> 20240306-alt1
- Update database.

* Tue Jan 09 2024 Kirill Izmestev <felixz@altlinux.org> 20240109-alt1
- Update database.

* Fri Dec 22 2023 Kirill Izmestev <felixz@altlinux.org> 20231222-alt1
- Update database.

* Fri Dec 08 2023 Kirill Izmestev <felixz@altlinux.org> 20231208-alt1
- Update database.

* Wed Nov 15 2023 Kirill Izmestev <felixz@altlinux.org> 20231115-alt1
- Update database.

* Fri Oct 27 2023 Kirill Izmestev <felixz@altlinux.org> 20231027-alt1
- Update database.

* Tue Oct 06 2023 Kirill Izmestev <felixz@altlinux.org> 20231006-alt1
- Update database.

* Tue Sep 19 2023 Kirill Izmestev <felixz@altlinux.org> 20230919-alt1
- Update database.

* Mon Sep 04 2023 Kirill Izmestev <felixz@altlinux.org> 20230904-alt1
- Update database.

* Thu Aug 03 2023 Kirill Izmestev <felixz@altlinux.org> 20230803-alt1
- Update database.

* Thu Jul 20 2023 Kirill Izmestev <felixz@altlinux.org> 20230720-alt1
- Update database.

* Thu Jul 6 2023 Kirill Izmestev <felixz@altlinux.org> 20230706-alt1
- Update database.

* Thu Jun 8 2023 Kirill Izmestev <felixz@altlinux.org> 20230622-alt1
- Update database.

* Thu Jun 8 2023 Kirill Izmestev <felixz@altlinux.org> 20230608-alt1
- Update database.

* Thu May 25 2023 Kirill Izmestev <felixz@altlinux.org> 20230525-alt1
- Update database.

* Thu May 11 2023 Kirill Izmestev <felixz@altlinux.org> 20230511-alt1
- Update database.

* Thu Apr 27 2023 Kirill Izmestev <felixz@altlinux.org> 20230427-alt1
- Update database.

* Thu Apr 13 2023 Kirill Izmestev <felixz@altlinux.org> 20230413-alt1
- Update database.

* Sat Mar 18 2023 Andrey Cherepanov <cas@altlinux.org> 20230318-alt1
- Update database.

* Tue Feb 28 2023 Andrey Cherepanov <cas@altlinux.org> 20230227-alt1
- Update database.

* Tue Feb 21 2023 Andrey Cherepanov <cas@altlinux.org> 20230220-alt1
- Update database from https://packages.microsoft.com/clamav.

* Tue Jan 19 2021 Andrey Cherepanov <cas@altlinux.org> 20210118-alt1
- Update database.

* Thu Jul 02 2020 Andrey Cherepanov <cas@altlinux.org> 20200601-alt1
- Update database.

* Sat Apr 18 2020 Andrey Cherepanov <cas@altlinux.org> 20200418-alt1
- Update database.

* Fri Nov 08 2019 Andrey Cherepanov <cas@altlinux.org> 20191107-alt1
- Update database.

* Fri May 10 2019 Andrey Cherepanov <cas@altlinux.org> 20190510-alt1
- Update database.

* Wed Apr 06 2016 Andrey Cherepanov <cas@altlinux.org> 20160404-alt1
- Update database
- Test checksum

* Mon Dec 28 2015 Andrey Cherepanov <cas@altlinux.org> 20151030-alt1
- Update database

* Tue Jan 27 2015 Andrey Cherepanov <cas@altlinux.org> 20150106-alt1
- Update database

* Wed Dec 24 2014 Andrey Cherepanov <cas@altlinux.org> 20141224-alt1
- Update database

* Sun Nov 30 2014 Andrey Cherepanov <cas@altlinux.org> 20141130-alt1
- Split clamav-db into undepended packages

