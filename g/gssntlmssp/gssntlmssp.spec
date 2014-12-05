%def_with wbclient

Name: gssntlmssp
Version: 0.5.0
Release: alt2
Summary: GSSAPI NTLMSSP Mechanism

Group: System/Libraries
License: LGPLv3+
Url: https://fedorahosted.org/gss-ntlmssp
Source: https://fedorahosted.org/released/gss-ntlmssp/%name-%version.tar

Requires: libkrb5 >= 1.13

BuildRequires: xsltproc xml-utils
BuildRequires: docbook-style-xsl docbook-dtds
BuildRequires: doxygen
BuildRequires: libkrb5-devel >= 1.13
BuildRequires: libunistring-devel
BuildRequires: zlib-devel
BuildRequires: libssl-devel
%{?_with_wbclient:BuildRequires: pkgconfig(wbclient)}

%description
A GSSAPI Mechanism that implements NTLMSSP

%package devel
Summary: Development header for GSSAPI NTLMSSP
Group: Development/C
License: LGPLv3+
BuildArch: noarch
Requires: %name = %version-%release

%description devel
Adds a header file with definition for custom GSSAPI extensions for NTLMSSP

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure \
    %{subst_with wbclient} \
    --disable-static

%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sysconfdir/gss/mech.d
install -pm644 examples/mech.ntlmssp %buildroot%_sysconfdir/gss/mech.d/ntlmssp.conf

%find_lang %name

%check
make test_gssntlmssp

%files -f %name.lang
%config(noreplace) %_sysconfdir/gss/mech.d/ntlmssp.conf
%_libdir/gssntlmssp
%_man8dir/gssntlmssp.8*
%doc COPYING

%files devel
%_includedir/gssapi/*

%changelog
* Thu Nov 13 2014 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt2
- build with krb5-1.13

* Thu Aug 28 2014 Alexey Shabalin <shaba@altlinux.ru> 0.5.0-alt1
- 0.5.0
- build with wbclient support

* Wed Jul 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Mon Jun 16 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- initial build
