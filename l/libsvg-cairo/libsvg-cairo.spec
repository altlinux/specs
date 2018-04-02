# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ imake libXt-devel xorg-cf-files
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major   1
%define lib_name libsvg-cairo%{major}
%define devel_name libsvg-cairo-devel

Name:             libsvg-cairo
Summary:          A SVG library based on cairo
Version:	0.1.6
Release:	alt2_19
License:          BSD
Group:            System/Libraries
Source:           %{name}-%{version}.tar.bz2
URL:              http://cairographics.org/snapshots/
BuildRequires:    libsvg-devel
BuildRequires:    libcairo libcairo-devel libcairo-gobject-devel libcairo-tools
BuildRequires:    libjpeg-devel libturbojpeg-devel
Source44: import.info

%description
Libsvg-cairo provides the ability to render SVG content from files or
buffers. All rendering is performed using the cairo rendering library.

%package -n %{lib_name}
Summary:          A SVG library based on cairo
Group:            System/Libraries

%description -n %{lib_name}
Libsvg-cairo provides the ability to render SVG content from files or
buffers. All rendering is performed using the cairo rendering library.

%package -n %{devel_name}
Summary:          Libraries and include files for developing with libsvg
Group:            Development/C
Requires:         %{lib_name} = %{version}
Provides:         %{name}-devel = %{version}
Provides:         lib%{name}-devel = %{version}

%description -n %{devel_name}
This package provides the necessary development libraries and include
files to allow you to develop with libsvg-cairo.


%prep
%setup -q

%build
export LIBS="-lm"
%configure --disable-static
%make

%install
%makeinstall
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%files -n %{lib_name}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{devel_name}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg-cairo.pc





%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt2_19
- new version

* Wed Aug 30 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.1.6-alt2
- updated build dependencies

* Sat Aug 13 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.6-alt1.1
- rebuild with libcairo-0.9.0

* Sat Jul 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Sat Feb 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.1.5-alt1
- initial release

