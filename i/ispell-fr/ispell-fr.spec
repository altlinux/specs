%define src_ver		1.0
%define languagelocal	francais
%define languageeng	french
%define languagecode	fr

Summary: French files for ispell
Summary(fr): Dictionnaire français pour ispell
Name: ispell-%{languagecode} 
Epoch:1
Version: 1.0
Release: alt1

Packager: Igor Vlasenko <viy@altlinux.ru>

Url: http://www.unil.ch/ling/cp/frgut.html
Source:	http://www.unil.ch/ling/cp/Francais-GUTenberg-v%{src_ver}.tar.bz2
License: GPL
Group: System/Internationalization

# Can't be noarch due to the byte order
#BuildArch: noarch
Autoreqprov: no

Requires: ispell
# the binary format changed with ispell 3.2.06
PreReq: ispell >= 3.2.06-2mdk
Provides: ispell-dictionary
BuildRequires: ispell

Obsoletes: ispell-francais-IREQ, ispell-french, ispell-francais
Obsoletes: ifrench

%description
ispell-fr is spelling data in French to be used by ispell program.
With this extension, you can compose a document in French and check
for the typos easily.

Ispell can be used directly from command line to check a file;
or used by several text dealing programs, like LyX, etc.

%description -l fr
Ceci est le dictionnaire français pour le correcteur
orthographique interactif de GNU ispell.

%prep
%setup -n Francais-GUTenberg-v%src_ver
# answer "oui" (yes) 10 times.
echo -e "o\no\no\no\no\no\no\no\no\no\n" | ./makehash
mv -f francais.dico %languagelocal.hash

%build
%install
mkdir -p $RPM_BUILD_ROOT%_libdir/ispell

install -m 644 %languagelocal.aff $RPM_BUILD_ROOT%_libdir/ispell/%languagelocal.aff
install -m 644 %languagelocal.hash $RPM_BUILD_ROOT%_libdir/ispell/%languagelocal.hash

# LaTeX babel
if [ "%languagelocal" != "%languageeng" ];then
 cd $RPM_BUILD_ROOT%_libdir/ispell
 ln -s %languagelocal.aff %languageeng.aff
 ln -s %languagelocal.hash %languageeng.hash
fi

%post
cd %_libdir/ispell
mv -f %languagelocal.hash %languagelocal.ispell
buildhash %languagelocal.ispell %languagelocal.aff %languagelocal.hash &> /dev/null
rm -f %languagelocal.ispell.stat %languagelocal.ispell.cnt %languagelocal.ispell

%files
%doc ALIRE HISTORIQUE docs/*.* utils
%_libdir/ispell/*

%changelog
* Fri Mar 07 2008 Igor Vlasenko <viy@altlinux.ru> 1:1.0-alt1
- epoch :1 due to rename ipl15mdk -> alt1

* Sat Aug 20 2005 Igor Vlasenko <viy@altlinux.ru> 1.0-ipl15mdk
- fixed #7663 (rebuild with new ispell); 
- sync with 1.0-15mdk; 
- removed noarch due to byte order

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-ipl12mdk
- rebuild

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Thu Oct 19 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0-10mdk
- BuilRequires: ispell

* Sat Aug 26 2000 Troels Liebe Bentsen <tlb@iname.com> 1.0-9mdk
- Small fix to the spec, no output on buildhash.

* Sun Aug 13 2000 Troels Liebe Bentsen <tlb@iname.com> 1.0-8mdk
- Cleaned up the spec and moved to standard template.

* Tue Jul 25 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-7mdk
- BM

* Thu Mar 30 2000 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-6mdk
- adapted to new Group: naming

* Wed Jan 12 2000 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Provides: ispell-dictionary

* Mon Dec 06 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- added Obsoletes: for easier installation over other rpms of same language
- changed the name to ispell-fr to standardize naming of ispell files

* Sat Nov 27 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- argh, another stupid symlink problem
- I alos made it obsoletes "ispell-french" (name used by Red Hat for the
  same package)

* Tue Nov 16 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- provided compatibility name 'french' (used by LaTeX/LyX)

* Fri Oct 22 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- fixed permissions problem of /usr/doc/%name

* Thu Oct 21 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- build with ispell-3.1.20-7mdk (which uses a MASKBITS of 64)
- First version for Mandrake.
