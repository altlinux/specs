Name: libbsd
Version: 0.3.0
Release: alt1

Summary: Library providing BSD-compatible functions for portability

License: BSD and ISC and Copyright only and Public Domain
Group: System/Libraries
Url: http://libbsd.freedesktop.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://libbsd.freedesktop.org/releases/%name-%version.tar

%description
libbsd provides useful functions commonly found on BSD systems, and
lacking on others like GNU systems, thus making it easier to port
projects with strong BSD origins, without needing to embed the same
code over and over again on each project.

%package devel
Summary: Development files for libbsd
Group: Development/Other
Requires: %name = %version-%release
Requires: pkg-config

%description devel
Development files for the libbsd library.

%prep
%setup

# fix encoding of flopen.3 man page
for f in src/flopen.3; do
  iconv -f iso8859-1 -t utf-8 $f >$f.conv
  touch -r $f $f.conv
  mv $f.conv $f
done

%build
%make_build CFLAGS="%optflags" \
     libdir=%_libdir \
     usrlibdir=%_libdir \
     exec_prefix=%prefix

%install
%makeinstall_std libdir=%_libdir \
     usrlibdir=%_libdir \
     exec_prefix=%prefix

# don't want static library
rm %buildroot%_libdir/%name.a
rm %buildroot%_man3dir/strlcpy*
rm %buildroot%_man3dir/strlcat*

# Move nlist.h into bsd directory to avoid conflict with elfutils-libelf.
# Anyone that wants that functionality should really used elfutils-libelf
# instead.
mv %buildroot%_includedir/nlist.h %buildroot%_includedir/bsd/

%files
%doc COPYING README TODO ChangeLog
%_libdir/%name.so.*

%files devel
%_man3dir/*.3.*
%_man3dir/*.3bsd.*
%_includedir/*.h
%_includedir/bsd
%_libdir/%name.so
%_pkgconfigdir/%name.pc
%_pkgconfigdir/%name-overlay.pc

%changelog
* Fri Dec 16 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- initial build for ALT Linux Sisyphus

* Sat Oct 08 2011 Eric Smith <eric@brouhaha.com> - 0.3.0-1
- Update to latest upstream release.
- Removed Patch0, fixed upstream.
- Removed BuildRoot, clean, defattr.

* Fri Jan 29 2010 Eric Smith <eric@brouhaha.com> - 0.2.0-3
- changes based on review by Sebastian Dziallas

* Fri Jan 29 2010 Eric Smith <eric@brouhaha.com> - 0.2.0-2
- changes based on review comments by Jussi Lehtola and Ralf Corsepious

* Thu Jan 28 2010 Eric Smith <eric@brouhaha.com> - 0.2.0-1
- initial version
