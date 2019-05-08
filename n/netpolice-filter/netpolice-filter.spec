Name: netpolice-filter
Version: 1.01
Release: alt5

Summary: URL filter for c-icap server
License: BSD
Group: System/Servers

Url: http://www.netpolice.ru/
Source0: %name-%version.tar.gz
Patch:   %name-fix-func-name-typo.patch
Packager: Anton Pischulin <letanton@altlinux.ru>

BuildRequires: gcc-c++ c-icap-devel libmemcache-devel opendbx-devel zlib-devel

Requires(pre): shadow-utils

Requires: %name = %version-%release
Requires: opendbx
Requires: opendbx-sqlite3

Provides: c-icap-url-filter

%description
ICAP module for checking URL against blacklist.

%prep
%setup
%patch -p2

%build
%autoreconf
%undefine __libtoolize
%undefine _configure_gettext
%configure cicapincdir=%_includedir/c_icap cicaplibs=-licapapi
%make_build

%install
%makeinstall_std
mv %buildroot%_libdir/%name/ %buildroot%_libdir/c_icap
rm -f %buildroot%_libdir/c_icap/*.la

%files
%doc AUTHORS README TODO
%_libdir/c_icap/srv_url_filter.so

%changelog
* Wed May 08 2019 Michael Shigorin <mike@altlinux.org> 1.01-alt5
- Use current g++

* Sun Oct 08 2017 Andrey Cherepanov <cas@altlinux.org> 1.01-alt4
- Rebuild with c-icap 0.5.2

* Mon Dec 07 2015 Andrey Cherepanov <cas@altlinux.org> 1.01-alt3
- Rebuild with new version of c-icap
- Fix typo in c-icap function name

* Sun Jul 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.01-alt2.5
- Fixed build

* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.4
- Delete Requires: name = version-release.
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.3
- Add provides.
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.2
- Fix spec.
* Mon Mar 1 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt1
- Initial ALTLinux release.
