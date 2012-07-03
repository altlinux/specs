Name: bbe
Version: 0.2.2
Release: alt5

Summary: Binary block editor
Group: Text tools
License: GPL
Url: http://sourceforge.net/projects/bbe-/

Source0: %name-%version.tar.gz

Patch0: bbe-0.1.9-alt-texinfo.patch

Packager: Igor Zubkov <icesik@altlinux.org>

%description
The bbe program is a sed-like editor for binary files. bbe performs basic
byte related transformations on blocks of input stream. bbe is
non-interactive command line tool and can be used as a part of a pipeline.
bbe makes only one pass over input stream.

bbe contains also grep-like features, like printing the filename, offset
and block number.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install DESTDIR=%buildroot htmldir=%_docdir/%name-%version/ install

install -p AUTHORS ChangeLog %buildroot%_docdir/%name-%version/

%files
%_bindir/bbe
%_man1dir/bbe.*
%_infodir/bbe.*
%dir %_docdir/bbe-%version
%doc %_docdir/%name-%version/*

%changelog
* Wed Dec 16 2009 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt5
- update Url

* Tue Aug 04 2009 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt4
- apply patch from repocop

* Thu Mar 26 2009 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt3
- fix repocop warning

* Sun Feb 18 2007 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt2
- update Url
- clean up build requires

* Tue Dec 12 2006 Igor Zubkov <icesik@altlinux.org> 0.2.2-alt1
- 0.1.9 -> 0.2.2
- buildreq

* Fri Jun 09 2006 Igor Zubkov <icesik@altlinux.ru> 0.1.9-alt2
- fix #8770

* Sat Mar 18 2006 Igor Zubkov <icesik@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Wed Nov 16 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Wed Nov 09 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Mon Nov 07 2005 Igor Zubkov <icesik@altlinux.ru> 0.1.6-alt1
- Initial build for Sisyphus
