# http://bugzilla.gnome.org/show_bug.cgi?id=347922
# guile -c "(use-modules (ice-9 slib)) (require 'printf)"
Name: slib
Version: 3a4
Release: alt2

Summary: platform independent library for scheme
License: distributable, see individual files for copyright
Group: Development/Scheme

BuildArch: noarch
# Do not install umb-scheme now
#Obsoletes: umb-scheme
# Do not use any guile during packaging
#BuildPreReq: guile16-devel plt2

Url: http://www-swiss.ai.mit.edu/~jaffer/SLIB.html
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://swiss.csail.mit.edu/ftpdir/scm/%name%version.tar.bz2

# for 3a4, update with new version (made manually due automatic build overhead)
Source1: slibcat
Patch: slib-3a4-guile.patch

%description
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accomodate packages specific to a site,
implementation, user, or directory.

%package guile
Summary: guile support for slib
Group: Development/Scheme
Requires: %name = %version-%release
Requires(post): %name = %version-%release
Requires(preun): %name = %version-%release

%description guile
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accomodate packages specific to a site,
implementation, user, or directory.

This package provides files necessary to use slib with guile

%package plt2
Summary: mzscheme support for slib
Group: Development/Scheme
Requires: plt2
Requires: %name = %version-%release

%description plt2
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accomodate packages specific to a site,
implementation, user, or directory.

This package provides files necessary to use slib with mzscheme

%package plt1
Summary: mzscheme support for slib
Group: Development/Scheme
Requires: plt1
Requires: %name = %version-%release

%description plt1
"SLIB" is a portable library for the programming language Scheme.
It provides a platform independent framework for using "packages" of
Scheme procedures and syntax.  As distributed, SLIB contains useful
packages for all Scheme implementations.  Its catalog can be
transparently extended to accomodate packages specific to a site,
implementation, user, or directory.

This package provides files necessary to use slib with mzscheme

%prep
%setup -q -n slib
%patch -p1 -b .guile
%__subst "s|/usr/lib/slib|%_datadir/%name|g" guile.init

%install
mkdir -p %buildroot%_datadir/slib/
cp *.scm guile.init *.xyz *.txt *.dat *.ps %buildroot%_datadir/slib/

mkdir -p %buildroot%_infodir
install -m644 slib.info %buildroot%_infodir

mkdir -p %buildroot%_datadir/guile/site/
ln -sf ../../slib %buildroot%_datadir/guile/site/%name

install -m644 %SOURCE1 %buildroot%_datadir/guile/site/slibcat

%files
%doc ANNOUNCE README COPYING FAQ ChangeLog slib.texi
%dir %_datadir/%name
%_datadir/%name/*.scm
%_datadir/%name/cie*
%_datadir/%name/saturate.txt
%_datadir/%name/nbs-iscc.txt
%_datadir/%name/grapheps.ps
%_datadir/%name/resenecolours.txt
%_infodir/*.info*

%files guile
%_datadir/%name/guile.init
%dir %_datadir/guile/site/
%_datadir/guile/site/%name/
%_datadir/guile/site/slibcat

# is not used anywhere
#%files plt2
#%_libdir/plt2/collects/%name/
#%ghost %_libdir/plt2/slibcat

%changelog
* Sat Jun 13 2009 Vitaly Lipatov <lav@altlinux.ru> 3a4-alt2
- remove post/postun sections (ALT#20365)

* Tue May 01 2007 Vitaly Lipatov <lav@altlinux.ru> 3a4-alt1
- fix guile part placement, checked with gnucash

* Sat Dec 23 2006 Vitaly Lipatov <lav@altlinux.ru> 3a4-alt0.4
- revert slib link, fix slibcat placement

* Wed Dec 13 2006 Vitaly Lipatov <lav@altlinux.ru> 3a4-alt0.3
- move slib link to guile/1.6
- fix guile dir for slibcat

* Sat Dec 09 2006 Vitaly Lipatov <lav@altlinux.ru> 3a4-alt0.2
- revert from orphaned, new version (3a4)
- disable plt2 package
- fix Url, fix Source Url
- move slibcat build to post scripts :(
- add some bugs to the package

* Thu Apr 22 2004 Alexey Voinov <voins@altlinux.ru> 3a1-alt1
- new version (3a1)

* Sun Sep 28 2003 Alexey Voinov <voins@voins.program.ru> 2d6-alt1
- ported to ALT Linux

* Wed Mar 14 2001 Radey Shouman <shouman@ne.mediaone.net>
- Adapted from the spec file of R. J. Meier.

* Mon Jul 12 2000 Dr. Robert J. Meier <robert.meier@computer.org> 0.9.4-1suse
- Packaged for SuSE 6.3

* Sun May 30 2000 Aubrey Jaffer <agj@Alum.mit.edu>
- Updated content
