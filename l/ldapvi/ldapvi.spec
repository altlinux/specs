Name: ldapvi
Version: 1.7
Release: alt1
Summary: Interactive LDAP client for Unix terminal
Group: Networking/Remote access
Url: http://www.lichteblau.com/ldapvi/
License: GPLv2
Source: %name-%version.tar.gz

# Automatically added by buildreq on Mon Nov 17 2014
# optimized out: libcloog-isl4 libncurses-devel libsasl2-3 libtinfo-devel pkg-config
BuildRequires: glib2-devel libldap-devel libpopt-devel libreadline-devel libsasl2-devel libsocket libssl-devel

%description
The ldapvi is an interactive LDAP client for Unix terminals. Using it,
you can update LDAP entries with a text editor. Think of it as vipw(1)
for LDAP.

ldapvi was written by David Lichteblau.

%prep
%setup
# XXX Hack out user defined getline
for N in `grep -rl getline .`; do sed -i 's/getline/GetLine/g' "$N"; done

%build
%configure
%make_build

%install
install -D %name %buildroot/%_bindir/%name
install -D %name.1 %buildroot/%_man1dir/%name.1

%files
%doc NEWS
%_man1dir/*
%_bindir/*

%changelog
* Mon Nov 17 2014 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Mon Nov 17 2014 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Initial build for ALT

