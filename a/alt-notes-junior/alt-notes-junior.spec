Name: alt-notes-junior
Version: 0.2
Release: alt1

Summary: Junior distribution license and relnotes
License: Distributable
Group: Documentation

Source: %name-%version-%release.tar

Provides: alt-license-junior = %version-%release
Obsoletes: alt-license-junior
Conflicts: alt-notes-hpc

BuildArch: noarch

%description
Junior distribution license and release notes

%prep
%setup

%install
install -d %buildroot%_datadir/alt-notes
install -pm0644 *.html %buildroot/%_datadir/alt-notes/

%files
%_datadir/alt-notes/*

%changelog
* Wed Mar 12 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2-alt1
- renamed to alt-notes-junior

* Thu Dec 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt2
- school licenses added

* Wed Sep 19 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1-alt1
- Initial release
