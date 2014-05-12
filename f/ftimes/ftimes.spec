Name: ftimes
Version: 3.10.0
Release: alt1

Summary: a system baselining and evidence collection tool
License: BSD (3-clause), Apache, MIT
Group: File tools

Url: http://ftimes.sourceforge.net/FTimes/
Source: %name-%version.tgz
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Mon May 12 2014
# optimized out: gnu-config libcloog-isl4 libcom_err-devel libkrb5-devel perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage
BuildRequires: libpcre-devel libssl-devel perl-podlators

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
%configure
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
%doc README*
#doc etc/*.cfg/*.cfg.*
#doc doc/*/

# TODO:
# - server-side?

%changelog
* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 3.10.0-alt1
- built for ALT Linux (proposed by Maxim Suhanov)

