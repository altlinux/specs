%define _keep_libtool_files 1
%define ruby 0

%define unstable 0
%define _optlevel s
%if %unstable
%define _optlevel 0
%endif

%define qtruby_docdir %_docdir/ruby-qt-%version
%define korundum_docdir %_docdir/ruby-korundum-%version
%add_findpackage_path %_K3bindir

Name: kdebindings
Version: 3.5.13
Release: alt1

Summary: bindings to KDE libraries for various programming languages 
Group: Graphical desktop/KDE
URL: http://www.kde.org
License: GPLv2 LGPL

Requires: perl-DCOP = %version-%release
%if %ruby
Requires: ruby-qt = %version-%release
Requires: ruby-korundum = %version-%release
%endif
Requires: kjsembed = %version-%release


Source0: %name-%version.tar
# ALT
Patch1: kdebindings-3.5.12-alt-fix-compile.patch
Patch2: kdebindings-3.5.12-alt-perl-ccflags.patch
#
Patch5: kdebindings-3.5.10-alt-ruby-getopts.patch
Patch6: kdebindings-3.5.12-alt-ruby-paths.patch
Patch7: kdebindings-3.5.10-alt-ruby-compile.patch

BuildRequires(pre): kdelibs-devel
BuildRequires: kdebase-devel libstdc++-devel gcc-c++ libjpeg-devel perl-devel libpng-devel
BuildRequires: xml-utils ruby libssl-devel libruby-devel

%description
This is the KDE bindings package.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.5
#
%description common
Common empty package for %name

%package devel
Summary: Devel stuff for kdepim
Group: Development/KDE and QT
Requires: %name-common = %version-%release
Requires: kdelibs-devel >= %{get_version kdelibs-devel}
%if %ruby
Requires: ruby-qt-doc = %version-%release
Requires: ruby-qt-devel = %version-%release
Requires: ruby-korundum-doc = %version-%release
%endif
Requires: kjsembed-devel = %version-%release
%description devel
Development files and headers for %name
%description devel -l ru_RU.UTF-8
Файлы для разработки приложений с %name

%package -n perl-DCOP
Summary: Perl module for DCOP
Summary(ru_RU.UTF-8): Модуль Perl для DCOP
Group: Development/Perl
Requires: %name-common = %version-%release
%description -n perl-DCOP
Perl module which allows to create DCOP clients and servers.
DCOP is a KDE protocol for programmatic access to
applications data and methods
%description -l ru_RU.UTF-8
Модуль Perl, позволяющий создавать клиентские и серверные приложения
DCOP. DCOP - это используемый в KDE протокол для программного доступа
к данным и методам приложений

%package -n ruby-qt
Summary: Qt bindings for Ruby
Summary(ru_RU.UTF-8): Расширение Ruby для использования библиотеки Qt
Group: Development/Ruby
Requires: %{get_dep libqt3}
Requires: %name-common = %version-%release
Provides: ruby-module-qt = %version-%release
Obsoletes: ruby-module-qt < %version-%release
%description -n ruby-qt
This package contains Ruby modules and service programs to create
applications with Qt GUI.
%description -n ruby-qt -l ru_RU.UTF-8
Данный пакет содержит модули языка Ruby и вспомогательные приложения,
которые позволяют создавать на Ruby приложения с графическим
интерфейсом, построенным на Qt.

%package -n ruby-qt-doc
Summary: Documentation and examples for Qt Ruby bindings
Summary(ru_RU.UTF-8): Документация и примеры к расширению Qt для Ruby
Group: Development/Ruby
Requires: %name-common = %version-%release
Provides: ruby-module-qt-doc = %version-%release
Obsoletes: ruby-module-qt-doc < %version-%release
%description -n ruby-qt-doc
Documentation and examples for Qt Ruby bindings
%description -n ruby-qt-doc -l ru_RU.UTF-8
Документация и примеры к расширению Qt для Ruby

%package -n ruby-qt-devel
Summary: Development files for ruby-qt
Group: Development/Ruby
#Requires: ruby-qt = %version-%release
Requires: %name-common = %version-%release
Provides: ruby-module-qt-devel = %version-%release
Obsoletes: ruby-module-qt-devel < %version-%release
%description -n ruby-qt-devel
This package contains utility files for ruby-qt package
%description -n ruby-qt-devel -l ru_RU.UTF-8
Этот пакет содержит утилиты для пакета ruby-qt

%package -n ruby-korundum
Summary: KDE bindings for Ruby
Summary(ru_RU.UTF-8): Расширение Ruby для использования библиотек KDE
Provides: korundum = %version-%release
Group: Development/Ruby
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %version-%release
Provides: ruby-module-korundum = %version-%release
Obsoletes: ruby-module-korundum < %version-%release
%description -n ruby-korundum
This package contains Ruby modules and service programs to create
applications built upon KDE interface and technologies.
with KDE GUI.
%description -n ruby-korundum -l ru_RU.UTF-8
Данный пакет содержит модули языка Ruby и вспомогательные приложения,
которые позволяют создавать на Ruby приложения с использованием интерфейса
и технологий среды KDE.

