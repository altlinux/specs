%def_disable static
%def_enable poppler
# OR
%def_disable mupdf
%def_disable mupdf_cjk

%define _name epdf

Name: lib%_name
Version: 0.0.1
Release: alt1

Summary: EFL PDF Reader
License: GPLv2/LGPLv3
Group: System/Libraries

Url: http://www.enlightenment.org/
#VCS: git://git.enlightenment.fr/vcs/svn/PROTO/epdf.git
Source: %_name-%version.tar

BuildRequires: gcc-c++ libecore-devel libevas-devel
%{?_enable_mupdf_cjk:BuildRequires: libfreetype-devel}
%{?_enable_poppler:BuildRequires: libpoppler-devel}
BuildRequires: doxygen

%description
Enlightenment PDF library.

%package devel
Summary: EFL PDF Reader development package
Group: Development/C
Requires: %name = %version-%release

%description devel
Enlightenment PDF library development package.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	%{subst_enable static} \
	%{subst_enable poppler} \
	%{subst_enable mupdf} \
	%{?_enable_mupdf_cjk:--enable-mupdf-cjk}
%make_build
%make doc

%install
%makeinstall_std

%files
%_libdir/%name.so.*
%doc AUTHORS COPYING README

%files devel
%_bindir/%{_name}_evas_test
%_libdir/%name.so
%_pkgconfigdir/%_name.pc
%_includedir/%_name/

%changelog
* Sun Jan 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.0.1-alt1
- first build for Sisyphus (4f02c256) using poppler

