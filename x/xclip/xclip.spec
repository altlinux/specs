Name: xclip
Version: 0.13
Release: alt2

Packager: Nikita Ermakov <arei@altlinux.org>

Summary: Provides an interface to X selections from the command line
License: GPLv2+
Group: System/XFree86

Url: https://github.com/astrand/xclip
Source: %name-%version.tar
Patch1: xclip-0.12-setsid.patch

BuildRequires: libICE-devel libXmu-devel

%description
xclip is a command line interface to the X11 clipboard. It can read data from
standard input or a file and place it in an X selection for pasting into other X
applications. xclip can also print an X selection to standard out, which can
then be redirected to a file or another program. It can also be used for copying
files, as an alternative to sftp/scp, thus avoiding password prompts when X11
forwarding has already been setup.

%prep
%setup
%patch1 -p1

%build
%autoreconf
%configure
%make_build

%install
make DESTDIR=%buildroot install install.man

%files
%doc README INSTALL
%_man1dir/*
%_bindir/*

%changelog
* Fri Nov 15 2019 Nikita Ermakov <arei@altlinux.org> 0.13-alt2
- Drop imake BR.

* Tue Aug 20 2019 Nikita Ermakov <arei@altlinux.org> 0.13-alt1
- Sync with an upstream (ALT bug #36554).
- Minor fixes to the spec file.

* Tue Jul 09 2019 Nikita Ermakov <arei@altlinux.org> 0.12-alt2
- NMU: Introduce -nonl option.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.12-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Nov 15 2009 Victor Forsyuk <force@altlinux.org> 0.12-alt1
- 0.12
- Applied patch suggested in ALT bug #19705.

* Sun Aug 17 2008 Victor Forsyuk <force@altlinux.org> 0.11-alt1
- 0.11

* Wed Feb 20 2008 Victor Forsyuk <force@altlinux.org> 0.10-alt1
- 0.10
- Enable utf8 support (patch pulled from Fedora).

* Mon Nov 06 2006 Victor Forsyuk <force@altlinux.org> 0.08-alt2
- Rebuild to change prefix: /usr/X11R6 --> /usr.
- Updated buildreqs.

* Tue Oct 29 2002 Victor Forsyuk <force@altlinux.ru> 0.08-alt1
- Initial build.
