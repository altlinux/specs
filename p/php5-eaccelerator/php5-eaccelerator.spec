%define php5_extension eaccelerator

Name: php5-eaccelerator
Version: 0.9.6.1
Release: alt8

Summary: PHP accelerator, optimizer, encoder and dynamic content cache
License: GPL
Group: System/Servers

Url: http://eaccelerator.net
Source0: http://bart.eaccelerator.net/source/%version/%php5_extension-%version.tar.bz2
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires(pre): rpm-build-php5
BuildRequires: rpm-build-php5 = %php5_version
BuildRequires: php5-devel = %php5_version
Prereq: php5-libs = %php5_version

%define eadocs AUTHORS ChangeLog NEWS README

%description
eAccelerator is a free open source PHP accelerator, optimizer,
encoder and dynamic content cache for PHP. It increases
performance of PHP scripts by caching them in compiled state,
so that the overhead of compiling is almost completely
eliminated.  It also optimises the script to speed up execution
of PHP scripts. eAccelerator typically reduces server load and
increases the speed of your PHP code by 1-10 times.  Works with
PHP FastCGI as well.

eLoader is not needed when using eAccelerator, because eAccelerator
already has the loader compiled in.

%prep
%setup -c

%build
%add_optflags -fPIC
pushd %php5_extension-%version
phpize
%configure \
	--enable-eaccelerator=shared \
	--without-eaccelerator-encoder \
	--without-eaccelerator-loader \
	--with-eaccelerator-shared-memory \
	--with-eaccelerator-content-caching
%php5_make
popd

%install
pushd %php5_extension-%version
%php5_make_install
mkdir -p %buildroot/%_cachedir/%php5_extension
install -pDm644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -pDm644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params
cp -alf %eadocs ..
popd

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%_cachedir/%php5_extension
%doc %eadocs
# doc/ belongs to examples subpackage, sample php code
#doc doc/

%post
%php5_extension_postin

%preun
%php5_extension_preun

# TODO:
# - conditional eloader/encoder build?
# - add/separate admin stuff (see also spec attached to #19996)

%changelog
* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt8
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt7
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt6
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt5
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt4
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 0.9.6.1-alt1
- new version

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 0.9.6-alt5
- Rebuild with php5-5.2.14.20100721-alt1 (part 2)

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 0.9.6-alt4
- Rebuild with php5-5.2.14.20100721-alt1

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 0.9.6-alt3
- Rebuild with php5-5.2.13.20100205-alt1

* Fri Feb 19 2010 Anton Farygin <rider@altlinux.ru> 0.9.6-alt2
- default eaccelerator.shm_size changed to 0 (closes: #22997)

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 0.9.6-alt1
- new version
- rebuild with php5-5.2.12
- added php5-lib requires

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 0.9.5.3-alt5
- added minimal documentation file set (closes: #19996)

* Mon Aug 03 2009 Michael Shigorin <mike@altlinux.org> 0.9.5.3-alt4
- built against php5-5.2.11.20090722-alt1

* Mon Feb 23 2009 Michael Shigorin <mike@altlinux.org> 0.9.5.3-alt3
- built against php5-5.2.9.20090205-alt1

* Sun Oct 05 2008 Michael Shigorin <mike@altlinux.org> 0.9.5.3-alt2
- built against php5-5.2.7.20080920

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 0.9.5.3-alt1
- 0.9.5.3 built against php5-5.2.7.20080627
- spec cleanup
- added Url:
- me as a Packager:

* Sun Apr 13 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.5.2-alt1
- New version

* Mon Jun 18 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.5.1-alt1
- New version
- Removed patch for use with PHP 5.2.x (fixed by upstream)
- Rebuild with new php

* Thu Apr 12 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.5-alt4
- Rebuild with new php5
- Patch for use with PHP 5.2.x

* Fri Mar 23 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.5-alt3
- Rebuild with new php5

* Sat Feb 03 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.5-alt2
- Fixed buildrequires

* Thu Feb 01 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.9.5-alt1
- First build for Sisyphus

