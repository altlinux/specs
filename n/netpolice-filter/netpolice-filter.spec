Name: netpolice-filter
Version: 1.01
Release: alt2.4
Packager: Anton Pischulin <letanton@altlinux.ru>

Summary: url filter for c-icap server
License: BSD
Group: System/Servers
Url: http://www.netpolice.ru/

Source0: %name-%version.tar.gz

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: gcc4.4-c++ c-icap-devel libmemcache-devel opendbx-devel zlib-devel

Requires(pre): shadow-utils

Requires: %name = %version-%release
Requires: opendbx
Requires: opendbx-sqlite3

Provides: c-icap-url-filter

%description
ICAP module for checking URL against blacklist.

%prep
%setup -q

%build
aclocal
autoconf  
autoheader
cp /usr/share/libtool-2.2/config/ltmain.sh ltmain.sh
automake --add-missing --copy  
cp INSTALL INSTALL.txt

%undefine __libtoolize
%configure cicapincdir=%_includedir/c-icap
%make_build --debug -j

%install
%make_install DESTDIR=%buildroot install
mv %buildroot%_libdir/%name/ %buildroot%_libdir/c-icap

%files
%doc AUTHORS README INSTALL.txt TODO
%_libdir/c-icap/srv_url_filter.so

%changelog
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.4
- Delete Requires: name = version-release.
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.3
- Add provides.
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.2
- Fix spec.
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt1
- Initial ALTLinux release.
