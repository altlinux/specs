Name: kstart
Version: 4.3
Release: alt1

Summary: Daemon version of kinit for Kerberos v5
License: MIT
Group:   Security/Networking
URL:     http://www.eyrie.org/~eagle/software/kstart/

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: libkrb5-devel
BuildRequires: perl-podlators

Source0: http://archives.eyrie.org/software/kerberos/kstart-%{version}.tar.gz


%description

k5start is a modified version of kinit which can use keytabs to
authenticate, can run as a daemon and wake up periodically to refresh
a ticket, and can run single commands with its own authentication
credentials and refresh those credentials until the command exits.

%prep
%setup -q

%build
%add_optflags -I%_includedir/krb5
%autoreconf
%configure --disable-k4start --enable-setpag --enable-reduced-depends \
           --with-krb5-include=%_includedir/krb5
%make

%install
%makeinstall_std

%files
%doc NEWS README
%_bindir/k5start
%_bindir/krenew
%_mandir/man1/k5start.1.*
%_mandir/man1/krenew.1.*

%changelog
* Sun Jul 03 2022 Andrey Cherepanov <cas@altlinux.org> 4.3-alt1
- New version.

* Fri Jan 13 2017 Andrey Cherepanov <cas@altlinux.org> 4.2-alt1
- New version

* Mon Dec 21 2015 Andrey Cherepanov <cas@altlinux.org> 4.1-alt2
- Do not use strict extension for man pages

* Wed Feb 13 2013 Andrey Cherepanov <cas@altlinux.org> 4.1-alt1
- Initial build in Sisyphus

