# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libcheck-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 3
%define libname libgalago%{major}
%define develname libgalago-devel

Summary: Base library of Galago
Name: libgalago
Version: 0.5.2
Release: alt1_21
Source0: http://www.galago-project.org/files/releases/source/libgalago/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.galago-project.org/
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: gtk-doc
BuildRequires: gettext-tools libasprintf-devel
Source44: import.info

%description
This is the base library of the Galago desktop presence framework.

%package -n %libname
Group: System/Libraries
Summary: Base library of Galago - shared library
#gw for the translations
Requires: %name >= %version
#gw for the sharp bindings
Provides: galago%major = %version-%release

%description -n %libname
This is the base library of the Galago desktop presence framework.

%package -n %develname
Group: Development/C
Summary: Base library of Galago - headers
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Provides: galago-devel = %version-%release
Obsoletes: libgalago3-devel

%description -n %develname
This is the base library of the Galago desktop presence framework.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
rm -rf $RPM_BUILD_ROOT %name.lang
%makeinstall_std MKINSTALLDIRS=`pwd`/mkinstalldirs
rm -rf %buildroot%_datadir/autopackage
%find_lang %name

# don't ship .la
find %{buildroot} -name '*.la' | xargs rm -f

%files -f %name.lang
%doc AUTHORS NEWS

%files -n %libname
%_libdir/lib*.so.%{major}*

%files -n %develname
%doc ChangeLog 
%_libdir/lib*.so
%_libdir/pkgconfig/libgalago.pc
%_includedir/%name/
%_datadir/gtk-doc/html/libgalago


%changelog
* Sun Nov 12 2023 Igor Vlasenko <viy@altlinux.org> 0.5.2-alt1_21
- fixed build

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_20
- update by mgaimport

* Sat Jun 16 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_17
- update by mgaimport

* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.5.2-alt1_16
- new version

* Wed Oct 08 2008 Alexey Shabalin <shaba@altlinux.ru> 0.5.2-alt1
- 0.5.2
- build devel-doc as noarch

* Wed Dec 27 2006 Igor Zubkov <icesik@altlinux.org> 0.5.1-alt1.1
- rebuild with new dbus

* Mon Jun 05 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.1-alt1
- Updated to 0.5.1
- Disabled static build by default
- Spec cleanup

* Wed Apr 19 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.3.3-alt1.1
- Rebuild with dbus-0.61-alt1 .

* Sun Sep 18 2005 Vital Khilko <vk@altlinux.ru> 0.3.3-alt1
- initial build

