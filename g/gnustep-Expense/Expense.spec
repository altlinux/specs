%set_verify_elf_method unresolved=strict

Name: gnustep-Expense
Version: 0.1
Release: alt1
Summary: Very lightweight application to track your expenses
License: GPLv2
Group: Graphical desktop/GNUstep
Url: http://www.eskimo.com/~pburns/Expense/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel

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
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2 -DGNUSTEP' \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	GNUSTEP_MAKEFILES=%_datadir/GNUstep/Makefiles

%files
%doc Documentation/*
%_bindir/*
%_libdir/GNUstep

%changelog
* Thu Jan 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

