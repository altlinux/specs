Name: fuse-nfs
Version: 1.0.0
Release: alt0.2

Summary: A FUSE module for NFSv3
License: GPLv3

Group: System/Libraries
Url: https://github.com/sahlberg/%name

#Source: %url/archive/%name-%version.tar.gz
Source: %name-%version.tar

PreReq: libcap-utils
Requires: fuse
BuildRequires: libfuse-devel libnfs-devel xsltproc docbook-style-xsl

%description
%name is a fuse module that implements the NFSv3 protocol.

%package devel
Group: Development/C
Summary: %name development files
Requires: %name = %version-%release

%description devel
%name is a fuse module that implements the NFSv3 protocol.

This package provides pkg-config file for %name.

%prep
%setup

%build
%autoreconf
%configure

%install
%makeinstall_std

%post
setcap 'cap_net_bind_service=+ep' %_bindir/%name 2>/dev/null ||:

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc README

%files devel
%_pkgconfigdir/%name.pc


%changelog
* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.2
- required fuse of course

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt0.1
- first preview for Sisyphus


