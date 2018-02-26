Summary: file history and comparison tools
Name: fhist
Version: 1.17
Release: alt2
License: %gpl3plus
Group: Development/Other
Source: %name-%version.tar
URL: http://fhist.sourceforge.net/fhist.html

Packager: Alexey Voinov <voins@altlinux.ru>

# Automatically added by buildreq on Wed Oct 08 2008
BuildRequires: cook groff-dvi groff-ps rpm-build-licenses

%description
The FHist package contains 3 utilities, a file history tool ``fhist'',
a file comparison tool ``fcomp'', and a file merging tool ``fmerge''.
All three are bundled together, because they all use the same
minimal-difference algorithm.

The history tool presented here, fhist, is a minimal history tool.
It provides no locking or branching.  This can be useful in contexts
where the configuration management or change control be being provided
by some other tool.

%prep
%setup -q

%build
%configure
make

%install
make RPM_BUILD_ROOT=$RPM_BUILD_ROOT install

%files
%_bindir/*
%_libdir/%name
%_datadir/%name
%_man1dir/*

%changelog
* Fri Sep 25 2009 Alexey Voinov <voins@altlinux.ru> 1.17-alt2
- url updated

* Wed Oct 08 2008 Alexey Voinov <voins@altlinux.ru> 1.17-alt1
- new version (1.17) 
- license changed to GPL3+
- buildreqs updated

* Wed Jan 04 2006 Alexey Voinov <voins@altlinux.ru> 1.16-alt1
- new version (1.16) 

* Sat Nov 26 2005 Alexey Voinov <voins@altlinux.ru> 1.15-alt1
- new version (1.15) 

* Fri Sep 17 2004 Alexey Voinov <voins@altlinux.ru> 1.14-alt1
- new version (1.14) 

* Wed Oct 01 2003 Alexey Voinov <voins@altlinux.ru> 1.13-alt1
- new version (1.13) 
- rebuilt without libintl1

* Mon Oct 21 2002 Alexey Voinov <vns@altlinux.ru> 1.10-alt2
- rebuilt with gcc3.2

* Tue Jul 09 2002 Alexey Voinov <voins@voins.program.ru> 1.10-alt1
- new version (1.10)

* Fri Apr 26 2002 Alexey Voinov <voins@voins.program.ru> 1.8-alt2
- buildreqs fixed

* Tue Nov 06 2001 Alexey Voinov <voins@voins.program.ru> 1.8-alt1
- adapted for Sisyphus from fhist.spec included in tarball

