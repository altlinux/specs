%define RELEASE altlinux
%global soversion 1
Name: fwupdate
Version: 11
Release: alt1%ubt
Summary: Tools to manage UEFI firmware updates
License: GPLv2+
Url: https://github.com/rhinstaller/fwupdate
Group: System/Kernel and hardware
Requires: %name-efi = %EVR
BuildRequires: libefivar-devel
BuildRequires: gnu-efi
BuildRequires: elfutils libpopt-devel gettext pkgconfig
BuildRequires: systemd
BuildRequires: pesign
BuildRequires: rpm-macros-uefi
BuildRequires(pre): rpm-build-ubt
%ifarch x86_64
BuildRequires: libsmbios-devel
%endif
ExclusiveArch: x86_64 aarch64
Source0: %name-%version.tar
Source1: %name-install
Patch0: %name-%version-alt.patch

%ifarch x86_64
%global efiarch x64
%global efialtarch ia32
%endif
%ifarch aarch64
%global efiarch aa64
%endif

%global efidir altlinux

%description
fwupdate provides a simple command line interface to the UEFI firmware updates.

%package common
Summary: Scripts and services for %name
Group: System/Kernel and hardware

%description common
Scripts and services for %name

%package -n lib%name%soversion
Summary: Library to manage UEFI firmware updates
Group: System/Kernel and hardware
%ifarch %ix86
Requires: shim-signed
%endif
Requires: %name-efi = %EVR

%description -n lib%name%soversion
Library to allow for the simple manipulation of UEFI firmware updates.

%package devel
Summary: Development headers for libfwup
Requires: lib%name%soversion = %EVR
Requires: libefivar-devel
Group: System/Kernel and hardware

%description devel
development headers required to use libfwup.

%package efi
Summary: UEFI binaries used by libfwupdate
Requires: lib%name%soversion = %EVR
Requires: %name-common = %EVR
Group: System/Kernel and hardware

%description efi
UEFI binaries used by libfwupdate.

%prep
%setup
%patch0 -p1
mkdir build-%efiarch
%ifarch x86_64
mkdir build-%efialtarch
%endif

%build
cd build-%efiarch
make TOPDIR=.. -f ../Makefile OPT_FLAGS="$RPM_OPT_FLAGS" \
     libdir=%_libdir bindir=%_bindir \
     libexecdir=%_libexecdir \
     EFIDIR=%efidir  GNUEFIDIR=%_libdir
cd ..

%ifarch x86_64
cd build-%efialtarch
setarch linux32 -B make TOPDIR=.. -f ../Makefile ARCH=%efialtarch \
                        OPT_FLAGS="$RPM_OPT_FLAGS" \
                        libdir=%_libdir bindir=%_bindir \
			libexecdir=%_libexecdir \
                        EFIDIR=%efidir GNUEFIDIR=%_prefix/lib
cd ..
%endif

%install
cd build-%efiarch
%makeinstall_std TOPDIR=.. -f ../Makefile \
              EFIDIR=%efidir RPMARCH=%_arch RELEASE=%RELEASE \
              libdir=%_libdir bindir=%_bindir mandir=%_mandir \
	      libdatadir=/lib \
              localedir=%_datadir/locale/ includedir=%_includedir \
              libexecdir=%_libexecdir datadir=%_datadir \
              sharedstatedir=%_sharedstatedir 
cd ..
install -pDm755 %SOURCE1 %buildroot%_libexecdir/fwupdate/install

%ifarch x86_64
cd build-%efialtarch
setarch linux32 -B %makeinstall_std ARCH=%efialtarch TOPDIR=.. -f ../Makefile \
                                 EFIDIR=%efidir RPMARCH=%_arch \
                                 RELEASE=%RELEASE libdir=%_libdir \
                                 bindir=%_bindir mandir=%_mandir \
                                 localedir=%_datadir/locale/ \
				 libdatadir=/lib \
                                 includedir=%_includedir \
                                 libexecdir=%_libexecdir \
                                 datadir=%_datadir \
                                 sharedstatedir=%_sharedstatedir
cd ..
%endif
touch %buildroot%_sharedstatedir/fwupdate/done
mkdir -p %buildroot/%_libdir/efi/fw/
mv %buildroot/boot/efi/EFI/%efidir/fwup* %buildroot/%_libdir/efi/fw/

%post efi
%_libexecdir/fwupdate/install 
%_libexecdir/fwupdate/cleanup

%files
%doc COPYING
%_bindir/fwupdate
%doc %_mandir/man1/*
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/fwupdate

%files devel
%doc %_mandir/man3/*
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files common
%_unitdir/fwupdate-cleanup.service
%attr(0755,root,root) %dir %_sharedstatedir/fwupdate/
%config(noreplace) %ghost %_sharedstatedir/fwupdate/done
%attr(0755,root,root) %dir %_libexecdir/fwupdate
%_libexecdir/fwupdate/cleanup
%_libexecdir/fwupdate/install

%files -n lib%name%soversion
%_libdir/*.so.%{soversion}*

%files efi
%dir %_libdir/efi/fw
%_libdir/efi/fw/fw*

%changelog
* Fri Apr 27 2018 Anton Farygin <rider@altlinux.ru> 11-alt1%ubt
- new version

* Wed Mar 28 2018 Anton Farygin <rider@altlinux.ru> 10-alt3
- rebuilt with new gnu-efi
- small improvement of the installation script

* Tue Mar 27 2018 Anton Farygin <rider@altlinux.ru> 10-alt2
- fixed efi files location in install script

* Mon Mar 05 2018 Anton Farygin <rider@altlinux.ru> 10-alt1
- first build for ALT, based on RH spec
