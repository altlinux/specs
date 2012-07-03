%def_disable static
%define _waf ./waf --prefix=%_prefix --bindir=%_bindir --configdir=%_sysconfdir --datadir=%_datadir --includedir=%_includedir --libdir=%_libdir --mandir=%_mandir --htmldir=%_docdir/%name-doc --docs

Name: libraul
Version: 0.7.0
Release: alt1

Summary: utility library for realtime multi-threaded audio applications
License: %gpl2plus
Group: System/Libraries
Url: http://drobilla.net/software/raul/
Packager: Timur Batyrshin <erthad@altlinux.org>

Source0: %name-%version.tar.bz2

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Wed Nov 24 2010
BuildRequires: boost-devel doxygen fonts-ttf-dejavu gcc-c++ glib2-devel graphviz python-modules-compiler python-modules-encodings python-modules-logging

%description
Raul (Realtime Audio Utility Library) is a C++ utility library primarily aimed
at audio/musical applications.

%package devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers for building software that uses %name

%if_enabled static
%package devel-static
Summary: Static libraries for %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
Static libs for building statically linked software that uses %name
%endif

%package doc
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description doc
Documentation for %name

%prep
%setup

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS  
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS  
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS  
%if_disabled static
export lt_cv_prog_cc_static_works=no 
%else
export lt_cv_prog_cc_static_works=yes
%endif
export lt_cv_deplibs_check_method=pass_all
%_waf configure
%_waf build

%install
%_waf install --destdir=%buildroot

%files
%_libdir/*.so.*
%doc AUTHORS README 

%files devel
%_libdir/*.so
%_includedir/raul
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif

%files doc
%doc %_docdir/%name-doc/

%changelog
* Tue Nov 23 2010 Timur Batyrshin <erthad@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Aug 03 2009 Timur Batyrshin <erthad@altlinux.org> 0.5.1-alt1
- Initial build for sisyphus

