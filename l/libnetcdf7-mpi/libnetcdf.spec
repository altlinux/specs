%define major 4
%define sover 6
%define oname netcdf
%define sname lib%oname
%define sover 7
%define c_sover 4
%define c4_sover 1
%define f_sover 5
%define priority 40

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: %sname%sover-mpi
Version: %major.1.3
Release: alt6

Summary: Parallel libraries to use the Unidata network Common Data Form (netCDF)

License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/packages/netcdf/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar
Source1: ftp://ftp.unidata.ucar.edu/pub/netcdf/guidec.pdf.bz2
Source2: ftp://ftp.unidata.ucar.edu/pub/netcdf/guidec.html.tar.bz2

Requires(post,preun): alternatives
Requires: libhdf5-mpi >= 1.8.3-alt5
%ifarch x86_64
Provides: %sname.so.%sover()(64bit)
%else
Provides: %sname.so.%sover
%endif
Provides: %sname-mpi = %version-%release
Conflicts: %sname-mpi < %version-%release
Obsoletes: %sname-mpi < %version-%release
Conflicts: %sname < 4.0.1-alt3

# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: flex gcc-c++ gcc-fortran %mpiimpl-devel

BuildPreReq: zlib-devel libsz2-devel libhdf5-mpi-devel /usr/bin/tex
BuildPreReq: libcurl-devel libexpat-devel chrpath

%description
NetCDF (network Common Data Form) is an interface for array-oriented data
access and a freely-distributed collection of software libraries for C,
Fortran, C++, and perl that provides an implementation of the interface.
The netCDF library also defines a machine-independent format for representing
scientific data. Together, the interface, library, and format support the
creation, access, and sharing of scientific data. The netCDF software was
developed at the Unidata Program Center in Boulder, Colorado.

NetCDF data is:

   o Self-Describing. A netCDF file includes information about the data it
     contains.

   o Network-transparent. A netCDF file is represented in a form that can be
     accessed by computers with different ways of storing integers, characters,
     and floating-point numbers.

   o Direct-access. A small subset of a large dataset may be accessed
     efficiently, without first reading through all the preceding data.

   o Appendable. Data can be appended to a netCDF dataset along one dimension
     without copying the dataset or redefining its structure. The structure of
     a netCDF dataset can be changed, though this sometimes causes the dataset
     to be copied.

   o Sharable. One writer and multiple readers may simultaneously access the
     same netCDF file.

This is parallel version of library.

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

Данный пакет содержит параллельную версию библиотеки.

%package -n %sname-cxx-%c_sover-mpi
Summary: Parallel NetCDF C++ library v3
Group: System/Libraries
Requires(post,preun): alternatives
Requires: %name = %version-%release
Provides: %sname-cxx-mpi = %version-%release
Conflicts: %sname-mpi < %version-%release
Obsoletes: %sname-mpi < %version-%release
Conflicts: %sname-cxx < 4.0.1-alt3

%description -n %sname-cxx-%c_sover-mpi
NetCDF (network Common Data Form) is an interface for array-oriented data
access and a freely-distributed collection of software libraries for C,
Fortran, C++, and perl that provides an implementation of the interface.
The netCDF library also defines a machine-independent format for representing
scientific data. Together, the interface, library, and format support the
creation, access, and sharing of scientific data. The netCDF software was
developed at the Unidata Program Center in Boulder, Colorado.

This package contains C++ interface library for parallel NetCDF version 3.

%description -n %sname-cxx-%c_sover-mpi -l ru_RU.UTF-8
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

Данный пакет содержит библиотеку C++ интерфейсов для NetCDF версии 3.

%package -n %sname-cxx4-%c4_sover-mpi
Summary: Parallel NetCDF C++ library v4
Group: System/Libraries
Requires(post,preun): alternatives
Requires: %name = %version-%release
Provides: %sname-cxx4-mpi = %version-%release
Conflicts: %sname-mpi < %version-%release
Obsoletes: %sname-mpi < %version-%release
Conflicts: %sname-cxx4 < 4.0.1-alt3

%description -n %sname-cxx4-%c4_sover-mpi
NetCDF (network Common Data Form) is an interface for array-oriented data
access and a freely-distributed collection of software libraries for C,
Fortran, C++, and perl that provides an implementation of the interface.
The netCDF library also defines a machine-independent format for representing
scientific data. Together, the interface, library, and format support the
creation, access, and sharing of scientific data. The netCDF software was
developed at the Unidata Program Center in Boulder, Colorado.

This package contains C++ interface library for parallel NetCDF version 4.

%description -l ru_RU.UTF-8 -n %sname-cxx4-%c4_sover-mpi
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

Данный пакет содержит библиотеку C++ интерфейсов для NetCDF версии 4.

