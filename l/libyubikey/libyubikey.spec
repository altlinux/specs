# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/doxygen /usr/bin/pkg-config /usr/bin/splint gcc-c++ pkgconfig(glib-2.0) unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libyubikey
Version:        1.7
Release:        alt2_2
Summary:        C library for decrypting and parsing Yubikey One-time passwords

Group:          Development/C
License:        BSD
URL:            http://code.google.com/p/yubico-c/
Source0:        http://yubico-c.googlecode.com/files/%{name}-%{version}.tar.gz
Source44: import.info

%description
This package holds a low-level C software development kit for the Yubico
authentication device, the Yubikey.

%package devel
Summary:        Development files for libyubikey
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the header file needed to develop applications that use
libyubikey.

%prep
%setup -q

%build
%configure --disable-static
# --disable-rpath doesn't work for the configure script
%{__sed} -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
%{__sed} -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{__make} %{?_smp_mflags}

%check
%{__make} check LD_LIBRARY_PATH=".libs"

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"

%files
%doc AUTHORS COPYING NEWS ChangeLog README
%{_bindir}/modhex
%{_bindir}/ykparse
%{_bindir}/ykgenerate
%{_libdir}/libyubikey.so.0
%{_libdir}/libyubikey.so.0.1.2

%files devel
%{_includedir}/yubikey.h
%{_libdir}/libyubikey.so

%changelog
* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_1
- initial import by fcimport

