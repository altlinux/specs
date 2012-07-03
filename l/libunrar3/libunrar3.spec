Name: libunrar3
Version: 3.8.5
Release: alt1

Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: Uncompressor library for .rar v.3.x format archive files.
License: RARLAB
Group: System/Libraries
URL: http://www.rarlab.com/rar

Source0: http://www.rarlab.com/rar/unrarsrc-%version.tar.gz

Patch0:  unrar-3.8.5_fix.patch

%define lname unrar

# Automatically added by buildreq on Thu Dec 02 2004
BuildRequires: gcc-c++ libstdc++-devel

%description
It's a uncompressor library for .rar v.3.x format archive files.

%package devel
Summary: libunrar3 header file
Group: Development/Other
Conflicts: %name < %version-%release, %name > %version-%release
Requires: %name

%description devel
This package includes libunrar3 header file

%prep
%setup -q -n %lname
%patch0 -p1

%build
make -f makefile.unix lib

%install
install -D libunrar3.so $RPM_BUILD_ROOT%_libdir/libunrar3.so
install -D dll.hpp $RPM_BUILD_ROOT%_includedir/libunrar3/dll.hpp

%files
%_libdir/libunrar3.so
%doc license.txt readme.txt 

%files devel
%dir %_includedir/libunrar3
%_includedir/libunrar3/dll.hpp

%changelog
* Thu Nov 13 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.8.5-alt1
- new version

* Wed Mar 05 2008 Sergey Y. Afonin <asy@altlinux.ru> 3.7.8-alt1
- new version

* Fri Feb 09 2007 Sergey Y. Afonin <asy@altlinux.ru> 3.7.3-alt1
- new version
- CVE-2007-0855

* Mon Dec 25 2006 Sergey Y. Afonin <asy@altlinux.ru> 3.6.8-alt1
- new version
- fixed: #10507 (%%dir %%_includedir/libunrar3)

* Thu Sep 22 2005 Sergey Y. Afonin <asy@altlinux.ru> 3.5.3-alt1
- new version
- move license.txt and readme.txt from doc to main package, doc
  package is removed.

* Thu Oct 21 2004 Sergey Y. Afonin <asy@altlinux.ru> 3.4.3-alt1
- initial build for Alt Linux

* Thu Oct 21 2004 Mokrushin I.V. aka McMCC <mcmcc@mail.ru> 3.4.3-1
- initial build
- unrar-3.4.3_fix.patch (http://mcmcc.bat.ru/clam_rar3.html)
