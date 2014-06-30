%define major 4
%define oname netcdf-fortran
%define sname libnetcdff
%define sover 5
%define priority 30
%define hdfdir %_libdir/hdf5-seq

Name: %sname%sover-seq
Version: %major.2
Release: alt3

Summary: Libraries to use the Unidata network Common Data Form (netCDF), Fortran interface

License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/packages/netcdf/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires(post,preun): alternatives
Requires: libhdf5-8-seq libnetcdf7-seq
Conflicts: %sname-mpi < 4.0.1-alt6
Provides: %sname = %version-%release
Provides: %sname%sover = %version-%release
Conflicts: %sname%sover < %version-%release
Obsoletes: %sname%sover < %version-%release
%ifarch x86_64
Provides: %sname.so.%sover()(64bit)
%else
Provides: %sname.so.%sover
%endif

Source: %name-%version.tar

# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: flex gcc-c++ gcc-fortran zlib-devel libhdf5-devel

BuildPreReq: libnetcdf-devel
BuildPreReq: libcurl-devel libexpat-devel

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

This package contains Fortran interface library for NetCDF.

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

Данный пакет содержит библиотеку Fortran интерфейсов для NetCDF версии 4.

%package -n %sname-devel
Summary: Development tools for the NetCDF library in Fortran
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF на Фортране
Group: Development/Other
Requires(post,preun): alternatives
Requires: %name = %version-%release
Requires: libnetcdf-devel
Conflicts: %sname-mpi-devel < 4.0.1-alt6

%description -n %sname-devel
This package contains the netCDF header files, shared devel libs, and
man pages.

If you want to develop applications which will use the NetCDF library
in Fortran, you'll need to install the %sname-devel package.

%description -l ru_RU.UTF-8 -n %sname-devel
Заголовочные файлы и документация для использования библиотеки NetCDF
в приложениях.

Если вы собираетесь разрабатывать приложения на Фортране, которые будут
использовать библиотеку NetCDF, вам необходимо установить пакет
%sname-devel.

%package doc
Summary: Documentation for NetCDF, Fortran interface
Summary(ru_RU.UTF-8): Документация по NetCDF (интерфейс для Фортрана)
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description doc
Documentation for NetCDF library, Fortran interface.

%description -l ru_RU.UTF-8 doc
Документация по NetCDF (интерфейс для Фортрана).

%prep
%setup

sed -i 's|@LIBDIR@|%_libdir|' netcdf-fortran.pc.in nf-config.in

%build
%add_optflags -I%hdfdir/include -I%hdfdir/include/netcdf
%add_optflags -fno-strict-aliasing %optflags_shared -DNO_NETCDF_2
%autoreconf
%configure \
	--enable-shared \
	--enable-static=no \
	--bindir=%hdfdir/bin \
	--libdir=%hdfdir/lib \
	--includedir=%hdfdir/include
%make_build

%install
%makeinstall_std

install -d %buildroot%hdfdir/include/netcdf
mv %buildroot%hdfdir/include/*.* %buildroot%hdfdir/include/netcdf/
rm -f %buildroot%hdfdir/lib/*.la

# alternatives

install -d %buildroot%_altdir
mkdir -p %buildroot%_libdir
pushd %buildroot%hdfdir/lib
for i in %sname.so.*; do
	ln -s ../..%hdfdir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %hdfdir/lib/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
done
for i in $(ls *.so); do
	echo "%_libdir/$i %hdfdir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-devel.alternatives
done
echo "%_bindir/nf-config %hdfdir/bin/nf-config %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives
echo "%_pkgconfigdir/%oname.pc %hdfdir/lib/pkgconfig/%oname.pc %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives
popd

%files
%doc COPYRIGHT README
%ghost %_libdir/%sname.so.*
%hdfdir/lib/%sname.so.*
%_altdir/%name.alternatives

%files -n %sname-devel
%hdfdir/bin/nf-config
%hdfdir/include/netcdf
%hdfdir/lib/*.so
%hdfdir/lib/pkgconfig/*
%_infodir/*
%_man3dir/*
%_altdir/%name-devel.alternatives

%files doc
%doc man4/*.pdf man4/*.txt man4/*.html examples

%changelog
* Mon Jun 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt3
- Rebuilt with gcc 4.8

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt2
- Rebuilt with new libhdf5

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Initial build for Sisyphus

