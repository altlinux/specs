# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: root-tail
Version: 1.2
Release: alt3

Summary: Print text directly to X11 root window
Group: Text tools
License: distributable
Url: http://goof.com/pcg/marc/root-tail.html
Packager: Slava Semushin <php-coder@altlinux.ru>

Source: http://www.goof.com/pcg/marc/data/%name-%version.tar.bz2
Patch: %name-deb-man-typo_fix.patch

BuildRequires: libX11-devel libXext-devel
BuildRequires: gccmakedep imake xorg-cf-files

%description
Displays a given file anywhere on your X11 root window with a
transparent background.

%prep
%setup
%patch -p2

%build
xmkmf -a
%make_build CDEBUGFLAGS="%optflags"

%install
%make_install DESTDIR=%buildroot install install.man

%files
%doc README Changes
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Mon Mar 09 2009 Slava Semushin <php-coder@altlinux.ru> 1.2-alt3
- Fixed typo in manual page (debian #343230)

* Wed Dec 10 2008 Slava Semushin <php-coder@altlinux.ru> 1.2-alt2
- New maintainer
- Fixed build (added libX11-devel to BuildRequires)

* Tue Sep 09 2008 Slava Semushin <php-coder@altlinux.ru> 1.2-alt1.1.1
- NMU
- Updated BuildRequires and fixed build

* Sat May 26 2007 Slava Semushin <php-coder@altlinux.ru> 1.2-alt1.1
- NMU
- Rebuild and move files from /usr/X11R6 to /usr (#11862)
- Set Packager tag to really maintainer
- Spec cleanup:
  + s/%%setup -q/%%setup/
  + s/$RPM_OPT_FLAGS/%%optflags/
  + s/$RPM_BUILD_ROOT/%%buildroot/
  + Don't use %%name macros in Url tag
  + Formatted %%description
- Enable _unpackaged_files_terminate_build

* Tue Oct 05 2004 Stanislav Ievlev <inger@altlinux.org> 1.2-alt1
- 1.2

* Mon Mar 01 2004 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- 0.9

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2-alt1
- 0.2

* Thu May 17 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.0.10-alt1
- Initial revision.
