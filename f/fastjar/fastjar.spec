Name: fastjar
Version: 0.98
Release: alt1

Summary: Archive tool for Java archives
License: GPLv2+
Group: Development/Java
Url: http://savannah.nongnu.org/projects/fastjar/
Packager: Dmitry V. Levin <ldv@altlinux.org>

# http://download.savannah.gnu.org/releases/fastjar/fastjar-%version.tar.gz
Source: fastjar-%version.tar

Patch: fastjar-%version-%release.patch

BuildRequires: zlib-devel

%description
fastjar is an implementation of Sun's jar utility that comes with the
JDK, written entirely in C, and runs in a fraction of the time while
being feature compatible.

%prep
%setup
%patch -p1
fgrep -lZ _LT_ m4/* |xargs -r0 rm -fv --

%build
%autoreconf
%configure --without-included-regex
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*
%_infodir/*.info*
%doc AUTHORS README NEWS TODO

%changelog
* Tue Sep 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.98-alt1
- Updated to 0.98.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sat Apr 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.97-alt1
- Updated to 0.97.

* Thu Oct 09 2008 Dmitry V. Levin <ldv@altlinux.org> 0.96-alt1
- Initial revision.
