#TODO split?
Name: clipart-openclipart
Version: 2.0
Release: alt1
Serial: 1

Summary: Open Clip Art Library
Summary(ru_RU.UTF-8): Свободная коллекция изображений (Clip Art)

License: Public domain
Group: Graphics
Url: http://www.openclipart.org/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.openclipart.org/downloads/%version/openclipart-%version-full.tar

%define clip_dir %_datadir/design/cliparts/openclipart

BuildArch: noarch

%description
This is a collection of 100 percent license-free, royalty-free, and
restriction-free art that you can use for whatever purpose you see fit.

Most of the art in this package is in the Scalable Vector Graphic (SVG)
format, which is an XML format approved by the W3C and used in a wide
range of software applications, including Inkscape, Adobe Illustrator,
Batik, and more.

The goal of the Open Clip Art Library is to provide the public with a
huge collection of reusable art for any purpose

For more information, including how you can contribute to this growing
library, please see http://www.openclipart.org/

%description -l ru_RU.UTF-8
Свободная коллекция изображений, пригодная для повторного использования
в любых целях без каких-либо органичений, включая лицензионные условия, и т.п.
Библиотека Open Clip Art является общественным достоянием (Public Domain).

Большинство изображений в пакете - векторная графика в формате SVG,
используемом в большом количестве приложений, включая Inkscape,
Adobe Illustrator, Batik, и др. Формат SVG (Scalable Vector Graphic)
- стандартный формат, утверждённый W3C, является разновидностью языка
разметки XML (eXtensible Markup Language).

Более подробную информацию, включая то, как вы можете внести свой вклад
в эту постоянно развивающуюся библиотеку, можно получить на сайте
проекта: http://www.openclipart.org/

%package svg
Summary: Open Clip Art Library in SVG format
License: Public domain
Group: Graphics
Requires: %name = %version

%description svg
This is a collection of 100 percent license-free, royalty-free, and
restriction-free art that you can use for whatever purpose you see fit.

Most of the art in this package is in the Scalable Vector Graphic (SVG)
format, which is an XML format approved by the W3C and used in a wide
range of software applications, including Inkscape, Adobe Illustrator,
Batik, and more.

The goal of the Open Clip Art Library is to provide the public with a
huge collection of reusable art for any purpose

For more information, including how you can contribute to this growing
library, please see http://www.openclipart.org/

%description svg -l ru_RU.UTF-8
Свободная коллекция изображений, пригодная для повторного использования
в любых целях без каких-либо органичений, включая лицензионные условия, и т.п.
Библиотека Open Clip Art является общественным достоянием (Public Domain).

В пакете %name-svg находится часть библиотеки, состоящая из
векторных изображений в формате SVG (Scalable Vector Graphic).

Более подробную информацию, включая то, как вы можете внести свой вклад
в эту постоянно развивающуюся библиотеку, можно получить на сайте
проекта: http://www.openclipart.org/


%package png
Summary: Open Clip Art Library in PNG format
License: Public domain
Group: Graphics
Requires: %name = %version

%description png
This is a collection of 100 percent license-free, royalty-free, and
restriction-free art that you can use for whatever purpose you see fit.

Most of the art in this package is in the Scalable Vector Graphic (SVG)
format, which is an XML format approved by the W3C and used in a wide
range of software applications, including Inkscape, Adobe Illustrator,
Batik, and more.

The goal of the Open Clip Art Library is to provide the public with a
huge collection of reusable art for any purpose

For more information, including how you can contribute to this growing
library, please see http://www.openclipart.org/

%description png -l ru_RU.UTF8
Свободная коллекция изображений, пригодная для повторного использования
в любых целях без каких-либо органичений, включая лицензионные условия, и т.п.
Библиотека Open Clip Art является общественным достоянием (Public Domain).

В пакете %name-png находится часть библиотеки, состоящая из
растровых изображений в формате PNG (Portable Network Graphics).

Более подробную информацию, включая то, как вы можете внести свой вклад
в эту постоянно развивающуюся библиотеку, можно получить на сайте
проекта: http://www.openclipart.org/


%prep
%setup -n openclipart-%version-full

%install
for tp in png svg txt ; do
	find -name "*.$tp" -print0 | xargs -0 -i'{}' install -D -m0644 "{}" "%buildroot%clip_dir/$tp/{}"
done
rm -f %buildroot%clip_dir/txt/*.txt

%files
%dir %clip_dir/
%clip_dir/txt/
%doc AUTHORS NEWS LICENSE README

%files svg
%clip_dir/svg/

%files png
%clip_dir/png/

%changelog
* Thu Feb 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1:2.0-alt1
- new version (2.0) import in git (closes bug: 25104)

* Fri Feb 11 2011 Vitaly Lipatov <lav@altlinux.ru> 2.8-alt1
- new version (2.8) import in git (closes bug: 24057, 25069)
- add russian description (closes bug: 22791)

* Mon Oct 31 2005 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- new version

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.17-alt1
- new version

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.16-alt1
- new version

* Sun Jul 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.15-alt1
- new version

* Mon Apr 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.12-alt1
- new version

* Sat Feb 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.10-alt1
- new version
- split to svg/png package

* Thu Jul 01 2004 Vitaly Lipatov <lav@altlinux.ru> 0.04-alt1
- first build for Sisyphus
