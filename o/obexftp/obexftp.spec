%def_enable perl
%def_enable python
%def_enable ruby
%def_enable tcl
%def_disable static
%def_disable swig

%if_enabled perl
%force_enable swig
%endif
%if_enabled python
%force_enable swig
%endif
%if_enabled ruby
%force_enable swig
%endif
%if_enabled tcl
%force_enable swig
%endif

Summary: ObexFTP implements the Object Exchange (OBEX) protocols file transfer.
Name: obexftp
Version: 0.23
Release: alt2.4.1

License: GPL
Group: Communications
URL: http://triq.net/gsm.html

Packager: Pavlov Konstantin <thresh@altlinux.ru>
Source: http://triq.net/obex/%name-%version.tar.bz2
Patch: obexftp-alt-STR2CSTR.patch
Patch1: obexftp-alt-version-check.patch

Requires: lib%name = %version-%release

BuildRequires: gcc-c++ libopenobex-devel libgsm-devel libbluez-devel libusb-compat-devel

BuildPreReq: chrpath

%if_enabled swig
BuildRequires: swig
%endif
%if_enabled perl
BuildRequires: perl-devel
%endif
%if_enabled python
BuildRequires: python-devel
%endif
%if_enabled ruby
BuildRequires: ruby libruby-devel
%endif
%if_enabled tcl
BuildRequires: tcl-devel tcl
%endif

%package -n lib%name
Summary: obexftp libraries
Group: System/Libraries

%package devel
Summary: Development files of obexftp
Group: Development/C
Requires: lib%name = %version-%release

%if_enabled static
%package devel-static
Summary: Static develop path of obexftp
Group: Development/C
Requires: lib%name-devel = %version-%release
%endif

%if_enabled python
%package -n python-module-obexftp
Summary: Python bindings for obexftp
Group: Development/Python
%endif

%if_enabled perl
%package -n perl-obexftp
Summary: Perl bindings for obexftp
Group: Development/Perl
%endif

%if_enabled tcl
%package -n tcl-obexftp
Summary: Tcl bindings for obexftp
Group: Development/Tcl
Requires: tcl
%endif

%if_enabled ruby
%package -n ruby-obexftp
Summary: Ruby bindings for obexftp
Group: Development/Ruby
Requires: ruby
%endif

%description
This package contains some command line tools and the ObexFTP library.
Using OpenOBEX it enables you to transfer data via IrDA, BlueTooth
as well as some custom (Siemens, Ericsson) serial port protocols.
Authors: Christian W. Zuckschwerdt <zany@triq.net>

%description -n lib%name
Libraries for obexftp

%description devel
This package contains some command line tools and the ObexFTP library.
Using OpenOBEX it enables you to transfer data via IrDA, BlueTooth
as well as some custom (Siemens, Ericsson) serial port protocols.

%if_enabled static
%description devel-static
Static development files for obexftp.
%endif

%if_enabled python
%description -n python-module-obexftp
Python bindings for obexftp.
%endif

%if_enabled perl
%description -n perl-obexftp
Perl bindings for obexftp.
%endif

%if_enabled tcl
%description -n tcl-obexftp
Tcl bindings for obexftp.
%endif

%if_enabled ruby
%description -n ruby-obexftp
Ruby bindings for obexftp.
%endif

%prep
%setup
%patch -p2
%patch1 -p2

%build
%autoreconf

%configure \
    --enable-bluetooth \
    --enable-builddocs \
    --enable-swig \
	%{subst_enable tcl} \
    %{subst_enable perl} \
    %{subst_enable python} \
    %{subst_enable ruby} \
	%{subst_enable static} 
