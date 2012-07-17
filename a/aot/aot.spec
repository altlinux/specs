#%set_verify_elf_skiplist %_libdir/libSynan.so.0.0.0 %_libdir/libEngSynan.so.0.0.0 %_libdir/libGerSynan.so.0.0.0

%def_disable static
Name: aot
Version: 1.80.1
Release: alt4.aot20090220.1

Summary: AOT project linguistic tools
License: LGPL
Group: Sciences/Other
Url: http://aot.ru

Packager: Kirill Maslinsky <kirill@altlinux.org>
Source: %name-%version.tar
Patch: aot-1.80.1-alt-DSO.patch

# Automatically added by buildreq on Sun Apr 08 2007
BuildRequires: bison flex gcc-c++ libpcrecpp-devel

Requires: lib%name = %version-%release, %name-utils = %version-%release
Provides: morph-lexicon = %version-%release

%description
AOT project (Avtomaticheskaya obrabotka teksta) is a collection of libraries,
dictionaries and utilities for Natural Language Processing, focused mainly on
Russian and German morphological analysis. It includes also tools for basic
syntactic analysis and morphology-aided corpus search engine (DDC). 

%package -n lib%name
Summary: AOT project shared libraries
Group: System/Libraries

%description -n lib%name
AOT project (Avtomaticheskaya obrabotka teksta) is a collection of libraries,
dictionaries and utilities for Natural Language Processing, focused mainly on
Russian and German morphological analysis. It includes also tools for basic
syntactic analysis and morphology-aided corpus search engine (DDC). 

This package contains shared libraries, used by various tools in AOT project.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Headers for building software that uses lib%name.

%if_enabled static
%package -n lib%name-devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Static libs for building statically linked software that uses %name
%endif

%package utils
Summary: AOT project utilities
Group: Sciences/Other
Requires: lib%name = %version-%release

%description utils
AOT project (Avtomaticheskaya obrabotka teksta) is a collection of libraries,
dictionaries and utilities for Natural Language Processing, focused mainly on
Russian and German morphological analysis. It includes also tools for basic
syntactic analysis and morphology-aided corpus search engine (DDC). 

This package contains small test utilities that show the use of AOT linguistic 
libraries.

NOTE that environment variable RML should be set to "/usr/share/aot" 
for utilities in this package to work.

%package -n ddc-concordance
Summary: Search engine for linguists
Group: Sciences/Other
Requires: lib%name = %version-%release, %name-dicts-graphan = %version-%release, %name-rus-morph = %version-%release, %name-ger-morph = %version-%release, %name-eng-morph = %version-%release 

%description -n ddc-concordance
This package contains DWDS/Dialing Concordance (DDC) - a collection of index 
and search tools for corpus linguists.

NOTE that environment variable RML should be set to "/usr/share/aot" 
for utilities in this package to work.

%package rus-morph
Summary: Russian morphologcal dictionary used by AOT project
Group: Sciences/Other
BuildArch: noarch

%description rus-morph
This package contains Russian morphological dictionary used by AOT project
in source and binary form.

%package ger-morph
Summary: German morphological dictionary user by AOT project 
Group: Sciences/Other
BuildArch: noarch

%description ger-morph
This package contains German morphological dictionary used by AOT project
in source and binary form.

Dictionary is based on Morphy project, see http://www-psycho.uni-paderborn.de/lezius

%package eng-morph
Summary: English morphological dictionary user by AOT project 
Group: Sciences/Other
BuildArch: noarch

%description eng-morph
This package contains English morphological dictionary used by AOT project
in source and binary form.

%package dicts-graphan
Summary: Dictionaries for graphematic analysis used by AOT project (rus, ger, eng)
Group: Sciences/Other
Provides: rus-graphan = %version-%release, ger-graphan = %version-%release
BuildArch: noarch

%description dicts-graphan
This package contains Russian and German dictionaries for graphematic analysis 
used by AOT project.


%package rus-syntax
Summary: Russian dictionaries for syntactic analysis 
Group: Sciences/Other
BuildArch: noarch

%description rus-syntax
This package contains Russian dictionaries for syntactic analysis used by AOT project.

%package ger-syntax
Summary: German dictionaries for syntactic analysis 
Group: Sciences/Other
BuildArch: noarch

%description ger-syntax
This package contains German dictionaries for syntactic analysis used by AOT project.


%prep
%setup -q
%patch -p1

%build
autoreconf -fisv
export lt_prog_compiler_static_works=no
%configure %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install
cp -r Dicts/SrcMorph %buildroot%_datadir/%name/Dicts/

