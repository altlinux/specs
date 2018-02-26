Name: xmms-in-speex
Version: 0.9.2b
Release: alt1

Summary: Speex input plugin for XMMS
License: GPL
Group: Sound
#Url: http://jzb.rapanden.dk/projects/speex-xmms/
#The original URL is dead. But the sources are still downloadable.
Url: http://www.sisyphus.ru/srpms/%name

Source: http://jzb.rapanden.dk/pub/speex-xmms-%version.tar.gz
Patch1: xmms-in-speex-0.9.2b-build-deb.patch.bz2
Patch2: xmms-in-speex-0.9.2b-gcc41-deb-alt.patch.bz2
Patch3: xmms-in-speex-0.9.2b-as-needed-alt.patch

# Automatically added by buildreq on Sat Dec 27 2003
BuildRequires: glib-devel gtk+-devel libogg-devel libspeex-devel libxmms-devel

%description
This is an input plugin for XMMS which can play Speex (.spx) files.

%prep
%setup -q -n speex-xmms
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export CFLAGS="%optflags %optflags_shared -I%_includedir/speex"
%make_build

%install
%__install -pD -m644 libspeex.so %buildroot`xmms-config --input-plugin-dir`/libspeex.so

%files
%_libdir/xmms/Input/*

%changelog
* Mon Dec 18 2006 Yury Aliaev <mutabor@altlinux.org> 0.9.2b-alt1
- Version 0.9.2b
- Fixed build with modern gcc and ld

* Sun Jun 19 2005 Andrey Astafiev <andrei@altlinux.ru> 0.9.1-alt2
- Fixed build with current speex. 

* Sat Dec 27 2003 Andrey Astafiev <andrei@altlinux.ru> 0.9.1-alt1
- First build for Sisyphus.
