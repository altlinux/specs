Name: kumir2
Version: 1.99.0.alpha7
Release: alt2

Summary: Kumir is a simple programming language and IDE for teaching programming
Summary(ru_RU.UTF-8): Кумир это простой язык программирования и среда разработки, применяемый при обучении

License: GPL
Group: Education
Url: http://lpm.org.ru/kumir
Packager: Denis Kirienko <dk@altlinux.ru>

BuildPreReq: libqt4-devel gcc-c++

Source: kumir2-svn224.tar.bz2

%description
Implementation of Kumir programming language, designed by academician
Ershov. It has very simple syntax, also known as "Russian algorithmical
language". Includes compiler, runtime, IDE and  modules "Robot", "Draw",
"Turtle" and some others.

This is a second generation of well-known Kumir system

%description -l ru_RU.UTF-8
Кумир - это учебный язык программирования, описанный в учебнике
А.Г.Кушниренко, и среда разработки. Он имеет простой синтаксис,
известный также как "русский алгоритмический язык". В состав среды также
входят канонические исполнители Робот, Чертежник, Черепаха и другие,
что делает Кумир очень удобным для начального обучения программированию.

Это вторая версия системы Кумир, пока находящаяся в стадии разработки.

%prep
%setup -n kumir2
find . -type f -name '*.pro' |while read f; do
echo >> $f
echo 'QMAKE_CXXFLAGS_RELEASE += %optflags' >> $f
done

