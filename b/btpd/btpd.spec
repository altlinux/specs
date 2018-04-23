Name: btpd
Version: 0.16.0.16.gita7fb9a8
Release: alt1
Packager: Paul Wolneykien <manowar@altlinux.ru>

Summary: Bittorrent download daemon.
License: Non-ad BSD license
Group: Networking/File transfer

Url: https://github.com/btpd/btpd
Source: %name-%version.tar.gz

Requires: libssl

# Automatically added by buildreq on Fri Aug 29 2008
BuildRequires: libssl-devel

%description
Btpd is a bittorrent client consisting of a daemon and client commands.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc README CHANGES
%_bindir/*
%_man1dir/*

%changelog
* Mon Apr 23 2018 Grigory Ustinov <grenka@altlinux.org> 0.16.0.16.gita7fb9a8-alt1
- Build new version.
- Add url tag (Closes: #19030).

* Wed Mar 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt2.qa2
- Fixed build with glibc 2.17

* Tue Dec 07 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2.qa1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.13-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * docdir-is-not-owned for btpd
  * postclean-05-filetriggers for spec file

* Fri Aug 29 2008 Paul Wolneykien <manowar@altlinux.ru> 0.13-alt2
- Copyright information placed into docs.
- Original documentation placed into docs.

* Fri Aug 22 2008 Paul Wolneykien <manowar@altlinux.ru> 0.13-alt1
- Initial relese for ALT Linux.
