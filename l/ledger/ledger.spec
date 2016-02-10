Name: ledger
Version: 3.1.aed3709
Release: alt1.1

Summary: Ledger is a highly flexible, double-entry accounting system

License: %bsd
Group: Office
Url: http://www.ledger-cli.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ledger/ledger/archive/v%version.tar.gz
Source: %name-%version.tar

Requires: libledger = %version-%release

BuildPreReq: cmake rpm-macros-cmake rpm-build-licenses

# manual removed: python3 ruby ruby-stdlibs  python-module-cmd2 python-module-mwlib python-module-protobuf
# Automatically added by buildreq on Sat Aug 15 2015
# optimized out: boost-devel boost-devel-headers boost-python-headers cmake cmake-modules libgmp-devel libstdc++-devel python-base python-devel python-module-distribute python-module-oslo.i18n python-module-oslo.utils python-modules python3-base
BuildRequires: boost-filesystem-devel boost-python-devel ccmake gcc-c++ libedit-devel libicu-devel libmpfr-devel

BuildRequires: libutfcpp-devel

%description
Ledger is an accounting program which is invoked from the command-line
using a textual ledger file.  To start using Ledger, you will need to
create such a file containing your financial transactions.
See the documentation (ledger.pdf, or ledger.info) for full documentation
on creating a ledger file and using Ledger to generate reports.

A sample has been provided in the file "sample.dat":
$ ledger -f %_docdir/%name-%version/sample.dat reg

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

%build
%cmake -DUSE_PYTHON=yes
# 15.08.2015: disabled due ledger3.info install bug
# -DBUILD_DOCS=yes
%cmake_build

%install
%cmakeinstall_std

%files
%doc LICENSE.md README.md
%doc test/input/sample.dat
%_bindir/%name
%_man1dir/*

%files -n libledger
%_libdir/libledger.so.3

%files -n libledger-devel
%_includedir/%name/
%_libdir/libledger.so

%files -n python-module-ledger
%_libdir/python*/site-packages/*

#%files -n emacs-ledger
#%_emacslispdir/*

%changelog
* Wed Feb 10 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 3.1.aed3709-alt1.1
- Rebuilt with libicuuc.so.56.

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 3.1.aed3709-alt1
- new version 3.1 (with rpmrb script)

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 3.0.2-alt1.1
- rebuild with boost 1.57.0

* Wed Sep 24 2014 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Fri Feb 07 2014 Vitaly Lipatov <lav@altlinux.ru> 2.6.3-alt1
- new version 2.6.3 (with rpmrb script)
- cleanup spec, remove emacs subpackage

* Fri Feb 29 2008 Alexey Voinov <voins@altlinux.ru> 2.6.0.90-alt1
- initial build

