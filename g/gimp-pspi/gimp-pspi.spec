%def_with prebuilt

%define _gimptool %_bindir/gimptool
%define _gimppluginsdir %_libdir/gimp/2.0/plug-ins
%define _gimp_version %{get_version gimp}

Name: gimp-pspi
Version: 1.0.7
Release: alt2

Summary: Running Photoshop plug-ins in GIMP
License: GPL
Group: Graphics

Url: http://tml.pp.fi/gimp/pspi.html
Source: http://tml.pp.fi/gimp/gimp-pspi-%version.tar.gz
%if_with prebuilt
# binary package because compiling needs the non-free Photoshop 6 SDK
Source1: http://tml.pp.fi/gimp/gimp-pspi-1.0.7.suse10.i386.tar.gz
#Source1: http://tml.pp.fi/gimp/gimp-pspi-1.0.5.ubuntu.i386.tar.gz
%endif

Requires: wine
Requires: gimp >= %_gimp_version

BuildPreReq: libgimp-devel
%if_with prebuilt
BuildRequires: gimp
%endif

# depends on wine so anyways (but win64+64-bit PS SDK available)
ExclusiveArch: %{ix86}

%description
PSPI is a GIMP plug-in that runs 3rd-party Photoshop plug-in filters.

%prep
%setup -n pspi-%version

%build
%if_with prebuilt
# We do not own the Photoshop SDK and use binaries instead
tar xf %SOURCE1
%else
%configure --with-pssdk
%make_build
%endif

%install
install -d %buildroot%_gimppluginsdir
install pspi %buildroot%_gimppluginsdir
install pspi.exe.so %buildroot%_gimppluginsdir
#_gimptool --prefix=%buildroot%prefix --install-admin-bin pspi
#_gimptool --prefix=%buildroot%prefix --install-admin-bin pspi.exe.so

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.linux
%_gimppluginsdir/pspi
%_gimppluginsdir/pspi.exe.so

%changelog
* Wed May 16 2012 Michael Shigorin <mike@altlinux.org> 1.0.7-alt2
- repackaged for gimp-2.8
- updated an Url:

* Sun Sep 20 2009 Michael Shigorin <mike@altlinux.org> 1.0.7-alt1
- built for ALT Linux (closes: #21081)
