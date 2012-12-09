Name: gnustep-dirs
Version: 1.0
Release: alt2

Summary: Common dirs for GNUstep enviroment

License: free
Group: System/Base

%description
Common dirs for GNUstep enviroment.

%prep
%install
install -d %buildroot%_libdir/GNUstep
install -d %buildroot%_datadir/GNUstep
install -d %buildroot%_sysconfdir/GNUstep

%files
%defattr(644,root,root,755)
%_libdir/GNUstep*
%_datadir/GNUstep
%_sysconfdir/GNUstep

%changelog
* Sun Dec 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added some directories

* Tue Jun 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.0
- Set as arch-dep package

* Sat Nov 05 2005 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux Sisyphus
- spec from PLD Team <feedback@pld-linux.org>
