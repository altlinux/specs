%define major 4
%define oname netcdf
%define sname lib%oname
%define sover 7
%define priority 40

%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: %sname%sover-mpi
Version: %major.3.2
Release: alt1

Summary: Parallel libraries to use the Unidata network Common Data Form (netCDF)

License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/packages/netcdf/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar

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
BuildPreReq: libcurl-devel libexpat-devel chrpath doxygen graphviz
BuildPreReq: libpnetcdf-devel

%description
NetCDF (network Common Data Form) is an interface for array-oriented
data access and a freely-distributed collection of software libraries
for C, Fortran, C++, and perl that provides an implementation of the
interface.  The netCDF library also defines a machine-independent format
for representing scientific data. Together, the interface, library, and
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

   o Sharable. One writer and multiple readers may simultaneously access
     the same netCDF file.

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

%package -n %sname-mpi-devel
Summary: Development tools for the NetCDF library
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF
Group: Development/Other
Provides: pkgconfig(%oname) = %EVR
Requires(post,preun): alternatives
Requires: %name = %version-%release
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

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -I%mpidir/include -fno-strict-aliasing %optflags_shared
%add_optflags -DHAVE_MPI_COMM_F2C
%autoreconf
%configure \
	--bindir=%mpidir/bin \
	--libdir=%mpidir/lib \
	--includedir=%mpidir/include \
	--enable-shared \
	--enable-static=no \
	--enable-netcdf-4 \
	--enable-f90 \
	--enable-cxx-4 \
	--enable-docs-install \
	--enable-ncgen4 \
	--with-udunits \
	--with-hdf5=%mpidir \
	--with-zlib=%prefix \
	--with-szlib=%prefix \
	--enable-doxygen \
	--enable-internal-docs \
	--enable-extra-example-tests \
	--enable-extra-tests \
	--enable-v2 \
	--enable-mmap \
	--disable-dap-remote-tests \
	--enable-parallel-tests \
	--enable-pnetcdf \
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

install -d %buildroot%mpidir/include/netcdf
ln -s netcdf %buildroot%mpidir/include/netcdf-3
install -p -m644 include/*.h %buildroot%mpidir/include/netcdf
sed -i 's|config\.h|netcdf_config.h|' \
	%buildroot%mpidir/include/netcdf/*
install -p -m644 config.h \
	%buildroot%mpidir/include/netcdf/netcdf_config.h
rm -f %buildroot%mpidir/include/netcdf/netcdf.h
mv %buildroot%mpidir/include/*.* %buildroot%mpidir/include/netcdf/
#install -p -m644 libsrc4/netcdf3.h libsrc4/netcdf_base.h libsrc4/nc4internal.h \
#	%buildroot%mpidir/include

#install -d %buildroot%_docdir/%oname%sover-mpi-tools
#mv %buildroot%_docdir/%oname/ncdump* %buildroot%_docdir/%oname/ncgen* \
#	%buildroot/%_docdir/%oname%sover-mpi-tools/
#mv %buildroot%_docdir/%oname %buildroot/%_docdir/%sname%sover-mpi-devel

# alternatives

install -d %buildroot%_altdir
mkdir -p %buildroot%_libdir
pushd %buildroot%mpidir/lib
for i in %sname.so.*; do
	ln -s ../..%mpidir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
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

for i in %buildroot%mpidir/lib/*.so %buildroot%mpidir/bin/*; do
	chrpath -r %mpidir/lib $i ||:
done

# There is a file in the package with a name starting with <tt>._</tt>, 
# the file name pattern used by Mac OS X to store resource forks in non-native 
# file systems. Such files are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f


%pre -n %sname-mpi-devel
rm -fR %mpidir/include/netcdf-3 %mpidir/include/netcdf

%files
%doc COPYRIGHT README* RELEASE_NOTES*
%ghost %_libdir/%sname.so.*
%mpidir/lib/%sname.so.*
%_altdir/%name.alternatives

%files -n %sname-mpi-devel
%mpidir/include/netcdf-3
%mpidir/include/netcdf
%mpidir/lib/*.so
%_man3dir/netcdf.3*
%mpidir/bin/nc-config
%mpidir/lib/pkgconfig/*
%_altdir/%name-devel.alternatives

%files -n %sname-mpi-devel-doc
%doc man4/html examples
%_man3dir/*
%exclude %_man3dir/netcdf.3*

%files -n %oname%sover-mpi-tools
#_docdir/%oname%sover-mpi-tools
%mpidir/bin/*
%exclude %mpidir/bin/nc-config
%_man1dir/*
%_altdir/%oname-mpi-tools.alternatives

%changelog
* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1
- Version 4.3.2

* Wed Jul 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt3
- Added Provides: pkgconfig(netcdf) = %EVR

* Fri Jul 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt2
- Applied repocop patch

* Wed Jul 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.0-alt1
- Version 4.3.0

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt2
- Rebuilt with new libhdf5

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt1.1
- Reenabled netCDF version 2 API

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.1.1-alt1
- Version 4.2.1.1

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

