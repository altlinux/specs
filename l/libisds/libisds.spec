# BEGIN SourceDeps(oneline):
BuildRequires: libexpat-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libisds
Version:        0.5
Release:        alt3_2
Summary:        Library for accessing the Czech Data Boxes

Group:          System/Libraries
License:        LGPLv3
URL:            http://xpisar.wz.cz/%{name}/
Source0:        http://xpisar.wz.cz/%{name}/dist/%{name}-%{version}.tar.xz

BuildRequires:  libxml2-devel libcurl-devel libgcrypt-devel libgpgme-devel
BuildRequires:  expat-devel >= 2.0.0 gnupg2
Requires:       gnupg2
Source44: import.info

%description
This is a library for accessing ISDS (InformaA.nA. systA.m datovA.ch schrA.nek
/ Data Box Information System) SOAPa..services as defined in Czech ISDS Act
(300/2008 Coll.) and implied documents.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libisds = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static \
    --enable-test \
    --with-libcurl
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%find_lang %{name}
mv doc specification
rm -rf client/.deps

%files -f %{name}.lang
%doc README AUTHORS NEWS TODO COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/isds.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%doc client specification

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_1
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_1
- initial import by fcimport

