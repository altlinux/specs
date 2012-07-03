%def_disable context
Name: tex4ht
Version: 1.0.2009_06_11_1038
Release: alt1

%define ht_scriptsdir %_datadir/%name

Summary: LaTeX and TeX for Hypertext
License: Latex Project Public License
Group: Publishing
Url: http://tug.org/tex4ht/
Packager: Kirill Maslinsky <kirill@altlinux.org>

#Source: http://www.cse.ohio-state.edu/~gurari/TeX4ht/fix/%name-all-%version.zip
Source: http://www.cse.ohio-state.edu/~gurari/TeX4ht/fix/%name-%version.tar
# man page from Debian package
Patch0: add_Makefile.diff
Patch1: add_java_manifest.diff
Patch2: add_manpage.diff
Patch3: add_scripts_sh.diff
#Patch4: fix_tex4ht_env.diff
Patch5: biblatex.4ht.diff

# alt patches
Patch10: alt_fix_mk4ht.diff

BuildRequires(Pre): /proc rpm-build-java rpm-build-texmf
BuildRequires: libkpathsea-devel
BuildRequires: java-devel-default
BuildRequires: fastjar

Requires: texmf-%name = %version-%release
# for oolatex
Requires: java zip
# for image processing
# skip for now, dvipng uninstallable with texlive
#Requires: dvipng
Requires: /usr/bin/convert

%description
TeX4ht is a highly configurable TeX-based authoring system dedicated mainly to
produce hypertext. It interacts with TeX-based applications through style files
and postprocessors, leaving the processing of the source files to the native
TeX compiler. Consequently, TeX4ht can handle the features of TeX-based systems
in general, and of the LaTeX and AMS style files in particular.

Pre-tailored configurations are offered for different output formats, including
(X)HTML, MathML, OpenDocument, and DocBook.

There are a number of different ways to convert glyphs and graphics in the DVI
files into PNG, GIF or JPEG. The default is to use dvipng. Alternatives using
ghostscript, imagemagick, netpbm and/or pstoedit are also possible.

This package contains the architecture dependent part for TeX4ht.

%package -n texmf-%name
Summary: TeX4ht texmf files
Group: Publishing
BuildArch: noarch

%description -n texmf-%name
TeX4ht is a highly configurable TeX-based authoring system dedicated mainly to
produce hypertext. It interacts with TeX-based applications through style files
and postprocessors, leaving the processing of the source files to the native
TeX compiler. Consequently, TeX4ht can handle the features of TeX-based systems
in general, and of the LaTeX and AMS style files in particular.

Pre-tailored configurations are offered for different output formats, including
(X)HTML, MathML, OpenDocument, and DocBook.

There are a number of different ways to convert glyphs and graphics in the DVI
files into PNG, GIF or JPEG. The default is to use dvipng. Alternatives using
ghostscript, imagemagick, netpbm and/or pstoedit are also possible.

This package contains files installed along with TeX4ht in texmf tree.

%if_enabled context
%package context
Summary: TeX4ht scripts for ConTeXt
Group: Publishing
BuildArch: noarch

%description context
TeX4ht is a highly configurable TeX-based authoring system dedicated mainly to
produce hypertext. It interacts with TeX-based applications through style files
and postprocessors, leaving the processing of the source files to the native
TeX compiler. Consequently, TeX4ht can handle the features of TeX-based systems
in general, and of the LaTeX and AMS style files in particular.

Pre-tailored configurations are offered for different output formats, including
(X)HTML, MathML, OpenDocument, and DocBook.

There are a number of different ways to convert glyphs and graphics in the DVI
files into PNG, GIF or JPEG. The default is to use dvipng. Alternatives using
ghostscript, imagemagick, netpbm and/or pstoedit are also possible.

This package contains scripts to use with ConTeXt.
%endif

%package xetex
Summary: TeX4ht scripts for XeTeX
Group: Publishing
BuildArch: noarch

%description xetex
TeX4ht is a highly configurable TeX-based authoring system dedicated mainly to
produce hypertext. It interacts with TeX-based applications through style files
and postprocessors, leaving the processing of the source files to the native
TeX compiler. Consequently, TeX4ht can handle the features of TeX-based systems
in general, and of the LaTeX and AMS style files in particular.