%build
qmake-qt4
lrelease-qt4 share/kumir2/translations/*.ts
%make_build

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT/%{_prefix} install
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/kumir2/translations
cp share/kumir2/translations/*.qm $RPM_BUILD_ROOT/%{_prefix}/share/kumir2/translations/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/icons/
cp -R app_icons/linux/* $RPM_BUILD_ROOT/%{_datadir}/icons/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications/
cp *.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/

%package common
Summary: Shared libraries for various Kumir components
Requires: kumir2-libs
Group: Education

%description common
Contains kumir2 extension system skeleton and other libraries

%files common
%dir %{_libdir}/kumir2
%{_libdir}/kumir2/libAbstractSyntaxTree.so*
%{_libdir}/kumir2/libErrorMessages.so*
%{_libdir}/kumir2/libExtensionSystem.so*
%{_libdir}/kumir2/libBytecode.so*
%dir %{_libdir}/kumir2/plugins
%dir %{_datadir}/kumir2/icons
%{_datadir}/kumir2/icons/*
%dir %{_datadir}/kumir2/translations
%{_datadir}/kumir2/translations/AbstractSyntaxTree*.qm
#%{_datadir}/kumir2/translations/Bytecode*.qm
%{_datadir}/kumir2/translations/ErrorMessages*.qm
%{_datadir}/kumir2/translations/ExtensionSystem*.qm

%package module-KumirAnalizer
Summary:	Kumir language analizer
Provides:	kumir2-module-Analizer
Requires:	kumir2-common
Requires:	kumir2-module-st_funct
Group: Education

%description module-KumirAnalizer
Kumir language analizer

%files module-KumirAnalizer
%{_libdir}/kumir2/plugins/libKumirAnalizer.so
%{_libdir}/kumir2/plugins/KumirAnalizer.pluginspec
%dir %{_datadir}/kumir2/kumiranalizer
%{_datadir}/kumir2/kumiranalizer/*
%{_datadir}/kumir2/translations/KumirAnalizer*.qm

%package module-KumirNativeGenerator
Summary:	Kumir AST to native execuable translator
Provides:	kumir2-module-Generator
Requires:	kumir2-common
Group: Education

%description module-KumirNativeGenerator
Generator of execuables by Kumir language AST (via gcc toolchain)

%files module-KumirNativeGenerator
%{_libdir}/kumir2/plugins/libKumirNativeGenerator.so
%{_libdir}/kumir2/plugins/KumirNativeGenerator.pluginspec
%dir %{_datadir}/kumir2/kumirnativegenerator/
%{_datadir}/kumir2/kumirnativegenerator/*
%{_datadir}/kumir2/translations/KumirNativeGenerator*.qm


%package module-KumirCodeGenerator
Summary:	Kumir AST to execuable bytecode translator
Provides:	kumir2-module-Generator
Requires:	kumir2-common
Group: Education

%description module-KumirCodeGenerator
Generator of bytecode to be evaluated by Kumir VM

%files module-KumirCodeGenerator
%{_libdir}/kumir2/plugins/libKumirCodeGenerator.so
%{_libdir}/kumir2/plugins/KumirCodeGenerator.pluginspec
%{_datadir}/kumir2/translations/KumirCodeGenerator*.qm


%package module-KumirCompiler
Summary:	Kumir compiler toolchain module
Requires:	kumir2-common
Requires:	kumir2-module-KumirAnalizer
Requires:	kumir2-module-KumirNativeGenerator
Group: Education

%description module-KumirCompiler
Provides ability to compile Kumir programs

%files module-KumirCompiler
%{_libdir}/kumir2/plugins/libKumirCompiler.so
%{_libdir}/kumir2/plugins/KumirCompiler.pluginspec
%{_datadir}/kumir2/translations/KumirCompiler*.qm

%package module-KumirBCompiler
Summary:	Kumir bytecode compiler toolchain module
Requires:	kumir2-common
Requires:	kumir2-module-KumirAnalizer
Requires:	kumir2-module-KumirCodeGenerator
Group: Education

%description module-KumirBCompiler
Provides ability to bytecode-compile Kumir programs

%files module-KumirBCompiler
%{_libdir}/kumir2/plugins/libKumirBCompiler.so
%{_libdir}/kumir2/plugins/KumirBCompiler.pluginspec
%{_datadir}/kumir2/translations/KumirBCompiler*.qm

%package module-KumirCodeRun
Summary:	Kumir bytecode interpreter module
Requires:	kumir2-common
Requires:	kumir2-module-st_funct
Group: Education

%description module-KumirCodeRun
Intepreter of Kumir-2 bytecode

%files module-KumirCodeRun
%{_libdir}/kumir2/plugins/libKumirCodeRun.so
%{_libdir}/kumir2/plugins/KumirCodeRun.pluginspec
%{_datadir}/kumir2/translations/KumirCodeRun*.qm

%package libs
Summary:	Libraries required to run Kumir-compiled programs
Group: Education

%description libs
This package is required in order to distribute Kumir-compiled
programs without Kumir system itself.

%files libs
%{_libdir}/kumir2/libKumirStdLib.so*
#%{_libdir}/kumir2/libKumirGuiRunner.so*
%{_datadir}/kumir2/translations/KumirStdLib*.qm
#%{_datadir}/kumir2/translations/KumirGuiRunner*.qm

%package module-st_funct
Summary:	Kumir Standard Library
Requires:	kumir2-common
Requires:	kumir2-libs
Group: Education

%description module-st_funct
Standart library module

%files module-st_funct
%{_libdir}/kumir2/plugins/libst_funct.so
%{_libdir}/kumir2/plugins/st_funct.pluginspec
%{_datadir}/kumir2/translations/st_funct*.qm

%package module-Editor
Summary:	Kumir program editor
Requires:	kumir2-common
Requires:	kumir2-module-Analizer
Group: Education

%description module-Editor
Kumir program editor module

%files module-Editor
%{_libdir}/kumir2/plugins/libEditor.so
%{_libdir}/kumir2/plugins/Editor.pluginspec
%dir %{_datadir}/kumir2/editor
%{_datadir}/kumir2/editor/*
%{_datadir}/kumir2/translations/Editor*.qm


%package module-Browser
Summary:	Kumir Webkit browser
Requires:	kumir2-common
Group: Education

%description module-Browser
WebKit browser

%files module-Browser
%{_libdir}/kumir2/plugins/libBrowser.so
%{_libdir}/kumir2/plugins/Browser.pluginspec
%{_datadir}/kumir2/translations/Browser*.qm


%package module-CoreGUI
Summary:	GUI for Kumir
Requires:	kumir2-module-Analizer
Requires:	kumir2-module-Generator
Requires:	kumir2-module-Editor
Requires:	kumir2-module-Browser
Group: Education

%description module-CoreGUI
GUI for Kumir

%files module-CoreGUI
%{_libdir}/kumir2/plugins/libCoreGUI.so
%{_libdir}/kumir2/plugins/CoreGUI.pluginspec
%dir %{_datadir}/kumir2/coregui
%{_datadir}/kumir2/coregui/*
%{_datadir}/kumir2/translations/CoreGUI*.qm


%package utils-cc
Summary:	Kumir to native execuable compiler tool
Requires:	kumir2-common
Requires:	kumir2-module-KumirCompiler
Group: Education

%description utils-cc
A tool to compile kumir-programs into native execuables via gcc.
Run "kumir2-cc --help" for more information

%files utils-cc
%{_bindir}/kumir2-cc


%package utils-bc
Summary:	Kumir to portable bytecode execuable compiler tool
Requires:	kumir2-common
Requires:	kumir2-module-KumirBCompiler
Group: Education

%description utils-bc
A tool to compile kumir-programs into portable execuable bytecode
Run "kumir2-bc --help" for more information

%files utils-bc
%{_bindir}/kumir2-bc

%package utils-as
Summary:	Kumir bytecode (dis)assembler tool
Requires:	kumir2-common
Group: Education

%description utils-as
A tool to assemble/disassemble Kumir portable execuable bytecode
Run "kumir2-as --help" for more information

%files utils-as
%{_bindir}/kumir2-as

%package utils-run
Summary:	Kumir portable bytecode interpreter
Requires:	kumir2-common
Requires:	kumir2-module-KumirCodeRun
Requires:	kumir2-module-st_funct
Group: Education

%description utils-run
Standalone kumir programs launcher

%files utils-run
%{_bindir}/kumir2-run

%package professional
Summary:	Kumir Professional Edition
Requires:	kumir2-libs
Requires:	kumir2-module-CoreGUI
Requires:	kumir2-module-Editor
Requires:	kumir2-module-KumirAnalizer
Requires:	kumir2-module-KumirCodeGenerator
Requires:	kumir2-module-KumirCodeRun
Requires:	kumir2-module-KumirNativeGenerator
Requires:	kumir2-module-st_funct
Group: Education

%description professional
Kumir IDE for high school applications

%files professional
%{_bindir}/kumir2-ide
%{_datadir}/applications/kumir2-professional.desktop
%{_datadir}/icons/hicolor/*/apps/kumir2.*

