Name: xst
Version: 0.9.0
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

cp README %buildroot/%docdir/
cp readme.org %buildroot/%docdir/
cp FAQ %buildroot/%docdir/
cp LEGACY %buildroot/%docdir/
cp LICENSE %buildroot/%docdir/
cp TODO %buildroot/%docdir/
#cp Xresources %buildroot/%docdir/
cp st.info %buildroot/%docdir/

%files
%_bindir/*
%_man1dir/*
%dir %_datadir/terminfo/x/
%_datadir/terminfo/x/*
%dir %docdir
%docdir/*

%changelog
* Fri Jul 28 2023 Andrey Bergman <vkni@altlinux.org> 0.9.0-alt1
- Update to version 0.9.0

* Sun May 22 2022 Andrey Bergman <vkni@altlinux.org> 0.8.5-alt1
- Update to version 0.8.5

* Thu Jan 28 2021 Andrey Bergman <vkni@altlinux.org> 0.8.4.1-alt1
- Update to version 0.8.4.1

* Sat Oct 10 2020 Andrey Bergman <vkni@altlinux.org> 0.8.4-alt1
- Update to version 0.8.4

* Sun Jun 23 2019 Andrey Bergman <vkni@altlinux.org> 0.7.1-alt1
- Initial release for Sisyphus.