%package -n %sname-fortran-%f_sover-mpi
Summary: Parallel NetCDF Fortran library
Group: System/Libraries
Requires(post,preun): alternatives
Requires: %name = %version-%release
Provides: %sname-fortran-mpi = %version-%release
Conflicts: %sname-mpi < %version-%release
Obsoletes: %sname-mpi < %version-%release
Conflicts: %sname-fortran < 4.0.1-alt3

%description -n %sname-fortran-%f_sover-mpi
NetCDF (network Common Data Form) is an interface for array-oriented data
access and a freely-distributed collection of software libraries for C,
Fortran, C++, and perl that provides an implementation of the interface.
The netCDF library also defines a machine-independent format for representing
scientific data. Together, the interface, library, and format support the
creation, access, and sharing of scientific data. The netCDF software was
developed at the Unidata Program Center in Boulder, Colorado.

This package contains Fortran interface library for parallel NetCDF.

%description -l ru_RU.UTF-8 -n %sname-fortran-%f_sover-mpi
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

Данный пакет содержит библиотеку Fortran интерфейсов для NetCDF версии 4.

%package -n %sname-mpi-devel
Summary: Development tools for the NetCDF library
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF
Group: Development/Other
Requires(post,preun): alternatives
Requires: %name = %version-%release
Requires: %sname-cxx-%c_sover-mpi = %version-%release
Requires: %sname-cxx4-%c4_sover-mpi = %version-%release
Requires: %sname-fortran-%f_sover-mpi = %version-%release
Conflicts: %sname-devel < 4.0.1-alt3

%description -n %sname-mpi-devel
This package contains the netCDF header files, shared devel libs, and
man pages.

If you want to develop applications which will use the NetCDF library,
you'll need to install the %name-devel package.  

%description -l ru_RU.UTF-8 -n %sname-mpi-devel
Заголовочные файлы и документация для использования библиотеки NetCDF
в приложениях.

Если вы собираетесь разрабатывать приложения, которые будут
использовать библиотеку NetCDF, вам необходимо установить пакет
%name-devel. 

%package -n %oname%sover-mpi-tools
Summary: NetCDF tools
Summary(ru_RU.UTF-8): Утилиты NetCDF
Group: Development/Tools
Requires(post,preun): alternatives
Requires: %name = %version-%release
Conflicts: %sname < 4.0.1-alt3
Conflicts: %sname-mpi < %version-%release
Obsoletes: %sname-mpi < %version-%release
Provides: %oname-mpi-tool = %version-%release

%description -n %oname%sover-mpi-tools
NetCDF tools.

%description -l ru_RU.UTF-8 -n %oname%sover-mpi-tools
Утилиты NetCDF.

%package -n %sname-mpi-devel-doc
Summary: Development documentation for the NetCDF library
Summary(ru_RU.UTF-8): Документация разработчика по библиотеке NetCDF
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release
Conflicts: %sname-mpi-devel < %version-%release
Conflicts: %sname-mpi-devel < %version-%release
Obsoletes: %sname-mpi-devel < %version-%release
Conflicts: %sname-mpi < %version-%release
Obsoletes: %sname-mpi < %version-%release
Conflicts: %sname

%description -n %sname-mpi-devel-doc
This package contains the netCDF development documentation.

%description -l ru_RU.UTF-8 -n %sname-mpi-devel-doc
Документация разработчика по библиотеке NetCDF.

%prep
%setup

%ifarch x86_64
LIB64=64
%endif
sed -i "s|@64@|$LIB64|g" nc-config.in

rm -fR udunits/expat

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -I%mpidir/include -fno-strict-aliasing %optflags_shared
%autoreconf
%configure \
	--bindir=%mpidir/bin \
	--libdir=%mpidir/lib \
	--includedir=%mpidir/include \
	--enable-shared \
	--enable-netcdf-4 \
	--enable-f90 \
	--enable-cxx-4 \
	--enable-docs-install \
	--enable-ncgen4 \
	--with-udunits \
	--with-hdf5=%mpidir \
	--with-zlib=%prefix \
	--with-szlib=%prefix \
	MPIDIR=%mpidir
sed -i 's|^\(postdeps.*\)\-l \(.*\)|\1 \2|' libtool
sed -i 's|^\(postdeps.*\)\-l \(.*\)|\1 \2|' libtool
sed -i 's|^\(postdeps.*\)\-l \(.*\)|\1 \2|' libtool
sed -i 's|\-l \-|-|' libtool
%make

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%makeinstall_std MPIDIR=%mpidir

