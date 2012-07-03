BuildArch: noarch
Packager: Denis Smirnov <mithraen@altlinux.ru>

Name: mithraen-utils
Version: 0.0.9
Release: alt1

Summary: Utilites for SVN
License: GPL
Group: System/Kernel and hardware

Obsoletes: seiros-utils <= 0.1-alt2
Conflicts: seiros-utils
Obsoletes: seiros-text-utils <= 0.1-alt2
Conflicts: seiros-text-utils

Source: %name.tar

# Automatically added by buildreq on Fri May 12 2006 (-bb)
BuildRequires: lame mencoder mkisofs

Requires: lynx

%description
%summary
%prep
%setup -q -c

%build
%install
mkdir -p %buildroot%_bindir
install -m 755 * %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Wed Jun 20 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.9-alt1
- add 'wallpaper' utility

* Tue Jun 19 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.8-alt1
- 0.0.8

* Sat Mar 10 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.7-alt1
- add notify-tts

* Sat Mar 03 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.6-alt1
- add tts script

* Sun Aug 29 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.5-alt1
- add log-if-die utility.
- remove utilites that must be simple aliases.

* Tue Sep 18 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.4-alt1
- small fixes and cleanups (thanks to php-coder@)

* Sun Sep 16 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.3-alt1
- fix typo in 'rpm.test' utility

* Sat Feb 17 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.2-alt1
- add dk/dw utilites (convert from HTML with windows or koi8-r codepage)

* Sat Feb 17 2007 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt1
- first build for Sisyphus
