%define _unpackaged_files_terminate_build 1

%define sover 7

Name: libnetcdff
Version: 4.5.3
Release: alt1
Summary: Libraries to use the Unidata network Common Data Form (netCDF), Fortran interface
License: NetCDF
Group: System/Libraries
Url: http://www.unidata.ucar.edu/software/netcdf/

# https://github.com/Unidata/netcdf-fortran.git
Source: %name-%version.tar

# Automatically added by buildreq on Sun Jan 18 2009
BuildRequires: flex gcc-c++ gcc-fortran zlib-devel libhdf5-devel
BuildRequires: libnetcdf-devel
BuildRequires: libcurl-devel libexpat-devel

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

%package -n %name%sover
Summary: Libraries to use the Unidata network Common Data Form (netCDF), Fortran interface
Group: System/Libraries

%description -n %name%sover
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

Данный пакет содержит библиотеку Fortran интерфейсов для NetCDF версии 4.

%package devel
Summary: Development tools for the NetCDF library in Fortran
Summary(ru_RU.UTF-8): Средства разработки программ на основе библиотеки NetCDF на Фортране
Group: Development/Other
Requires: libnetcdf-devel

%description devel
This package contains the netCDF header files, shared devel libs, and
man pages.

If you want to develop applications which will use the NetCDF library
in Fortran, you'll need to install the %name-devel package.

%description -l ru_RU.UTF-8 devel
Заголовочные файлы и документация для использования библиотеки NetCDF
в приложениях.

Если вы собираетесь разрабатывать приложения на Фортране, которые будут
использовать библиотеку NetCDF, вам необходимо установить пакет
%name-devel.

%package doc
Summary: Documentation for NetCDF, Fortran interface
Summary(ru_RU.UTF-8): Документация по NetCDF (интерфейс для Фортрана)
Group: Documentation
BuildArch: noarch

%description doc
Documentation for NetCDF library, Fortran interface.

%description -l ru_RU.UTF-8 doc
Документация по NetCDF (интерфейс для Фортрана).

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	--enable-shared \
	--disable-static \
	%nil

%make_build

%install
%makeinstall_std

%files -n %name%sover
%doc COPYRIGHT README.md
%_libdir/*.so.%{sover}
%_libdir/*.so.%{sover}.*

%files devel
%_bindir/nf-config
%_libdir/*.so
%_libdir/*.settings
%_pkgconfigdir/*
%_includedir/*
%_man3dir/*

%files doc
%doc docs/*.pdf docs/*.txt docs/*.html examples

%changelog
* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.3-alt1
- Updated to upstream version 4.5.3.
- Removed alternatives.
- Updated packaging scheme.

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.4-alt1
- Updated to upstream version 4.4.4.
- Changed sover to 6.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt4
- Rebuilt with gcc 4.9

* Mon Jun 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt3
- Rebuilt with gcc 4.8

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt2
- Rebuilt with new libhdf5

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2-alt1
- Initial build for Sisyphus

