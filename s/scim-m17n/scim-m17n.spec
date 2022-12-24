Group: System/Libraries
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           scim-m17n
Version:        0.2.3
Release:        alt3_31
Summary:        SCIM IMEngine for m17n-lib

License:        GPL-2.0-or-later
URL:            https://github.com/scim-im/scim-m17n
Source0:        %{name}-%{version}.tar.gz

Buildrequires:  scim-devel, libm17n-devel
BuildRequires:  gcc-c++

#Obsoletes:      iiimf-le-unit <= 1:12.2
Requires:       scim >= 1.4.4

Patch0:         %{name}-no-M17N-prefix.patch
Patch1:         %{name}-aarch64.patch
Patch2: scim-m17n-configure-c99.patch
Source44: import.info

%description
scim-m17n provides a SCIM IMEngine for m17n-lib, which allows
input of many languages using the input table maps from m17n-db.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1


%build
%autoreconf
%configure --disable-static
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/IMEngine/m17n.la


%files
%doc AUTHORS README THANKS
%doc --no-dereference COPYING
%{_libdir}/scim-1.0/*/IMEngine/m17n.so
%{_datadir}/scim/icons/*


%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 0.2.3-alt3_31
- update to new release by fcimport

* Mon Dec 06 2021 Igor Vlasenko <viy@altlinux.org> 0.2.3-alt3_27
- fixed build

* Sat Oct 17 2015 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.2.3-alt2.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.3-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_9
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_8
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_7
- initial fc import

