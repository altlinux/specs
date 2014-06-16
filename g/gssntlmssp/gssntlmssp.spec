Name: gssntlmssp
Version: 0.3.1
Release: alt1
Summary: GSSAPI NTLMSSP Mechanism

Group: System/Libraries
License: LGPLv3+
Url: https://fedorahosted.org/gss-ntlmssp
Source: https://fedorahosted.org/released/gss-ntlmssp/%name-%version.tar

Requires: libkrb5 >= 1.11.2

BuildRequires: xsltproc xml-utils
BuildRequires: docbook-style-xsl docbook-dtds
BuildRequires: doxygen
BuildRequires: libkrb5-devel >= 1.11.2
BuildRequires: libunistring-devel
BuildRequires: zlib-devel
BuildRequires: libssl-devel

%description
A GSSAPI Mechanism that implements NTLMSSP

%package devel
Summary: Development header for GSSAPI NTLMSSP
Group: Development/C
License: LGPLv3+
Requires: %name = %version-%release

%description devel
Adds a header file with definition for custom GSSAPI extensions for NTLMSSP

%prep
%setup

%build
%add_optflags -I%_includedir/krb5
mkdir -p m4
%autoreconf
%configure \
    --includedir=%_includedir/krb5 \
    --disable-static

%make_build

%install
%makeinstall_std
install -d -m755 %buildroot%_sysconfdir/gss
install -pm644 examples/mech.ntlmssp %buildroot%_sysconfdir/gss/mech.ntlmssp

%check
make test_gssntlmssp

%files
%config(noreplace) %_sysconfdir/gss/mech.ntlmssp
%_libdir/gssntlmssp
%_man8dir/gssntlmssp.8*
%doc COPYING

%files devel
%_includedir/krb5/gssapi/*

%changelog
* Mon Jun 16 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- initial build
