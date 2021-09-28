Name: cups-backend-bjnp
Version: 2.0.3
Release: alt2
License: GPLv2
URL: https://sourceforge.net/projects/cups-bjnp/
# Source: http://downloads.sourceforge.net/cups-bjnp/cups-bjnp-%version.tar.gz
Source: cups-bjnp-%version.tar
Patch: fix-off-by-one.patch

Group: System/Configuration/Printing

BuildRequires: cups libcups-devel
Requires: cups

Summary: CUPS backend for the Canon BJNP network printers 
%define cups_backend_dir /usr/lib/cups/backend

%description
This package contains a backend for CUPS for Canon printers using the
proprietary BJNP network protocol.

%prep
%setup -n cups-bjnp-%version
%patch -p1

%build
%configure --with-cupsbackenddir=%cups_backend_dir
%make_build

%install
%make DESTDIR=%buildroot install

%files
%cups_backend_dir/bjnp
%doc COPYING ChangeLog TODO NEWS README

%changelog
* Tue Sep 28 2021 Oleg Solovyov <mcpain@altlinux.org> 2.0.3-alt2
- Fix build

* Mon Feb 08 2021 Oleg Solovyov <mcpain@altlinux.org> 2.0.3-alt1
- Build version 2.0.3

* Tue Nov 05 2019 Oleg Solovyov <mcpain@altlinux.org> 2.0.1-alt2
- Fix FTBFS

* Tue May 29 2018 Oleg Solovyov <mcpain@altlinux.org> 2.0.1-alt1
- Build version 2.0.1

* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 1.0.0-alt1
- New version

* Mon Mar 15 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.5.4-alt1
- Build for Sisyphus
