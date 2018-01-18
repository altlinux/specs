%define _version 10.2+0.94+2

Name: libcdio-paranoia
Version: %(echo %_version |sed -e 's|\+|.|g')
Release: alt1

Summary: CD paranoia library from libcdio
Group: System/Libraries
License: GPLv3+
Url: http://www.gnu.org/software/libcdio/

Source: http://ftp.gnu.org/gnu/libcdio/libcdio-paranoia-%_version.tar.gz

BuildRequires: libcdio-devel >= 0.93 help2man

%description
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from the
CDROM directly as data, with no analog step between, and writes the
data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files and libraries for %name.

%prep
%setup -n %name-%_version

# fix *.pc files
subst 's|-I${includedir}|-I${includedir}/cdio/paranoia|g' *.pc.in

%build
%autoreconf
%configure -disable-static
%make_build

%install
%makeinstall_std
# temporarily link headers for backward compatibility
for f in  %buildroot%_includedir/cdio/paranoia/*.h; do
ln -s paranoia/`basename $f` %buildroot%_includedir/cdio/`basename $f`
done

rm -rf %buildroot%_mandir/jp

%files
%_bindir/*
%_libdir/*.so.*
%_man1dir/*
%doc AUTHORS NEWS README* THANKS

%files devel
%_includedir/cdio/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sat Jan 13 2018 Yuri N. Sedunov <aris@altlinux.org> 10.2.0.94.2-alt1
- 10.2.0.94.2

* Wed Nov 16 2016 Yuri N. Sedunov <aris@altlinux.org> 10.2.0.93.1-alt2
- rebuild with libcdio-0.94

* Mon Jul 20 2015 Yuri N. Sedunov <aris@altlinux.org> 10.2.0.93.1-alt1
- first build for Sisyphus

