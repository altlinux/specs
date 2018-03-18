# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(libusb-1.0)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 7
%define libname libticables2_%{major}
%define devname libticables2-devel

Summary:	Library to handle the different TI link cables
Name:		libticables2
Version:	1.3.5
Release:	alt1_4
License:	LGPLv2+
Group:		Communications
Url:		https://sourceforge.net/projects/tilp/
Source0:	https://download.sourceforge.net/tilp/%{name}-%{version}.tar.bz2
# Udev rules taken from Arch AUR package.
Source1:	http://tc01.fedorapeople.org/tilp2/69-libticables.rules
BuildRequires:	pkgconfig(libusb)
BuildRequires:	glib2-devel
BuildRequires:	gettext-tools libasprintf-devel
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

%package i18n
Summary:	Internationalization and locale data for %{name}
Group:		System/Internationalization
BuildArch:	noarch
Conflicts:	libticables2-devel < 1.3.5-2

%description i18n
Internationalization and locale data for %{name}.

%package -n %{libname}
Summary:	Library to handle different TI link cables
Group:		System/Libraries
Requires:	%{name}-i18n >= %{version}-%{release}

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

%package -n %{devname}
Summary:	Development related files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	ticables2-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}ticables-devel < 1:1.3.5

%description -n %{devname}
This package contains headers and other necessary files to develop or compile
applications that use %{name}.

%prep
%setup -q


%build
autoreconf -vfi
%configure \
	--enable-libusb10 \
	--enable-logging \
	--disable-rpath
%make_build

%install
%makeinstall_std

#Rule to allow users to access handhelds
mkdir -p %{buildroot}%{_usr}/lib/udev/rules.d/
install -m0644 %{SOURCE1} %{buildroot}%{_usr}/lib/udev/rules.d/

#we don't want these
find %{buildroot} -name "*.la" -delete

%find_lang %{name}

%files i18n -f %{name}.lang

%files -n %{libname}
%{_usr}/lib/udev/rules.d/69-libticables.rules
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{devname}
%doc AUTHORS ChangeLog README
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/ticables2.pc
%{_includedir}/tilp2/*


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.3.5-alt1_4
- new version