mkdir -p %buildroot%mpidir/include/netcdf-3
#install -p -m644 libsrc4/netcdf3.h libsrc4/netcdf_base.h libsrc4/nc4internal.h \
#	%buildroot%mpidir/include
mv %buildroot%mpidir/include/*.* %buildroot%mpidir/include/netcdf-3

bzcat %SOURCE1 > guidec.pdf
bzcat %SOURCE2 | tar xvf -
#install -d %buildroot%_docdir/%oname%sover-mpi-tools
#mv %buildroot%_docdir/%oname/ncdump* %buildroot%_docdir/%oname/ncgen* \
#	%buildroot/%_docdir/%oname%sover-mpi-tools/
#mv %buildroot%_docdir/%oname %buildroot/%_docdir/%sname%sover-mpi-devel

# alternatives

install -d %buildroot%_altdir
mkdir -p %buildroot%_libdir
pushd %buildroot%mpidir/lib
for i in %sname.so.* libudunits2.so.*; do
	ln -s ../..%mpidir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
done
for i in $(ls %{sname}_c++.so.*); do
	ln -s ../..%mpidir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-cxx.alternatives
done
for i in $(ls %{sname}_c++4.so.*); do
	ln -s ../..%mpidir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-cxx4.alternatives
done
for i in $(ls %{sname}f.so.*); do
	ln -s ../..%mpidir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-fortran.alternatives
done
for i in $(ls *.so); do
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-devel.alternatives
done
echo "%_bindir/nc-config %mpidir/bin/nc-config %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives
echo "%_pkgconfigdir/%oname.pc %mpidir/lib/pkgconfig/%oname.pc %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives
popd
pushd %buildroot%mpidir/bin
for i in $(ls |egrep -v 'nc\-config'); do
	echo "%_bindir/$i %mpidir/bin/$i %priority" >> \
		%buildroot%_altdir/%oname-mpi-tools.alternatives
done
popd

for i in %buildroot%mpidir/lib/*.so; do
	chrpath -r %mpidir/lib $i ||:
done

%files
%doc COPYRIGHT README RELEASE_NOTES
%ghost %_libdir/%sname.so.*
%mpidir/lib/%sname.so.*
%ghost %_libdir/libudunits2.so.*
%mpidir/lib/libudunits2.so.*
%_altdir/%name.alternatives
#_datadir/udunits

%files -n %sname-cxx-%c_sover-mpi
%ghost %_libdir/%{sname}_c++.so.*
%mpidir/lib/%{sname}_c++.so.*
%_altdir/%name-cxx.alternatives

%files -n %sname-cxx4-%c4_sover-mpi
%ghost %_libdir/%{sname}_c++4.so.*
%mpidir/lib/%{sname}_c++4.so.*
%_altdir/%name-cxx4.alternatives

%files -n %sname-fortran-%f_sover-mpi
%ghost %_libdir/%{sname}f.so.*
%mpidir/lib/%{sname}f.so.*
%_altdir/%name-fortran.alternatives

%files -n %sname-mpi-devel
%mpidir/include/netcdf-3
%mpidir/include/netcdf
%mpidir/lib/*.so
%_man3dir/*
%mpidir/bin/nc-config
%mpidir/lib/pkgconfig/*
%_altdir/%name-devel.alternatives

%files -n %sname-mpi-devel-doc
%doc guidec.pdf guidec
%_infodir/*

%files -n %oname%sover-mpi-tools
#_docdir/%oname%sover-mpi-tools
%mpidir/bin/*
%exclude %mpidir/bin/nc-config
%_man1dir/*
%_altdir/%oname-mpi-tools.alternatives

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt6
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt5
- Fixed build

* Fri Mar 09 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt4
- Fixed flags in nc-config

* Thu Mar 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt3
- Fixed alternative for %oname.pc (ALT #27049)
- Fixed Cflags in %oname.pc

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt2
- Fixed RPATH

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.3-alt1
- Version 4.1.3

* Sat Apr 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2
- Disabled devel-static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt2
- Rebuilt with debuginfo

* Wed Nov 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.1-alt1
- Version 4.1.1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt10
- Fixed soname set-versions by ghost links (thnx ldv@)

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt9
- Fixed linking of libraries

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt8
- Set NC_MAX_DIMS=65536 and NC_MAX_VARS=524288 for client software

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt7
- Set NC_MAX_DIMS=65536 and NC_MAX_VARS=524288

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt6
- Enabled szlib compression
- Created alternatives

* Fri Jun 05 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt5
- Added explicit conflicts with sequential version of libraries
- Extract development documentation into separate package

* Tue Jun 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt4
- Enable zlib compression

* Sun May 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt3
- Rebuild with szlib support

* Fri May 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt2
- Splitted libraries into subpackages
- Moved tools into separate package

* Thu May 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.1-alt1
- MPI version: initial build for Sisyphus

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

