Summary: CUPS backend for the Canon BJNP network printers 
Name: cups-backend-bjnp
Version: 1.0.0
Release: alt1
License: GPLv2
Source: http://downloads.sourceforge.net/cups-bjnp/cups-bjnp-%{version}.tar.gz
Group: System/Servers
URL: https://sourceforge.net/projects/cups-bjnp/
Packager: Sergei Epiphanov <serpiph@altlinux.ru>

BuildRequires: cups-devel
Requires: cups

%define cups_backend_dir /usr/lib/cups/backend

%description
This package contains a backend for CUPS for Canon printers using the
proprietary BJNP network protocol.

%prep
%setup -q -n cups-bjnp-%version

%build
%configure --with-cupsbackenddir=%cups_backend_dir
%make

%install
%make DESTDIR=%buildroot install

%files
%cups_backend_dir/bjnp
%doc COPYING ChangeLog TODO NEWS README

%changelog
* Thu Jul 21 2011 Sergei Epiphanov <serpiph@altlinux.ru> 1.0.0-alt1
- New version

* Mon Mar 15 2010 Sergei Epiphanov <serpiph@altlinux.ru> 0.5.4-alt1
- Build for Sisyphus
