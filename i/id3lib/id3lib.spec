Name: id3lib
Version: 3.8.3
Release: alt9

Summary: A software library for manipulating ID3v1 and ID3v2 tags
License: LGPL
Group: System/Libraries
Url: http://id3lib.sourceforge.net
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

Source: http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2
Patch1: %name-3.8.0-no_included_zlib.patch
Patch2: %name-3.8.2-doxygen.patch
Patch3: id3lib-3.8.3-libadd.patch
Patch4: id3lib-3.8.3-SA26536-fix.diff
Patch5: id3lib-3.8.3-gcc-4.3.patch

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

# Automatically added by buildreq on Wed Dec 03 2003
BuildRequires: doxygen gcc-c++ libstdc++-devel zlib-devel

Summary(ru_RU.CP1251): Библиотека для работы с тегами ID3v1 и ID3v2

%description
This package provides a software library for manipulating ID3v1 and ID3v2 tags.
It provides a convenient interface for software developers to include
standards-compliant ID3v1/2 tagging capabilities in their applications.
Features include identification of valid tags, automatic size conversions,
(re)synchronisation of tag frames, seamless tag (de)compression, and optional
padding facilities.

%description -l ru_RU.CP1251
Пакет содержит библиотеку для работы с тегами ID3v1 и ID3v2.
Разработчикам предоставляется удобный интерфейс, отвечающий
стандартам ID3v1/2, для использования библиотеки в приложениях.
Основными функциями являются проверка тегов, автоматическое преобразование
размера, синхронизация фреймов тегов и прозрачная (де)компрессия тегов.

%package utils
Summary: A set of small applications that use the id3lib library.
Group: Sound
Requires: %name = %version-%release

%description utils
This package contains simple applications that make use of
id3lib, a software library for ID3v1 and ID3v2 tag manipulation.

%description utils -l ru_RU.CP1251
В пакете находятся примеры программ, использующих библиотеку id3lib.

%package devel
Summary: Headers for developing programs that will use id3lib
Group: Development/C
PreReq: %name = %version-%release
Requires: libpopt-devel, libstdc++-devel, zlib-devel

%description devel
This package contains the headers and API documentation that programmers
will need to develop applications which will use id3lib, the software
library for ID3v1 and ID3v2 tag manipulation.

%description devel -l ru_RU.CP1251
В этом пакете находятся файлы и документация по API библиотеки,
необходимые для использования библиотеки id3lib в разработке приложений.

%package devel-static
Summary: Headers for developing programs that will use id3lib
Group: Development/C
PreReq: %name-devel = %version-%release

%description devel-static
This package contains development libraries required for packaging
statically linked software with id3lib.

%description devel-static -l ru_RU.CP1251
В этом пакете находятся статические библиотеки, необходимые
для разработки статических приложений, использующих id3lib.

%prep
%setup -q
rm -rfv zlib
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p1

%build
autoconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
export ac_cv_lib_z_uncompress=yes
%configure %{subst_enable static} 
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build
%make_build docs

gzip ChangeLog

%install
%makeinstall

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog.gz HISTORY NEWS README THANKS TODO

%files utils
%_bindir/*

%files devel
%_includedir/*
#_libdir/*.la
%_libdir/*.so
%doc doc/*.{html,png,jpg,gif,txt,ico,php,css} doc/api

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt9
- Fixed RPATH

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt8
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt7
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 3.8.3-alt6.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for id3lib
  * postun_ldconfig for id3lib

* Mon Oct 27 2008 Pavlov Konstantin <thresh@altlinux.ru> 3.8.3-alt6
- Fix FTBFS with gcc 4.3.

* Fri Sep 14 2007 Pavlov Konstantin <thresh@altlinux.ru> 3.8.3-alt5
- Fixed CVE-2007-4460 (SA26536):
  Insecure temporary file privilege escalation.

* Sat Jan 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 3.8.3-alt4
- Compressed ChangeLog (fixes #8976).

* Fri Jun 02 2006 Pavlov Konstantin <thresh@altlinux.ru> 3.8.3-alt3
- Fixed build.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.8.3-alt2.1
- Rebuilt with libstdc++.so.6.

* Wed Dec 03 2003 Alexey Tourbin <at@altlinux.ru> 3.8.3-alt2
- Do not package .la files.
- Do not package %name-devel-static by default.

* Fri Mar 07 2003 Andrey Astafiev <andrei@altlinux.ru> 3.8.3-alt1
- 3.8.3

* Mon Jan 13 2003 Andrey Astafiev <andrei@altlinux.ru> 3.8.2-alt1
- 3.8.2

* Wed Nov 13 2002 Andrey Astafiev <andrei@altlinux.ru> 3.8.1-alt1
- 3.8.1
- fixed build of api documentation.

* Tue Sep 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.8.0-alt3
- rebuilt with gcc-3.2 (%name-mdk-gcc3.2_cvs.patch)

* Mon Aug 12 2002 Andrey Astafiev <andrei@altlinux.ru> 3.8.0-alt2
- 3.8.0

* Fri Jul 12 2002 Andrey Astafiev <andrei@altlinux.ru> 3.8.0-alt1pre3
- 3.8.0pre3
- Library uses dynamically linked zlib.

* Mon May 27 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.8.0-alt0.9pre2.1
- 3.8.0pre2.1

* Thu Jan 10 2002 Yuri N. Sedunov <aris@altlinux.ru> 3.8.0-alt0.8pre2
- 3.8.0pre2.
- utils package.

* Wed Aug 15 2001 Andrey Astafiev <andrei@altlinux.ru> 3.7.13-alt1
- First version of RPM package
