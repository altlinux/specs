# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define oname libticables2

%define major 6
%define libname libticables%{major}
%define develname libticables-devel

Summary:	Library to handle the different TI link cables
Name:		libticables
Version:	1.3.4
Release:	alt1_1
Epoch:		1
License:	LGPLv2+
Group:		Communications
Url:		http://tilp.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/tilp/%{oname}-%{version}.tar.bz2
# Udev rules taken from Arch AUR package.
Source1:        http://tc01.fedorapeople.org/tilp2/69-libticables.rules
# Patch to add error checking to libusb_init calls.
Patch0:         http://tc01.fedorapeople.org/tilp2/libticables-libusb_check.patch
# Patch to add AArch64 handling
Patch1:         aarch64.patch
# Patch to add PPC64le handling
Patch2:         ppc64le.patch
BuildRequires:	pkgconfig(libusb)
BuildRequires:	glib2-devel
Source44: import.info

%description
The TiCables library is a part of the TiLP project and constitutes with
the other libraries a complete framework for developping and/or linking
TI files oriented applications.

It is able to handle the different link cables designed for TI's graphing
calculators (also called handheld), without worrying about different link
cables characteristics as well as different platforms.

It supports all the currently available link cables:
- home-made parallel (aka $5-cable)
- home-made serial (aka $4-cable)
- TI's BlackLink
- TI's GrayLink
- TI's SilverLink
- AVRlink

It also supports some 'virtual' link cables for connection with emulators:
- Virtual TI (VTi)
- (Gtk)TiEmu

%package -n %{libname}
Summary:	Library to handle different TI link cables
Group:		System/Libraries
Provides:   %{name} = %epoch:%version-%release

%description -n %{libname}
The TiCables library is a part of the TiLP project and constitutes with
the other libraries a complete framework for developping and/or linking
TI files oriented applications.

It is able to handle the different link cables designed for TI's graphing
calculators (also called handheld), without worrying about different link
cables characteristics as well as different platforms.

It supports all the currently available link cables:
- home-made parallel (aka $5-cable)
- home-made serial (aka $4-cable)
- TI's BlackLink
- TI's GrayLink
- TI's SilverLink
- AVRlink

It also supports some 'virtual' link cables for connection with emulators:
- Virtual TI (VTi)
- (Gtk)TiEmu

%package -n %{develname}
Summary:	Development related files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{epoch}:%{version}-%{release}

%description -n %{develname}
This package contains headers and other necessary files to develop or compile
applications that use %{name}.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure \
	--enable-libusb10 \
	--enable-logging \
	--disable-rpath
%make

%install
%makeinstall_std gnulocaledir=%{buildroot}%{_datadir}/locale

rm -f %{buildroot}%{_libdir}/*.la

%find_lang %{oname}

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname} -f %{oname}.lang
%doc AUTHORS ChangeLog README
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1:1.3.4-alt1_1
- new version

