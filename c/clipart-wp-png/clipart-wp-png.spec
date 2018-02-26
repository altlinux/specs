#TODO: disable all verifies for speed

Name: clipart-wp-png
Version: 2.4
Release: alt0.1

Summary: WP Clip Art Library
Summary(ru_RU.KOI8-R): Свободная коллекция изображений (WP Clip Art)

License: Public domain
Group: Graphics
Url: http://www.pcbypaul.com/wpclipart/

Packager: Vitaly Lipatov <lav@altlinux.ru>

%define oname wpclipart
%define clip_dir %_datadir/design/cliparts/wp

Source: http://www.ibiblio.org/abiclipart/downloads/%{oname}-%version.tar.bz2

BuildArch: noarch

%description
WP Clipart is an attempt to make a useful clipart package of public
domain images for use in word processors. Packages also include a
cross-platform viewer/editor written with Python/wxWidgets. It contains
about 6,300 pieces of non-transparent PNG clip art, which is exactly
what AbiWord prints and scales well. It has been optimized for use in
all word processors (scaled down, midtones expanded for inkjet print
quality, etc.) It is suitable for documents as well as Web graphics,
but also has business application (credit cards, promo graphics) and
educational uses (pictures of all US presidents, all country flags,
all US states, historical figures, and a sign language alphabet).

You can found demo preview at %url/browse.html page

%prep
%setup -q -n %{oname}-%version

%install
mkdir -p doc
find -name "*.txt" -print0 | xargs -0 -i'{}' cp {} ./doc
find -name "*.png" -print0 | xargs -0 -i'{}' install -D -m0644 "{}" "%buildroot%clip_dir/{}"

%files
%doc doc/*.txt
%clip_dir/

%changelog
* Wed Dec 13 2006 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt0.1
- new version 2.4 (with rpmrb script)

* Sun Aug 06 2006 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt0.1
- new version 2.3 (with rpmrb script)

* Fri Mar 31 2006 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt0.1
- new version (1.9)

* Mon Feb 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt0.1
- new version (1.5)

* Wed Feb 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- initial build for Sisyphus
