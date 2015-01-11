Name: ledger
Version: 3.0.2
Release: alt1.1

Summary: Ledger is a highly flexible, double-entry accounting system

License: %bsd
Group: Office
Url: http://www.newartisans.com/software/ledger.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ledger/ledger/archive/v2.6.3.tar.gz
Source: %name-%version.tar
Patch: %name-2.6.0.90-alt-makefile.patch

Requires: libledger = %version-%release

BuildPreReq: rpm-build-licenses

# manual removed: python3 ruby ruby-stdlibs
# Automatically added by buildreq on Fri Feb 07 2014
# optimized out: boost-python-headers libstdc++-devel makeinfo python-base python-devel python-module-distribute python-module-zope python-modules python-modules-compiler python-modules-email python3-base
BuildRequires: boost-devel-headers boost-python-devel gcc-c++ glibc-devel libexpat-devel libgmp-devel libofx-devel libpcre-devel python-module-cmd2 python-module-mwlib python-module-protobuf

%description
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

%package -n libledger
Summary: Libraries for ledger accounting system
Group: System/Libraries

%description -n libledger
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains libraries for ledger to use.

%package -n libledger-devel
Summary: Development files for ledger accounting system
Group: Development/C
Requires: libledger = %version-%release

%description -n libledger-devel
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains files needed for developing programs using
ledger facilities.

%package -n python-module-%name
Summary: Python bindings for ledger
Group: Development/Python
Requires: libledger = %version-%release

%description -n python-module-%name
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains python bindings for some of ledger
functionality.

%package -n emacs-ledger
Summary: Emacs mode for ledger accounting system
Group: Editors
Requires: ledger = %version-%release

%description -n emacs-ledger
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.  A sample
has been provided in the file "sample.dat".  See the documentation
(ledger.pdf, or ledger.info) for full documentation on creating a
ledger file and using Ledger to generate reports.

This package contains emacs libraries to ease use of ledger.

%prep
%setup
%patch -p1
touch AUTHORS
%autoreconf

%build
%add_optflags -I %_includedir/pcre
%add_optflags -I %_includedir/libofx
%add_optflags -I %_includedir/python2.7
%configure --disable-static --enable-xml --enable-ofx --enable-python
%make_build

%install
%makeinstall

%files
%doc LICENSE README NEWS sample.dat
%_bindir/%name
%_infodir/*

%files -n libledger
%_libdir/*.so.*
%_libdir/libledger-*.so

%files -n libledger-devel
%_includedir/%name
%_libdir/libledger.so
%_libdir/libamounts.so

%files -n python-module-ledger
%_libdir/python*/site-packages/*

#%files -n emacs-ledger
#%_emacslispdir/*

%changelog
* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 3.0.2-alt1.1
- rebuild with boost 1.57.0

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 2.6.3-alt1
- new version 2.6.3 (with rpmrb script)
- cleanup spec, remove emacs subpackage

* Fri Feb 29 2008 Alexey Voinov <voins@altlinux.ru> 2.6.0.90-alt1
- initial build

