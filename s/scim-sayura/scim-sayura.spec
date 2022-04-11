# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: scim-sayura
Version: 0.3.3
Release: alt1
Summary: Sri Lankan input method for SCIM
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv2
Url: http://sinhala.sourceforge.net/
Source: http://sinhala.sourceforge.net/files/%name-%version.tar.gz
Patch0: scim-sayura-0.3.0-fix-constructor.patch
Patch1: scim-sayura-aarch64.patch
BuildRequires: scim-devel
Requires: scim
Source44: import.info

%description
This package provides a Sinhala Trans input method for SCIM.

%prep
%setup
%patch0 -p1 -b .fix-constructor
%patch1 -p1 -b .aarch64-support

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%_libdir/scim-1.0/*/*/*.la

%files
%doc README AUTHORS COPYING
%_libdir/scim-1.0/*/IMEngine/sayura.so
%_datadir/scim/icons/scim-sayura.png

%changelog
* Mon Apr 11 2022 Ilya Mashkin <oddity@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Sat Oct 17 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.3.0-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.3.0-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_12
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_11
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_10
- initial fc import

