Summary: ELF core file debugger
Name: viewcore
Version: 0.1
Release: alt3.1
License: GPL
Group: Development/Debuggers
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version-2.tar.bz2
Url: http://turing.gcsu.edu/~adimitro/index.html

# Automatically added by buildreq on Sun Nov 27 2005
BuildRequires: gcc-c++ libstdc++-devel

%description
Program to debug ELF core files.

%prep
%setup -n %name

%build
%configure
%make_build

%install
%make_install install \
	DESTDIR=%buildroot

%files
%attr(0755, root, root) %_bindir/viewcore

%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt3.1
- rebuild (with the help of girar-nmu utility)

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt3
- cleanup spec

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1-2
-

