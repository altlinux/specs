Name: openvpn-auth-ldap
Version: 2.0.4
Release: alt4

Summary: OpenVPN plugin for LDAP authentication
License: BSD
Group: Networking/WWW
URL: https://github.com/threerings/openvpn-auth-ldap

Source0: %name-%version.tar
# tools are not compiled with given CFLAGS
Patch1: auth-ldap-tools-CFLAGS.patch
# Patch from upstream issue nA.4, to fix tap bridging.
Patch2: auth-ldap-remoteAddress.patch
# fixed buffer overflow
Patch3: auth-ldap-fix-cve-2024-28820.patch

Buildrequires: doxygen
BuildRequires: gcc-objc
BuildRequires: libcheck-devel
BuildRequires: gnustep-base-devel
Buildrequires: libldap-devel
Buildrequires: libssl-devel
Buildrequires: openvpn-devel
BuildRequires: re2c
BuildRequires: autoconf
Requires: openvpn >= 2.0

%description
The OpenVPN Auth-LDAP Plugin implements username/password authentication via
LDAP for OpenVPN 2.x.

%prep
%setup
%patch1 -p1 -b .tools-CFLAGS
%patch2 -p1 -b .remoteAddress
%patch3 -p1
# Fix plugin from the instructions in the included README
sed -i 's|^plugin .*| plugin %_libdir/openvpn/plugins/openvpn-auth-ldap.so "/etc/openvpn/auth/ldap.conf"|g' README.md
autoconf
autoheader

%build
%configure CFLAGS="%optflags -fPIC -std=gnu99" \
    --libdir=%_libdir/openvpn/plugins \
    --with-openvpn=%_includedir

%make_build

%install
# Main plugin
mkdir -p %buildroot%_libdir/openvpn/plugins
%makeinstall_std
# Example config file
install -D -p -m 0600 auth-ldap.conf \
    %buildroot%_sysconfdir/openvpn/auth/ldap.conf


%files
%doc --no-dereference LICENSE
%doc README.md auth-ldap.conf
%dir %_sysconfdir/openvpn/auth/
%config(noreplace) %_sysconfdir/openvpn/auth/ldap.conf
%_libdir/openvpn/plugins/openvpn-auth-ldap.so

%changelog
* Sat Sep 14 2024 Nikolay Burykin <bne@altlinux.org> 2.0.4-alt4
- Fix for buffer overflow in extract_openvpn_cr() (CVE-2024-28820) (ALT #51361)

* Mon May 22 2023 Nikolay Burykin <bne@altlinux.org> 2.0.4-alt3
- Initial build for ALT
