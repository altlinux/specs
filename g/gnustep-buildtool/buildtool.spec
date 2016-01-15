Name: gnustep-buildtool
Version: r36614
Release: alt3.svn20130513.1
Summary: The GNUstep buildtool
License: GPLv2+
Group: Development/Tools
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/tools/buildtool/trunk/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel gnustep-base-devel
BuildPreReq: libgnustep-xcode-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-xcode-devel

%description
GNUstep buildtool.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ChangeLog
%_bindir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> r36614-alt3.svn20130513.1
- NMU: Rebuild with libgnutls30.

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r36614-alt3.svn20130513
- Built with clang

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r36614-alt2.svn20130513
- Added Requires: gnustep-xcode-devel

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r36614-alt1.svn20130513
- New snapshot

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r35695-alt1.svn20121015
- Initial build for Sisyphus

