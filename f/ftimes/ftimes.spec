Name: ftimes
Version: 3.11.0
Release: alt2

Summary: a system baselining and evidence collection tool
License: BSD (3-clause), Apache, MIT
Group: File tools

Url: http://ftimes.sourceforge.net/FTimes/
Source: %name-%version.tgz
Packager: Michael Shigorin <mike@altlinux.org>

ExclusiveArch: x86_64 %ix86 %e2k

# Automatically added by buildreq on Mon May 12 2014
# optimized out: gnu-config libcloog-isl4 libcom_err-devel libkrb5-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage
BuildRequires: libpcre-devel libssl-devel perl-podlators perl-devel

%description
FTimes is a system baselining and evidence collection tool.
The primary purpose of FTimes is to gather and/or develop topographical
information and attributes about specified directories and files
in a manner conducive to intrusion and forensic analysis.

%prep
%setup
sed -i 's,pcre.h,pcre/pcre.h,' configure* src/app-includes.h
sed -i 's,XMAGIC_PREFIX"/etc/xmagic","/etc/xmagic",' src/xmagic.h

%build
%autoreconf
%configure --bindir=%_bindir --without-ssl
%make_build

%check
%make test

%install
%makeinstall_std
mkdir -p %buildroot{%_man1dir,%_sysconfdir}
mv %buildroot/usr/man/man1/* %buildroot%_man1dir/
mv %buildroot/usr/etc/xmagic %buildroot%_sysconfdir/

%files
%_bindir/*
%_man1dir/*
%_sysconfdir/*
%_prefix/etc/*
%doc README*
%doc etc/*.cfg/*.cfg.*
#doc doc/*/

# TODO:
# - server-side?

%changelog
* Wed Dec 08 2021 Michael Shigorin <mike@altlinux.org> 3.11.0-alt2
- added e2k support

* Tue Jan 29 2019 Leontiy Volodin <lvol@altlinux.org> 3.11.0-alt1
- 3.11.0
- disabled openssl support
- added ExclusiveArch (don't support aarch64)

* Tue May 13 2014 Michael Shigorin <mike@altlinux.org> 3.10.0-alt2
- added sample configuration files

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 3.10.0-alt1
- built for ALT Linux (proposed by Maxim Suhanov)

