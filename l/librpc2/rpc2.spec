%add_optflags %optflags_shared
%define oldname rpc2
Name:           librpc2
Version:        2.10
Release:        alt1_14.1
Summary:        C library for remote procedure calls over UDP
Group:          System/Libraries
License:        LGPLv2
URL:            http://www.coda.cs.cmu.edu/
Source0:        ftp://ftp.coda.cs.cmu.edu/pub/rpc2/src/%{oldname}-%{version}.tar.gz
Source1:        ftp://ftp.coda.cs.cmu.edu/pub/rpc2/src/%{oldname}-%{version}.tar.gz.asc
Patch0:		rpc2-2.10-lua-5.2-fix.patch
Patch1:		rpc2-2.10-format-security-fix.patch
BuildRequires:  liblwp-devel lua-devel flex bison
Source44: import.info
Provides: rpc2 = %{version}-%{release}

%description
The RPC2 library, a C library for remote procedure calls over UDP.

%package        devel
Summary:        Development files for %{oldname}
Group:          Development/C
# headers are LGPLv2, rp2gen is GPLv2
License:        LGPLv2 and GPLv2
Requires:       librpc2 = %{version}
Provides: rpc2-devel = %{version}-%{release}

%description    devel
The %{oldname}-devel package contains libraries and header files for
developing applications that use %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1 -b .lua52fix
%patch1 -p1 -b .format-security

%build
export CC="gcc -fPIC"
%configure --disable-static --with-lua
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc COPYING NEWS
%{_libdir}/*.so.*
%{_datadir}/%{oldname}

%files devel
%{_bindir}/rp2gen
%{_includedir}/%{oldname}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{oldname}.pc

%changelog
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_14.1
- rebuild with new lua 5.3

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_10
- update to new release by fcimport

* Sun Apr 28 2013 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1_7
- initial fc import

