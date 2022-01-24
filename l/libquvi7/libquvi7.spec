%def_without devel
%define _name quvi
%define ver_major 0.4
%define soversion 7
%define libname libquvi

Name: lib%{_name}%soversion
Version: %ver_major.1
Release: alt3

Summary: Command line tool for parsing video download links
Group: System/Legacy libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/lib%_name/%ver_major/lib%_name-%version.tar.xz

Requires: libquvi-scripts

BuildRequires: lib%_name-scripts-devel >= %version
BuildRequires: libcurl-devel lua-devel

# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

%description
%name is a library for parsing video download links. It supports Youtube
and other similar video websites.

%package -n %libname
Summary: Shared library files libquvi
Group: Networking/Other
Requires: libquvi-scripts >= 0.9

%description -n %libname
Shared library files libquvi.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name.

%prep
%setup -q -n lib%_name-%version

%build
%configure --disable-static
%make_build

%check
#%%make check

%install
%make DESTDIR=%buildroot install

%files -n %libname
%_libdir/lib%_name.so.%{soversion}*
%doc NEWS README

%if_with devel
%files devel
%_libdir/lib%_name.so
%_libdir/pkgconfig/lib%_name.pc
%_includedir/%_name/
%_man3dir/lib%_name.*
%endif

%changelog
* Mon Jan 24 2022 Igor Vlasenko <viy@altlinux.org> 0.4.1-alt3
- compat package for cclive migration

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2.1
- rebuild with new lua 5.3

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt2
- reqs: libquvi-scripts (ALT #31354)

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus

