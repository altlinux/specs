# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libaesgm
Version:	20090429
Release:	alt2_12
License:	BSD
Summary:	Library implementation of AES (Rijndael) cryptographic methods
URL:		http://gladman.plushost.co.uk/oldsite/AES/index.php
Source0:	http://gladman.plushost.co.uk/oldsite/AES/aes-src-29-04-09.zip
Source1:	Makefile.aes
# Add fileencryption support
# http://www.gladman.me.uk/cryptography_technology/fileencrypt/
Patch0:		libaesgm-20090429-fileencrypt.patch
Group:		System/Libraries
Source44: import.info

%description
Library implementation of AES (Rijndael) cryptographic methods.

%package devel
Summary:	Development files for libaesgm
Group:		Development/C
Requires:	%{name} = %{version}

%description devel
Development headers and libraries for libaesgm.

%prep
%setup -q -c -n %{name}-%{version}
cp %{SOURCE1} Makefile
%patch0 -p1 -b .fileencrypt
sed -i 's/\r//' *.txt

%build
make CFLAGS="%{optflags} -fPIC -DUSE_SHA1"

%install
make DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" install

%files
%doc *.txt
%{_libdir}/libaesgm.so.*

%files devel
%{_includedir}/aes/
%{_libdir}/libaesgm.so

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_12
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_8
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_7
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_6
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_5
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_4
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 20090429-alt1_4
- initial import by fcimport

