%define _name libquvi
%define ver_major 0.9

Name: %_name%ver_major
Version: %ver_major.4
Release: alt2.1

Summary: Command line tool for parsing video download links
Group: System/Libraries
License: LGPLv2+
Url: http://quvi.sourceforge.net/

Source: http://downloads.sourceforge.net/project/%_name/%ver_major/%_name-%version.tar.xz

Requires: libquvi-scripts%ver_major

BuildRequires: %_name-scripts%ver_major-devel
BuildRequires: libgio-devel libcurl-devel lua-devel libproxy-devel libgcrypt-devel

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
* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.4-alt2.1
- rebuild with new lua 5.3

* Tue Sep 08 2015 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt2
- reqs: libquvi-scripts0.9

* Mon Sep 15 2014 Yuri N. Sedunov <aris@altlinux.org> 0.9.4-alt1
- 0.9.4

* Tue Sep 10 2013 Yuri N. Sedunov <aris@altlinux.org> 0.9.3-alt1
- first build for Sisyphus



