Name: paxutils
Version: 0.0.1.160.481b

Release: alt1

Summary: GNU pax library
License: GPLv3+
Group: Development/C
BuildArch: noarch
Url: https://www.gnu.org/software/gnulib/
# git://git.altlinux.org/gears/p/paxutils.git
Source: %name-%version-%release.tar
AutoReqProv: no

%description
Currently paxutils provides initial version of pax library,
containing internal buffering support.

%prep
%setup -n %name-%version-%release

%install
find -name DISTFILES -printf '%%h\n' |
while read srcdir; do
	cd "$srcdir"
	destdir="%buildroot%_datadir/%name/$srcdir"
	mkdir -p -- "$destdir"
	xargs -r ln -t "$destdir" -- DISTFILES < DISTFILES
	cd - >/dev/null
done
ln gnulib.modules %buildroot%_datadir/%name/

%files
%_datadir/%name/

%changelog
* Fri Sep 08 2023 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.0.1.160.481b-alt1
- v0.0.1-139-g2f7d215 -> v0.0.1-160-g481bae1.

* Mon Mar 01 2021 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.139.2f7d-alt1
- v0.0.1-125-g5693984 -> v0.0.1-139-g2f7d215.

* Fri Dec 28 2018 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.125.5693-alt1
- v0.0.1-124-g4ef7f9a -> v0.0.1-125-g5693984.

* Tue Jul 31 2018 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.124.4ef7-alt1
- v0.0.1-121-gec72abd -> v0.0.1-124-g4ef7f9a.

* Mon Mar 20 2017 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.121.ec72-alt1
- v0.0.1-119-g45af163 -> v0.0.1-121-gec72abd.

* Fri Nov 07 2014 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.119.45af-alt1
- Updated to v0.0.1-119-g45af.

* Tue Oct 22 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.113.edfd8bc-alt1
- Updated to v0.0.1-113-gedfd8bc.

* Tue Jan 15 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.111.0b3d84a-alt1
- GNU paxutils snapshot v0.0.1-111-g0b3d84a with ALT fixes.
