Name: cuneiform
Version: 1.0
Release: alt2.1

Summary: Cuneiform is an OCR system originally developed and open sourced by Cognitive technologies.
Summary(ru_RU.KOI8-R): Программа распознавания символов (OCR) Cuneiform, Linux-версия

License: BSD-style
Group: Graphics
Url: https://launchpad.net/cuneiform-linux

Packager: Sergey Alembekov <rt@altlinux.ru>

Source: http://launchpad.net/%name-linux/%version/%version/+download/%name-%version.tar.bz2

Requires: %name-data
BuildRequires: gcc-c++ libImageMagick-devel cmake

%description
Cuneiform is an OCR system originally developed and open sourced by
Cognitive technologies. This project aims to create a fully portable
version of Cuneiform.

%description -l ru_RU.KOI8-R
Программа распознавания символов (OCR) Cuneiform, некогда очень
популярная в нашей стране, была выложена компанией Cognitive
Technologies в свободный доступ в 2008 году. Проект cuneiform-linux
ставит своей целью полное портирование и дальнейшее развитие Cuneiform
под Linux и другие операционные системы.

%package data
Summary: Language support and other data files required for Cuneiform OCR
Summary(ru_RU.KOI8-R): Поддержка различных языков и другие файлы с данными для OCR Cuneiform
Group: Graphics
BuildArch: noarch

%description data
Language support and other data files required for Cuneiform OCR

%description -l ru_RU.KOI8-R data
Поддержка различных языков и другие файлы с данными для OCR Cuneiform

%prep
%setup

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%_prefix
%make_build

%install
cd build
%make preinstall
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%prefix -P cmake_install.cmake

%files
%_bindir/%name
%_libdir/*.so*
%_includedir/%name.h

%files data
%dir %_datadir/%name
%_datadir/%name/*

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 1.0-alt2.1
- Rebuild with new libImageMagick

* Mon Feb 28 2011 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2
- Closes bug: #21335
- fix debuginfo.req errors
- remove circular dependencies on cuneiform-data 

* Tue Sep 14 2010 Anton Farygin <rider@altlinux.ru> 1.0-alt1.1
- Rebuild with new libImageMagick

* Fri Jul 16 2010 Sergey Alembekov <rt@altlinux.ru> 1.0-alt1
- upstream version 1.0
- remove broken libidl patch

* Fri Aug 21 2009 Dmitry V. Levin <ldv@altlinux.org> 0.6-alt1.1
- Rebuilt with libMagick++.so.2.

* Tue Mar 03 2009 Sergey Alembekov <rt@altlinux.ru> 0.6-alt1
- new upstream version

* Tue Dec 16 2008 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt1.1
- add forgotten libidl patch
- add cuneiform-data to requires

* Mon Dec 15 2008 Sergey Alembekov <rt@altlinux.ru> 0.5.0-alt1
- New 0.5 version build

* Sat Aug 16 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build from scratch
- Thanks thresh@ for libdl hint

