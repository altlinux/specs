Name: flac123
Version: 2.1.1
Release: alt1
Summary: flac123 is a command-line program for playing flac-encoded files
License: GPL-2.0-only
Group: Sound
URL: https://github.com/flac123/flac123
Source0: %name-%version.tar
BuildRequires: libao-devel libflac-devel libpopt-devel
BuildRequires: libogg-devel

%description
flac123 is a command-line program for playing flac-encoded files.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS BUGS ChangeLog INSTALL NEWS README.md README.remote
%_bindir/flac123
%_man1dir/*.1.*

%changelog
* Wed Jul 10 2024 Anton Farygin <rider@altlinux.ru> 2.1.1-alt1
- 0.0.12 -> 2.1.1

* Sun Sep 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.12-alt1
- Version 0.0.12

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
