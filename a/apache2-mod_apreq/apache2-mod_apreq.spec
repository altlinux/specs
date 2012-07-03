Name: apache2-mod_apreq
Version: 2.13
Release: alt1

Summary: Apache2 HTTP request library
License: Apache Software License v. 2.0
Group: System/Servers

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

URL: http://httpd.apache.org/apreq/
Source0: libapreq2-%version.tar

Source1: apreq.conf
Source2: apreq.start

Source3: libapreq2.pc.in

Patch0: libapreq2-build.patch
Patch1: libapreq2-2.07-rc3-ldflags.patch
Patch2: libapreq2-2.09-pkgconfig.patch
Patch3: libapreq2-2.12-install.patch

Patch10: libapreq2-2.10-alt-apreq2-config.patch
Patch11: libapreq2-2.13-alt-t-util-stack.patch

Provides: libapreq  = %version
Provides: libapreq2 = %version

Requires(pre): apache2 >= %apache2_version
BuildRequires(pre): apache2-devel >= 2.2.5
BuildRequires: %apache2_apr_buildreq
BuildRequires: chrpath

# Automatically added by buildreq on Sat Oct 15 2011
BuildRequires: apache2-httpd-prefork apache2-mod_perl-devel libexpat-devel perl-ExtUtils-XSBuilder perl-libwww

# Skip search dependencies in modules with user-defined hooks
#add_findreq_skiplist */APR/Request/*.pm
#add_findreq_skiplist */Apache2/*.pm

%define common_desc  libapreq  is a shared library with associated modules for manipulating\
client request data via the Apache API.\

%description
%common_desc
Functionality includes parsing of application/x-www-form-urlencoded
and multipart/form-data content,  as well as  HTTP cookies. It also
includes language bindings for Perl (Apache::Request and
Apache::Cookie).

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release
Requires: apache2-devel
Provides: libapreq-devel = %version
Provides: libapreq2-devel = %version

%description devel
%common_desc
This file contains files needed for building XS modules that use
libapreq2.

%package doc
Summary: Documentation for %name
Group: System/Servers
BuildArch: noarch

%description doc
%common_desc
This file contains documentation for libapreq2.

%package -n perl-libapreq2
Summary: Perl interface to the Apache HTTP request library
Group: Development/Perl
Requires: apache2-mod_perl >= 2.0.0
Provides: perl-libapreq = %version

%description -n perl-libapreq2
%common_desc
This package contains a Perl interface to the Apache HTTP request
library.

%prep
%setup -q -n libapreq2-%version

%patch0
%patch1
%patch2
%patch3 -p1

%patch10
%patch11 -p2

# Fix multilib
sed -i -e 's,^libdir=.*,libdir=`pkg-config --variable=libdir libapreq2`,' \
       -e 's,^LDFLAGS=.*,LDFLAGS=`pkg-config --libs libapreq2`,' \
       -e 's,^LIBS=.*,LIBS=`pkg-config --libs libapreq2`,' \
       -e 's,^INCLUDES=.*,INCLUDES=`pkg-config --cflags-only-I libapreq2`,' \
        apreq2-config.in

cp -p %SOURCE3 .

%build
./buildconf
%autoreconf
%configure \
  --disable-dependency-tracking \
  --disable-static \
  --with-apache2-apxs=%apache2_apxs \
  --with-apr-config=%apache2_apr_config \
  --with-apu-config=%apache2_apu_config \
  --enable-perl-glue \
  --with-mm-opts=INSTALLDIRS=vendor \
  %nil
%make_build

%check
make test

%install
%make_install install DESTDIR=%buildroot

mkdir -p %buildroot%_pkgconfigdir
install -p -m644 libapreq2.pc %buildroot%_pkgconfigdir/

install -pD -m644 %SOURCE1 %buildroot%apache2_mods_available/apreq.load
install -pD -m644 %SOURCE2 %buildroot%apache2_mods_start/100-apreq.conf

