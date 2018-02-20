%def_enable static
%def_enable shared
%def_with pic

Name: nas
%define dname %{name}d
Version: 1.9.4
Release: alt2.git20131009
Summary: Network Audio System - a portable, network-transparent audio system
Group: Sound
License: distributable
URL: http://radscan.com/%name.html
# git://git.code.sf.net/p/nas/nas.git
Source0: %name-%version.src.tar
Source1: %dname.init

BuildRequires: flex gccmakedep imake libXaw-devel libXp-devel xorg-sdk
BuildRequires: libXau-devel libXpm-devel libXext-devel zlib-devel
BuildPreReq: libICE-devel libSM-devel libXmu-devel gcc-c++ gcc-fortran
BuildRequires: xorg-cf-files >= 1.0.1-alt5

%description
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.


%package -n %dname
Summary: Network Audio System Daemon
Group: Sound

%description -n %dname
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.


%if_enabled shared
%package -n libaudio
Summary: Network Audio System client library
Group: Sound

%description -n libaudio
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.

This package contains NAS client library.
%endif


%package -n libaudio-devel
Summary: NAS client library - development headers
Group: Development/C
Requires: libaudio%{?_disable_shared:-devel-static} = %version-%release

%description -n libaudio-devel
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.

This package contains development headers for NAS client library.


%if_enabled static
%package -n libaudio-devel-static
Summary: NAS client library - static library
Group: Development/C
Requires: libaudio-devel = %version-%release

%description -n libaudio-devel-static
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.

This package contains static version of NAS client library.
%endif


%package utils
Summary: Network Audio System utilites
Group: Sound
Requires: libaudio = %version-%release

%description utils
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.

This package contains miscellaneous NAS client utilites.


%package examples
Summary: Network Audio System examples
Group: Sound
Requires: libaudio = %version-%release

%description examples
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.


%package doc
Summary: Network Audio System documentation
Group: Books/Computer books
BuildArch: noarch
# Hack to have same versions of all packages
Conflicts: %dname < %version-%release
Conflicts: %dname > %version-%release
Conflicts: libaudio < %version-%release
Conflicts: libaudio > %version-%release
Conflicts: libaudio-devel < 1.9.1-alt1

%description doc
The Network Audio System service is a network-transparent system
developed at Network Computing Devices for playing, recording, and
manipulating audio data over a network. It uses the client/server
model to separate application code from the software drivers
needed to control specific audio input and output devices.


%prep
%setup
subst 's|/%_sysconfdir/%name\(/%dname\.conf\.eg\)|%_docdir/%dname-%version\1|g' \
    doc/html/%dname.conf.5.html server/%dname.conf.man


%build
echo "#define NasConfigSearchPath /etc/" >> config/NetAudio.def
echo "#define SharedLibX YES" >> config/NetAudio.def
echo "#define NormalLibX YES" >> config/NetAudio.def
xmkmf
pushd config
%configure --with-gnu-ld %{subst_with pic}
popd
%make_build BOOTSTRAPCFLAGS="%optflags" CDEBUGFLAGS="%optflags" CXXDEBUGFLAGS="%optflags" World
bzip2 --keep --force --best HISTORY


%install
%make_install DESTDIR=%buildroot ETCDIR=%_docdir/%dname-%version install install.man
install -D -m 0755 %SOURCE1 %buildroot%_initdir/%dname
echo "# See %dname.conf(5) and sample at %_docdir/%dname-*/" > %buildroot%_sysconfdir/%dname.conf


%post -n %dname
%post_service %dname ||:


%preun -n %dname
%preun_service %dname ||:


%files -n %dname
%_docdir/%dname-%version
%config(noreplace) %_sysconfdir/%dname.conf
%_initdir/*
%_bindir/%dname
%_man1dir/%dname.1*
%_man5dir/*


%if_enabled shared
%files -n libaudio
%_libdir/libaudio.so.*
%_datadir/X11/AuErrorDB
%endif


%files -n libaudio-devel
%_libdir/libaudio.so
%_includedir/audio


%if_enabled static
%files -n libaudio-devel-static
%_libdir/libaudio.a
%endif


%files utils
%_bindir/au*
%_man1dir/au*
%_man1dir/%name.1*


%files examples
%_bindir/checkmail
%_bindir/issndfile
%_bindir/playbucket
%_bindir/soundtoh
%_man1dir/checkmail.1*
%_man1dir/issndfile.1*
%_man1dir/playbucket.1*
%_man1dir/soundtoh.1*


%files doc
%doc FAQ HISTORY.* README TODO
%doc doc/actions doc/*.txt doc/*.ps doc/pdf
%_man3dir/*


%changelog
* Tue Feb 20 2018 Andrew Savchenko <bircoph@altlinux.org> 1.9.4-alt2.git20131009
- E2K: Fix preprocessing with lcc.

* Tue Sep 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt1.git20131009
- Version 1.9.4

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.9.2-alt4.1.qa1
- NMU: rebuilt for debuginfo.

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.9.2-alt4.1
- rebuilt with perl 5.12

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.2-alt4
- Rebuilt for soname set-versions

* Sun Mar 15 2009 Led <led@altlinux.ru> 1.9.2-alt3
- 1.9.2

* Tue Dec 02 2008 Led <led@altlinux.ru> 1.9.1-alt3
- updated BuildRequires
- cleaned up spec

* Mon Nov 10 2008 Led <led@altlinux.ru> 1.9.1-alt2
- rebuilt with libXaw.so.7
- updated BuildRequires

* Mon Nov 12 2007 Led <led@altlinux.ru> 1.9.1-alt1
- 1.9.1
- added:
  + %name-1.9.1-config.patch
  + %name-1.9.1-pidfile.patch
  + %_initdir/%dname
- removed:
  + %dname.xinit
  + %name-1.6-alt-shared-libs.patch

* Wed May 23 2007 Led <led@altlinux.ru> 1.9-alt1
- rebuild for Sisyphus

* Wed May 09 2007 Led <led@altlinux.ru> 1.9-alt0.1
- 1.9
- updated BuildRequires
- cleaned up spec

* Thu Feb 09 2006 Anton Farygin <rider@altlinux.ru> 1.7b-alt1.1
- NMU: fixed build for x86_64

* Sat Jan 28 2006 Sir Raorn <raorn@altlinux.ru> 1.7b-alt1
- [1.7b]
- Rebuilt with new Xorg, buildreqs updated

* Thu Sep 16 2004 Sir Raorn <raorn@altlinux.ru> 1.6e-alt1
- [1.6e]

* Fri Mar 26 2004 Sir Raorn <raorn@altlinux.ru> 1.6c-alt1.1
- --with/--without static

* Thu Mar 25 2004 Sir Raorn <raorn@altlinux.ru> 1.6c-alt1
- [1.6c]

* Fri Jun 13 2003 Sir Raorn <raorn@altlinux.ru> 1.6-alt2
- Oops! Forgot to add nasd.xinit to filelist...

* Thu Jun 12 2003 Sir Raorn <raorn@altlinux.ru> 1.6-alt1
- Built for Sisyphus
- Patches from Debian package by Steve McIntyre <93sam AT debian DOT org>:
  * Fixed typo in Xtutil.h. Thanks to Stephen J. Turnbull. Sent upstream too.
  * Backed out the previous change - it didn't help. The real problem was
    lonking libaudio with libXau, which isn't necessary or possible on Debian.
    Removed the -lXau for the libaudio build, and all seems to work now.
  * Fix so nas build with latest version of bison.
