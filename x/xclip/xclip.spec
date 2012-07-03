Name: xclip
Version: 0.12
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Provides an interface to X selections from the command line
License: GPLv2+
Group: System/XFree86

Url: http://sourceforge.net/projects/xclip
Source: http://dl.sf.net/xclip/xclip-%version.tar.gz
Patch1: xclip-0.12-setsid.patch

# Automatically added by buildreq on Sun Nov 15 2009
BuildRequires: imake libICE-devel libXmu-devel xorg-cf-files

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
%configure
%make_build

%install
make DESTDIR=%buildroot install install.man

%files
%doc README
%_man1dir/*
%_bindir/*

%changelog
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
