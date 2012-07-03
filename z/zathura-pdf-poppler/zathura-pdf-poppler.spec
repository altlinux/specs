Name: zathura-pdf-poppler
Version: 0.2.0
Release: alt1

Summary: PDF support for zathura (poppler)
License: %bsdstyle
Group: Office

URL: http://pwmt.org/projects/zathura/plugins/zathura-pdf-poppler
# git.alt:packages/zathura-pdf-poppler.git
Source: %name-%version.tar
#Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libgirara-devel zathura-devel
BuildRequires: intltool libpoppler-glib-devel

Requires: zathura >= 0.1.2

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
%doc AUTHORS
%_libdir/zathura/*.so

%changelog
* Fri Jun 15 2012 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Updated to 0.2.0.

* Thu Mar 29 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt2
- Rebuild with zathura-0.1.2.
- Require zathura.

* Mon Mar 19 2012 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1
- Initial build.

