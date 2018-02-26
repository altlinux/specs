# $Id: sablotron.spec 4586 2006-07-26 21:05:33Z dries $
# Authority: dag
# Upstream: <sablist$gingerall,cz>

%define real_name Sablot

Summary: XSLT, XPath and DOM processor
Name: sablotron
Version: 1.0.3
Release: alt1.1
License: GPL
Group: System/Base
Url: http://www.gingerall.org/sablotron.html

Packager: Boris Savelev <boris@altlinux.org>

Source: http://download-1.gingerall.cz/download/sablot/Sablot-%version.tar.gz
Patch: lib%name-alt-link.patch

# Automatically added by buildreq on Wed May 13 2009
BuildRequires: gcc-c++ libexpat-devel libjs-devel libncurses-devel libreadline-devel perl-XML-Parser

%description
Sablotron is an XML (XSLT 1.0, XPath 1.0, DOM Level2) processor.
It is written in C++ by Ginger Alliance.

%package -n lib%name
Summary: Libraries for %name
Group: Development/C++

%description -n lib%name
This package contains the libraries for %name.

%package -n lib%name-devel
Summary: Header files, libraries and development documentation for %name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the header files, and development
documentation for %name.

%package -n lib%name-devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the static libraries for %name.

%prep
%setup -n %real_name-%version
%patch0 -p2

%build
export CPLUS_INCLUDE_PATH="%_includedir/js"
export SABLOT_GPL="1"
%configure \
	--enable-javascript \
	--with-readline \
	--enable-debugger
%make_build

%install
%makeinstall_std

%files
%doc README* RELEASE doc/misc/DEBUGGER doc/misc/NOTES src/TODO
%_man1dir/sabcmd.1*
%_bindir/sabcmd

%files -n lib%name
%_libdir/libsablot.so.*

%files -n lib%name-devel
%doc doc/apidoc/jsdom-ref doc/apidoc/sablot doc/apidoc/sxp
%_bindir/sablot-config
%_libdir/libsablot.so
%_includedir/*.h

%files -n lib%name-devel-static
%_libdir/libsablot.a

%changelog
* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.1
- Rebuilt for soname set-versions

* Wed May 13 2009 Boris Savelev <boris@altlinux.org> 1.0.3-alt1
- initial build for Sisyphus

* Wed Jul 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.3-1 - 4586/dries
- Updated to release 1.0.3.
- Fixed the urls.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.2-1.2
- Rebuild for Fedora Core 5.

* Sat Mar 26 2005 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Initial package. (using DAR)
