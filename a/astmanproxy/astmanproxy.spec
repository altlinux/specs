%define svndate 20061015

Name: astmanproxy
Summary: Asterisk manager proxy
Version: 1.22
Release: alt5.pre.%svndate.1
License: GPL
Group: System/Servers
Epoch: %svndate

Url: http://www.popvox.com/astmanproxy/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name.tar

# Automatically added by buildreq on Wed May 10 2006
BuildRequires: libssl-devel openssl

Patch1: %name.config.patch
Patch2: %name.pidfile.patch
Patch3: %name.securityfix.patch
Patch4: %name.gmi.patch

Requires(pre): asterisk-base >= 0.6-alt1

%description
%summary

%prep
%setup -c
%patch1 -p0
%patch2 -p0
%patch3 -p1
%patch4 -p1
subst 's!/usr/lib!%_libdir!' Makefile src/dlfcn.c

%build
sed -i 's/^host =/;host =/' configs/astmanproxy.conf
sed -i 's/^\([^;]\)/;\1/' configs/astmanproxy.users 
CFLAGS="%optflags -fPIC -iquote src/include -I/usr/include/openssl -Wall -D_REENTRANT"
subst "s!^CFLAGS:=.*!CFLAGS:=$CFLAGS!" Makefile
%make_build
%install
%make_install install DESTDIR=%buildroot PREFIX=/usr
install -D -m 755 %name-init %buildroot%_initdir/%name
mkdir -p %buildroot/var/run/astmanproxy

%preun
%preun_service astmanproxy
%post
%post_service astmanproxy

%files
%_initdir/%name
%attr(0770,_asterisk,_asterisk) %dir /var/run/astmanproxy
%dir %_libdir/%name
%dir %_libdir/%name/modules
%attr(0660,_asterisk,pbxadmin) %config(noreplace) %_sysconfdir/asterisk/astmanproxy.conf
%attr(0660,_asterisk,pbxadmin) %config(noreplace) %_sysconfdir/asterisk/astmanproxy.users
%_libdir/%name/modules/csv.so
%_libdir/%name/modules/http.so
%_libdir/%name/modules/xml.so
%_libdir/%name/modules/standard.so
%_sbindir/%name
%doc README INSTALL TODO VERSIONS
%doc doc/README.*

%changelog
* Tue Dec 21 2010 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt5.pre.20061015.1
- remove password samples from config

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt4.pre.20061015.1
- rebuild with new openssl

* Mon Apr 20 2009 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt4.pre.20061015
- fix build (patch by Kirill A. Shutemov)

* Fri Jul 25 2008 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt3.pre.20061015
- move /etc/asterisk to asterisk-base

* Mon Nov 19 2007 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt2.pre.20061015
- Add patches that fix compatibility with some  AMI clients (Gaetan Minet)

* Fri Apr 13 2007 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt1.pre.20061015
- buffer overflow fixed

* Sun Oct 15 2006 Denis Smirnov <mithraen@altlinux.ru> 20061015:1.22-alt0.pre.20061015
- svn update
- import to git.altlinux.ru
- rediff pid-file creation patch

* Thu Sep 28 2006 Denis Smirnov <mithraen@altlinux.ru> 20060928:1.22-alt0.pre.20060928
- svn update

* Tue Sep 26 2006 Denis Smirnov <mithraen@altlinux.ru> 20060926:1.22-alt0.pre.20060926
- svn update

* Thu Sep 21 2006 Denis Smirnov <mithraen@altlinux.ru> 20060921:1.22-alt0.pre.20060921
- svn update

* Wed Sep 20 2006 Denis Smirnov <mithraen@altlinux.ru> 20060920:1.22-alt0.pre.20060920
- svn update

* Tue Sep 19 2006 Denis Smirnov <mithraen@altlinux.ru> 20060919:1.22-alt0.pre.20060919
- svn update

* Sun Sep 17 2006 Denis Smirnov <mithraen@altlinux.ru> 20060917:1.22-alt0.pre.20060917
- svn update

* Sat Sep 16 2006 Denis Smirnov <mithraen@altlinux.ru> 20060916:1.22-alt0.pre.20060916
- svn update

* Fri Sep 15 2006 Denis Smirnov <mithraen@altlinux.ru> 20060915:1.22-alt0.pre.20060915
- svn update

* Thu Sep 14 2006 Denis Smirnov <mithraen@altlinux.ru> 20060914:1.22-alt0.pre.20060914
- svn update

* Wed Sep 13 2006 Denis Smirnov <mithraen@altlinux.ru> 20060913:1.22-alt0.pre.20060913
- svn update

* Tue Sep 12 2006 Denis Smirnov <mithraen@altlinux.ru> 20060912:1.22-alt0.pre.20060912
- svn update

* Mon Sep 11 2006 Denis Smirnov <mithraen@altlinux.ru> 20060911:1.22-alt0.pre.20060911
- svn update

* Sun Sep 10 2006 Denis Smirnov <mithraen@altlinux.ru> 20060910:1.22-alt0.pre.20060910
- svn update

* Sat Sep 09 2006 Denis Smirnov <mithraen@altlinux.ru> 20060909:1.22-alt0.pre.20060909
- svn update

* Fri Sep 08 2006 Denis Smirnov <mithraen@altlinux.ru> 20060908:1.22-alt0.pre.20060908
- svn update

* Thu Sep 07 2006 Denis Smirnov <mithraen@altlinux.ru> 20060907:1.22-alt0.pre.20060907
- svn update

* Wed Sep 06 2006 Denis Smirnov <mithraen@altlinux.ru> 20060906:1.22-alt0.pre.20060906
- svn update

* Tue Sep 05 2006 Denis Smirnov <mithraen@altlinux.ru> 20060905:1.22-alt0.pre.20060905
- svn update

* Mon Sep 04 2006 Denis Smirnov <mithraen@altlinux.ru> 20060904:1.22-alt0.pre.20060904
- svn update

* Sun Sep 03 2006 Denis Smirnov <mithraen@altlinux.ru> 20060903:1.22-alt0.pre.20060903
- svn update

* Sat Sep 02 2006 Denis Smirnov <mithraen@altlinux.ru> 20060902:1.22-alt0.pre.20060902
- svn update

* Fri Sep 01 2006 Denis Smirnov <mithraen@altlinux.ru> 20060901:1.22-alt0.pre.20060901
- building with correct options

* Wed May 10 2006 Denis Smirnov <mithraen@altlinux.ru> 20060510:1.20-alt0.1
- first build
