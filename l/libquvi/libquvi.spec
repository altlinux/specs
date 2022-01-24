%define _name libquvi
%define api 0.9

Name: %_name
Version: %api.4
Release: alt3

%define major %version
%define develname libquvi-devel
# hack for compatibility with old libquvi0.9;
# remove on version upgrade and use libquvi%{api}_%{major}
%if "%version" == "0.9.4"
%define libname libquvi%{api}
%else
%define libname libquvi%{api}_%{major}
%endif

Summary: Command line tool for parsing video download links
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%_name/%api/%_name-%version.tar.xz

BuildRequires: pkgconfig(glib-2.0) >= 2.24
BuildRequires: pkgconfig(libcurl) >= 7.21
BuildRequires: pkgconfig(libproxy-1.0) >= 0.3.1
BuildRequires: pkgconfig(libquvi-scripts-0.9) >= %api
BuildRequires: libgcrypt-devel
BuildRequires: libgio-devel
BuildRequires: lua-devel


# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

# opensuse
Patch1: libquvi-0.9.4-lua-5.2.patch


%description
%name is a library for parsing video download links. It supports Youtube
and other similar video websites.

%package -n %libname
Summary: Shared library files libquvi
Group: Networking/Other
Requires: libquvi-scripts >= 0.9

%description -n %libname
Shared library files libquvi.

%package -n %develname
Summary: Development files for %name
Group: Development/C
Requires: %libname = %EVR
%if "%version" == "0.9.4"
Provides: libquvi0.9-devel
%else
%define libname libquvi%{api}_%{major}
%endif

%description -n %develname
This package provides files needed for building applications against
%name.

%prep
%setup -n %_name-%version
%patch1 -p1

%build
%configure --disable-static
%make_build

%check
#%%make check

%install
%makeinstall_std

%files -n %libname
%_libdir/%_name-%api-%major.so
%doc NEWS README

%files -n %develname
%_includedir/quvi-%api
%_libdir/%_name-%api.so
%_pkgconfigdir/%_name-%api.pc
%_man3dir/%_name.*
%_man7dir/quvi-object.7.*

%changelog
* Mon Jan 24 2022 Igor Vlasenko <viy@altlinux.org> 0.9.4-alt3
- consolidated libquvi and libquvi0.9

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt2.1
- rebuild with new lua 5.3

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt2
- reqs: libquvi-scripts (ALT #31354)

* Sat May 26 2012 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus
