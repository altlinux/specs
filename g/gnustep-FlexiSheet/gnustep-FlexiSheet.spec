%set_verify_elf_method unresolved=strict

Name: gnustep-FlexiSheet
Version: 0.1
Release: alt5.cvs20140127.1
Summary: A Quantrix-like spreadsheet
License: BSD
Group: Graphical desktop/GNUstep
Url: http://gap.nongnu.org/flexisheet/index.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# cvs -d:pserver:anonymous@cvs.sv.gnu.org:/sources/gap co gap/user-apps/FlexiSheet
Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-ObjcUnit-devel
BuildPreReq: gnustep-simplewebkit-devel

Requires: gnustep-ObjcUnit
Requires: gnustep-simplewebkit
Requires: gnustep-back

%description
A Quantrix-like spreadsheet.

%package docs
Summary: Documentation for FlexiSheet
Group: Documentation
BuildArch: noarch

%description docs
A Quantrix-like spreadsheet.

This package contains documentation for FlexiSheet.

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

# The package contains a CVS/.svn/.git/.hg/.bzr/_MTN directory of revision control system.
# It was most likely included by accident since CVS/.svn/.hg/... etc. directories 
# usually don't belong in releases. 
# When packaging a CVS/SVN snapshot, export from CVS/SVN rather than use a checkout.
find $RPM_BUILD_ROOT -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:
# the find below is useful in case those CVS/.svn/.git/.hg/.bzr/_MTN directory is added as %%doc
find . -type d \( -name 'CVS' -o -name '.svn' -o -name '.git' -o -name '.hg' -o -name '.bzr' -o -name '_MTN' \) -print -exec rm -rf {} \; ||:

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%files docs
%doc Application/FlexiSheet\ Help
%doc Documentation

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt5.cvs20140127.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt5.cvs20140127
- Built with clang

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4.cvs20140127
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3.cvs20140127
- Added Requires: gnustep-back

* Tue Jan 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.cvs20140127
- Applied repocop patch

* Mon Jan 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.cvs20140127
- Initial build for Sisyphus

