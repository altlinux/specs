%define _unpackaged_files_terminate_build 1

%define oname netcdf
%define sover 19

Name: lib%oname
Version: 4.8.0
Release: alt1
Summary: Libraries to use the Unidata network Common Data Form (netCDF)
License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/software/netcdf/

# https://github.com/Unidata/netcdf-c.git
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: flex gcc-c++ gcc-fortran zlib-devel libhdf5-devel
BuildRequires: /usr/bin/tex libcurl-devel libexpat-devel doxygen graphviz

%description
NetCDF (network Common Data Form) is an interface for array-oriented
data access and a freely-distributed collection of software libraries
for C, Fortran, C++, and perl that provides an implementation of the
interface.
The netCDF library also defines a machine-independent format for
representing scientific data. Together, the interface, library, and
format support the creation, access, and sharing of scientific data. The
netCDF software was developed at the Unidata Program Center in Boulder,
Colorado.

NetCDF data is:

   o Self-Describing. A netCDF file includes information about the data
     it contains.

   o Network-transparent. A netCDF file is represented in a form that
     can be accessed by computers with different ways of storing
     integers, characters, and floating-point numbers.

   o Direct-access. A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding data.

   o Appendable. Data can be appended to a netCDF dataset along one
     dimension without copying the dataset or redefining its structure.
     The structure of a netCDF dataset can be changed, though this
     sometimes causes the dataset to be copied.

   o Sharable. One writer and multiple readers may simultaneously
     access the same netCDF file.

%description -l ru_RU.UTF-8
NetCDF (network Common Data Form) - это ориентированный на массивы
интерфейс для доступа к данным и, одновременно, свободно
распространяемая коллекция программ и библиотек для C, Fortran, C++,
которые реализуют этот интерфейс. Программы netCDF были
разработаны Гленом Дэвисом (Glenn Davis), Руссом Рью (Russ Rew),
Стивом Еммерсоном (Steve Emmerson), Джоном Кэроном (John Caron) и
Харвей Дэвисом (Harvey Davies) в Unidata Program Center в Боулдере,
Колорадо и расширены вкладами от других пользователей netCDF.
Библиотеки netCDF определяют машиннонезависимый  формат для
представления научных данных. Интерфейс, библиотеки и сам формат
поддерживают создание, доступ и совместное использование научных
данных.

%package -n %name%sover
Summary: Libraries to use the Unidata network Common Data Form (netCDF)
Group: System/Libraries

%description -n %name%sover
NetCDF (network Common Data Form) is an interface for array-oriented
data access and a freely-distributed collection of software libraries
for C, Fortran, C++, and perl that provides an implementation of the
interface.
The netCDF library also defines a machine-independent format for
representing scientific data. Together, the interface, library, and
format support the creation, access, and sharing of scientific data. The
netCDF software was developed at the Unidata Program Center in Boulder,
Colorado.

NetCDF data is:

   o Self-Describing. A netCDF file includes information about the data
     it contains.

   o Network-transparent. A netCDF file is represented in a form that
     can be accessed by computers with different ways of storing
     integers, characters, and floating-point numbers.

   o Direct-access. A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding data.

   o Appendable. Data can be appended to a netCDF dataset along one
     dimension without copying the dataset or redefining its structure.
     The structure of a netCDF dataset can be changed, though this
     sometimes causes the dataset to be copied.

   o Sharable. One writer and multiple readers may simultaneously
     access the same netCDF file.

%description -l ru_RU.UTF-8 -n %name%sover
NetCDF (network Common Data Form) - это ориентированный на массивы
интерфейс для доступа к данным и, одновременно, свободно
распространяемая коллекция программ и библиотек для C, Fortran, C++,
которые реализуют этот интерфейс. Программы netCDF были
разработаны Гленом Дэвисом (Glenn Davis), Руссом Рью (Russ Rew),
Стивом Еммерсоном (Steve Emmerson), Джоном Кэроном (John Caron) и
Харвей Дэвисом (Harvey Davies) в Unidata Program Center в Боулдере,
Колорадо и расширены вкладами от других пользователей netCDF.
Библиотеки netCDF определяют машиннонезависимый  формат для
представления научных данных. Интерфейс, библиотеки и сам формат
поддерживают создание, доступ и совместное использование научных
данных.

%package -n %oname-tools
Summary: NetCDF tools
Group: Development/Tools

%description -n %oname-tools
This package contains tools for work with NetCDF

