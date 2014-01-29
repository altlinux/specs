%set_verify_elf_method unresolved=strict

Name: gnustep-Connect
Version: 0.1
Release: alt2
Summary: Connect is a GNUstep frontend to pppd
License: Free
Group: Graphical desktop/GNUstep
Url: http://stepmaker.sourceforge.net/connect.html
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: ppp
Requires: gnustep-back

%description
Connect is a GNUstep frontend to pppd.

Features:

- visual configuration of PPP sessions;
- displaying of connecting process;
- redialing on connection drop (planned);
- do not drop connection until "On connect" scripts finished or ask user
  (planned);
- load graph in application icon (planned);
- gathering statistics on connection time, speed (planed).

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
%doc TODO
%_bindir/*
%_libdir/GNUstep

%changelog
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Tue Jan 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

