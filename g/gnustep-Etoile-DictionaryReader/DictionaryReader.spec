%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-DictionaryReader
Version: r7926
Release: alt1.git20121130.1
Summary: DictionaryReader is a dictionary application
License: MIT
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/etoile/DictionaryReader.git
Source: %name-%version.tar
Source1: gnustep-DictionaryReader.menu

BuildPreReq: clang-devel gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-gui-devel gnustep-Etoile-devel
BuildPreReq: libgmp-devel libgnutls-devel libgcrypt-devel
BuildPreReq: libxslt-devel libffi-devel libicu-devel zlib-devel
BuildPreReq: gnustep-Etoile-DocGenerator

Requires: gnustep-back

%description
DictionaryReader is a dictionary application that queries Dict servers
in the internet to let you look up words. It's aimed to be lightweight
and easy to use.

%prep
%setup

cp %_libdir/GNUstep/Etoile/* ~/
prepare_docgen

%build
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%make \
	messages=yes \
	debug=yes \
	strip=no \
	documentation=yes \
	PROJECT_NAME=DictionaryReader

%install
. %_datadir/GNUstep/Makefiles/GNUstep.sh 

export LD_LIBRARY_PATH=%_libdir/io/addons/Range/_build/dll

%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM \
	documentation=yes \
	PROJECT_NAME=DictionaryReader

#install -d %buildroot%_docdir/GNUstep/UnitKit
#cp -fRP Documentation/* %buildroot%_docdir/GNUstep/UnitKit/

install -p -D -m644 %SOURCE1 \
	%buildroot%_menudir/gnustep-DictionaryReader

%files
%doc ChangeLog README TODO
%_bindir/*
%_libdir/GNUstep
%_menudir/*

%changelog
* Thu Jan 14 2016 Mikhail Efremov <sem@altlinux.org> r7926-alt1.git20121130.1
- NMU: Rebuild with libgnutls30.

* Fri Mar 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r7926-alt1.git20121130
- Initial build for Sisyphus

