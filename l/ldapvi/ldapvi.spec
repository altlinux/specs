Name: ldapvi
Version: 1.7
Release: alt3
Summary: Interactive LDAP client for Unix terminal
Group: Networking/Remote access
Url: http://www.lichteblau.com/ldapvi/
License: GPLv2
Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Jan 24 2019
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libsasl2-3 libtinfo-devel pkg-config python-base python3 python3-base sh4
BuildRequires: glib2-devel libldap-devel libncurses-devel libpopt-devel libreadline-devel libsasl2-devel libsocket libssl-devel

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
* Thu Jan 24 2019 Fr. Br. George <george@altlinux.ru> 1.7-alt3
- Fix build

* Thu Nov 27 2014 Fr. Br. George <george@altlinux.ru> 1.7-alt2
- Make Fedoraimport happy

* Mon Nov 17 2014 Fr. Br. George <george@altlinux.ru> 1.7-alt1
- Autobuild version bump to 1.7

* Mon Nov 17 2014 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Initial build for ALT

