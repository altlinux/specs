# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
# END SourceDeps(oneline)
%global debug_package %{nil}
Name:		hyena
Version:	0.5
Release:	alt2_9
Summary:	A library of GUI and non-GUI C sharp code
Summary(es):	Una librería para aplicaciones escritas en C#
Group:		Development/C
License:	MIT
URL:		http://live.gnome.org/Hyena
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{version}/%{name}-%{version}.tar.gz
#fixed in git upstream:
Patch0:		%{name}-fix-makefile.diff
ExclusiveArch:  %{mono_arches}

BuildRequires:	mono-devel
BuildRequires:	libgtk-sharp2-devel
BuildRequires:	mono-data
BuildRequires:	mono-nunit-devel >= 2.4.7

Requires:	libgtk-sharp2
Requires:	mono-nunit
Source44: import.info

%description
This is a library of useful GUI and non-GUI C sharp code, originally used in 
Banshee.

%description -l es
Esta es una librería útil para escribir aplicaciones en C# usada
originalmente en Banshee.

%package devel
Summary:	Development files for %{name}
Summary(es):	Archivos de desarrollo de %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development package for %{name}

%description devel -l es
Paquete de desarrollo para %{name}

%prep
%setup -q 
%patch0 -p1

%build
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

chmod a-x %{buildroot}%{_libdir}/hyena/*.config

%files
%doc NEWS README COPYING
%{_libdir}/%{name}

%files devel
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Oct 06 2016 Igor Vlasenko <viy@altlinux.ru> 0.5-alt2_9
- to Sisyphus

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_9
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_8
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_7
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_6
- update to new release by fcimport

* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.5-alt1_5
- initial fc import

