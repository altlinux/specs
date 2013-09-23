%define _name libquvi
%define ver_major 0.9

Name: %_name%ver_major
Version: %ver_major.3
Release: alt1

Summary: Command line tool for parsing video download links
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://downloads.sourceforge.net/project/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires: %_name-scripts%ver_major-devel
BuildRequires: libgio-devel libcurl-devel liblua5-devel libproxy-devel libgcrypt-devel

# for check
#BuildRequires: perl-Test-Deep perl-JSON perl-Test-Pod

%description
%name is a library for parsing video download links. It supports Youtube
and other similar video websites.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files needed for building applications against
%name.

%prep
%setup -n %_name-%version

%build
%configure --disable-static
%make_build

%check
#%%make check

%install
%makeinstall_std

%files
%_libdir/%_name-%ver_major-%version.so
%doc NEWS README

%files devel
%_includedir/quvi-%ver_major
%_libdir/%_name-%ver_major.so
%_pkgconfigdir/%_name-%ver_major.pc
%_man3dir/%_name.*
%_man7dir/quvi-object.7.*

%changelog
* Tue Sep 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- first build for Sisyphus



