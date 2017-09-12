# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
#BuildRequires: /usr/bin/pkg-config pkgconfig(glib-sharp-2.0) pkgconfig(gtk-sharp-2.0)
# END SourceDeps(oneline)
%global debug_package %{nil}
Name:		hyena
Version:	0.5
Release:	alt3
Packager: 	Korneechev Evgeniy <ekorneechev@altlinux.org>
Summary:	A library of GUI and non-GUI C sharp code
Summary(es):	Una librería para aplicaciones escritas en C#
Group:		Development/C
License:	MIT
URL:		https://wiki.gnome.org/Hyena
Source0:	%name-%version.tar.gz
#fixed in git upstream:
Patch0:		%name-fix-makefile.diff
Patch1:		%name-%version-alt-fix-configure.diff
ExclusiveArch:  %{mono_arches}

BuildRequires:	mono-full mono-devel-full
BuildRequires:	libgtk-sharp2-devel

Requires:	libgtk-sharp2
Source44: 	import.info

%description
This is a library of useful GUI and non-GUI C sharp code, originally used in 
Banshee.

%description -l es
Esta es una librería útil para escribir aplicaciones en C# usada
originalmente en Banshee.

%package devel
Summary:	Development files for %name
Summary(es):	Archivos de desarrollo de %name
Group:		Development/C
Requires:	%name = %version-%release

%description devel
Development package for %name

%description devel -l es
Paquete de desarrollo para %name

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=%buildroot

chmod a-x %buildroot%_libdir/hyena/*.config

%files
%doc NEWS README COPYING
%_libdir/%name

%files devel
%_libdir/pkgconfig/*.pc

%changelog
* Tue Sep 12 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.5-alt3
- rebuild with mono5

* Mon Oct 03 2016 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.5-alt2
- autoimports -> Sisuphus

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

