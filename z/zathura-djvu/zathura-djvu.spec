Name: zathura-djvu
Version: 0.2.0
Release: alt1

Summary: DjVU support for zathura
License: %bsdstyle
Group: Office

URL: http://pwmt.org/projects/zathura/plugins/%name
# git://pwmt.org/zathura-djvu.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgirara-devel zathura-devel
BuildRequires: intltool libcairo-devel libdjvu-devel

Requires: zathura >= 0.1.2

%description
The zathura-djvu plugin adds DjVu support to zathura by using
the djvulibre library.

%prep
%setup
%patch -p1

%build
export CFLAGS="%optflags"
%make_build VERBOSE=1 PREFIX=%prefix LIBDIR=%_libdir

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir
%find_lang %name

%files -f %name.lang
%doc AUTHORS
%_libdir/zathura/*.so

%changelog
* Fri Jun 15 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Wed Mar 21 2012 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

