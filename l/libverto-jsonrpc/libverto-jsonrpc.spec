Group: Other
%add_optflags %optflags_shared
Name:           libverto-jsonrpc
Version:        0.1.0
Release:        alt1_9
Summary:        JSON-RPC support for libverto

License:        MIT
URL:            https://fedorahosted.org/libverto
Source0:        https://fedorahosted.org/releases/l/i/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  libverto-devel >= 0.2.4
BuildRequires:  libjson-devel
BuildRequires:  findutils
Source44: import.info

%description
A library for doing JSON-RPC over a socket, using the libverto API.

%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%{_includedir}/verto-jsonrpc.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_7
- initial fc import

