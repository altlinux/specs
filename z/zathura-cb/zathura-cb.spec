Name: zathura-cb
Version: 0.1.2
Release: alt1

Summary: Comic book support for zathura
License: %bsdstyle
Group: Office

URL: http://pwmt.org/projects/zathura/plugins/%name
# git://pwmt.org/zathura-cb.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgirara-devel zathura-devel
BuildRequires: intltool libcairo-devel libarchive-devel

Requires: zathura >= 0.1.2

%description
The zathura-cb plugin adds comic book support to zathura.

%prep
%setup
#patch -p1

%build
export CFLAGS="%optflags"
%make_build VERBOSE=1 PREFIX=%prefix LIBDIR=%_libdir

%install
%makeinstall_std PREFIX=%prefix LIBDIR=%_libdir
%find_lang %name

%files -f %name.lang
%doc AUTHORS LICENSE
%_libdir/zathura/*.so
%_desktopdir/*.desktop

%changelog
* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Package LICENSE.
- Updated to 0.1.1.

* Tue Jun 19 2012 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