%package devel
Summary: Development tools for the NetCDF library
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF
Group: Development/C
Provides: pkgconfig(netcdf) = %EVR

%description devel
This package contains the netCDF-3 header files, shared devel libs, and
man pages.

If you want to develop applications which will use the NetCDF library,
you'll need to install the %name-devel package.

%description -l ru_RU.UTF-8 devel
Заголовочные файлы и документация для использования библиотеки NetCDF
в приложениях.

Если вы собираетесь разрабатывать приложения, которые будут
использовать библиотеку NetCDF, вам необходимо установить пакет
%name-devel.

%package doc
Summary: Documentation for NetCDF
Summary(ru_RU.UTF-8): Документация по NetCDF
Group: Documentation
BuildArch: noarch

%description doc
Documentation for NetCDF library.

%description -l ru_RU.UTF-8 doc
Документация по NetCDF.

%prep
%setup

rm -fR udunits/expat

%build
%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	--enable-shared \
	--enable-static=no \
	--enable-netcdf-4 \
	--enable-doxygen \
	--enable-internal-docs \
	--enable-v2 \
	--enable-mmap \
	--disable-dap-remote-tests \
	--disable-filter-testing \
	%nil

%make

%install
%makeinstall_std

%files -n %name%sover
%doc COPYRIGHT
%doc README* RELEASE_NOTES*
%_libdir/*.so.%{sover}
%_libdir/*.so.%{sover}.*

%files devel
%_bindir/nc-config
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_man3dir/netcdf.3*

%files -n %oname-tools
%_bindir/*
%exclude %_bindir/nc-config
%_libdir/*.settings
%_man1dir/*

%files doc
%doc docs/html examples

%changelog
* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.0-alt1
- Updated to upstream version 4.8.0.
- Removed alternatives.
- Updated packaging scheme.

* Fri Sep 08 2017 Mikhail Gordeev <obirvalger@altlinux.org> 4.4.1.1-alt3
- (ALT#33843) Fix broken update

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1.1-alt2
- Split into separate package named libnetcdf11-seq.

* Thu Aug 24 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.1.1-alt1
- Updated to stable upstream version 4.4.1.1.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Wed Jul 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3
- Added Provides: pkgconfig(netcdf) = %EVR

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2
- Applied repocop patch

* Wed Jul 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1
- Version 4.3.0

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt3
- Rebuilt with new libhdf5

* Sat Sep 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt2
- Avoid conflict with man-pages

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt1.1
- Reenabled netCDF version 2 API

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt1
- Version 4.2.1.1

* Fri Jun 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt4
- Rebuilt

* Fri Mar 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt3
- Fixed flags in nc-config

* Thu Mar 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt2
- Fixed alternative for netcdf.pc (ALT #27049)
- Fixed Cflags in netcdf.pc

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt2
- Set %_libdir/libudunits2.so.* as %%ghost

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2
- Disabled devel-static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt8
- Fixed soname set-versions by ghost links (thnx ldv@)

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt7
- Rebuilt for soname set-versions

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt6
- Set NC_MAX_DIMS=65536 and NC_MAX_VARS=524288 for client software

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt5
- Set NC_MAX_DIMS=65536 and NC_MAX_VARS=524288

* Mon Jun 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt4.1
- Fixed bug when installing devel package

* Mon Jun 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt4
- Fixed bug when installing devel package (ALT #20510)

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3
- Created alternatives

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Added explicit conflicts with parallel version of libraries

* Tue Jun 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- Version 4.0.1

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- new version build based on Mandriva's srpm and obsoleted libnetcdf from ALT Linux Sisyphus

* Thu Aug 14 2008 Emmanuel Andry <eandry@mandriva.org> 4.0-1mdv2009.0
+ Revision: 271832
- New version
- fix license

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.6.3-1mdv2009.0
+ Revision: 232195
- 3.6.3
- added a patch from gentoo, though it won't help much
- use _disable_ld_as_needed and _disable_ld_no_undefined to make it build

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Thauvin <nanardon@mandriva.org>
    - unzip source in %%install instead %%check

* Sun Jan 20 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-4mdv2008.1
+ Revision: 155303
- fix devel static package name
- drop obsoletes

* Sat Jan 19 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-3mdv2008.1
+ Revision: 155130
- fix obsoletes

* Sat Jan 19 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-2mdv2008.1
+ Revision: 155081
- rebuild

* Thu Jan 03 2008 Emmanuel Andry <eandry@mandriva.org> 3.6.2-1mdv2008.1
+ Revision: 144107
- import netcdf

