Name: asco
Version: 0.4.11
Release: alt1

Summary: A SPICE Circuit Optimizer

Packager: Vitaly Lipatov <lav@altlinux.ru>

Url: http://asco.sourceforge.net/
License: GPLv2
Group: Engineering

# Source-url: http://downloads.sourceforge.net/project/asco/asco/%version/ASCO-%version.tar.gz
Source: %name-%version.tar
Patch: %name-as-needed.patch

# Automatically added by buildreq on Sun Sep 03 2006
BuildRequires: linux-libc-headers

%description
ASCO project aims to bring circuit optimization capabilities to existing
SPICE simulators using a high-performance parallel differential evolution
(DE) optimization algorithm. Currently out-of-the-box support for Eldo
(TM), HSPICE (R), LTspice (TM), Spectre (R) and Qucs exist.

%prep
%setup
tar -zxf Autotools.tar.gz
# Remove useless C++ compiler check
sed -i '/AC_PROG_CXX/d' configure.ac
#%patch

%build
export CFLAGS="%optflags -fcommon"
%autoreconf
%configure
%make_build

%install
install -D -m755 %name %buildroot%_bindir/%name

%files
%doc AUTHORS README examples/ doc/ASCO.pdf
%_bindir/*

%changelog
* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 0.4.11-alt1
- new version 0.4.11 (with rpmrb script)

* Thu Mar 11 2021 Slava Aseev <ptrnine@altlinux.org> 0.4.10-alt3
- fixed build with gcc-10

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4.10-alt2
- change group to Engineering (ALT bug 16233)

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 0.4.10-alt1
- new version 0.4.10 (with rpmrb script)

* Tue Jul 26 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4.9-alt1
- new version (0.4.9) with rpmgs script

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.6-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.4.6-alt1
- new version 0.4.6 (with rpmrb script)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.5-alt0.1
- new version 0.4.5 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt1.1
- initial build for ALT Linux Sisyphus
