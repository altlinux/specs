%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-ScriptServices
Version: r4296
Release: alt1.svn20090120
Summary: Gateway between GNUstep system services and Unix scripts
License: MIT
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Services/Private/ScriptServices/
Source: %name-%version.tar

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator
BuildPreReq: gnustep-Etoile-EtoileFoundation-devel
BuildPreReq: gnustep-Etoile-Languages-devel

Requires: gnustep-back gnustep-Etoile-EtoileFoundation
Requires: gnustep-Etoile-Languages

%description
ScriptServices is a gateway between GNUstep system services and Unix
scripts.  It turns Unix scripts into GNUstep system services.
Scripts should be put under
~/GNUstep/Library/ApplicaitonSupport/ScriptServices/
Whenever new scripts are installed, you need to update services by doing
`openapp ScriptServices --update`
A default script using `bc` comes with ScriptServices.
More scripts are in Examples directory.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=ScriptServices

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=ScriptServices

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

%files
%doc README Examples
%_bindir/*
%_libdir/GNUstep

%changelog
* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r4296-alt1.svn20090120
- Initial build for Sisyphus

