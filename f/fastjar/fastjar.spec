Name: fastjar
Version: 0.98
Release: alt3

Summary: Archive tool for Java archives
License: GPLv2+
Group: Development/Java
Url: http://savannah.nongnu.org/projects/fastjar/

# http://download.savannah.gnu.org/releases/fastjar/fastjar-%version.tar.gz
Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: makeinfo zlib-devel

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
* Thu Dec 10 2015 Dmitry V. Levin <ldv@altlinux.org> 0.98-alt3
- Added makeinfo to BuildRequires.

* Fri Apr 19 2013 Dmitry V. Levin <ldv@altlinux.org> 0.98-alt2
- Built with LFS support enabled.

* Tue Sep 08 2009 Dmitry V. Levin <ldv@altlinux.org> 0.98-alt1
- Updated to 0.98.
- Removed obsolete %%install_info/%%uninstall_info calls.

* Sat Apr 25 2009 Dmitry V. Levin <ldv@altlinux.org> 0.97-alt1
- Updated to 0.97.

* Thu Oct 09 2008 Dmitry V. Levin <ldv@altlinux.org> 0.96-alt1
- Initial revision.
