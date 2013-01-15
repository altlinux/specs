Name: paxutils
Version: 0.0.1.111.0b3d84a
Release: alt1

Summary: GNU pax library
License: GPLv3+
Group: Development/C
BuildArch: noarch
Url: http://www.gnu.org/software/gnulib/
Source: %name-%version-%release.tar
AutoReqProv: no

%description
Currently paxutils provides initial version of pax library,
containing internal buffering support.

%prep
%setup -n %name-%version-%release

%install
find -name DISTFILES -printf '%h\n' |
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
* Tue Jan 15 2013 Dmitry V. Levin <ldv@altlinux.org> 0.0.1.111.0b3d84a-alt1
- GNU paxutils snapshot v0.0.1-111-g0b3d84a with ALT fixes.
