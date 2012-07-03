Summary: The fileschanged utility reports when files have been altered
Name: fileschanged
Version: 0.6.9
Release: alt2
License: GPL
Group: File tools
Url: http://savannah.nongnu.org/projects/%name/
Packager: Boris Savelev <boris@altlinux.org>

Source: http://download.savannah.gnu.org/releases/%name/%name-%version.tar.gz
Patch: fileschanged-info-dircategory.patch

# Automatically added by buildreq on Sat Oct 04 2008
BuildRequires: gcc-c++ libgamin-devel help2man

%description
This software is a client to the FAM (File Alteration Monitor) server.
Here's how the fileschanged FAM client works:
you give it some filenames on the command line, it monitors those for changes.
When it discovers that a file has changed (or has been altered),
it displays the filename on the standard-output.

%prep
%setup
%patch0 -p1

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%doc README
%_bindir/fileschanged
%_datadir/fileschanged
%_man1dir/*
%_datadir/info/*

%changelog
* Mon May 25 2009 Boris Savelev <boris@altlinux.org> 0.6.9-alt2
- fix build

* Sat Oct 04 2008 Boris Savelev <boris@altlinux.org> 0.6.9-alt1
- initial build for Sisyphus from Mandriva

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.6.5-1mdv2008.1
+ Revision: 136415
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import fileschanged

* Thu Jun 22 2006 Erwan Velu <erwan@seanodes.com> 0.6.5-1
- 0.6.5

* Tue Jan 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.4-2mdk
- Fix PreReq

* Tue Jan 24 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.6.4-1mdk
- New release 0.6.4
- use mkrel

* Fri Jan 07 2005 Erwan Velu <erwan@seanodes.com> 0.6.0-2mdk
- Rebuild against gamin
* Mon Aug 16 2004 Erwan Velu <erwan@mandrakesoft.com> 0.6.0-1mdk
- Initial Release
