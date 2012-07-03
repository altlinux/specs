Name: libesmtp
Version: 1.0.6
Release: alt1

Summary: LibESMTP is a library to manage posting email using SMTP
License: GPL
Group: System/Libraries
Url: http://www.stafford.uklinux.net/libesmtp/
Packager: Vladimir Lettiev <crux@altlinux.ru>

Source: %name-%version.tar.bz2
Patch1: libesmtp-build.patch

# Automatically added by buildreq on Sat Apr 24 2004
BuildRequires: libssl-devel

%description
LibESMTP is a library to manage posting (or submission of) electronic
mail using SMTP to a preconfigured Mail Transport Agent (MTA) such as
Exim or Postfix.  It may be used as part of a Mail User Agent (MUA) or
another program that must be able to post electronic mail but where mail
functionality is not the program's primary purpose.

%package devel
Summary: Development files for libESMTP
Group: Development/C
PreReq: %name = %version-%release
License: GPL

%description devel
This package contains development files required for packaging
libESMTP-based software.

%prep
%setup -q
%patch1 -p1

%build
%configure \
    --enable-pthreads \
    --enable-require-all-recipients \
    --enable-etrn \
    --disable-static

%make_build

%install
%makeinstall_std
rm %buildroot%_libdir/esmtp-plugins/*.la

%files
%_libdir/libesmtp.so.*
%_libdir/esmtp-plugins
%doc AUTHORS README ChangeLog INSTALL COPYING TODO NEWS Notes doc/api.xml

%files devel
%_bindir/*
%_includedir/*
%_libdir/*.so

%changelog
* Tue Oct 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.6-alt1
- New version 1.0.6:
  + Fixed CVE-2010-1192, CVE-2010-1194 (certificate validation flaws)
- Build changes:
  + Disabled static build
  + Fixed install section
  + Plugins moved from devel subpackage to the main

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt2.1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libesmtp
  * postun_ldconfig for libesmtp

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.4-alt2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Mar 12 2007 Ildar Mulyukov <ildar@altlinux.ru> 1.0.4-alt2
- libesmtp-build.patch and libesmtp-1.0.4-ssl.patch by
-   shaba@ to build with new binutils/gcc

* Tue Dec 20 2005 Andrey Semenov <mitrofan@altlinux.ru> 1.0.4-alt1
- new version

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.3-alt1.1
- Rebuilt with openssl-0.9.7d.

* Fri Apr 23 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.0.3-alt1
- 1.0.3
- Updated build requires
- Added memrchr() implementation for systems that don't have one

* Wed Jan 7 2004 Andrey Semenov <mitrofan@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Mon Sep 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.1-alt2
- *.la files removed

* Mon Sep 15 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Mar 23 2003 Andrey Semenov <mitrofan@altlinux.ru> 1.0-alt1
- First version of RPM package.
