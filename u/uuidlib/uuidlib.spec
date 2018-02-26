# for set release
%define release_pre alt
%define release_base_num 1
%define release_base_num2 %nil
%define release_suff %nil

# for distr selected
%def_without M40
%def_without M41

# for set distr release
%define release_distr_num 1

# %%distr_switch set
%define distr_switch %nil
%if_with M40
%define distr_switch M40
%endif
%if_with M41
%define distr_switch M41
%endif

# %%release_num and %%release_distr set
%if "%distr_switch" == ""
%define release_distr %nil
%if "%release_base_num2" == ""
%define release_num %release_base_num
%else
%define release_num %release_base_num.%release_base_num2
%endif
%else
%define release_distr .%distr_switch.%release_distr_num
%if "%release_base_num2" == ""
%define release_num %(expr %release_base_num - 1)
%else
%define release_num %release_base_num.%(expr %release_base_num2 - 1)
%endif
%endif

# %%release_base set
%define release_base %release_pre%release_num%release_distr

# %%package_release set
%define package_release %release_base%release_suff

# set firebird UDF dir
%define firebirddir %_libdir/firebird
%define firebirdudfdir %firebirddir/UDF

%define uuidlib_name uuidlib
%define uuidlib_so %uuidlib_name.so

Name: %uuidlib_name
Version: 1.3
Release: %package_release

Summary: This module contains UDFs to generate UUIDs
Summary(ru_RU.UTF-8): Этот модуль содержит UDF для генерации UUID
License: %bsdstyle
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>
Source: %name-%version.tar
Patch: %name-%version-alt-makefile.0.1.patch

Requires: %firebirdudfdir

BuildPreReq: rpm-build-licenses
BuildPreReq: libuuid-devel

%description
This library contains UDF library for guid generation.
The functions are:
fn_guid_create() returns the created uuid as a 36 char guid.
fn_guid_create2() returns the created uuid as a 36 char guid
    (uppercase).

%description -l ru_RU.UTF-8
Эта библиотека содержит UDF библиотека для генерации GUID.
Функции:
fn_guid_create() возвращает созданный UUID, как 36 значный GUID.
fn_guid_create2() возвращает созданный UUID, как 36 значный GUID
    (в верхнем регистре).
   
%prep
%setup
%patch -p1

%build
%make_build LIBDIR=%_libdir

%install
install -pD %uuidlib_so %buildroot%firebirdudfdir/%uuidlib_so
%find_lang %name

%files -f %name.lang
%doc README *.txt *.sql
%firebirdudfdir/*

%changelog
* Mon Nov 17 2008 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt1
- Initial build
