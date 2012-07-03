%define rel %nil
Name: cspot
Version: 0.0.5
Release: alt1.1

Summary: Text based developer tool to search in source code 

License: GPL
Group: Text tools
Url: http://atrey.karlin.mff.cuni.cz/~susa/work/cspot/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://atrey.karlin.mff.cuni.cz/~susa/work/cspot/%name-%version.tar.bz2
Patch: %name-as-needed.patch
Patch1: %name-0.0.4-gcc43.patch
Patch2: %name-0.0.5-glibc.patch

%set_gcc_version 4.5
# Automatically added by buildreq on Sun May 28 2006
BuildRequires: libreadline-devel

%description
Text based developer tool to search in source code 
  - can run in interactive and non-interactive mode
  - has a simple plugin to emacs

%prep
%setup -q -n %name-%version%rel
%patch
%patch1
%patch2

%build
#make_build
# SMP incompatible
%__make

%install
#makeinstall

install -D -m755 cspot %buildroot%_bindir/cspot
install -D -m755 cspot_cc %buildroot%_bindir/cspot_cc

%files
%doc doc/
%_bindir/cspot
%_bindir/cspot_cc

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.1
- Fixed build

* Tue Jun 16 2009 Vitaly Lipatov <lav@altlinux.ru> 0.0.5-alt1
- update URL, fix build with new toolchain

* Tue Nov 04 2008 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt1
- rebuild

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.0.4-alt0.1
- new version 0.0.4 (with rpmrb script)

* Sun May 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.0.2-alt0.1
- initial build for ALT Linux Sisyphus

