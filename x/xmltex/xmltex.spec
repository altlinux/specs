Name: xmltex
Version: 1.8
Release: alt6
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: TeX-based XML parser
Group: Publishing
License:  LPPL

BuildRequires(pre): rpm-build-texmf
BuildArch: noarch

Source0: xmltex-%version.tar.gz

%description
xmltex: A non validating (and not 100%% conforming)
namespace aware XML parser implemented in TeX

%prep
%setup -q 

%install
mkdir -p %buildroot%_texmfmain/tex/%name
install -c -m644 *.xmt *.tex *.ini *.cfg *.x[ms]l %buildroot%_texmfmain/tex/%name/

mkdir -p %buildroot%_bindir
ln -s pdftex %buildroot%_bindir/xmltex
ln -s pdftex %buildroot%_bindir/pdfxmltex

mkdir -p %buildroot%_sysconfdir/texmf/{fmtutil,fmt.d}
ln -s ../fmtutil/format.%name.cnf %buildroot%_sysconfdir/texmf/fmt.d/20-%name.cnf
cat <<EOF >%buildroot%_sysconfdir/texmf/fmtutil/format.%name.cnf
# format	engine	pattern-file	arguments
xmltex		pdftex	language.dat	xmltex.ini
pdfxmltex	pdftex	language.dat	pdfxmltex.ini
EOF

%files 
%doc lppl.txt manual.html
%_texmfmain/tex/%name
%_bindir/*
%_sysconfdir/texmf/fmt.d/*
%_sysconfdir/texmf/fmtutil/*

%changelog
* Tue Oct 20 2009 Grigory Batalov <bga@altlinux.ru> 1.8-alt6
- Sources were updated from SuSE package 2007.8.1-23.
- Rebuilt with texlive.
- Specfile was cleaned up.
- Unnesessary texhash in %%post-script was removed.
- Formats (*.fmt) are built on install automatically.

* Fri Feb 14 2003 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.8-alt5
- buildreq fixed
- sisyphus check compatibility fixed
- passivetex dependance removed


* Fri Feb 14 2003 Anton V. Boyarshinov <boyarsh@altlunux.ru> 1.8-alt4
- Rebuild against tetex-2.0-alt1 (i knowing nothing about alt3)

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt2.2
- Fix interdependencies with passivetex (%name requires fotex.sty
  but passivetex requires name. Our requirement is stronger due
  xmltex executables, thus PreReq: on passivetex)

* Sun Nov 24 2002 Alexander Bokovoy <ab@altlinux.ru> 1.8-alt2.1
- Rebuild against tetex-2.0-alt0.5

* Mon Sep 02 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 1.8-alt2
- dependences fixed

* Tue Jun 25 2002 Anton V. Boyarshinov <boyarsh@altlunux.ru> 1.8-alt1
- first build
