%define php5_extension xaira
%def_disable static

Name: xaira
Version: 1.26
Release: alt6

Summary: XML Aware Indexing and Retrieval Application 
License: GPLv2+
Group: Text tools
Url: http://www.xaira.org

Packager: Kirill Maslinsky <kirill@altlinux.org>
Source0: %name-%version.tar
#Patch0: alt-x86_64.patch
Patch1: alt-termcap.patch
Patch2: alt-destdir.patch
Patch3: alt-linking.patch
#Patch4: alt-100buffer.patch
Patch5: alt-php-make.patch

BuildRequires(pre): rpm-build-php5
BuildRequires: gcc-c++ libxerces-c-devel libicu-devel libreadline-devel zlib-devel libtinfo-devel
BuildRequires: php5-devel php5

%description 
Xaira is the current name for a new version of SARA, the text
searching software originally developed at OUCS for use with the British
National Corpus. This new version has been entirely re-written as a general
purpose XML search engine, which will operate on any corpus of well-formed XML
documents. It is however best used with TEI-conformant documents.

Xaira has full Unicode support. This means you can use it to search and display
text in any language, provided you have a suitable Unicode font installed on
your system.

%package -n lib%name
Summary: Shared libs for %name
Group: Development/C

%description -n lib%name
Shared libs for %name

%package -n lib%name-devel
Summary: Headers for %name
Group: Development/C
Requires: %name = %version-%release

%description -n lib%name-devel
Headers for building software that uses %name

%package php
Summary: Simple PHP interface for xaira
Group: Networking/WWW
Requires: lib%name = %version-%release

%description php
Simple PHP interface for xaira

%prep
%setup
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1

find -name Makefile.am -exec sed -i '/AM_CPPFLAGS/s/-w//' {} \;

%build
export LDFLAGS=-lphp-%_php5_version
%add_optflags %optflags_debug
%autoreconf 
%configure --with-php5=%php5_includedir/%_php5_version
%make_build 

%install
%makeinstall_std 
%find_lang %name
# rename binaries
pushd %buildroot/%_bindir/
mv indexer xaira_indexer
mv solve xaira_solve
popd

%check
%make_build check XAIRA_DATAPATH=../server/

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files -f %name.lang
%doc AUTHORS ChangeLog NEWS README docs/*
%_bindir/*
%_sbindir/*
%_datadir/%name
%_logdir/%name

%files -n lib%name
%_libdir/*.so.*
%exclude %_libdir/libphpXaira.so*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*.h
%exclude %_libdir/libphpXaira.so

%files php
%_libdir/libphpXaira.so
%_libdir/libphpXaira.so.*
%php5_extdir/*
%_var/www/%name

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name.a
%endif


%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 1.26-alt6
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.26-alt5
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 1.26-alt4
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 1.26-alt3
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 1.26-alt2
- Rebuild with php5-5.3.5.20110105-alt1

* Sat Jan 15 2011 Kirill Maslinsky <kirill@altlinux.org> 1.26-alt1
- 1.26
- rename indexer and solve binaries into xaira_indexer and xaira_solve
  to avoid conflicts with sphinx and possible other packages
- upstream support for x86_64, drop local workaround patches
- %%check enabled

* Fri Dec 10 2010 Dmitry V. Levin <ldv@altlinux.org> 1.25-alt5
- Blind rebuild with ICU 4.6.

* Tue Mar 16 2010 Kirill Maslinsky <kirill@altlinux.org> 1.25-alt4
- %%check disabled due to indexer fail on x86_64

* Mon Mar 15 2010 Kirill Maslinsky <kirill@altlinux.org> 1.25-alt3
- rebuilt with ICU 4.4

* Mon Oct 05 2009 Kirill Maslinsky <kirill@altlinux.org> 1.25-alt2
- %%check enabled
- indexer now works
  + alt-100buffer.patch: simple workaround patch for potential
    buffer overflow in indexer (thanks ldv@ for advice)
- PHP interface built (as xaira-php subpackage)

* Wed Sep 16 2009 Kirill Maslinsky <kirill@altlinux.org> 1.25-alt1
- initial build for Sisyphus
- this is an ALPHA-stage packaging
  + indexer doesn't work (memory allocation problems)
  + PHP and java clients not built yet

