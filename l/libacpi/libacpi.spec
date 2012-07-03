# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/gtkdocize gcc-c++ libaccounts-glib-devel pkgconfig(dbus-1) pkgconfig(glib-2.0) pkgconfig(gobject-2.0) unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libacpi
Version:        0.2
Release:        alt2_16
Summary:        General purpose library for ACPI 

Group:          System/Libraries
License:        MIT
URL:            http://www.ngolde.de/libacpi.html
Source0:        http://www.ngolde.de/download/%{name}-%{version}.tar.gz
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-sysfs.patch
ExcludeArch:    ppc ppc64
Source44: import.info

%description    
libacpi is a general purpose shared library for programs gathering 
ACPI data on Linux. Features: Thermal zones support, Battery support, 
Fan support, AC support

Note: This is no portable code, it will only run on i386/x86_64 Linux systems.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i "s/CFLAGS += .*/CFLAGS += -fPIC $RPM_OPT_FLAGS/;s&usr/local&usr&" config.mk
sed -i "s&share/doc/%{name}&share/doc/%{name}-%{version}&g" Makefile


%build
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%_libdir
chmod +x $RPM_BUILD_ROOT%{_libdir}/%{name}.so.*
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%{_mandir}/man3/*
%dir %{_defaultdocdir}/%{name}-%{version}
%doc %{_defaultdocdir}/%{name}-%{version}/AUTHORS
%doc %{_defaultdocdir}/%{name}-%{version}/CHANGES
%doc %{_defaultdocdir}/%{name}-%{version}/README
%doc %{_defaultdocdir}/%{name}-%{version}/LICENSE
%{_libdir}/*.so.*

%files devel
%dir %{_defaultdocdir}/%{name}-%{version}/doc
%doc %{_defaultdocdir}/%{name}-%{version}/doc/*
%{_bindir}/test-libacpi
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_16
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt2_15
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.2-alt1_15
- initial import by fcimport

