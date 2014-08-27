# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gtk+-2.0)
# END SourceDeps(oneline)
Name: scim-anthy
Version: 1.2.7
Release: alt2

License: GPLv2+
Url: http://scim-imengine.sourceforge.jp/
Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildRequires: scim-devel
BuildRequires: libanthy-devel >= 6700b-1 gettext-devel
Source0: http://osdn.dl.sourceforge.jp/scim-imengine/37309/%name-%version.tar.gz
Patch0: %name-aarch64.patch

Summary: SCIM IMEngine for anthy for Japanese input
Group: System/Libraries
Requires: scim kasumi
# This was necessary for the upgrade path from IIIMF
# and ensure the installation of future version of IIIMF.
# No Provides line for iiimf-le-canna is intentional because
# This package doesn't really provide the Language Engine for IIIMF.
# This just works on only SCIM.
Obsoletes: iiimf-le-canna <= 1:12.2
Source44: import.info
%description
Scim-anthy is a SCIM IMEngine module for anthy to support Japanese input.

%prep
%setup
%patch0 -p1 -b .0-aarch64

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

rm $RPM_BUILD_ROOT%_libdir/scim-1.0/*/*/*.la

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_libdir/scim-1.0/*/Helper/anthy-imengine-helper.so
%_libdir/scim-1.0/*/IMEngine/anthy.so
%_libdir/scim-1.0/*/SetupUI/anthy-imengine-setup.so
%_datadir/scim/Anthy
%_datadir/scim/icons/*png

%changelog
* Wed Aug 27 2014 Ilya Mashkin <oddity@altlinux.ru> 1.2.7-alt2
- build for Sisyphus

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1_12
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1_11
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1_10
- initial fc import

