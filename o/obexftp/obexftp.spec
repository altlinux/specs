%def_enable perl
%def_enable python
%def_enable ruby
%def_disable tcl
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

Summary: ObexFTP implements the Object Exchange (OBEX) protocols file transfer
Name: obexftp
Version: 0.24.2
Release: alt2

License: GPLv2
Group: Communications
URL: https://sourceforge.net/projects/openobex/

Source: %name-%version.tar

# Patches from Fedora
Patch0: %name-norpath.patch
Patch1: %name-0.24-fix-absurd-install-path.patch

# ALT Linux patches
Patch2: %name-alt-fix-library-link.patch

Requires: lib%name = %version-%release

BuildRequires(pre): cmake
BuildRequires: gcc-c++ libopenobex-devel libgsm-devel libbluez-devel
BuildRequires: libusb-compat-devel libfuse-devel asciidoc xmlto
BuildRequires: libexpat-devel

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
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
%cmake
%cmake_build all doc RUBY="ruby -rvendor-specific"

%install
%cmakeinstall_std

%if_enabled ruby
install -Dm 0755 %buildroot/usr/lib/ruby/vendor_ruby/*/*/obexftp.so %buildroot%ruby_sitearchdir/obexftp.so
rm -f %buildroot/usr/lib/ruby/vendor_ruby/*/*/obexftp.so
%endif

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
* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.24.2-alt2
- Rebuild with new %%ruby_sitearchdir location

* Fri Sep 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.24.2-alt1
- New version
- Apply patches from Fedora
- tcl support is deprecated
- Enable Perl

* Sun Dec 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt6.git76127.1
- disable perl subpackage not to hinder perl 5.20.1 update

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.23-alt5.git76127.1
- Rebuilt with ruby-2.0.0-alt1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt5.git76127
- built for perl 5.18

* Fri Nov 30 2012 Led <led@altlinux.ru> 0.23-alt4.git76127.1
- Rebuilt with ruby-1.9.3-alt1

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 0.23-alt4.git76127
- rebuilt for perl-5.16

* Mon Sep 03 2012 Alexey Shabalin <shaba@altlinux.ru> 0.23-alt3.git76127
- buils upstream snapshot 76127c541fc7fab4a86a4eca11e407fbd91f81aa

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
