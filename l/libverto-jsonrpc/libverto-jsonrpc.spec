Group: Other
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libverto-jsonrpc
Version:        0.1.0
Release:        alt3_22
Summary:        JSON-RPC support for libverto

License:        MIT
URL:            https://fedorahosted.org/libverto
Source0:        https://fedorahosted.org/releases/l/i/%{name}/%{name}-%{version}.tar.gz

Patch0:         libverto-jsonrpc-0.1.0_json-c_013.patch

BuildRequires:  libverto-devel >= 0.2.4
BuildRequires:  libjson-c-devel
BuildRequires:  findutils
BuildRequires:  libtool
Source44: import.info

%description
A library for doing JSON-RPC over a socket, using the libverto API.

%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

autoreconf -fiv

%build
%configure --disable-static
%make_build

%install
%makeinstall_std
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%{_includedir}/verto-jsonrpc.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Dec 05 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt3_22
- update to new release by fcimport

* Fri May 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt3_9
- Rebuild with libjson-c

* Tue May 02 2017 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt2_9
- Rebuild with new version of libjson

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.1.0-alt1_7
- initial fc import

