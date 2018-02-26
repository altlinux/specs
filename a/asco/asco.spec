Name: asco
Version: 0.4.6
Release: alt1

Summary: A SPICE Circuit Optimizer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://asco.sourceforge.net/
License: GPL
Group: Video

Source: http://dl.sourceforge.net/%name/%name-%version.tar.bz2
Patch: %name-as-needed.patch

# Automatically added by buildreq on Sun Sep 03 2006
BuildRequires: linux-libc-headers

%description
ASCO project aims to bring circuit optimization capabilities to existing
SPICE simulators using a high-performance parallel differential evolution
(DE) optimization algorithm. Currently out-of-the-box support for Eldo
(TM), HSPICE (R), LTspice (TM), Spectre (R) and Qucs exist.

%prep
%setup -q
#%patch

%build
#configure
%make_build

%install
install -D -m755 %name %buildroot%_bindir/%name

%files
%doc AUTHORS README examples/ doc/asco.pdf
%_bindir/*

%changelog
* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- new version 0.4.6 (with rpmrb script)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt0.1
- new version 0.4.5 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt1.1
- initial build for ALT Linux Sisyphus
