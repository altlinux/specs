Name: texlive-lang
Version: 2008.0
Release: alt0.14
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Language-specific macros, fonts, etc.
License: Distributable
Group: Publishing
Url: http://tug.org/texlive/

Source0: %name-texmf-%version-%release.tar
Source1: %name-texmf-dist-%version-%release.tar
Source2: %name-alt-%version.tar

BuildArch: noarch

BuildRequires: tex-common texlive-common
BuildRequires(pre): rpm-build-texmf
BuildRequires: less vim-console rpm-utils automake autoconf

%set_compress_method none

# don't check documentation and sources
%add_findreq_skiplist %_datadir/texmf/doc/*
%add_findreq_skiplist %_datadir/texmf-texlive/doc/*
%add_findreq_skiplist %_datadir/texmf/source/*
%add_findreq_skiplist %_datadir/texmf-texlive/source/*

# texlive-lang-arab
#_datadir/texmf-texlive/tex/latex/arabtex/kashmiri.tex
%add_texmf_req_skip latex/kashmiri

# texlive-lang-cyrillic
#_datadir/texmf-texlive/tex/latex/cmcyralt/russian.sty
%add_texmf_req_skip latex/cmcyr
#_datadir/texmf-texlive/tex/latex/disser/disser.cls
#_datadir/texmf-texlive/tex/latex/eskd/eskd.cls
%add_texmf_req_skip latex/pscyr

# texlive-lang-czechslovak
#_datadir/texmf-texlive/tex/latex/csbulletin/csbulletin.cls
%add_texmf_req_skip latex/SpecChar
%add_texmf_req_skip latex/csbulobalka
%add_texmf_req_skip latex/csbulutf8

%description
(none)

%package -n texlive-lang-african
Group: Publishing
Summary: African scripts
Requires: texlive-base

%description -n texlive-lang-african
Fonts for typesetting some African scripts

%package -n texlive-lang-arab
Group: Publishing
Summary: Arabic
Requires: texlive-base

%description -n texlive-lang-arab
Fonts and support for typesetting Arabic

%package -n texlive-lang-armenian
Group: Publishing
Summary: Armenian
Requires: texlive-base

%description -n texlive-lang-armenian
Essential armenian

%package -n texlive-lang-cjk
Group: Publishing
Summary: Chinese, Japanese, Korean
Requires: texlive-base, texlive-base-bin, texlive-doc-zh

%description -n texlive-lang-cjk
CJK (Chinese, Japanese, Korean) macros, fonts, documentation.

%package -n texlive-lang-croatian
Group: Publishing
Summary: Croatian
Requires: texlive-base

%description -n texlive-lang-croatian
Essential croatian

%package -n texlive-lang-cyrillic
Group: Publishing
Summary: Cyrillic
Requires: texlive-base, texlive-base-bin

%description -n texlive-lang-cyrillic
Fonts and macro packages to typeset Cyrillic texts.

%package -n texlive-lang-czechslovak
Group: Publishing
Summary: Czech/Slovak
Requires: texlive-base, texlive-base-bin, texlive-latex-base

%description -n texlive-lang-czechslovak
Czech/Slovak packages and hyphenation support.

%package -n texlive-lang-danish
Group: Publishing
Summary: Danish
Requires: texlive-base

%description -n texlive-lang-danish
Essential Danish

%package -n texlive-lang-dutch
Group: Publishing
Summary: Dutch
Requires: texlive-base

%description -n texlive-lang-dutch
Essential Dutch

%package -n texlive-lang-finnish
Group: Publishing
Summary: Finnish
Requires: texlive-base

%description -n texlive-lang-finnish
Essential finnish

%package -n texlive-lang-french
Group: Publishing
Summary: French
Requires: texlive-base

%description -n texlive-lang-french
Packages and hyphenation support for French.

%package -n texlive-lang-german
Group: Publishing
Summary: German
Requires: texlive-base

%description -n texlive-lang-german
Essential German

%package -n texlive-lang-greek
Group: Publishing
Summary: Greek
Requires: texlive-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-lang-greek
Fonts and support for typesetting Greek

%package -n texlive-lang-hebrew
Group: Publishing
Summary: Hebrew
Requires: texlive-base

%description -n texlive-lang-hebrew
Fonts and support for typesetting Hebrew

%package -n texlive-lang-hungarian
Group: Publishing
Summary: Hungarian
Requires: texlive-base
# file conflicts
Conflicts: tetex-core

%description -n texlive-lang-hungarian
Essential Hungarian

%package -n texlive-lang-italian
Group: Publishing
Summary: Italian
Requires: texlive-base

%description -n texlive-lang-italian
(none)

%package -n texlive-lang-latin
Group: Publishing
Summary: Latin
Requires: texlive-base

%description -n texlive-lang-latin
Essential Latin

%package -n texlive-lang-mongolian
Group: Publishing
Summary: Mongolian
Requires: texlive-base

%description -n texlive-lang-mongolian
Support for Mongolian.

%package -n texlive-lang-norwegian
Group: Publishing
Summary: Norwegian
Requires: texlive-base

%description -n texlive-lang-norwegian
Essential Norwegian

%package -n texlive-lang-other
Group: Publishing
Summary: Other hyphenation files
Requires: texlive-base

%description -n texlive-lang-other
Hyphenation patterns for languages with no other support.

%package -n texlive-lang-polish
Group: Publishing
Summary: Polish
Requires: texlive-base-bin, texlive-latex-base

%description -n texlive-lang-polish
Pick this if you want Polish fonts and other packages

%package -n texlive-lang-portuguese
Group: Publishing
Summary: Portuguese
Requires: texlive-base

%description -n texlive-lang-portuguese
(none)

%package -n texlive-lang-spanish
Group: Publishing
Summary: Spanish
Requires: texlive-base

%description -n texlive-lang-spanish
(none)

%package -n texlive-lang-swedish
Group: Publishing
Summary: Swedish
Requires: texlive-base

%description -n texlive-lang-swedish
Essential swedish

%package -n texlive-lang-tibetan
Group: Publishing
Summary: Tibetan
Requires: texlive-base

%description -n texlive-lang-tibetan
Fonts and support for typesetting Tibetan

%package -n texlive-lang-ukenglish
Group: Publishing
Summary: UK English
Requires: texlive-base

%description -n texlive-lang-ukenglish
Essential UK English

%package -n texlive-lang-vietnamese
Group: Publishing
Summary: Vietnamese
Requires: texlive-base

%description -n texlive-lang-vietnamese
Vietnamese support

%prep
%setup -c -T -a2
sed -i -e 's,coding.bak$,coding,g' \
	alt-linux/texlive-lang-cyrillic.files

%install
mkdir -p %buildroot/%_datadir
tar xf %SOURCE0 -C %buildroot/%_datadir/
tar xf %SOURCE1 -C %buildroot/%_datadir/

mkdir -p %buildroot/%_sysconfdir/texmf/{updmap.d,language.d}
cp alt-linux/*.cfg %buildroot/%_sysconfdir/texmf/updmap.d/
cp alt-linux/*.{dat,def} %buildroot/%_sysconfdir/texmf/language.d/

(cd %buildroot/%_datadir/texmf-dist/doc/fonts/cmcyr/;
 mv coding.bak coding)

mv %buildroot/%_datadir/texmf-dist %buildroot/%_datadir/texmf-texlive

mkdir -p %buildroot/%_sysconfdir/texmf/fmt.d
mkdir -p %buildroot/%_datadir/texmf-texlive/tex
mkdir -p %buildroot/%_datadir/texmf-texlive/tex/xelatex
mkdir -p %buildroot/%_datadir/texmf-texlive/tex/xelatex/cjk
mv %buildroot/%_datadir/texmf-texlive/tex/latex/cjk/xCJK.sty %buildroot/%_datadir/texmf-texlive/tex/xelatex/cjk/xCJK.sty
ln -s ../fmtutil/format.cyramstex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-cyrillic-cyramstex.cnf
ln -s ../fmtutil/format.cyrtex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-cyrillic-cyrtex.cnf
ln -s ../fmtutil/format.cyrtexinfo.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-cyrillic-cyrtexinfo.cnf
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/plain
mkdir -p %buildroot/%_sysconfdir/texmf/tex/plain/cyrplain
mv %buildroot/%_datadir/texmf-texlive/tex/plain/cyrplain/cyramstx.ini %buildroot/%_sysconfdir/texmf/tex/plain/cyrplain/cyramstx.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/cyrplain/cyrblue.ini %buildroot/%_sysconfdir/texmf/tex/plain/cyrplain/cyrblue.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/cyrplain/cyrtex.cfg %buildroot/%_sysconfdir/texmf/tex/plain/cyrplain/cyrtex.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/plain/cyrplain/cyrtex.ini %buildroot/%_sysconfdir/texmf/tex/plain/cyrplain/cyrtex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/plain/cyrplain/cyrtxinf.ini %buildroot/%_sysconfdir/texmf/tex/plain/cyrplain/cyrtxinf.ini
ln -s ../fmtutil/format.csplain.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-czechslovak-csplain.cnf
ln -s ../fmtutil/format.cslatex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-czechslovak-cslatex.cnf
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/cslatex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/cslatex/base
mkdir -p %buildroot/%_sysconfdir/texmf/tex/csplain
mkdir -p %buildroot/%_sysconfdir/texmf/tex/csplain/base
mv %buildroot/%_datadir/texmf-texlive/tex/cslatex/base/cslatex-utf8.ini %buildroot/%_sysconfdir/texmf/tex/cslatex/base/cslatex-utf8.ini
mv %buildroot/%_datadir/texmf-texlive/tex/cslatex/base/cslatex.ini %buildroot/%_sysconfdir/texmf/tex/cslatex/base/cslatex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/cslatex/base/fonttext.cfg %buildroot/%_sysconfdir/texmf/tex/cslatex/base/fonttext.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/cslatex/base/hyphen.cfg %buildroot/%_sysconfdir/texmf/tex/cslatex/base/hyphen.cfg
mv %buildroot/%_datadir/texmf-texlive/tex/csplain/base/cseplain.ini %buildroot/%_sysconfdir/texmf/tex/csplain/base/cseplain.ini
mv %buildroot/%_datadir/texmf-texlive/tex/csplain/base/csplain-utf8.ini %buildroot/%_sysconfdir/texmf/tex/csplain/base/csplain-utf8.ini
mv %buildroot/%_datadir/texmf-texlive/tex/csplain/base/csplain.ini %buildroot/%_sysconfdir/texmf/tex/csplain/base/csplain.ini
mv %buildroot/%_datadir/texmf/fmtutil/format.cslatex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.cslatex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.csplain.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.csplain.cnf
ln -s ../fmtutil/format.mex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-polish-mex.cnf
ln -s ../fmtutil/format.utf8mex.cnf %buildroot%_sysconfdir/texmf/fmt.d/10-texlive-lang-polish-utf8mex.cnf
mkdir -p %buildroot/%_sysconfdir/texmf
mkdir -p %buildroot/%_sysconfdir/texmf/fmtutil
mkdir -p %buildroot/%_sysconfdir/texmf/tex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/mex
mkdir -p %buildroot/%_sysconfdir/texmf/tex/mex/config
mkdir -p %buildroot/%_sysconfdir/texmf/tex/mex/utf8mex
mv %buildroot/%_datadir/texmf-texlive/tex/mex/config/mex.ini %buildroot/%_sysconfdir/texmf/tex/mex/config/mex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/mex/config/pdfmex.ini %buildroot/%_sysconfdir/texmf/tex/mex/config/pdfmex.ini
mv %buildroot/%_datadir/texmf-texlive/tex/mex/utf8mex/utf8mex.ini %buildroot/%_sysconfdir/texmf/tex/mex/utf8mex/utf8mex.ini
mv %buildroot/%_datadir/texmf/fmtutil/format.mex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.mex.cnf
mv %buildroot/%_datadir/texmf/fmtutil/format.utf8mex.cnf %buildroot/%_sysconfdir/texmf/fmtutil/format.utf8mex.cnf

%files -n texlive-lang-african -f alt-linux/texlive-lang-african.files

%files -n texlive-lang-arab -f alt-linux/texlive-lang-arab.files

%files -n texlive-lang-armenian -f alt-linux/texlive-lang-armenian.files

%files -n texlive-lang-cjk -f alt-linux/texlive-lang-cjk.files

%files -n texlive-lang-croatian -f alt-linux/texlive-lang-croatian.files

%files -n texlive-lang-cyrillic -f alt-linux/texlive-lang-cyrillic.files

%files -n texlive-lang-czechslovak -f alt-linux/texlive-lang-czechslovak.files

%files -n texlive-lang-danish -f alt-linux/texlive-lang-danish.files

%files -n texlive-lang-dutch -f alt-linux/texlive-lang-dutch.files

%files -n texlive-lang-finnish -f alt-linux/texlive-lang-finnish.files

%files -n texlive-lang-french -f alt-linux/texlive-lang-french.files

%files -n texlive-lang-german -f alt-linux/texlive-lang-german.files

%files -n texlive-lang-greek -f alt-linux/texlive-lang-greek.files

%files -n texlive-lang-hebrew -f alt-linux/texlive-lang-hebrew.files

%files -n texlive-lang-hungarian -f alt-linux/texlive-lang-hungarian.files

%files -n texlive-lang-italian -f alt-linux/texlive-lang-italian.files

%files -n texlive-lang-latin -f alt-linux/texlive-lang-latin.files

%files -n texlive-lang-mongolian -f alt-linux/texlive-lang-mongolian.files

%files -n texlive-lang-norwegian -f alt-linux/texlive-lang-norwegian.files

%files -n texlive-lang-other -f alt-linux/texlive-lang-other.files

%files -n texlive-lang-polish -f alt-linux/texlive-lang-polish.files

%files -n texlive-lang-portuguese -f alt-linux/texlive-lang-portuguese.files

%files -n texlive-lang-spanish -f alt-linux/texlive-lang-spanish.files

%files -n texlive-lang-swedish -f alt-linux/texlive-lang-swedish.files

%files -n texlive-lang-tibetan -f alt-linux/texlive-lang-tibetan.files

%files -n texlive-lang-ukenglish -f alt-linux/texlive-lang-ukenglish.files

%files -n texlive-lang-vietnamese -f alt-linux/texlive-lang-vietnamese.files

%changelog
* Tue Jul 28 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.14
- Remove dependencies from recommended packages to extra.

* Thu Jun 04 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.12
- Skip latex unmets.

* Thu Mar 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.10
- Re-arrange documentation
  + leave texmf/doc and texmf-texlive/doc untouched
  + move man1 and man5 pages to %%_mandir

* Thu Feb 26 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.9
- Add tex-common and texlive-common to BuildRequires.
- Set conflicts with tetex-* packages.

* Tue Feb 17 2009 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.7
- CJK (Chinese, Japanese, Korean) support was added.

* Tue Nov 25 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.5
- Move bin-cyrillic to texlive-base-bin.
- Move bin-vlna.i386-linux to texlive-base-bin.

* Fri Oct 31 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.4
- Sources repacked.

* Wed Oct 08 2008 Grigory Batalov <bga@altlinux.ru> 2008.0-alt0.1
- Initial build for ALT Linux.
