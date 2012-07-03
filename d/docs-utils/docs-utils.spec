Name: docs-utils
Version: 0.0.3
Release: alt1

Buildarch: noarch

Summary: scripts to manage installed documentation
Group: System/Base
License: GPL

Packager: Kirill Maslinsky <kirill@altlinux.org>
Requires: alt-docs-main
Conflicts: rpm-build-docs < 0.4.1

Source: %name-%version.tar.bz2

%description
scripts to manage installed documentation

%prep
%setup -q

%install
%__mkdir_p %buildroot/%_bindir \
	    %buildroot/%_docdir/alt-docs/modules
%__cp bin/* %buildroot/%_bindir/

%files
%_bindir/*
%_docdir/alt-docs/modules

%changelog
* Thu Aug 02 2007 Kirill Maslinsky <kirill@altlinux.ru> 0.0.3-alt1
- fixed HTML syntax in generated docs modules index (closes #11996)

* Thu Dec 08 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.2-alt4.1
- rebuild with rpm-build-docs-0.4.5-alt7 .

* Mon Sep 05 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.0.2-alt4
dependency on alt-docs-main added

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.0.2-alt3
- bugfix

* Sun Jul 17 2005 Kirill Maslinsky <kirill@altlinux.ru> 0.0.2-alt2
- html encoding fixed

* Sat Jul 16 2005 Alexey Gladkov <legion@altlinux.ru> 0.0.2-alt1
- Change generation index.html;

* Tue Jun 14 2005 Alexey Gladkov <legion@altlinux.ru> 0.0.1-alt1
- First build for Sisyphus.