%package -n ruby-korundum-doc
Summary: Documentation and examples for Korundum
Summary(ru_RU.UTF-8): Документация и примеры для Korundum
Provides: korundum = %version-%release
Group: Development/Ruby
Requires: %name-common = %version-%release
Provides: ruby-module-korundum-doc = %version-%release
Obsoletes: ruby-module-korundum-doc < %version-%release
%description -n ruby-korundum-doc
Documentation and examples for Korundum
%description -n ruby-korundum -l ru_RU.UTF-8
Документация и примеры для Korundum

%package -n kjsembed-devel
Summary: Development files and headers for kjsembed
Summary(ru_RU.UTF-8): Заголовочные и другие файлы для разработки приложений с kjsembed
Group: Development/KDE and QT
Requires: %name-common = %version-%release
%description -n kjsembed-devel
Development files and headers for kjsembed
%description -n kjsembed-devel -l ru_RU.UTF-8
Заголовочные и другие файлы для разработки приложений с kjsembed

%package -n kjsembed
Summary: KJS Javascript command line interpreter and utilities
Summary(ru_RU.UTF-8): Интерпретатор Javascript KJS и вспомогательные приложения
Group: Graphical desktop/KDE
Requires: kdelibs >= %{get_version kdelibs}
Requires: %name-common = %version-%release
Provides: libkjsembed = %version-%release
Obsoletes: libkjsembed < %version-%release
%description -n kjsembed
KJS Javascript command line interpreter and utilities
%description -n kjsembed -l ru_RU.UTF-8
Интерпретатор Javascript KJS (версия для командной строки) и вспомогательные
приложения.

%prep
%setup -q
cp -ar altlinux/admin ./

%patch1 -p1
%patch2 -p1
#
##%if %ruby
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
##%endif

sed -i '\|\${kdeinit}_LDFLAGS[[:space:]]=[[:space:]].*-no-undefined|s|-no-undefined|-no-undefined -Wl,--warn-unresolved-symbols|' admin/am_edit
for f in `find $PWD -type f -name Makefile.am`
do
    sed -i -e '\|_la_LDFLAGS.*[[:space:]]-module[[:space:]]|s|-module|-module \$(KDE_PLUGIN)|' $f
    #sed -i -e '\|_la_LDFLAGS.*[[:space:]]-no-undefined|s|-no-undefined|-no-undefined -Wl,--allow-shlib-undefined|' $f
    grep -q -e 'lib.*SOURCES' $f || continue
    RPATH_LINK_OPTS+=" -Wl,-rpath-link,`dirname $f`/.libs"
done
sed -i "s|\(-Wl,--as-needed\)| $RPATH_LINK_OPTS \1|g" admin/acinclude.m4.in
sed -i -e 's|\$USER_INCLUDES|-I%_includedir/tqtinterface \$USER_INCLUDES|' admin/acinclude.m4.in

find ./ -type f -name Makefile.am | \
while read f
do
    sed -i -e 's|\(.*_la_LIBADD[[:space:]]*\)=\(.*\)|\1= -lkdefx -lDCOP -lkdesu -lkdeinit_kded \$(LIB_KPARTS) \$(LIB_KHTML) \$(LIB_KIO) \$(LIB_KDEUI) \$(LIB_KDECORE) \$(LIB_QT) \2|' $f
done

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common cvs ||:

%build
%add_optflags -I%_includedir/tqtinterface
export QTDIR=%_qt3dir
export KDEDIR=%prefix
DO_NOT_COMPILE="python dcoppython kdejava"
%if %ruby
%else
export DO_NOT_COMPILE+=" smoke qtruby korundum"
%endif
export DO_NOT_COMPILE
export PATH=$QTDIR/bin:%_K3bindir:$PATH \
%K3configure \
    --enable-closure \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
    --sysconfdir=%_sysconfdir \
    --without-java

# remove rpath
sed -i 's|LD_RUN_PATH=[^[:space:]][^[:space:]]*[[:space:]]||' dcopperl/Makefile
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool

%make

%check
cd dcopperl
perl -Mblib -MDCOP -e1

%install
%if %unstable
%set_strip_method none
%endif
%make DESTDIR=%buildroot INSTALLDIRS=vendor bindir=%_bindir datadir=%_K3datadir install

