Name: btpd
Version: 0.13
Release: alt2.qa1.1
Packager: Paul Wolneykien <manowar@altlinux.ru>

Summary: Bittorrent download daemon.
License: Non-ad BSD license
Group: Networking/File transfer

Source: %name-%version.tar.gz

Requires: libssl

# Automatically added by buildreq on Fri Aug 29 2008
BuildRequires: libssl-devel

%description
Btpd is a bittorrent client consisting of a daemon and client commands.

%prep
%setup -q

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_mandir/man1/*
%_datadir/doc/%name-%version/*
# The package does not own its own docdir subdirectory.
# The line below is added by repocop to fix this bug in a straightforward way. 
# Another way is to rewrite the spec to use relative doc paths.
%dir %_docdir/btpd-%version 

%changelog
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
