%define _unpackaged_files_terminate_build 1

Name: zathura-cb
Version: 0.1.7
Release: alt1

Summary: Comic book support for zathura
License: %bsdstyle
Group: Office

URL: http://pwmt.org/projects/zathura/plugins/%name
# https://git.pwmt.org/pwmt/zathura-cb.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgirara-devel zathura-devel
BuildRequires: libgdk-pixbuf-devel libgio-devel
BuildRequires: intltool libcairo-devel libarchive-devel

Requires: zathura

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
* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1
- Updated to 0.1.7.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.1.6-alt1
- Updated to 0.1.6.

* Wed Dec 23 2015 Mikhail Efremov <sem@altlinux.org> 0.1.5-alt1
- Updated to 0.1.5.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt2
- Rebuild with libgirara-0.2.4.

* Tue Nov 11 2014 Mikhail Efremov <sem@altlinux.org> 0.1.4-alt1
- Updated to 0.1.4.

* Fri Oct 17 2014 Mikhail Efremov <sem@altlinux.org> 0.1.3-alt1
- Updated to 0.1.3.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt2
- Rebuild with new libgirara and zathura for GTK+3.

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Package LICENSE.
- Updated to 0.1.1.

* Tue Jun 19 2012 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1
- Initial build.

