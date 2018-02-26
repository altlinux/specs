Summary:	a tar post-processor
Name:		tardy
Version:	1.17
Release:	alt2

Packager:	Alexey Voinov <voins@altlinux.ru>

License:	%gpl3plus
Group:		Archiving/Backup
Source:		%name-%version.tar
URL:		http://tardy.sourceforge.net/

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Thu May 08 2008
BuildRequires: gcc-c++ groff-base zlib-devel

%description
The tardy program is a tar(1) post-processor.  It may be used to
manipulate the file headers tar(5) archive files in various ways.

The reason the tardy program was written was because the author wanted
to "spruce up" tar files before posting them to the net, mostly to
remove artefacts of the development environment, without introducing more.

The tardy program was designed to allow you to alter certain atrributes
of files after they have been included in the tar file.  Among them are:

  * change file owner (by number or name)
  * change file group (by number or name)
  * add directory prefix (for example, dot)
  * change file protections (for example, from 600 to 644)

Note that all of these affect ALL files in the archive.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install RPM_BUILD_ROOT=$RPM_BUILD_ROOT install

%files
%_bindir/tardy
%_man1dir/tardy.1*
%_man1dir/tardy_license.1*

%changelog
* Tue Jun 02 2009 Alexey Voinov <voins@altlinux.ru> 1.17-alt2
- fixed problem with const and strchr

* Wed Oct 08 2008 Alexey Voinov <voins@altlinux.ru> 1.17-alt1
- new version (1.17)

* Thu May 08 2008 Alexey Voinov <voins@altlinux.ru> 1.16-alt1
- new version (1.16) 
- buildreqs updated

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.12-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Aug 17 2004 Alexey Voinov <voins@altlinux.ru> 1.12-alt1
- new version (1.12)
- url updated
- buildreqs updated

* Mon Oct 06 2003 Alexey Voinov <voins@altlinux.ru> 1.11-alt2
- buildreq fixed

* Sun Oct 27 2002 Alexey Voinov <voins@voins.program.ru> 1.11-alt1
- new version(1.11)
- spec clean up
- buildreq updated
- group fixed

* Fri Apr 26 2002 Alexey Voinov <voins@voins.program.ru> 1.8-alt2
- buildreqs fixed

* Mon Nov 12 2001 Alexey Voinov <voins@voins.program.ru> 1.8-alt1
- adapted for Sisyphus from tardy.spec included in tarball 