%if %ruby
mkdir -p %buildroot/%qtruby_docdir
cp -pr qtruby/{AUTHORS,ChangeLog,README,README.1st} %buildroot/%qtruby_docdir/
cp -pr qtruby/rubylib/tutorial %buildroot/%qtruby_docdir/
cp -pr qtruby/rubylib/examples %buildroot/%qtruby_docdir/
cp -pr qtruby/rubylib/designer/examples %buildroot/%qtruby_docdir/designer_examples
mkdir -p %buildroot/%korundum_docdir
cp -pr korundum/{AUTHORS,ChangeLog,README,TODO} %buildroot%korundum_docdir
cp -pr korundum/rubylib/{tutorials,examples,templates} %buildroot%korundum_docdir
mkdir -p %buildroot/%korundum_docdir/rbkconfig_compiler
cp -pr korundum/rubylib/rbkconfig_compiler/{autoexample.rb,exampleprefs_base.kcfgc,kcfg.xsd,example.rb,myoptions_base.ui,TODO,example.kcfg,general_base.ui,README.dox} \
	%buildroot/%korundum_docdir/rbkconfig_compiler
%endif

%files
%files common
%files devel

%files -n perl-DCOP
# doc files

%perl_vendor_archlib/DCOP*
%perl_vendor_autolib/DCOP

%if %ruby
%files -n ruby-qt
%docdir %qtruby_docdir
%qtruby_docdir/AUTHORS
%qtruby_docdir/ChangeLog
%qtruby_docdir/README
%qtruby_docdir/README.1st
%_bindir/rbuic
%_bindir/rbqtsh
%_bindir/rbqtapi
%_bindir/qtrubyinit
%_libdir/libsmokeqt.so.*
%ruby_sitearchdir/qtruby.so*
%ruby_sitearchdir/qui.so*
%ruby_sitelibdir/Qt*

%files -n ruby-qt-doc
%docdir %qtruby_docdir
%qtruby_docdir/tutorial
%qtruby_docdir/examples
%qtruby_docdir/designer_examples


%files -n ruby-qt-devel
%_K3includedir/smoke.h
%_libdir/libsmokeqt.so
%if %_keep_libtool_files
%_libdir/libsmokeqt.la
%endif

%files -n ruby-korundum
%docdir %korundum_docdir
%korundum_docdir/AUTHORS
%korundum_docdir/ChangeLog
%korundum_docdir/README
%korundum_docdir/TODO

%_bindir/rbkdesh
%_bindir/rbkdeapi
%_bindir/rbkconfig_compiler
%_bindir/krubyinit
%_libdir/libsmokekde.so.*
%ruby_sitearchdir/korundum.so*
%ruby_sitelibdir/Korundum.*
%ruby_sitelibdir/KDE

%files -n ruby-korundum-doc
%docdir %korundum_docdir
%korundum_docdir/tutorials
%korundum_docdir/examples
%korundum_docdir/templates
%korundum_docdir/rbkconfig_compiler
%endif

%files -n kjsembed-devel
%_libdir/libkjsembed.so
%_K3includedir/kjsembed
%if %_keep_libtool_files
%_libdir/libkjsembed.la
%endif

%files -n kjsembed
%doc kjsembed/README kjsembed/TODO
%_bindir/embedjs
#%_bindir/jsaccess
%_bindir/kjscmd

%_libdir/libkjsembed.so.*

%_K3xdg_apps/kjscmd.desktop
%_K3applnk/Utilities/embedjs.desktop
%_K3apps/embedjs
%_K3apps/kjsembed

%_man1dir/kjscmd.*

%_kde3_iconsdir/*/*/apps/embedjs.*

# Plugins
%_K3lib/libjavascript.so
%_K3lib/libjavascript.la
%_K3lib/lib*plugin.so
%_K3lib/lib*plugin.la
%_K3srv/*.desktop
%_K3srvtyp/*.desktop

# Kate plugin
%_K3apps/kate/scripts/*

%changelog
* Sun Jun 17 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Wed Feb 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.12-alt2.2
- Removed bad RPATH

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 3.5.12-alt2.1
- rebuilt for perl-5.14

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt2
- move to alternate place

* Fri Dec 24 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.12-alt1
- new version

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 3.5.10-alt3.1
- rebuilt with perl 5.12

* Wed Mar 03 2010 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt3
- fix to build with new autotools

* Wed Jul 01 2009 Sergey V Turchin <zerg@altlinux.org> 3.5.10-alt2
- fix to build with new automake
- rename ruby modules (ALT#16917)
- rebuild with ruby getopts removed (ALT#20651); thanx raorn@alt

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Wed Jul 04 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt2
- cleanup specfile

* Thu May 31 2007 Alexey Morozov <morozov@altlinux.org> 3.5.7-alt1
- new version (3.5.7)
- added few patches from kdebindings_3.5.7-1ubuntu2:
 * 028-make-cmdline.js-executable.diff (#22)
 * 029-ruby1.8-not-just-ruby.diff (#23)
 * 032_fix-kjscmd-manpage-typo (#24)
- updated and re-organized local patches. Now they are splitted more
  reasonably (##0-1 -> ##0-2) and renamed according their purposes

* Mon Feb 26 2007 Alexey Morozov <morozov@altlinux.org> 3.5.6-alt1
- New version (3.5.6)

* Mon Dec  4 2006 Alexey Morozov <morozov@altlinux.org> 3.5.5-alt1
- Initial build for ALT Linux


