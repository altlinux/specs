Name:		cups-x2go
Version:	3.0.1.4
Release:	alt1.1

Summary:	CUPS backend for printing from X2Go
License:	GPLv2+
Group:		Publishing
Url:		http://www.x2go.org/
BuildArch:	noarch

# Upstream:	git://code.x2go.org/cups-x2go.git
Source:		%name-%version.tar

Patch1:		cups-x2go-setpdfwrite.patch

Requires:	perl
Requires:	x2goserver
Requires:	x2goserver-printing
Requires:	cups
Requires:	ghostscript
Requires:	openssh-clients

%description
X2Go is a server based computing environment with
- session resuming
- low bandwidth support
- session brokerage support
- client side mass storage mounting support
- audio support
- authentication by smartcard and USB stick

CUPS backend for printing from X2Go.

%prep
%setup
%patch1 -p1

%install
mkdir -p %buildroot%prefix/lib/cups/backend
# The cups-x2go backends wants root permissions. So give it to them.
# http://www.cups.org/documentation.php/doc-1.4/man-backend.html says:
# Backends without world execute permissions are run as the root user.
# Otherwise, the backend is run using the unprivileged user account,
# typically "lp".
install -p -m700 cups-x2go %buildroot%prefix/lib/cups/backend/
mkdir -p %buildroot%_sysconfdir/cups
cp -p cups-x2go.conf %buildroot%_sysconfdir/cups/
mkdir -p %buildroot%_datadir/ppd/cups-x2go
cp -p CUPS-X2GO.ppd %buildroot%_datadir/ppd/cups-x2go/
mkdir -p %buildroot%_datadir/x2go/versions
cp -p VERSION.cups-x2go %buildroot%_datadir/x2go/versions/

%files
%prefix/lib/cups/backend/cups-x2go
%config(noreplace) %_sysconfdir/cups/cups-x2go.conf
%_datadir/x2go/versions/VERSION.cups-x2go
%dir %_datadir/ppd/cups-x2go
%_datadir/ppd/cups-x2go/*
%doc README.txt

%changelog
* Sun Feb 19 2023 Elena Mishina <lepata@altlinux.org> 3.0.1.4-alt1.1
- Fix GhostScript command line (closes: #45151).

* Thu Nov 22 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.1.4-alt1
- New version.

* Fri Apr 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.1.3-alt3
- Build from upstream git.

* Mon Sep 12 2017 Leonid Krivoshein <klark@altlinux.org> 3.0.1.3-alt1
- Initial build in Sisyphus.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> 3.0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> 3.0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> 3.0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Orion Poplawski <orion@cora.nwra.com> 3.0.1.3-1
- Update to 3.0.1.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 3.0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Orion Poplawski <orion@cora.nwra.com> 3.0.1.1-1
- Update to 3.0.1.1
- Require openssh-clients

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> 3.0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 9 2014 Orion Poplawski <orion@cora.nwra.com> 3.0.1.0-1
- Update to 3.0.1.0

* Wed Sep 4 2013 Orion Poplawski <orion@cora.nwra.com> 3.0.0.4-2
- Use install to set permissions on cups-x2go
- Drop %%doc for now
- Mark config file as %%config(noreplace)
- Fix Group
- Drop tabs

* Fri Dec 14 2012 Orion Poplawski <orion@cora.nwra.com> 3.0.0.4-1
- Initial Fedora package

