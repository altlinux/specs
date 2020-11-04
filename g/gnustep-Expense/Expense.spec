%set_verify_elf_method unresolved=strict

Name: gnustep-Expense
Version: 0.1
Release: alt6
Summary: Very lightweight application to track your expenses
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.eskimo.com/~pburns/Expense/
Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar
Source1: %name.menu

BuildPreReq: gnustep-make-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

Requires: gnustep-back

%description
Expense is a very lightweight application to track your expenses, much
like you might expect to find on a PDA.

Features:

* Date, category, and item filters, generated from the contents of your
  expenses.
* Localized for Thai.
* Full source code available.

%prep
%setup

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

install -p -D -m644 %SOURCE1 %buildroot%_menudir/%name

%files
%doc Documentation/*
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Wed Nov 04 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt6
- Remove redundant clang-devel for build

* Wed Oct 07 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt5
- Build without libgnustep-objc2-devel.

* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt4.1
- NMU: Rebuild with libgnutls30.

* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt4
- Built with clang

* Mon Feb 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added menu file (thnx kostyalamer@)

* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added Requires: gnustep-back

* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

