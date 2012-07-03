Name: algol68g
Version: 2.4.1
Release: alt1
Summary: Algol 68 interpreter
License: GPL
Group: Development/Other
Url: http://jmvdveer.home.xs4all.nl/algol.html
Packager: %packager

Source: %name-%version.tar
Patch: algol68g-2.2.0-alt-configure.patch

# Automatically added by buildreq on Sun Aug 14 2011
# optimized out: libtinfo-devel
BuildRequires: libncurses-devel

%description
The development of Algol played an important role in establishing
computer science as an academic discipline. The Algol 68 Genie
project preserves Algol 68 out of educational as well as
scientific-historical interest, by making available Algol 68 Genie;
a recent, well-featured implementation written from scratch.
Algol 68 Genie is a practically full implementation of the language
defined by the Revised Report. The implementation is a hybrid
compiler-interpreter; units with considerable interpreter-overhead
can optionally be compiled.

%prep
%setup
%patch -p1

%build
%configure
%make

%install
mkdir -p %buildroot/{%_bindir,%_docdir}
install -pm755 a68g %buildroot/%_bindir/a68g

install -pm644 AUTHORS %buildroot%_docdir/
install -pm644 NEWS %buildroot%_docdir/
install -pm644 README %buildroot%_docdir/
install -pm644 COPYING %buildroot%_docdir/
install -pm644 ChangeLog %buildroot%_docdir/

%files
%_bindir/*
%_docdir/*

%changelog
* Fri Jun 29 2012 Andrey Bergman <vkni@altlinux.org> 2.4.1-alt1
- Version update

* Sun Jun 10 2012 Andrey Bergman <vkni@altlinux.org> 2.4.0-alt1
- Version update

* Wed Apr 18 2012 Andrey Bergman <vkni@altlinux.org> 2.3.9-alt1
- Version update

* Wed Apr 11 2012 Andrey Bergman <vkni@altlinux.org> 2.3.8-alt1
- Version update

* Sat Mar 17 2012 Andrey Bergman <vkni@altlinux.org> 2.3.7-alt1
- Version update

* Sat Feb 25 2012 Andrey Bergman <vkni@altlinux.org> 2.3.6-alt1
- Version update

* Sun Feb 05 2012 Andrey Bergman <vkni@altlinux.org> 2.3.5-alt1
- Version update

* Tue Nov 29 2011 Andrey Bergman <vkni@altlinux.org> 2.3.4-alt1
- Version update

* Sun Oct 02 2011 Andrey Bergman <vkni@altlinux.org> 2.3.0-alt1
- Version update

* Sun Aug 14 2011 Andrey Bergman <vkni@altlinux.org> 2.2.0-alt1
- Initial release for Sisyphus.

