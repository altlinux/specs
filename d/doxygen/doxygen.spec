Name: doxygen
Version: 1.7.6.1
Release: alt1
Epoch: 1

Summary: Doxygen is a documentation system for C, C++ and IDL
License: GPLv2+
Group: Development/Other
Url: http://www.doxygen.org/

# ftp://ftp.stack.nl/pub/users/dimitri/doxygen-%version.src.tar.gz
Source: doxygen-%version.src.tar
Patch: doxygen-1.7.5-rh-timestamp.patch

# Automatically added by buildreq on Sun Aug 02 2009
BuildRequires: flex gcc-c++ graphviz libqt4-devel python-modules-xml texlive-extra-utils texlive-generic-recommended texlive-publishers

%description
Doxygen is a documentation system for C, C++ and IDL.  It can generate
an on-line class browser (in HTML) and/or an off-line reference manual
(in LaTeX) from a set of documented source files.  There is also support
for generating man pages and for converting the generated output into
Postscript, hyperlinked PDF or compressed HTML.  The documentation is
extracted directly from the sources.

Doxygen can also be configured to extract the code-structure from
undocumented source files.  This can be very useful to quickly find
your way in large source distributions.

%package wizard
Summary: GUI frontend for doxygen
Group: Development/Other
Requires: %name = %epoch:%version-%release

%description wizard
Doxywizard is a GUI front-end for creating and editing
configuration files that are used by doxygen.

%package doc
Summary: Documentation and examples for doxygen
Group: Development/Other
BuildArch: noarch
Requires: %name = %epoch:%version-%release

%description doc
This package contains doxygen examples and documentation in html and
pdf formats.

%prep
%setup
%patch -p1

find -name unistd.h -delete -print
perl -pi -e '
	s|^(TMAKE_CFLAGS\s*=\s*).*|$1\$(RPM_OPT_FLAGS)|;
	s|^(TMAKE_CFLAGS_WARN_ON\s*=).*|$1|;
	s|^(TMAKE_CFLAGS_WARN_OFF\s*=).*|$1|;
	s|^(TMAKE_CFLAGS_RELEASE\s*=).*|$1|;
	s|^(TMAKE_CFLAGS_DEBUG\s*=).*|$1|;
	s|^(TMAKE_CFLAGS_SHLIB\s*=\s*).*|$1%optflags_shared|;
	s|/usr/X11R6/lib|/usr/X11R6/%_lib|;
	' tmake/lib/linux-g++/tmake.conf

%build
# Exceptions and RTTI are used only in addon/xmlread, which is not built.
%add_optflags %optflags_nocpp

export QTDIR=%_libdir/qt4
export PATH="$QTDIR/bin:$PATH"
./configure --prefix %prefix --release --with-doxywizard
make
make pdf

%install
mkdir -p %buildroot{%_bindir,%_man1dir}
install -pm755 bin/* %buildroot%_bindir/
install -pm644 doc/*.1 %buildroot%_man1dir/

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir/pdf
install -pm644 latex/*.pdf %buildroot%docdir/pdf/
cp -a html examples %buildroot%docdir/
find %buildroot%docdir/ -type f -name Makefile.\* -delete
find %buildroot%docdir/ -type f -name Makefile -print0 |
	xargs -r0 perl -pi -e '
	s|/bin/doxygen||g;
	s|^(DOXYGEN\s*=\s*).*|$1%_bindir/doxygen|;
	s|^(TMAKE\s*=\s*).*|$1%_bindir/tmake|;
	s/^(TMAKEPATH|INST|DOXYDOCS).*//g;
	' --

%files
%_bindir/doxygen
%_bindir/doxytag
%_man1dir/doxygen.*
%_man1dir/doxytag.*

%files wizard
%_bindir/doxywizard
%_man1dir/doxywizard.*

%files doc
%docdir

%changelog
* Fri Jan 13 2012 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.6.1-alt1
- Updated to 1.7.6.1.

