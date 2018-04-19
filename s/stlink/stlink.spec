Summary: STM32 microcontrolles programmer and debuger, using STLINKv1/v2
Name: stlink
Version: 2018.04.18
Release: alt1
License: Other
Group: Development/Other
URL: https://github.com/texane/stlink.git
Source0: %name-master.zip

# Automatically added by buildreq on Wed Apr 18 2018
BuildRequires: cmake git-core libgtk+3-devel libusb-devel-static python3-dev python3-module-mpl_toolkits python3-module-yieldfrom ruby-stdlibs selinux-policy unzip

%description
First, you have to know there are several boards supported by the software.
Those boards use a chip to translate from USB to JTAG commands. The chip is
called stlink and there are 2 versions:
. STLINKv1, present on STM32VL discovery kits,
. STLINKv2, present on STM32L discovery and later kits.

2 different transport layers are used:
. STLINKv1 uses SCSI passthru commands over USB,
. STLINKv2 uses raw USB commands.


%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Lib files for stlink

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
Development files for libstlink

%prep
%setup -q -n %name-master

%build
%make_build CMAKEFLAGS="-DCMAKE_INSTALL_PREFIX:PATH=%prefix -DCMAKE_INSTALL_LIBDIR=%_libdir"

%install
pushd build/Release
%makeinstall DESTDIR=%buildroot
%ifarch x86_64
	%__mv %buildroot/usr/lib %buildroot%_libdir
%endif
popd

%files
%doc ChangeLog.md LICENSE README.md
%dir %_datadir/%name

%_sysconfdir/modprobe.d/*
%_sysconfdir/udev/rules.d/*

%_bindir/*

%_datadir/applications/*
%_liconsdir/*
%_man1dir/*
%_datadir/%name/*

%files -n lib%name
%_libdir/*.so*

%files -n lib%name-devel
%_libdir/*.a
%dir %_includedir/%name
%_includedir/%name.h
%_includedir/%name/*.h
%_pkgconfigdir/*

%changelog
* Wed Apr 18 2018 Grigory Milev <week@altlinux.ru> 2018.04.18-alt1
- Updated to latest git version
- devide package to libs, main tools and devel packages

* Wed Mar 05 2014 Grigory Milev <week@altlinux.ru> 2014.03.05-alt2
- Change 0700 -> 0644 for file saved from flash

* Wed Mar 05 2014 Grigory Milev <week@altlinux.ru> 2014.03.05-alt1
- Initial build.
