# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name opencdk
%define libgcrypt_version 1.1.94

%define major	10
%define libname lib%{name}%{major}
%define libname_orig lib%{name}
%define develname lib%{name}-devel

Summary:	Open Crypto Development Kit
Name:		opencdk
Version:	0.6.6
Release:	alt1_12
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnutls.org/
Source0:	http://www.gnu.org/software/gnutls/releases/opencdk/%{name}-%{version}.tar.bz2
Source1:	http://www.gnu.org/software/gnutls/releases/opencdk/%{name}-%{version}.tar.bz2.sig
Patch0:		opencdk-0.6.6-link.patch
BuildRequires:	zlib-devel
BuildRequires:	gcrypt-utils libgcrypt-devel
Source44: import.info

%description
%{name} library provides basic parts of the OpenPGP message format.
Due to some possible security problems, the library also implements
parts of draft-ietf-openpgp-rfc2440bis-08.txt.

The aim of the library is *not* to replace any available OpenPGP version.
There will be no real support for key management (sign, revoke,
alter preferences, ...) and some other parts are only rudimentary
available. The main purpose is to handle and understand OpenPGP
packets and to use basic operations. For example to encrypt/decrypt
or to sign/verify and packet routines.

%package -n	%{libname}
Summary:	Open Crypto Development Kit
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{libname_orig} = %{version}-%{release}

%description -n	%{libname}
%{name} library provides basic parts of the OpenPGP message format.
Due to some possible security problems, the library also implements
parts of draft-ietf-openpgp-rfc2440bis-08.txt.

The aim of the library is *not* to replace any available OpenPGP version.
There will be no real support for key management (sign, revoke,
alter preferences, ...) and some other parts are only rudimentary
available. The main purpose is to handle and understand OpenPGP
packets and to use basic operations. For example to encrypt/decrypt
or to sign/verify and packet routines.


%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	gcrypt-utils
Obsoletes:	lib%{name}8-devel

%description -n	%{develname}
%{name} library provides basic parts of the OpenPGP message format.

You will need to install this package if you want to develop or 
compile any applications/libraries that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la

install -D -m 644 src/opencdk.m4 %{buildroot}%{_datadir}/aclocal/opencdk.m4

echo #multiarch_binaries %{buildroot}%{_bindir}/*-config

%files -n %{libname}
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/opencdk-api.html
%{_bindir}/opencdk-config
#multiarch %{multiarch_bindir}/*-config
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/opencdk.pc


%changelog
* Sat Apr 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.6.6-alt1_12
- new version

* Mon Dec 03 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.6.6-alt1
- 0.6.6 release.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.6.4-alt1
- 0.6.4 release.

* Wed Feb 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.5.9-alt2
- Added Packager field.
- Minor specfile cleanup.

* Sun Sep 10 2006 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.9-alt1
- Release 0.5.9
- Renamed the source package to opencdk

* Tue Nov 29 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.8-alt1
- 0.5.8

* Sun Aug 14 2005 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.7-alt1
- Updated to 0.5.7

* Sat Oct 16 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.5-alt1
- New upstream release
- Built against libgcrypt 1.2

* Sat Mar 27 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.4-alt2
- Rebuilt against libgcrypt 1.1.93

* Sat Mar 06 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.4-alt1
- New upstream release
- Fixes to build with new autotools

* Thu Jan 29 2004 Mikhail Zabaluev <mhz@altlinux.ru> 0.5.3-alt1
- Initial release