Pre-tailored configurations are offered for different output formats, including
(X)HTML, MathML, OpenDocument, and DocBook.

There are a number of different ways to convert glyphs and graphics in the DVI
files into PNG, GIF or JPEG. The default is to use dvipng. Alternatives using
ghostscript, imagemagick, netpbm and/or pstoedit are also possible.

This package contains scripts to use with XeTeX.

%prep
%setup -q
find . -name "*.jar" -exec rm -f {} \;
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch10 -p2


%build
cd src
mkdir -p class
%make_build JAVAC=%javac

sed -i 's,[^ ]\+/tex4ht.jar,%_javadir/tex4ht.jar,g' tex4ht.env
sed -i 's,[^ ]\+/xtpipes/,%_texmfmain/tex4ht/xtpipes/,g' tex4ht.env

%install
cd src
%makeinstall DESTDIR=%buildroot
install -m 755 -d %buildroot%_javadir
mv %buildroot%ht_scriptsdir/*.jar %buildroot%_javadir

mkdir -p %buildroot%_texmfmain/tex4ht/base
ln -s %_sysconfdir/tex4ht/tex4ht.env %buildroot%_texmfmain/tex4ht/base/tex4ht.env

find %buildroot%_texmfmain/ -type f -exec chmod 644 {} \;

%files
%_sysconfdir/tex4ht
%_bindir/*
%ht_scriptsdir
%exclude %ht_scriptsdir/*context
%exclude %ht_scriptsdir/*xetex
%exclude %ht_scriptsdir/*xelatex
%_man1dir/*
%_texmfmain/%name/base/tex4ht.env

%files -n texmf-%name
%_texmfmain/tex/generic/%name
%_texmfmain/%name
%exclude %_texmfmain/%name/base/tex4ht.env
%_javadir/*.jar

%if_enabled context
%files context
%ht_scriptsdir/*context
%endif

%files xetex
%ht_scriptsdir/*xetex
%ht_scriptsdir/*xelatex

%changelog
* Sat Feb 04 2012 Kirill Maslinsky <kirill@altlinux.org> 1.0.2009_06_11_1038-alt1
- update 1.0.2009_06_11_1038 (last Eitan's release)
- drop context subpackage due to tetex dependency
- apply texlive's bibatex.4ht patch (borrowed from debian)

* Thu May 14 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0.2009_05_02_1757-alt3.2
- fixes for packaging mistakes introduced overnight

* Thu May 14 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0.2009_05_02_1757-alt3.1
- drop dvipng dependency for now

* Wed May 13 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0.2009_05_02_1757-alt3
- switch to debian packaging scheme
  + apply relevant debian patches
  + move auxiliary scripts into /usr/share/tex4ht/
    this helps to avoid filename conflicts with dblatex and others
- build with rpm-build-texmf
  + texmf-tex4ht now provides texmf(latex/tex4ht)

* Tue May 05 2009 Kirill Maslinsky <kirill@altlinux.org> 1.0.2009_05_02_1757-alt2
- tex4ht-context now explicitly requires tetex-latex 
  (workaround for apt, thanks at@ for suggestion)
- please note, that texht-context currently couldn't be installed 
  along with tex4ht-xetex due to tetex/texlive conflict.

* Tue May 05 2009 Kirill Maslinsky <kirill@altlinux.ru> 1.0.2009_05_02_1757-alt1
- 1.0.2007_07_02_1327 -> 1.0.2009_05_02_1757
- package splitted into tex4ht, texmf-tex4ht, tex4ht-context, tex4ht-xetex
- built with libkpathsea.so.4 (texlive)

* Wed Jul 04 2007 Grigory Batalov <bga@altlinux.ru> 1.0.2007_07_02_1327-alt1
- New version.
- Build for ALT Linux.

* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2005_07_17_1932-2mdv2007.0
- %%mkrel

* Fri Jul 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2005_07_17_1932-1mdk
- new version
- fix script shellbangs

* Wed May 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2005_05_11_0314-2mdk
- fix font handling
- use a patch instead of perl substitution

* Wed May 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.2005_05_11_0314-1mdk
- initial mandriva release
