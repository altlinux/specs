Summary: Library for connection to iTunes music shares
Name: libopendaap
Version: 0.4.0
Release: alt1.1
License: GPL
Group: Networking/Other
Url: http://crazney.net/programs/itunes/libopendaap.html

Packager: Repocop Q. A. Robot <repocop@altlinux.org>

Source: http://crazney.net/programs/itunes/files/libopendaap-%version.tar.bz2

BuildRequires: gcc-c++

%description
Libopendaap is a library written in C which enables applications to
discover, and connect to, iTunes music shares.

%package devel
Summary: Header files, libraries and development documentation for %name
Group: Networking/Other
Requires: %name = %version-%release

%description devel
This package contains the header files, static libraries and development
documentation for %name. If you like to develop programs using %name,
you will need to install %name-devel.

%prep
%setup

%build
%configure \
    --disable-static
%make_build

%install
%__rm -rf %buildroot
%makeinstall

%files
%_libdir/*.so.*

%files devel
%doc AUTHORS ChangeLog COPYING NEWS README
%_includedir/daap
%_libdir/*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%changelog
* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.0-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libopendaap
  * postun_ldconfig for libopendaap

* Wed Apr 12 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.4.0-alt1
- Initial build for Sisyphus, reworked specfile by Dries Verachtert.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.4.0-2 - 4204/thias
- Disable/remove static library, nothing seems to use it.

* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Thu Jan 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.0
- Initial package.
