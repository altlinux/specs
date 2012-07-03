Name: asio
Version: 1.4.7
Release: alt1

Summary: C++ library for network programming
License: Boost Software License
Group: Development/C++

Url: http://asio.sourceforge.net/

Source0: %name-%version.tar.bz2

Packager: Ilya Mashkin <oddity@altlinux.ru>
BuildArch: noarch

# Automatically added by buildreq on Thu Apr 03 2008 (-bi)
BuildRequires: boost-devel gcc-c++ libssl-devel

%description
asio is a cross-platform C++ library for network programming that provides
developers with a consistent asynchronous I/O model using a modern C++
approach.

%prep
%setup -q

%build
%configure

%install
cd include
%make_install DESTDIR=%buildroot install

%files
%doc COPYING INSTALL LICENSE_1_0.txt README doc src
%_includedir/asio.hpp
%dir %_includedir/asio
%_includedir/asio/

%changelog
* Sun Jan 09 2011 Ilya Mashkin <oddity@altlinux.ru> 1.4.7-alt1
- 1.4.7

* Tue Jun 01 2010 Ilya Mashkin <oddity@altlinux.ru> 1.4.5-alt1
- 1.4.5

* Tue Aug 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Thu Jan 08 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt1
- New stable version 1.2.0

* Sun Apr 20 2008 Igor Zubkov <icesik@altlinux.org> 1.0.0-alt1
- 0.3.9 -> 1.0.0

* Thu Apr 03 2008 Igor Zubkov <icesik@altlinux.org> 0.3.9-alt1
- 0.3.7 -> 0.3.9
- buildreq

* Sat May 12 2007 Igor Zubkov <icesik@altlinux.org> 0.3.7-alt1
- build for Sisyphus

