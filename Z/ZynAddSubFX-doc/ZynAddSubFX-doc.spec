%define _name ZynAddSubFX

Name: %_name-doc
Version: 1.4.3
Release: alt0.5

Summary: Documentation for %_name
Summary(ru_RU.KOI8-R): Документация к %_name
Group: Sound
License: GPL
Url: http://%_name.sourceforge.net
Packager: Yuri N. Sedunov <aris@altlinux.ru>

Source: http://prdownloads.sourceforge.net/%name-%version.tar.gz

BuildArch: noarch

%description
%_name is a realtime software synthesizer with many features,
including polyphony, multi-timbral and microtonal capabilities. It
includes randomness of some parameters, which makes warm sounds, like
analogue synthesizers.

This package contains documentation for %_name.

%description -l ru_RU.KOI8-R
%_name -- это программный полифонический синтезатор, работающий в режиме
реального времени. Встроенная функция создания случайных значений
некоторых параметров позволяет добиться "тёплого" звучания, свойственного
старым аналоговым синтезаторам.

Этот пакет содержит документацию к %_name.

%install
%__mkdir_p %buildroot%_docdir/%_name-%version/html
%__gzip -cd %SOURCE0 | %__tar -xC %buildroot -f -
%__mv %buildroot/%name-%version/* %buildroot%_docdir/%_name-%version/html

%files
%_docdir/%_name-%version/html

%changelog
* Sun Aug 31 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.3-alt0.5
- 1.4.3

* Thu Jul 17 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.2-alt0.5
- 1.4.2
- summary, description by avp.

* Thu May 08 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.1-alt0.5
- 1.4.1

* Wed Apr 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.4.0-alt0.5
- 1.4.0

* Mon Apr 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt0.5
- 1.2.1

* Fri Mar 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.2.0-alt0.5
- First build for Sisyphus.

