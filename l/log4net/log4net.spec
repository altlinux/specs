Name: log4net
Version: 1.2.11
Release: alt1

Summary: A .NET framework for logging

License: ASL 2.0
Group: System/Libraries
Url: http://logging.apache.org/log4net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.apache.org/dist/logging/log4net/source/%name-%version-src.zip
Source2: %name.pc
Patch1: log4net-1.2.11-mono-2.0.patch

BuildRequires: mono-mcs mono-web nant mono-data-sqlite mono-devel unzip
BuildRequires: /proc

%description
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime.

%prep
%setup -q
%patch1 -p1

%build
export LC_CTYPE=en_US.UTF-8
nant -buildfile:log4net.build compile-all

%install
install -d %buildroot%_pkgconfigdir/
cp %SOURCE2 %buildroot%_pkgconfigdir/
gacutil -f -package log4net -root %buildroot%_monodir/.. -i bin/mono/2.0/release/log4net.dll

%files
%_monogacdir/log4net
%_monodir/log4net
%_pkgconfigdir/log4net.pc

%changelog
* Wed Feb 15 2012 Alexey Shabalin <shaba@altlinux.ru> 1.2.11-alt1
- 1.2.11
- build over nant

* Fri Nov 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.10-alt2
- cleanup spec
- fix install dir (bug #17809)

* Fri May 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.10-alt1
- new version 1.2.10 (with rpmrb script)

* Fri May 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2.9-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)

