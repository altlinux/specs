BuildRequires: chrpath
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/gtkdocize gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname phat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary: A collection of GTK+ widgets useful for audio applications
Name:          libphat
Version:       0.4.1
Release:       alt1_22
License:       GPLv2+
URL:           http://phat.berlios.de/
Source0:       http://download.berlios.de/%{oldname}/%{oldname}-%{version}.tar.gz
# Remove unused variables - to be submitted upstream
Patch0:        phat-unused-but-set-variable.patch
Patch1:        phat-fix-fsf-address.patch
Patch2:        phat-gdk-unref.patch

BuildRequires:  gcc
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel 
BuildRequires: libgnomecanvas-devel
Source44: import.info
Provides: phat = %{version}-%{release}

%description
PHAT is a collection of GTK+ widgets geared toward pro-audio apps. The
goal is to eliminate duplication of effort and provide some
standardization (well, at least for GTK+ apps).

%package devel
Group: Development/Other
Summary:       Header files for PHAT 
Requires:      %{name} = %{version}-%{release}
Provides: phat-devel = %{version}-%{release}

%description devel
Header files and additional libraries used for developing applications
with the PHAT Audio Toolkit.

%package docs
Group: Development/Other
Summary:       Documentation for PHAT 
BuildArch: noarch
Provides: phat-docs = %{version}-%{release}

%description docs
Documentation for the PHAT Audio Toolkit.

%prep
%setup -n %{oldname}-%{version} -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

sed -i s,-Werror,, configure.ac configure

%build
%configure --enable-debug --disable-static
%make_build 

%install
make DESTDIR=%{buildroot} install

rm %{buildroot}%{_libdir}/libphat.*a
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111 ! -name '*.la' `; do
	chrpath -d $i ||:
done



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
* Mon Jan 13 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_22
- fixed build

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1_16
- update to new release by fcimport

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

