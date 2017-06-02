%define post 35
Name: 	  omi
Version:  1.2.0
Release:  alt1

Summary:  Open Management Infrastructure
License:  MIT
Group:    Other
Url:      https://github.com/Microsoft/omi

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Microsoft/omi/archive/v%version-%post.tar.gz
Source:   %name-%version.tar

# Automatically added by buildreq on Fri Jun 02 2017
# optimized out: libcom_err-devel libkrb5-devel libstdc++-devel lsb-release pkg-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ libpam-devel libssl-devel openssl lsb-core

%description
Open Management Infrastructure (OMI) is an open source project
to further the development of a production quality implementation
of the DMTF CIM/WBEM standards.
The OMI CIMOM is also designed to be portable and highly modular.

In order to attain its small footprint, it is coded in C,
which also makes it a much more viable CIM Object Manager for embedded systems
and other infrastructure components that have memory constraints for their management processor.

%package -n lib%name

Summary: Open Management Infrastructure
Group: Development/C

%description -n lib%name
Open Management Infrastructure (OMI) is an open source project
to further the development of a production quality implementation
of the DMTF CIM/WBEM standards.
The OMI CIMOM is also designed to be portable and highly modular.

In order to attain its small footprint, it is coded in C,
which also makes it a much more viable CIM Object Manager for embedded systems
and other infrastructure components that have memory constraints for their management processor.

%package -n lib%name-devel

Summary: Open Management Infrastructure
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for %name.


%prep
%setup
%__subst "s|.*-rpath.*|true|g" Unix/buildtool

%build
# FIXME: version
export OMI_BUILDVERSION_MAJOR=1
export OMI_BUILDVERSION_MINOR=2
export OMI_BUILDVERSION_PATCH=0
export OMI_BUILDVERSION_BUILDNR=%post
cd Unix
./configure --prefix=%prefix --localstatedir=/var/omi --sysconfdir=/etc/omi \
	--libdir=%_libdir --includedir=%_includedir --datadir=%_datadir/%name \
	--certsdir=/etc/omi/ssl
#	 --credsdir=/etc/omi/creds

%make_build

%install
cd Unix
%makeinstall_std

#%check
#%make_build check

%files
%dir %_sysconfdir/omi/
%_sysconfdir/omi/omiregister/
%_sysconfdir/omi/ssl/
%config(noreplace) %_sysconfdir/omi/*.conf
%_bindir/*
#_man1dir/*
%doc LICENSE CONTRIBUTING.md README.md

%files -n lib%name
%_libdir/*.so
%_datadir/%name/

%files -n lib%name-devel
%_includedir/*

%changelog
* Fri Jun 02 2017 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Sisyphus
