%set_verify_elf_method unresolved=strict

Name: gnustep-Etoile-DevDoc
Version: 0.4.2
Release: alt1.svn20120503
Summary: Developer documentation helper for Etoile
License: BSD
Group: Graphical desktop/GNUstep
Url: http://etoileos.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# svn://svn.gna.org/svn/etoile/trunk/Etoile/Developer/Documentation/
Source: %name-%version.tar
BuildArch: noarch

%description
Developer documentation helper for Etoile.

%prep
%setup

%install
install -d %buildroot%_datadir/GNUstep/DevDoc
install -m755 *.sh %buildroot%_datadir/GNUstep/DevDoc/

%files
%doc Guides/*
%_datadir/GNUstep

%changelog
* Wed Mar 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.svn20120503
- Initial build for Sisyphus