%package standard
Summary:	Kumir Standard Edition
Requires:	kumir2-libs
Requires:	kumir2-module-CoreGUI
Requires:	kumir2-module-Editor
Requires:	kumir2-module-KumirAnalizer
Requires:	kumir2-module-KumirCodeGenerator
Requires:	kumir2-module-KumirCodeRun
Requires:	kumir2-module-st_funct
Group: Education

%description standard
Kumir IDE for school applications

%files standard
%{_bindir}/kumir2-classic
%{_datadir}/applications/kumir2-standard.desktop
%{_datadir}/icons/hicolor/*/apps/kumir2-classic.*

%package libs-painter
Summary:	Actor Painter runtime libraries
Requires:	kumir2-libs
Group: Education

%description libs-painter
Libraries required to distribute Kumir-compiled programs
using actor Painter

%files libs-painter
%{_libdir}/kumir2/libActorPainterC.so*
%{_datadir}/kumir2/translations/ActorPainterC_*.qm

%package actor-painter
Summary:	Actor Painter for Kumir
Requires:	kumir2-common
Requires:	kumir2-libs-painter
Group: Education

%description actor-painter
Actor Painter adds raster-painting feauteres for Kumir

%files actor-painter
%{_libdir}/kumir2/plugins/libActorPainter.so
%{_libdir}/kumir2/plugins/ActorPainter.pluginspec
%{_datadir}/kumir2/translations/ActorPainter_*.qm

%changelog
* Tue Mar 20 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.99.0.alpha7-alt2
- rebuilt with optflags

* Sat Aug 20 2011 Denis Kirienko <dk@altlinux.ru> 1.99.0.alpha7-alt1
- Initial build for Sisyphus - alpha-version, only for testing.

