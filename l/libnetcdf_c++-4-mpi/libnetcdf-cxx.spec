%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define major 4
%define oname netcdf-cxx
%define sname libnetcdf_c++
%define sover 4
%define priority 30
%define hdfdir %mpidir

Name: %sname-%sover-mpi
Version: %major.2
Release: alt2

Summary: Libraries to use the Unidata network Common Data Form (netCDF) v3, C++ interface

License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/packages/netcdf/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Requires(post,preun): alternatives
Requires: libhdf5-7-mpi libnetcdf7-mpi
Conflicts: %sname < 4.0.1-alt6
Provides: %sname-mpi = %version-%release
Provides: %sname-%sover-mpi = %version-%release
Conflicts: %sname-%sover-mpi < %version-%release
Obsoletes: %sname-%sover-mpi < %version-%release
%ifarch x86_64
Provides: %sname.so.%sover()(64bit)
%else
Provides: %sname.so.%sover
%endif

Source: %name-%version.tar

BuildRequires: flex gcc-c++ gcc-fortran zlib-devel libhdf5-mpi-devel

BuildPreReq: libnetcdf-mpi-devel %mpiimpl-devel
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

This package contains C++ interface library for NetCDF v3.

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

Данный пакет содержит библиотеку C++ интерфейсов для NetCDF версии 3.

%package -n %sname-mpi-devel
Summary: Development tools for the NetCDF v3 library in C++
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF v3 на C++
Group: Development/C++
Requires(post,preun): alternatives
Requires: %name = %version-%release
Requires: libnetcdf-mpi-devel

%description -n %sname-mpi-devel
This package contains the netCDF v3 header files, shared devel libs, and
man pages.

If you want to develop applications which will use the NetCDF v3 library
in C++, you'll need to install the %sname-devel package.

%description -l ru_RU.UTF-8 -n %sname-mpi-devel
Заголовочные файлы и документация для использования библиотеки NetCDF v3
в приложениях.

Если вы собираетесь разрабатывать приложения на C++, которые будут
использовать библиотеку NetCDF, вам необходимо установить пакет
%sname-devel.

%package doc
Summary: Development documentation for the NetCDF v3 library in C++
Group: Development/Documentation
BuildArch: noarch
Conflicts: %sname-%sover-seq-doc

%description doc
This package contains the netCDF v3 development documentation.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -I%hdfdir/include -I%hdfdir/include/netcdf
%add_optflags -fno-strict-aliasing %optflags_shared
%autoreconf
%configure \
	--enable-shared \
	--enable-static=no \
	--bindir=%hdfdir/bin \
	--libdir=%hdfdir/lib \
	--includedir=%hdfdir/include
%make_build

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

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
popd

%filter_from_requires /^debug.*(libnetcdf\.so.*/s/^/libnetcdf7-mpi-debuginfo\t/

%files
%doc COPYRIGHT
%ghost %_libdir/%sname.so.*
%hdfdir/lib/%sname.so.*
%_altdir/%name.alternatives

%files -n %sname-mpi-devel
%hdfdir/include/netcdf
%hdfdir/lib/*.so
%_altdir/%name-devel.alternatives

%files doc
%doc man4/{*.html,*.pdf} examples
%_infodir/*

%changelog
* Tue Sep 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt2
- Forced requirement on libnetcdf7-mpi-debuginfo for
  libnetcdf_c++-4-mpi-debuginfo

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Initial build for Sisyphus

