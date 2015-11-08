Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(check) pkgconfig(libftdi) pkgconfig(libusb-1.0) pkgconfig(libzip)
# END SourceDeps(oneline)
Name:           libsigrok
Version:        0.3.0
Release:        alt1_3
Summary:        Basic hardware access drivers for logic analyzers
# Combined GPLv3+ and GPLv2+ and BSD
License:        GPLv3+
URL:            http://www.sigrok.org/
Source0:        http://sigrok.org/download/source/libsigrok/%{name}-%{version}.tar.gz
# backport libftdi-1 detection from master
Patch1:         %{name}-0.3.0-libftdi1.patch

BuildRequires:  glib2-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel
BuildRequires:  libusb-devel
BuildRequires:  libftdi-devel
BuildRequires:  libserialport-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:	libtool
Source44: import.info

%description
%{name} is a shared library written in C which provides the basic API
for talking to hardware and reading/writing the acquired data into various
input/output file formats.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Group:          Documentation
Summary:        API documentation for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains documentation for developing software
with %{name}.


%prep
%setup -q
%patch1 -p1 -b .ftdi1

autoreconf -vif


%build
%configure --disable-static
make %{?_smp_mflags} V=1

# This builds documentation for the -doc package
doxygen Doxyfile


%install
%makeinstall_std
# Install udev rules
install -D -p -m 0644 contrib/z60_libsigrok.rules %{buildroot}%{_udevrulesdir}/60-libsigrok.rules

find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc README README.devices NEWS COPYING
%{_libdir}/libsigrok.so.2*
%{_udevrulesdir}/60-libsigrok.rules

%files devel
%{_includedir}/libsigrok/
%{_libdir}/libsigrok.so
%{_libdir}/pkgconfig/libsigrok.pc

%files doc
%doc doxy/html-api/


%changelog
* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1_3
- new version

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_4
- update to new release by fcimport

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_3
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1_1
- update to new release by fcimport

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1_1
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_1
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt1_3
- initial fc import

