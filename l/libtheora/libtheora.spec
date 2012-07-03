Name: libtheora
Version: 1.1.1
Release: alt4
Epoch: 2

Summary: Theora Video Compression Codec
License: BSD-style
Group: System/Libraries
Url: http://www.theora.org/
# http://downloads.xiph.org/releases/theora/%name-%version.tar.bz2
Source: %name-%version.tar
Patch: libtheora-1.1.1-alt-link.patch

# Automatically added by buildreq on Tue Nov 23 2010
BuildRequires: doxygen libSDL-devel libpng-devel libvorbis-devel

%description
Theora is Xiph.Org's first publicly released video codec, intended
for use within the Ogg's project's Ogg multimedia streaming system.
Theora is derived directly from On2's VP3 codec.  Currently the two are
nearly identical, varying only in encapsulating decoder tables in the
bitstream headers, but Theora will make use of this extra freedom
in the future to improve over what is possible with VP3.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %epoch:%version-%release

%description devel
This package contains development files for the software development
using %name library.

%package devel-doc
Summary: Documentation for developing Theora applications
Group: Development/C
BuildArch: noarch
Requires: %name = %epoch:%version-%release

%description devel-doc
This package contains documentation for the software development
using %name library.

%package -n theora-tools
Summary: Command line tools for Theora videos
Group: Video
Requires: %name = %epoch:%version-%release

%description -n theora-tools
This package contains simple command line tools for use with
theora bitstreams.

%prep
%setup
%patch -p1
ln -s m4/as-ac-expand.m4 acinclude.m4

%build
%autoreconf
%configure \
    --disable-static
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_bindir
install -pm755 examples/.libs/dump_video \
	%buildroot%_bindir/theora_dump_video
install -pm755 examples/.libs/encoder_example \
	%buildroot%_bindir/theora_encode
install -pm755 examples/.libs/player_example \
	%buildroot%_bindir/theora_player
install -pm755 examples/.libs/png2theora \
	%buildroot%_bindir/png2theora
%define docdir %_docdir/%name-%version
install -pm644 AUTHORS CHANGES COPYING LICENSE README %buildroot%docdir/

%check
%make_build -k check

%files
%dir %docdir
%docdir/[ACLR]*
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*.pc

%files devel-doc
%docdir
%exclude %docdir/[ACLR]*
%exclude %docdir/latex
%exclude %docdir/*.stamp
%exclude %docdir/*.xml

%files -n theora-tools
%_bindir/*

%changelog
* Thu Apr 21 2011 Dmitry V. Levin <ldv@altlinux.org> 2:1.1.1-alt4
- Rebuilt for debuginfo.

* Thu Dec 09 2010 Dmitry V. Levin <ldv@altlinux.org> 2:1.1.1-alt3
- Moved development documentation to separate subpackage.
- Packaged theora-tools (closes: #24443).

* Tue Nov 23 2010 Dmitry V. Levin <ldv@altlinux.org> 2:1.1.1-alt2
- Fixed documentation packaging.
- Cleaned up specfile.
- Updated build requirements.
- Enabled test suite.
- Rebuilt for soname set-versions.

* Wed Oct 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.1-alt1
- 1.1.1

* Fri Sep 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.1.0-alt1
- 1.1.0

* Thu Jun 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 2:1.0-alt5
- 1.0 release

* Fri Mar 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:1.1-alt0.alpha1
- 1.1alpha1

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt4
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Tue Nov 04 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt3
- final 1.0 release

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt2
- cleanup libtheora-1.0-alt-link.patch

* Mon Oct 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt1
- 1.0 release

* Thu Apr 17 2008 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt0.beta3
- 1.0beta3

* Sun Oct 14 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt0.beta2
- 1.0beta2
- disable static

* Sun Sep 23 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt0.beta1
- 1.0beta1

* Fri Sep 21 2007 Valery Inozemtsev <shrek@altlinux.ru> 1:1.0-alt0.alpha8
- 1.0alpha8

* Thu Jun 22 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0alpha7-alt1
- 1.0alpha7

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0alpha5-alt1.1
- Rebuilt for new pkg-config dependencies.

* Tue Aug 23 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0alpha5-alt1
- 1.0altha5

* Sat Jan 22 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0alpha4-alt1
- 1.0alpha4

* Sun Oct 24 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0alpha3-alt3
- added theora.pc patch

* Sun Jun 20 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0alpha3-alt2
- fixed URL

* Thu Jun 17 2004 Valery Inozemtsev <shrek@altlinux.ru> 1.0alpha3-alt1
- initial release

