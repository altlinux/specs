Name: chntpw
Version: 110511
Release: alt1

Summary: Offline Windows NT password & registry editor
License: GPLv2+
Group: System/Configuration/Other

Url: http://pogostick.net/~pnh/ntpasswd/
Source: http://pogostick.net/~pnh/ntpasswd/chntpw-source-%version.zip

# Automatically added by buildreq on Sat Jun 11 2011
BuildRequires: libssl-devel unzip

%description
This little program will enable you to view some information and change user
passwords in a Windows NT SAM userdatabase file (NT/2k/XP/Vista etc system).

You do not need to know the old passwords. However, you need to get at the file
some way or another yourself. In addition it contains a simple registry editor
with full write support, and hex-editor which enables you to fiddle around with
bits&bytes in the file as you wish yourself.

%prep
%setup -n %name-%version

%build
subst 's/ -m32//' Makefile
%make_build chntpw cpnt reged CC="gcc %optflags" LIBS="-lcrypto"
subst 's/\r$//' WinReg.txt

%install
install -d %buildroot%_bindir
install -pm755 chntpw cpnt reged %buildroot%_bindir/

%files
%_bindir/*
%doc README.txt WinReg.txt regedit.txt syskey.txt

%changelog
* Sat Jun 11 2011 Victor Forsiuk <force@altlinux.org> 110511-alt1
- Release from 2011-05-11.

* Mon Feb 14 2011 Victor Forsiuk <force@altlinux.org> 100627-alt1
- Release from 2010-06-27.

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 070923-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 070923-alt2.1
- Automated rebuild due to libcrypto.so.6 -> libcrypto.so.7 soname change.

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 070923-alt2
- x86_64 build spec-fix

* Thu May 08 2008 Mikhail Pokidko <pma@altlinux.org> 070923-alt1
- Version up. thnx to mike@

* Sat Jan 13 2007 Mikhail Pokidko <pma@altlinux.org> 040818-alt1 
- Initial build
