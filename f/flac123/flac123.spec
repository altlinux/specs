Name: flac123
Version: 0.0.11
Release: alt2

Summary: flac123 is a command-line program for playing flac-encoded files
License: GPL
Group: Sound
URL: http://flac-tools.sourceforge.net/

Packager: Alexey Morsov <swi@altlinux.ru>

Source0: %name-%version.tar.bz2

Patch0: flac123-0.0.9-alt-fix-warning.patch

# Automatically added by buildreq on Tue Mar 21 2006
BuildRequires: libao-devel libflac-devel libpopt-devel
BuildRequires: libogg-devel

%description
flac123 is a command-line program for playing flac-encoded files.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS BUGS ChangeLog INSTALL README README.remote
%_bindir/flac123

%changelog
* Sat Apr 16 2011 Alexey Morsov <swi@altlinux.ru> 0.0.11-alt2
- fix build

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 0.0.11-alt1
- FLAC 1.1.4 support
- obey ~/.libao default_driver="" setting
- fixed buffer overflow in vorbis comment parsing


* Sat Jun 30 2007 Alexey Morsov <swi@altlinux.ru> 0.0.10-alt2
- version 0.0.10
- fixed buffer overflow in vorbis comment parsing

* Mon Mar 05 2007 Alexey Morsov <swi@altlinux.ru> 0.0.9-alt4
- add patch for flac >= 1.1.3 (by led)

* Thu Jan 11 2007 Alexey Morsov <swi@altlinux.ru> 0.0.9-alt3
- change maintainer

* Mon Mar 20 2006 Igor Zubkov <icesik@altlinux.ru> 0.0.9-alt2
- fix build with new ld / --as-needed

* Sat Jun 25 2005 Igor Zubkov <icesik@altlinux.ru> 0.0.9-alt1
- Initial build for Sisyphus.
