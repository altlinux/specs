%define upname libdca
%define altver 0

Name: %upname%altver
Version: 0.0.5
Release: alt3
Summary: DTS Coherent Acoustics decoder
License: GPL

Packager: Pavlov Konstantin <thresh@altlinux.org>
Group: System/Libraries
URL: http://developers.videolan.org/libdca.html

Source0: %upname-%version.tar.gz

# Automatically added by buildreq on Tue Apr 11 2006
BuildRequires: gcc-c++

%description
Free decoder for the DTS Coherent Acoustics format. It consists of a
library and a command line decoder. DTS is a high quality
multi-channel (5.1) digital audio format used in DVDs and DTS audio
CDs.

%package -n dca-apps
Summary: apps from libdca library
Group: Sound
Requires: %name = %version-%release

Conflicts: libdca < 0.0.5

%description -n dca-apps
Apps from libdca package.

%package -n %upname-devel
Summary: Header files for libdca library
Group: Development/C++
Requires: %name = %version-%release

%description -n %upname-devel
Header files for libdca library.

%prep
%setup -q -n %upname-%version

%build
%__autoreconf
%configure \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_libdir/lib*.so.*

%files -n dca-apps
%_bindir/*
%_man1dir/*.1*

%files -n %upname-devel
%doc doc/libdca.txt
%_libdir/lib*.so
%_includedir/*.h
%_pkgconfigdir/*.pc

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt3
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.5-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libdca0
  * postun_ldconfig for libdca0
  * postclean-05-filetriggers for spec file

* Tue Aug 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.5-alt2
- Introduce dca-apps, libdca0 subpackages.

* Wed Jul 09 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.0.5-alt1
- 0.0.5 release.

* Thu May 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.0.2-alt3
- fixed crashes on some corrupted streams (closed #11733)

* Tue Apr 25 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.2-alt2
- rename to libdca
- update URL

* Tue Apr 11 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.0.2-alt1
- initial release

