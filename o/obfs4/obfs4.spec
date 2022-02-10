%global __find_debuginfo_files %nil
%global _unpackaged_files_terminate_build 1

%set_verify_elf_method unresolved=no
%add_debuginfo_skiplist %_bindir
%brp_strip_none %_bindir/*

%global cmdname obfs4proxy

Name:		obfs4
Version:	0.0.13
Release:	alt1
Summary:	The obfourscator, a pluggable transport for Tor

Group:		System/Servers
License:	GPLv3 and BSD
URL:		https://gitlab.com/yawning/obfs4

Packager:	Vladimir Didenko <cow@altlinux.org>

Source0: %name-%version.tar
Source1: %name.torrc

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
Requires: tor

%description
This is a look-like nothing obfuscation protocol that incorporates ideas and
concepts from Philipp Winter's ScrambleSuit protocol.  The obfs naming was
chosen primarily because it was shorter, in terms of protocol ancestry obfs4
is much closer to ScrambleSuit than obfs2/obfs3.

The notable differences between ScrambleSuit and obfs4:
 * The handshake always does a full key exchange (no such thing as a Session
   Ticket Handshake).
 * The handshake uses the Tor Project's ntor handshake with public keys
   obfuscated via the Elligator 2 mapping.
 * The link layer encryption uses NaCl secret boxes (Poly1305/XSalsa20).

As an added bonus, obfs4proxy also supports acting as an obfs2/3 client and
bridge to ease the transition to the new protocol.

%prep
%setup -q

%build
go build -mod=vendor -o ./%cmdname/%cmdname ./%cmdname

%install
# install main binary
mkdir -p -- %buildroot/%_bindir
install -Dpm0755 %cmdname/%cmdname %{buildroot}%{_bindir}/

# install man pages
install -d -p %{buildroot}%{_mandir}/man1
install -Dpm0644 doc/%cmdname.1 %{buildroot}%{_mandir}/man1/

# install config file
install -d -p %{buildroot}%{_sysconfdir}/tor
install -Dpm0644 %SOURCE1 %{buildroot}%{_sysconfdir}/tor

%files
%doc LICENSE LICENSE-GPL3.txt README.md
%_bindir/%cmdname
%_mandir/man1/%cmdname.1*
%config(noreplace) %{_sysconfdir}/tor/obfs4.torrc

%changelog
* Thu Feb 10 2022 Vladimir Didenko <cow@altlinux.org> 0.0.13-alt1
- New release

* Tue Nov 16 2021 Vladimir Didenko <cow@altlinux.org> 0.0.11-alt1.gite330d1b7
- Initial build for Sisyphus
