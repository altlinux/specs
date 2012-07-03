# for set release
%define release_pre alt
%define release_base_num 2
%define release_base_num2 %nil
%define release_suff %nil

# for distr selected
%def_without M40
%def_without M41
%def_without M50

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
%if_with M50
%define distr_switch M50
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

Name: FreeAdhocUDF
Version: 0.0.0.20090128a
Release: %package_release

Summary: Large UDF Library of over 360+ functions for FireBird
Summary(ru_RU.UTF-8): Большая (более 360+ функций) UDF библиотека для FireBird
License: %lgpl3only
Group: Development/Other
Url: http://www.udf.adhoc-data.de/

Packager: Aleksey Avdeev <solo@altlinux.ru>
Source: %name-%version.tar
Patch1: %name-%version-alt-makefile.0.1.patch
Patch2: %name-%version-alt-fix-uuid_functions.0.1.patch

Requires: %firebirdudfdir

BuildPreReq: rpm-build-licenses
BuildPreReq: firebird-devel

%description
The FreeadhocUDFs depends on

    * FreeUDFLib (in Delphi, 1998 from Gregory Deatz)
    * FreeUDFLibC (ported to C, 1999 from Gregory Deatz)

and are compatible to

    * FreeUDFLib from AvERP (in Delphi, with some enhancements) - complete
    * GrUDF (in Delphi and Kylix 2004 from Torsten Grundke and Gerd Kroll) - complete
    * rFunc (in C++ from Polaris Software, last version 2003-11-27) - nearly complete

The FreeadhocUDFs returns the same values in Windows, Windows64, Linux, LinuxAMD64 and MacOSXintel32.
The FreeadhocUDFs returns the same values from InterBase 5.6 to InterBase2007 and FireBird 1.0 to FireBird 2.1.RC1

%description -l ru_RU.UTF-8
FreeadhocUDFs зависят от

    * FreeUDFLib (в Delphi, 1998 Gregory Deatz)
    * FreeUDFLibC (порт на C, 1999 Gregory Deatz)

и совместимы с

    * FreeUDFLib из AvERP (в Delphi, с некоторыми аксессуарами) - полностью
    * GrUDF (в Delphi и Kylix 2004 от Torsten Grundke и Gerd Kroll) - полностью
    * rFunc (в C++ от Polaris Software, последняя версия 2003-11-27) - почти полностью

FreeadhocUDFs возвращают одинаковые значения в Windows, Windows64, Linux, LinuxAMD64 и MacOSXintel32.
FreeadhocUDFs возвращают одинаковые значения в InterBase от 5.6 до InterBase2007 и FireBird от 1.0 до 2.1.RC1
   
%prep
%setup
%patch1 -p1
%patch2 -p1

%build
pushd source/adhoc/

cp Makefile.Linux Makefile
%make_build LIB=%_libdir new
popd

%install
install -d %buildroot%firebirdudfdir/
pushd source/adhoc/
%make_install DBDIR=%buildroot%firebirddir/ install
popd
%find_lang %name

%files -f %name.lang
%doc *.txt install/ documentation/UDF.adhoc-data.de/
%firebirdudfdir/*

%changelog
* Mon Aug 03 2009 Aleksey Avdeev <solo@altlinux.ru> 0.0.0.20090128a-alt2
- Fix always overflow destination buffer (Closes: #20941)

* Mon Apr 06 2009 Aleksey Avdeev <solo@altlinux.ru> 0.0.0.20090128a-alt1
- New version.

* Fri Apr 03 2009 Aleksey Avdeev <solo@altlinux.ru> 0.0.0.20080303-alt2
- Fix package license (thanks to Christoph Theuring <UDF adhoc-data de>)

* Mon Nov 17 2008 Aleksey Avdeev <solo@altlinux.ru> 0.0.0.20080303-alt1
- Initial build
