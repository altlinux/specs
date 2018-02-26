Name: gettext-lint
Version: 0.4
Release: alt3.1

Summary: Gettext linting tools
License: GPL v2
URL: http://gettext-lint.sourceforge.net/
Source: %name/%name-%version.tar.gz
Group: Development/Other

BuildArch: noarch

Packager: Andrey Cherepanov <cas@altlinux.org> 

BuildRequires: python-devel

%description
The gettext lint tools are a collection of tools for checking the
validity, consistency and spelling of PO and POT files.
An experimental glossary building tool is also included.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
chmod +x %buildroot/%_datadir/%name/Glossary.py

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/POFileChecker
%_bindir/POFileClean
%_bindir/POFileConsistency
%_bindir/POFileEquiv
%_bindir/POFileFill
%_bindir/POFileGlossary
%_bindir/POFileSpell
%_bindir/POFileStatus
%_man1dir/POFileChecker.*
%_man1dir/POFileClean.*
%_man1dir/POFileConsistency.*
%_man1dir/POFileEquiv.*
%_man1dir/POFileFill.*
%_man1dir/POFileGlossary.*
%_man1dir/POFileSpell.*
%_man1dir/POFileStatus.*
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt3.1
- Rebuild with Python-2.7

* Thu Jun 10 2010 Andrey Cherepanov <cas@altlinux.org> 0.4-alt3
- fix DOS CR line ends
- return to Sisyphus

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 0.4-alt2
- don't use obsoletes macros in spec file
- buildreq

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 0.4-alt1
- build for Sisyphus