%if_enabled swig
rm -f swig/*/*_wrap.c
%endif
%make_build RUBY="ruby -rvendor-specific"

%install

%make_install noinstdir=`pwd`/docs DESTDIR="%buildroot" INSTALLDIRS=vendor install

for i in obexmv; do
	ln -s obexftp %buildroot%_bindir/$i
done

mv %buildroot%_bindir/discovery %buildroot%_bindir/obexftp-discovery
install -m 0644 -D doc/%name.1 %buildroot%_man1dir/%name.1

%if_enabled tcl
mkdir -p %buildroot%_tcllibdir
mv %buildroot%_libdir/obexftp.so* %buildroot%_tcllibdir/
LD_LIBRARY_PATH=%buildroot%_libdir %tea_makeindex -C %buildroot%_tcldatadir/obexftp
%endif

%if_enabled python
mv %buildroot%python_sitelibdir/obexftp/_*.so* %buildroot%python_sitelibdir
%endif

chrpath -d %buildroot%perl_vendor_autolib/OBEXFTP/OBEXFTP.so

%files
%doc AUTHORS ChangeLog NEWS README* THANKS TODO
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/lib*.so.*

%files devel
%dir %_includedir/bfb
%dir %_includedir/multicobex
%dir %_includedir/obexftp
%_includedir/*/*
%_libdir/*.so
%_pkgconfigdir/obexftp.pc
%if_enabled tcl
%_tcldatadir/*
%endif

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%if_enabled perl
%files -n perl-obexftp
%perl_vendor_archlib/OBEXFTP*
%perl_vendor_autolib/OBEXFTP*
%endif

%if_enabled python
%files -n python-module-obexftp
%python_sitelibdir/*
%endif

%if_enabled tcl
%files -n tcl-obexftp
%_tcllibdir/*
%_tcldatadir/*
%endif

%if_enabled ruby
%files -n ruby-obexftp
%ruby_sitearchdir/*
%endif

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.23-alt2.4.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Feb 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt2.4
- Removed bad RPATH

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.23-alt2.3.1
- Rebuild with Python-2.7

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt2.3
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt2.2.1
- rebuilt with perl 5.12

* Sun Sep 26 2010 Alexey I. Froloff <raorn@altlinux.org> 0.23-alt2.2
- Rebuilt with Ruby 1.9.2

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt2.1
- Rebuilt with python 2.6

* Fri Jul 03 2009 Alexey I. Froloff <raorn@altlinux.org> 0.23-alt2
- Rebuilt with Ruby 1.9
- Force update swig-generated wrappers

* Mon Apr 20 2009 Pavlov Konstantin <thresh@altlinux.ru> 0.23-alt1
- 0.23 release.
- Build with libusb-compat-devel.

* Thu Aug 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt2
- 0.22 release.

* Tue Nov 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt1.rc9
- 0.22 RC9.

* Fri Sep 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt1.rc7
- 0.22 RC7.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt1.rc6
- 0.22 RC6.

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt1.rc4
- 0.22 RC4.

* Fri Jun 01 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt1.rc1
- 0.22 RC1.

* Wed Feb 21 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.22-alt1.pre4
- Add dummy changelog to make incominger happy.

* Mon Jan 08 2007 Andrey Rahmatullin <wrar@altlinux.ru> 0.22-alt1.pre4
- 0.22-pre4
- fix Motorola cable OBEX

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.21-alt2
- Properly packing ruby module.
- Dealed with #10251 & #7145: obexftp-discovery now fixed.

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.21-alt1
- 0.21 release.
- Incorporated patches into the source tree.

* Sat Aug 26 2006 Grigory Milev <week@altlinux.ru> 0.20-alt2
- rebuild with new bluetooth libs

* Fri Aug 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.20-alt1
- 0.20.
- Added -as-needed patch.
- Added -avoid-version patch to deal with tcl bindings.
- Added a switch to deal with static. Default: off.
- Substited Copyright tag with License.
- Changed Packager: field.
- Fixed summaries and descriptions.
- Fixed install part.
- Added perl, python & tcl packages with bindings.

* Mon Aug 22 2005 Grigory Milev <week@altlinux.ru> 0.10.7-alt2
- rebuild with bluetooth support

* Fri Aug  5 2005 Grigory Milev <week@altlinux.ru> 0.10.7-alt1
- new version released

* Tue Feb 24 2004 Grigory Milev <week@altlinux.ru> 0.10.4-alt3.rc3
- new version released

* Fri Dec 12 2003 Grigory Milev <week@altlinux.ru> 0.10.4-alt2.rc1
- remove *.la files due policy

* Wed Oct 22 2003 Grigory Milev <week@altlinux.ru> 0.10.4-alt1.rc1
- new version released

* Fri May 30 2003 Grigory Milev <week@altlinux.ru> 0.10.3-alt1
- new version release

* Thu Apr 17 2003 Grigory Milev <week@altlinux.ru> 0.10.0-alt2
- move libraries to separate package
- move static development libs to separate package

* Tue Jan 21 2003 Grigory Milev <week@altlinux.ru> 0.10.0-alt1
- new version released

* Tue Dec 17 2002 Grigory Milev <week@altlinux.ru> 0.9.3-alt1
- initial build for ALT linux


