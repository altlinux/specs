Group: System/Libraries
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		libaesgm
Version:	20090429
Release:	alt2_20
License:	BSD
Summary:	Library implementation of AES (Rijndael) cryptographic methods
URL:		http://gladman.plushost.co.uk/oldsite/AES/index.php
Source0:	http://gladman.plushost.co.uk/oldsite/AES/aes-src-29-04-09.zip
Source1:	Makefile.aes
# Add fileencryption support
# http://www.gladman.me.uk/cryptography_technology/fileencrypt/
Patch0:		libaesgm-20090429-fileencrypt.patch

BuildRequires: gcc
Source44: import.info

%description
Library implementation of AES (Rijndael) cryptographic methods.

%package devel
Group: Development/Other
Summary:	Development files for libaesgm
Requires:	%{name} = %{version}-%{release}

%description devel
Development headers and libraries for libaesgm.

%prep
%setup -q -c -n %{name}-%{version}
cp %{SOURCE1} Makefile
%patch0 -p1 -b .fileencrypt
sed -i 's/\r//' *.txt

%build
make CFLAGS="%{optflags} -fPIC -DUSE_SHA1" LDFLAGS="%{build_ldflags}"

%install
make DESTDIR="%{buildroot}" LIBDIR="%{_libdir}" install



%files
%doc *.txt
%{_libdir}/libaesgm.so.*

%files devel
%{_includedir}/aes/
%{_libdir}/libaesgm.so

%changelog
* Sat Feb 16 2019 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_20
- fc merge

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 20090429-alt2_13
- update to new release by fcimport

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

