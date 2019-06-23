Name: xst
Version: 0.7.1
Release: alt1

Packager: %packager

Summary: st fork that uses Xresources and some pretty good patches
License: GPL
Group: Terminals
URL: https://github.com/gnotclub/xst/
# Original st is located at http://suckless.org/

Source: %name-%version.tar

# Automatically added by buildreq on Sun Jun 23 2019
BuildRequires: libXext-devel libXft-devel termutils-devel

%description
st is a simple terminal implementation for X.
xst is an in progress st fork that:
    Loads settings from Xresources. See https://git.io/vVisW
    Live-reloads settings from xrdb on USR1 signal (like termite)
    Has cursor blinking options
    Has the following st-patches applied:
        spoiler
        clipboard
        externalpipe
        boldcolors (only the ability to disable bold fonts)
        vertcenter
        alpha (transparent background)

%prep
%setup

%build
%make PREFIX=%_exec_prefix MANPREFIX=%_mandir

%install
%define docdir %_docdir/%name-%version

%makeinstall DESTDIR=%buildroot PREFIX=%_exec_prefix MANPREFIX=%_mandir
mkdir -p %buildroot/%docdir

cp README.md %buildroot/%docdir/
cp doc/* %buildroot/%docdir/
rm -f %buildroot/%docdir/xst.1

%files
%_bindir/*
%_man1dir/*
%dir %_datadir/terminfo/x/
%_datadir/terminfo/x/*
%dir %docdir
%docdir/*

%changelog
* Sun Jun 23 2019 Andrey Bergman <vkni@altlinux.org> 0.7.1-alt1
- Initial release for Sisyphus.
