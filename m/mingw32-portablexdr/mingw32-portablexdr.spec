BuildRequires: rpm-build-mingw32
%define __strip %{_mingw32_strip}
%define __objdump %{_mingw32_objdump}

Name:		mingw32-portablexdr
Version:	4.9.1
Release:	alt1_3
Summary:	MinGW Windows PortableXDR / RPC Library

License:	LGPLv2+
Group:		System/Libraries
URL:		http://et.redhat.com/~rjones/portablexdr/
Source0:	http://et.redhat.com/~rjones/portablexdr/portablexdr-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	mingw32-filesystem >= 56
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-binutils

# Remove include of config.h from public header.
Patch0:         portablexdr-4.9.1-no-config-h.patch
Source44: import.info


%description
MinGW Windows PortableXDR XDR / RPC library.

%prep
%setup -q -n portablexdr-%{version}

%patch0 -p1

%build
%{_mingw32_configure} --disable-static
make %{?_smp_flags}


%install
make DESTDIR=$RPM_BUILD_ROOT install


%files
%doc COPYING.LIB
%{_mingw32_bindir}/portable-rpcgen.exe
%{_mingw32_bindir}/libportablexdr-0.dll
%{_mingw32_libdir}/libportablexdr.dll.a
%{_mingw32_libdir}/libportablexdr.la
%{_mingw32_includedir}/rpc


%changelog
* Thu Aug 18 2011 Igor Vlasenko <viy@altlinux.ru> 4.9.1-alt1_3
- initial release by fcimport