* Thu Sep 29 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.5.1-alt1
- Updated to 1.7.5.1.

* Sun Apr 10 2011 Dmitry V. Levin <ldv@altlinux.org> 1:1.7.4-alt1
- Updated to 1.7.4 (closes: #25270).

* Sun Aug 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.9-alt2
- Updated build dependencies.

* Thu Jun 25 2009 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.9-alt1
- Updated to 1.5.9.
- Built wizard with qt4.
- Packaged -doc subpackage as noarch.

* Thu Apr 24 2008 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.5-alt1
- Updated to 1.5.5.
- Updated build dependencies.
- Packaged manpages.
- Moved documentation and examples to -doc subpackage (#9742).

* Sun Nov 26 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.5.1-alt1
- Updated to 1.5.1.

* Tue Jun 13 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.7-alt1
- Updated to 1.4.7.

* Fri Feb 10 2006 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.6-alt1
- Updated to 1.4.6.

* Mon Oct 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.5-alt1
- Updated to 1.4.5.
- Fixed build with new flex.

* Thu May 26 2005 Dmitry V. Levin <ldv@altlinux.org> 1:1.4.3-alt1
- Updated to 1.4.3.
- Added multilib support (mouse, closes #6732).

* Mon Jan 24 2005 Stanislav Ievlev <inger@altlinux.org> 1:1.4.1-alt1.1
- 1.4.1

* Wed Jan 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.3.9.1-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Oct 19 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.3.9.1-alt1
- 1.3.9.1

* Mon Apr 05 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.3.6-alt1
- 1.3.6

* Tue Jan 27 2004 Stanislav Ievlev <inger@altlinux.org> 1:1.3.5-alt1
- 1.3.5

* Thu Sep 11 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.3.3-alt1
- 1.3.3

* Thu Sep 19 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.18-alt1
- 1.2.18
- The image map generation patch merged upstream.
- Added changelog.html to docs.

* Fri Aug 09 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.17-alt2
- Fixed image map generation (#0001188).

* Wed Jul 17 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.17-alt1
- 1.2.17

* Thu May 23 2002 Dmitry V. Levin <ldv@altlinux.org> 1:1.2.16-alt1
- 1.2.16

* Fri Apr 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.15-alt1
- 1.2.15.

* Thu Mar 14 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.14-alt2
- Fixed %%clean.

* Tue Feb 19 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.14-alt1
- 1.2.14.

* Thu Jan 24 2002 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.13.1-alt1
- 1.2.13.1

* Mon Nov 19 2001 Dmitry V. Levin <ldv@alt-linux.org> 1:1.2.12-alt1
- 1.2.12

* Wed Oct 10 2001 Rider <rider@altlinux.ru> 1.2.11.1-alt1
- 1.2.11.1

* Mon Jun 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.8.1-alt1
- 1.2.8.1

* Thu Jun  7 2001 Sergey Vlasov <vsu@altlinux.ru> 1.2.8-alt2
- Fixed compilation options in qtools
- Compile with --no-exceptions --no-rtti
- Fixed QTDIR setting; removed broken conf patch from Mandrake
- Build doxywizard (separate package doxygen-wizard)

* Tue Jun 05 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Wed Jan 03 2001 Dmitry V. Levin <ldv@fandra.org> 1.2.4-ipl1mdk
- 1.2.4

* Sat Nov 11 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.3-ipl1mdk
- 1.2.3

* Sun Oct 01 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.2-ipl1mdk
- 1.2.2
- Automatically added BuildRequires.

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 1.2.1-ipl1mdk
- RE adaptions.

* Sun Aug 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.1-1mdk
- 1.2.1

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2.0-2mdk
- automatically added BuildRequires

* Mon Jul 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.0-1mdk
- 1.2.0

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-4mdk
- BM
- macros

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.0-3mdk
- ExcludeArch: alpha (yep lazzyness).

* Sat Apr  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.0-1mdk
- first Mandrake release
- patch to fix wrong lookup of Qt include/lib