# remove non-packaged files
rm -vf %_libdir/*.la

%files

%files -n lib%name
%doc AUTHORS ChangeLog NEWS README 
%dir %_datadir/aot
%dir %_datadir/aot/Bin
%_datadir/aot/Bin/rml.ini
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/aot/*/*.h

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files utils
%_bindir/GraphmatThick
%_bindir/MorphGen
%_bindir/StructDictLoader
%_bindir/SimpleGrammarPrecompiled
%_bindir/TestLem
%_bindir/FileLem
%_bindir/TestSynan
%_bindir/ConvertTrigramBinary
%_bindir/RusCorpusXmlConvertor
%_bindir/SynColloc
%_bindir/SynanDaemon


%files -n ddc-concordance
%doc Docs/DDCReadme.doc Docs/DDC_ChangeLog.txt Docs/DDC_Unix.txt
%_bindir/ConcordConsole
%_bindir/ConcordDaemon
%_bindir/ConcordIndex
%_bindir/ConcordSimple
%_bindir/ConcordStatis
%_bindir/ddc_xml
%_bindir/ddc_search
# these files disappeared from upstream
#%_datadir/aot/Bin/*.cfg
#%_datadir/aot/Bin/ddc_template.xml
#%_datadir/aot/Logs/concord/concord.dir

%files rus-morph
%doc Docs/Morph_UNIX.txt
%_datadir/aot/Dicts/Morph/Rus/*
%_datadir/aot/Dicts/Morph/rgramtab.tab
%_datadir/aot/Dicts/SrcMorph/RusSrc/morphs.mrd
%_datadir/aot/Dicts/SrcMorph/Rus.mwz

%files ger-morph
%_datadir/aot/Dicts/Morph/Ger/*
%_datadir/aot/Dicts/Morph/ggramtab.tab
%_datadir/aot/Dicts/SrcMorph/GerSrc/morphs.mrd
%_datadir/aot/Dicts/SrcMorph/Ger.mwz

%files eng-morph
%_datadir/aot/Dicts/Morph/Eng/*
%_datadir/aot/Dicts/Morph/egramtab.tab
%_datadir/aot/Dicts/SrcMorph/EngSrc/morphs.mrd
%_datadir/aot/Dicts/SrcMorph/Eng.mwz

%files dicts-graphan
%doc Docs/Graphan.htm Docs/GraphanReadmeRus.txt Docs/Graphan_Unix.txt
%_datadir/aot/Dicts/GraphAn/*
%_datadir/aot/Dicts/Obor/*
%_datadir/aot/Dicts/GerObor/*

%files rus-syntax
%doc Docs/HistoryOfSynan.htm Docs/Syntax_UNIX.txt
%_datadir/aot/Dicts/Ross/*
%_datadir/aot/Dicts/SynAn/*
%_datadir/aot/Dicts/Trigram/*
%_datadir/aot/Thes/Comp/StatThes/*
%_datadir/aot/Thes/Fin/StatThes/*
%_datadir/aot/Thes/Omni/StatThes/*
%_datadir/aot/Thes/Loc/StatThes/*

%files ger-syntax
%_datadir/aot/Dicts/GerSynan/*
%_datadir/aot/Dicts/SimpleGrammar/*

%changelog
* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.80.1-alt4.aot20090220.1
- Fixed build

* Mon May 25 2009 Kirill Maslinsky <kirill@altlinux.org> 1.80.1-alt4.aot20090220
- source and dictionaries updated to 2009/02/20 (from http://aot.ru)
- fixed build

* Thu Nov 13 2008 Kirill Maslinsky <kirill@altlinux.org> 1.80.1-alt3
- remove call to ldconfig from %%post*-scripts due to 
  post-transaction filetrigger in rpm-4.0.4-alt96.11

* Mon Oct 27 2008 Kirill Maslinsky <kirill@altlinux.org> 1.80.1-alt2
- fix build with gcc 4.3

* Wed Sep 17 2008 Kirill Maslinsky <kirill@altlinux.ru> 1.80.1-alt1
- version up (1.74.1 -> 1.80.1)
  + current dictionaries and utilities from aot.ru
  + current ddc-concordance from sourceforge
- fixes:
  + TestSynan should now work properly (fixed linking with circular dependent libs)
  + new utils added: SynanDaemon, SynColloc, ConcordStatis, RusCorpusXmlConvertor
  + fixed directory ownership (fixes build)
- packaging:
  + subpackages with dictionaries marked as noarch

* Wed Apr 18 2007 Kirill Maslinsky <kirill@altlinux.ru> 1.74.1-alt0.1
- initial build for Sisyphus (prerelease)
	+ this release is not thoroughly tested but seems to work in general
	+ some packaging decisions are definitely suboptimal (see BUGS and TODO)
	+ lacking documentation, especially package-specific
