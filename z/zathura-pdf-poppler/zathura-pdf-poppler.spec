%define _unpackaged_files_terminate_build 1

Name: zathura-pdf-poppler
Version: 0.2.8
Release: alt1

Summary: PDF support for zathura (poppler)
License: %bsdstyle
Group: Office

URL: http://pwmt.org/projects/zathura/plugins/zathura-pdf-poppler
# https://git.pwmt.org/pwmt/zathura-pdf-poppler.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgirara-devel zathura-devel
BuildRequires: intltool libpoppler-glib-devel libcairo-devel

Requires: zathura

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using
the poppler rendering engine.

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
%_desktopdir/*.desktop
%_libdir/zathura/*.so
%_datadir/metainfo/*.xml

%changelog
* Mon Jan 15 2018 Mikhail Efremov <sem@altlinux.org> 0.2.8-alt1
- Fixed appdata location.
- Updated to 0.2.8.

* Tue Jan 24 2017 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1
- Updated to 0.2.7.

* Wed Dec 23 2015 Mikhail Efremov <sem@altlinux.org> 0.2.6-alt1
- Updated to 0.2.6.

* Fri Apr 17 2015 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt2
- Rebuild with libgirara-0.2.4.

* Fri Feb 21 2014 Mikhail Efremov <sem@altlinux.org> 0.2.5-alt1
- Updated to 0.2.5.

* Thu Nov 14 2013 Mikhail Efremov <sem@altlinux.org> 0.2.4-alt1
- Updated to 0.2.4.

* Mon May 13 2013 Mikhail Efremov <sem@altlinux.org> 0.2.3-alt1
- Package LICENSE.
- Updated to 0.2.3.

* Tue Feb 12 2013 Mikhail Efremov <sem@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.

* Wed Jan 09 2013 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Fri Jun 15 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt2
- Rebuild with zathura-0.1.2.
- Require zathura.

* Mon Mar 19 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Initial build.

