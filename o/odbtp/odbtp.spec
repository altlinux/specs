Name: odbtp
Version: 1.1.4
Release: alt1.qa1

Summary: Accessing win32-based databases using TCP/IP protocol

License: LGPL
Url: http://odbtp.sourceforge.net/
Group: System/Libraries

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/odbtp/%name-%version.tar.bz2
Patch0: %name-libtool.patch

# Automatically added by buildreq on Fri Oct 26 2007
BuildRequires: gcc-c++

%description
ODBTP is a TCP/IP protocol for connecting to Win32-based databases
from any platform. It is ideal for remotely accessing MS SQL Server,
MS Access, and Visual FoxPro database from Linux or Unix machines.
ODBTP is fast, efficient, and has many features that make it a quality
Open Source solution for database connectivity.

%package devel
Summary: Header files for odbtp library
Group: Development/C
Requires: %name = %version-%release

%description devel
Header files for odbtp library.

%package static
Summary: Static odbtp library
Group: Development/C
Requires: %name-devel = %version-%release

%description static
Static odbtp library.

%prep
%setup -q
%patch0 -p1

%build
%__autoreconf
%configure --disable-static
%make_build

%install
%make_install install \
	DESTDIR=%buildroot

install -d %buildroot%_sysconfdir/%name
install examples/odbtp.conf %buildroot%_sysconfdir/%name

%files
%doc AUTHORS ChangeLog NEWS README README.64bitOS docs
%dir %_sysconfdir/%name
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/odbtp.conf
%_libdir/libodbtp.so.*

%files devel
%_libdir/libodbtp.so
%_includedir/odbtp.h

#%files static
#%_libdir/libodbtp.a

%changelog
* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.1.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for odbtp
  * postun_ldconfig for odbtp
  * postclean-05-filetriggers for spec file

* Fri Oct 26 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

