Name: stoken
Version: 0.91
Release: alt1
Summary: Token code generator compatible with RSA SecurID 128-bit (AES) token
License: %lgpl2plus
Group: System/Libraries
Url: https://github.com/cernekee/stoken
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar

BuildPreReq: rpm-build-licenses
BuildRequires: libtomcrypt-devel libgtk+3-devel libxml2-devel libnettle-devel

%description
stoken is a tokencode generator compatible with RSA SecurID 128-bit (AES)
tokens. The project includes several components:
- A simple command line interface (CLI) used to manage and manipulate tokens
- A GTK+ GUI with cut&paste functionality
- A shared library allowing other software to generate tokencodes on demand

%package -n lib%name
Summary: %name library
Group: System/Libraries

%description -n lib%name
This package contains stoken library.

%package -n lib%name-devel
Summary: Header files and library for development with %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files and development libraries needed
to develop programs that use %name library.

%package -n %name-cli
Summary: Command line tool for %name
Group: Security/Networking

%description -n %name-cli
Command line tool for %name

%package -n %name-gui
Summary: Graphical interface program for %name
Group: Security/Networking

%description -n %name-gui
Graphical interface program for %name

%prep
%setup -q

%build
%autoreconf
%configure --disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_docdir/%name
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files -n %name-cli
%_bindir/%name
%_man1dir/%name.1.*

%files -n %name-gui
%_bindir/%name-gui
%_man1dir/%name-gui.1.*
%_datadir/%name
%_datadir/applications/*.desktop
%_datadir/pixmaps/*.png

%changelog
* Wed Feb 1 2017 Vladimir Didenko <cow@altlinux.org> 0.91-alt1
- New version

* Fri Oct 7 2016 Vladimir Didenko <cow@altlinux.org> 0.90-alt1
- Initial build for Sisyphus
