# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/dot /usr/bin/doxygen gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define version 0.7.9
%define uname cegui
%define libname lib%{uname}%{version}
%define develname lib%{uname}-devel

Summary:	A free library providing windowing and widgets for graphics APIs / engines
Name:		cegui0.7
Version:	0.7.9
Release:	alt1_13
License:	MIT
Group:		Development/C++
URL:		http://www.cegui.org.uk
Source0:	http://prdownloads.sourceforge.net/crayzedsgui/CEGUI-%{version}.tar.gz
Patch1:		cegui-0.7.9-gcc7.patch
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	libGL-devel
BuildRequires:	pkgconfig(glu)
BuildRequires:	libfreetype-devel
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	libfreeimage-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(xerces-c)
BuildRequires:	gtk2-devel
BuildRequires:	libdevil-devel
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(tinyxml)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	libirrlicht-devel
Source44: import.info

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available,
or severely lacking. The library is object orientated, written in C++,
and targeted at games developers who should be spending their time creating
great games, not building GUI sub-systems!

%package -n %{libname}
Summary:	CEGUI library
Group:		Games/Other

%description -n %{libname}
This is a library used by CEGUI.

%package -n %{develname}
Summary:	Development files for CEGUI
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{uname}-devel = %{version}-%{release}
Provides:	%{uname}-devel = %{version}-%{release}
Conflicts:	libCEUI0.6-devel

%description -n  %{develname}
Development file for CEGUI.

%prep
%setup -q -n CEGUI-%{version}
%patch1 -p1

%build
%configure \
	--with-gtk2 \
	--disable-static --disable-corona --disable-samples \
	--enable-freeimage \
	--disable-directfb-renderer --disable-irrlicht-renderer \
	--enable-bidirectional-text \
	--with-default-xml-parser=ExpatParser \
	--with-pic

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/libCEGUI*-%{version}.so

%files -n %{develname}
%{_libdir}/*.so
%exclude %{_libdir}/libCEGUI*-%{version}.so
%{_includedir}/CEGUI
%{_libdir}/pkgconfig/*.pc
%{_datadir}/CEGUI


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.7.9-alt1_13
- new version

