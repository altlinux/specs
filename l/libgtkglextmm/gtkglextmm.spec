# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: chrpath
%add_optflags %optflags_shared
%define oldname gtkglextmm
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define gtkglext_major 1.0
%define gtkglextmm_major 1.2
%define gtkmm_major 2.4

Summary: C++ wrapper for GtkGlExt
Name: libgtkglextmm
Version: 1.2.0
Release: alt2_25
License: LGPLv2+
Group: System/Libraries
URL: http://projects.gnome.org/gtkglext/

Source0: http://downloads.sourceforge.net/gtkglext/%{oldname}-%{version}.tar.gz
Patch0: gtkglextmm-1.2.0-aclocal.diff
Patch1: fix_ftbfs_gtk_2_20.patch
Patch2: fix_ftbfs_gtk_2_36.patch
Patch3: fix_ftbfs_gtk_2_37.patch

BuildRequires: libgtkglext-devel >= %{gtkglext_major}
BuildRequires: libgtkmm2-devel >= %{gtkmm_major}
Provides: gtkglextmm = %{version}-%{release}
Patch33: gtkglextmm-1.2.0-fix-deprecated.patch


%description
gtkglextmm is a C++ wrapper for GtkGlExt, an OpenGL extension to GTK+.

%package devel
Summary: Development tools for gtkglextmm
Group: Development/Other

Requires: %{name} = %{version}
Provides: gtkglextmm-devel = %{version}-%{release}

%description devel
The gtkglextmm-devel package contains the header files, static libraries,
and developer docs for gtkglextmm.

%prep
%setup -q -n gtkglextmm-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# file-not-utf8
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
iconv -f iso8859-1 -t utf-8 README > README.conv && mv -f README.conv README

# zero-length
echo '# Nothing' >> tools/m4/convert_gtkglext.m4
%patch33 -p2

%build
%configure --disable-static --disable-dependency-tracking

# remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
DESTDIR=$RPM_BUILD_ROOT make install
# kill rpath
for i in `find %buildroot{%_bindir,%_libdir,/usr/libexec,/usr/lib,/usr/sbin} -type f -perm -111`; do
	chrpath -d $i ||:
done

%files
%doc ChangeLog README AUTHORS COPYING.LIB COPYING NEWS
%{_libdir}/libgtkglextmm-x11-*so.*
%{_libdir}/libgdkglextmm-x11-*so.*

%files devel
%{_includedir}/*
%{_libdir}/%{oldname}-%{gtkglextmm_major}
%{_libdir}/lib*so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%dir %{_datadir}/doc/%{oldname}-%{gtkglextmm_major}
%doc %{_datadir}/doc/%{oldname}-%{gtkglextmm_major}/html/

%changelog
* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_25
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_24
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_23
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_21
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_19
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_18
- new fc release

* Mon Apr 15 2013 Andrey Cherepanov <cas@altlinux.org> 1.2.0-alt2_15.1
- Fix deprecated functions use

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_15
- applied repocop patches

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_15
- initial fc import

