# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize gcc-c++ pkgconfig(gtk+-2.0) pkgconfig(libgnomecanvas-2.0)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname phat
Summary: A collection of GTK+ widgets useful for audio applications
Name:          libphat
Version:       0.4.1
Release:       alt1_15
License:       GPLv2+
Group:         System/Libraries
URL:           http://phat.berlios.de/
Source0:       http://download.berlios.de/%{oldname}/%{oldname}-%{version}.tar.gz
# Remove unused variables - to be submitted upstream
Patch0:        phat-unused-but-set-variable.patch
Patch1:        phat-fix-fsf-address.patch
Patch2:        phat-gdk-unref.patch

BuildRequires: gtk2-devel 
BuildRequires: libgnomecanvas-devel
Source44: import.info
Provides: phat = %{version}-%{release}

%description
PHAT is a collection of GTK+ widgets geared toward pro-audio apps. The
goal is to eliminate duplication of effort and provide some
standardization (well, at least for GTK+ apps).

%package devel
Summary:       Header files for PHAT 
Group:         Development/C
Requires:      %{name}%{?_isa} = %{version}
Provides: phat-devel = %{version}-%{release}

%description devel
Header files and additional libraries used for developing applications
with the PHAT Audio Toolkit.

%package docs
Summary:       Documentation for PHAT 
Group:         Development/C
Provides: phat-docs = %{version}-%{release}

%description docs
Documentation for the PHAT Audio Toolkit.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure --enable-debug --disable-static
make %{?_smp_mflags} 

%install
make DESTDIR=%{buildroot} install

rm %{buildroot}%{_libdir}/libphat.*a

%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/phat*
%{_libdir}/libphat.so.*
%{_datadir}/%{oldname}

%files devel
%{_libdir}/libphat.so
%{_libdir}/pkgconfig/%{oldname}.pc
%{_includedir}/%{oldname}

%files docs
%{_datadir}/gtk-doc/html/%{oldname}

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_14
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_11
- update to new release by fcimport

* Sun Apr 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_10
- initial fc import