chrpath -d %buildroot%perl_vendor_autolib/*/*/*.so
chrpath -d %buildroot%perl_vendor_autolib/*/*/*/*.so

# Documentation
cp -pR docs/html __docs
rm -rf __docs/installdox
mkdir -p %buildroot%_man3dir
cp -pR docs/man/man3/*  %buildroot%_man3dir/
rm -f %buildroot%_man3dir/apreq_xs*
rm -f %buildroot%_man3dir/todo*

%post
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:

if [ -e %apache2_mods_enabled/apreq.load ]; then
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To use libapreq2 check configuration and start %apache2_dname service."
    echo
    fi
else
    echo "Apache2 libapreq2 module had been installed, but does't enabled."
    echo "Check %apache2_mods_start directory for files with 'apreq=no' lines."
    echo
fi

%preun
if [ "$1" = "0" ] ; then # last uninstall
    [ -e %apache2_mods_enabled/apreq.load ] && %apache2_sbindir/a2dismod apreq 2>&1 >/dev/null ||:
fi

%postun
# Reconfigure Apache2:
%apache2_sbindir/a2chkconfig ||:
if [ "$1" = "0" ] ; then # last uninstall
    CONF_OK=0
    %apache2_sbindir/apachectl2 configtest && CONF_OK=1 ||:
    if [ "$CONF_OK" = "1" ]; then
	service %apache2_dname condrestart ||:
    else
        echo "Some errors detected in Apache2 configuration!"
	echo "To complete libapreq2 uninstalling check configuration and restart %apache2_dname service."
	echo
    fi
fi

%files
%doc CHANGES NOTICE README

%config %apache2_mods_available/apreq.load
%config %apache2_mods_start/100-apreq.conf

%apache2_moduledir/mod_apreq2.so
%exclude %apache2_moduledir/mod_apreq2.la
%_libdir/libapreq2.so.*

%files devel
%_bindir/apreq2-config
%_includedir/apreq2*
%apache2_includedir/apreq2*
%_libdir/libapreq2.so
%_libdir/pkgconfig/*.pc
%_man3dir/apreq*
%_man3dir/libapreq*
%_man3dir/mod_apreq*

%files doc
%doc __docs/* docs/*.tag

%files -n perl-libapreq2
%doc glue/perl/README
%perl_vendor_autolib/APR*
%perl_vendor_archlib/APR*
%perl_vendor_archlib/Apache2*

%changelog
* Sat Oct 15 2011 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.12 -> 2.13
- built for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.12-alt1.1
- rebuilt with perl 5.12
- fixed build

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 2.12-alt1
- New version 2.12

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.10-alt0.rc1.1
- Initial build for ALT Linux Sisyphus

* Sat Dec 13 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.10-alt0.rc1.0.1
- Build for ALT Linux

* Thu Nov 13 2008 Bojan Smojver <bojan@rexursive.com> - 2.10-0.rc1.1
- bump up to 2.10-RC1

* Tue Jul  8 2008 Bojan Smojver <bojan@rexursive.com> - 2.09-0.18.rc2
- add patch to use --avoid-ldap with apu-1-config

* Thu Jun  5 2008 Bojan Smojver <bojan@rexursive.com> - 2.09-0.17.rc2
- bump to re-tag

* Thu Jun  5 2008 Bojan Smojver <bojan@rexursive.com> - 2.09-0.16.rc2
- new autoconf changed the format of config.status

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-0.15.rc2
- Rebuild for perl 5.10 (again)

* Sat Feb  9 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-0.rc2.14
- rebuild for GCC 4.3

* Sat Feb  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.09-0.rc2.13
- rebuild for new perl

* Mon Dec  3 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.12
- tag for rebuild

* Fri Oct 26 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.11
- err on the side of caution and include more in LIBS

* Tue Oct 23 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.10
- retag for rebuild

* Tue Oct 23 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.9
- only use pkg-config for --ldflags in apreq2-config (closer, but not perfect)

* Mon Oct 22 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.8
- attempt to fix multilib issues (bug #341901)

* Sat Sep 01 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.7
- rebuild against apr-1.2.9-3 (bug #254241)

* Wed Aug 29 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.6
- rebuild against expat 2.0.1 (bug #195888)

* Wed Aug 22 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.5
- fix license

* Thu Mar 01 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.4
- build requires perl-devel

* Thu Mar 01 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.3
- build requires perl(Apache::Test)

* Wed Jan 31 2007 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.2
- fix version_check.pl

* Fri Nov 10 2006 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc2.1
- bump up to 2.09-rc2

* Sat Sep 16 2006 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc1.3.1
- mass rebuild

* Sat Sep 09 2006 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc1.3
- fix cleanup of the symlink

* Sat Sep 09 2006 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc1.2
- re-tag

* Sat Sep 09 2006 Bojan Smojver <bojan at rexursive.com> - 2.09-0.rc1.1
- bump up to 2.09-rc1

* Fri Aug 11 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-1
- bump up to 2.08

* Mon Aug 07 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc5.1
- bump up to 2.08-RC5

* Fri Jul 21 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc4.1
- bump up to 2.08-RC4

* Mon Jul 10 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc3.1
- bump up to 2.08-RC3

* Thu Jun 01 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc2.3
- include exisiting CFLAGS too

* Thu Jun 01 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc2.2
- add -fno-strict-aliasing to CFLAGS (prevent endless loop)

* Tue May 23 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc2.1
- bump up to 2.08-RC2 for Rawhide
- revert back some changes to spec file made for 2.08-RC1

* Fri May 19 2006 Bojan Smojver <bojan at rexursive.com> - 2.08-0.rc1.1
- bump up to 2.08-RC1 for Rawhide

* Wed Mar 01 2006 Bojan Smojver <bojan at rexursive.com> - 2.07-1.1
- rebuild

* Mon Feb 13 2006 Bojan Smojver <bojan at rexursive.com> - 2.07-1
- bump up to 2.07

* Fri Feb 03 2006 Bojan Smojver <bojan at rexursive.com> - 2.07-0.2.rc4
- re-tag for rebuild

* Fri Feb 03 2006 Bojan Smojver <bojan at rexursive.com> - 2.07-0.1.rc4
- bump up to 2.07-rc4

* Sat Dec 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.07-0.2.rc3
- Filter unversioned perl(*) provides for which a versioned one exists.

* Thu Dec  8 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.07-0.1.rc3
- Adapt to new apr, httpd.
- Don't print -L for standard dirs in apreq2-config --link-ld output.

* Sun Oct 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.07-0.rc3
- 2.07-rc3.

* Sat Oct 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.07-0.rc2
- 2.07-rc2.

* Fri Aug  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.06-2
- Include *.tag files in -devel docs, thanks to Bojan Smojver.
- Remove *.la instead of using %%exclude.

* Thu Jul 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.06-1
- 2.06.

* Tue Jul 19 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.06-0.2.rc4
- 2.06-dev-rc4.

* Sat Jul 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.06-0.2.rc3
- 2.06-dev-rc3.

* Wed Jul 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.06-0.2.rc2
- 2.06-dev-rc2.

* Sun Jul 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.06-0.1.rc1
- 2.06-dev-rc1.
- Improve summaries and descriptions.

* Wed Jun 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.05-0.6
- Rebuild with mod_perl 2.0.1.
- Drop static libs.

* Sat Jun 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.05-0.5
- Rebuild for FC4.

* Tue May 24 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.05-0.4
- Require httpd-mmn.

* Sat May 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.05-0.3
- Rebuild with mod_perl 2.0.0.

* Wed May 18 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.05-0.2
- Prevent %%post from failing at first install if httpd is not running.
- Provide (perl-)libapreq(-devel).

* Thu May  5 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.05-0.1
- 2.05-dev, aclocal patch applied upstream.

* Sat Dec  4 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.04_03-0.fdr.2
- Buildrequire mod_perl-devel, not mod_perl.

* Wed Aug 18 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.03_04-0.fdr.1
- Update to 2.03_04.
- Disable dependency tracking to speed up the build.

* Thu May 27 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.03-0.fdr.1
- First build.
