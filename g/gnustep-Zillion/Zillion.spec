%set_verify_elf_method unresolved=strict

Name: gnustep-Zillion
Version: 0.1
Release: alt1
Summary: Zillion distributed computing Project
License: BSD
Group: Graphical desktop/GNUstep
Url: http://zillion.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%_bindir/*
%_libdir/GNUstep

%changelog
* Sat Jan 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

