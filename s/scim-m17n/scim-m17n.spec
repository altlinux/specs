# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
Name: scim-m17n
Version: 0.2.3
Release: alt2
Summary: SCIM IMEngine for m17n-lib
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group: System/Libraries
License: GPLv2+
Url: http://www.scim-im.org/projects/imengines
Source0: %name-%version.tar.gz
BuildRequires: scim-devel libm17n-devel
Obsoletes: iiimf-le-unit <= 1:12.2
Requires: scim >= 1.4.4
Patch0: %name-no-M17N-prefix.patch
Patch1: %name-aarch64.patch
Source44: import.info
%description
scim-m17n provides a SCIM IMEngine for m17n-lib, which allows
input of many languages using the input table maps from m17n-db.

%prep
%setup
%patch0 -p1 -b .0-name-prefix
%patch1 -p1 -b .1-aarch64

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%_libdir/scim-1.0/*/IMEngine/m17n.la

%files
%doc AUTHORS COPYING README THANKS
%_libdir/scim-1.0/*/IMEngine/m17n.so
%_datadir/scim/icons/*

%changelog
* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.3-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_9
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_8
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.3-alt1_7
- initial fc import

