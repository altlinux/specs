%set_verify_elf_method unresolved=strict

Name: gnustep-Zillion
Version: 0.1
Release: alt5.1
Summary: Zillion distributed computing Project
License: BSD
Group: Graphical desktop/GNUstep
Url: http://zillion.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
#Source1: %name.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
The Zillion Project is a distributed computing project reminiscent of
the good old Zilla.app of NeXTstep days. It is based on GNUstep, the
most promising OPENSTEP replacement as of today.  Jobs can be created
from simple template projects and can be submitted with a single command
to the Zillion Server which in turn will distribute the job amongst the
registered clients. No other network resources than the distributed
objects (DO) port of the server machine has to be available. The key
features are as follows:

* Rapid turn around cycles for job submission
* Dynamic addition/removal of client nodes
* Full OO-design
* No need for shared network resources
* Real-time capabilities
* Lean and clean
* Open and free

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

#install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%_bindir/*
%_libdir/GNUstep
#_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt5.1
- NMU: Rebuild with libgnutls30.

* Fri Mar 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt5
- Removed menu file

* Mon Feb 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Added menu file (thnx kostyalamer@)

* Sat Feb 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Built with clang

* Thu Jan 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

