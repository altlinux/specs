%define bname mpfc
%define Name MPFC
Name: %bname-flac
Version: 0.2.1
Release: alt3
Summary: FLAC format playback plugin for %Name
License: %gpl2plus
Group: Sound
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-0.2.1-alt.patch

BuildRequires: libflac-devel libmpfc-devel
BuildRequires: rpm-build-licenses

%description
FLAC format playback plugin for %Name.


%prep
%setup
%patch -p1


%build
%autoreconf
%configure --enable-shared --disable-static --with-pic
%make_build LDFLAGS=-avoid-version


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS README
%_libdir/%bname/input/*.so


%changelog
* Wed Sep 24 2008 Led <led@altlinux.ru> 0.2.1-alt3
- rebuild with lib%bname.so.0

* Wed Aug 13 2008 Led <led@altlinux.ru> 0.2.1-alt2
- fixed spec
- added %name-0.2.1-alt.patch

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.2.1-alt1
- 0.2.1
- fixed License
- removed %name-0.1+flac-1.1.3.patch (fixed in upstream)

* Mon Feb 19 2007 Led <led@altlinux.ru> 0.1-alt2.1
- added %name-0.1+flac-1.1.3.patch
- rebuild with new libflac

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 0.1-alt2
- use LDFLAGS=-avoid-version

* Mon Jun 26 2006 Alexey Tourbin <at@altlinux.ru> 0.1-alt1
- initial revision
