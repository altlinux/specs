%define origname compFUSEd

Name: fuse-compFUSEd
Version: 200712321
Release: alt2
License: GPL2
Group: System/Kernel and hardware
Url: http://www.biggerbytes.be/documents-related-to-compfused
Summary: FUSE filesystem providing transparent R/W compression
Packager: Ildar Mulyukov <ildar@altlinux.ru>

#cf-GISMO-200712321.tgz from http://www.biggerbytes.be/remository?func=download&id=1&chk=8032120f87806de7b241f7674fd9d581&no_html=1
Source: cf-GISMO-200712321.tar
Patch: %name-alt-build.patch

# Automatically added by buildreq on Thu Oct 14 2010
BuildRequires: bzlib-devel libfuse-devel liblzo2-devel zlib-devel

%description
An overlay filesystem providing transparent compression with both read and
write support. This filesystem sits on top of an existing fs. Fully
configurable, different compression algorithms available (lzo, zlib, bzip2).
Use with CAUTION!

%prep
%setup -n CompFused/Gismo
%patch -p2

%build
make clean
make \
    CFLAGS="%optflags -fPIC -I .. `pkg-config --cflags fuse` -I/usr/include/lzo" LIBS0="-lpthread `pkg-config --libs fuse`" \
    USE_LZO=0\

%install
mkdir -p old
cp -a HOWTO.txt old/

mkdir -p %buildroot{%_bindir/,%_libdir/%origname/plugins/}
install \
	cf_main cf_fsinfo cf_inspect \
	%buildroot%_bindir
install plugins/*.so %buildroot%_libdir/%origname/plugins/
%__subst 's|/usr/local/lib/|%_libdir/%origname/plugins/|' compFUSEd.conf

%files
%doc FEEDBACK.txt README.gismo compFUSEd.conf old/
%_bindir/*
%_libdir/%origname/

%changelog
* Mon Dec 06 2010 Ildar Mulyukov <ildar@altlinux.ru> 200712321-alt2
- remove lzo plugin
- fix lzo2 plugin

* Wed Oct 13 2010 Ildar Mulyukov <ildar@altlinux.ru> 200712321-alt1
- 1st release to ALTLinux
