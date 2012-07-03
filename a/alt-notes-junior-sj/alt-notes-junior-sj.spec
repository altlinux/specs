Name: alt-notes-junior-sj
Version: 0.2
Release: alt4

Summary: Linux Junior 4.0 distribution license and relnotes
License: Distributable
Group: Documentation

Source: %name-%version-%release.tar

Provides: alt-license-junior-sj = %version-%release
Obsoletes: alt-license-junior-sj
Conflicts: alt-notes-junior alt-notes-junior-sm alt-notes-hpc

BuildArch: noarch

%description
Linux Junior 4.0 distribution license and release notes

%prep
%setup

%install
install -d %buildroot%_datadir/alt-notes
install -pm0644 *.html %buildroot/%_datadir/alt-notes/

%files
%_datadir/alt-notes/*

%changelog
* Tue Apr 29 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt4
- brand in license text fixed

* Fri Apr 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt3
- more license tweaks (cas@)

* Fri Apr 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt2
- license tweaks

* Thu Apr 10 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- renamed to alt-notes-junior-sj

* Thu Dec 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- school licenses added

* Wed Sep 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial release
