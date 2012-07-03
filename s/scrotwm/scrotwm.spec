%define PRIO 15

Name: scrotwm
Version: 0.9.23
Release: alt3

Summary: Tiling window manager for X

License: ISC
Group: Graphical desktop/Other
Url: http://scrotwm.org/

Source: http://scrotwm.org/snapshot/%name-%version.tgz
Packager: Dmitry Derjavin <dd@altlinux.org>

Source1: scrotwm.wmsession

BuildRequires: libX11-devel libXrandr-devel libXrender-devel libXt-devel iconv

%description
Scrotwm is a small dynamic tiling window manager for X11.
It tries to stay out of the way so that valuable screen real estate
can be used for much more important stuff. It has sane defaults
and does not require one to learn a language to do any configuration.
It was written by hackers for hackers and it strives to be small,
compact and fast.

%prep
%setup -q

%build
%make_build -C linux PREFIX=%_prefix LIBDIR=%_libdir

%install
%makeinstall_std -C linux PREFIX=%_prefix LIBDIR=%_libdir

# to be fixed:
for lang in $(ls %buildroot%_man1dir/%name\_??.1 | cut -f 2 -d _ | cut -f 1 -d .); do
    mkdir -p %buildroot%_mandir/$lang/man1
    mv %buildroot%_man1dir/%name\_$lang.1 %buildroot%_mandir/$lang/man1/%name\.1
done

# to be fixed:
# - inplace conversion;
# - `%__cat %_mandir/ru/.charset` instead of plain 'koi8-r'
iconv -f utf-8 -t koi8-r %buildroot%_mandir/ru/man1/%name\.1 > manpage.txt
mv manpage.txt %buildroot%_mandir/ru/man1/%name\.1

install -pD -m 644 %SOURCE1 %buildroot%_x11sysconfdir/wmsession.d/%PRIO%name

%files
%_bindir/%name
%_libdir/libswmhack.*
%_man1dir/*
%_mandir/??/*
%config %_x11sysconfdir/wmsession.d/%PRIO%name
#%doc README

%changelog
* Tue Feb 08 2011 Dmitry Derjavin <dd@altlinux.org> 0.9.23-alt3
- libdir fix for debuginfo.

* Tue Jul 27 2010 Dmitry Derjavin <dd@altlinux.org> 0.9.23-alt2
- spec file cleanup.

* Fri Apr 30 2010 Dmitry Derjavin <dd@altlinux.org> 0.9.23-alt1
- Initial ALTLinux build.
