%define		php5_extension	array2arraymap-sdb

Name:	 	php5-%php5_extension
Version:	0.13
Release:	alt6

Summary:	php5 module to access static db (SDB) files.
Group:		System/Servers
License:	PHP License
Packager:	Igor Vlasenko <viy@altlinux.org>

Source0:	%name-%version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version
BuildRequires:	libmapsdb-devel >= 0.13 gcc-c++ libstdc++-devel
# for make test
BuildRequires:  php5-suhosin

%description
%{summary}

%prep
%setup -q

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
./configure \
	--enable-%php5_extension
%php5_make CC=g++

%install
# hack ...
# ln -s %_libdir/php/%_php5_version/extensions/suhosin.so modules/

%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 0.13-alt6
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 0.13-alt5
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 0.13-alt4
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 0.13-alt3
- Rebuild with php5-5.3.5.20110105-alt2

* Wed Feb 09 2011 Anton Farygin <rider@altlinux.ru> 0.13-alt2
- Rebuild with php5-5.3.5.20110105-alt1

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- build against libmapsdb 0.13

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt9
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt8
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt7
- Rebuild with php5-5.3.3.20100722-alt1

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt6
- rebuild with new php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt5
- Rebuild with php5-5.2.13.20100205-alt1

* Thu Feb 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.12-alt4
- re-release with win32 fixes

* Wed Feb 17 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt3.4
- Rebuild with php5-5.2.12.20091216-alt5

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt3.3
- Rebuild with php5-5.2.12.20091216-alt4

* Thu Jan 28 2010 Anton Farygin <rider@altlinux.ru> 0.12-alt3.2
- Rebuild with php5-5.2.12.20091216-alt1

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 0.12-alt3.1.1.1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Tue Feb 10 2009 Alexey Gladkov <legion@altlinux.ru> 0.12-alt3.1.1
- NMU: Rebuild with php5-5.2.9.20090205-alt1.

* Tue Oct 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3.1
- rebuild with new php

* Tue Sep 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt3
- rebuild with new php

* Wed May 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt2
- rebuild with new php

* Tue Oct 02 2007 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- built against libmapsdb 0.12

* Mon Sep 24 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- built against libmapsdb 0.11

* Mon Aug 06 2007 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- first Sisyphus version;
