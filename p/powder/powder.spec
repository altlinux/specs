%define names32 %name-sse %name-sse2 %name-sse3
%define names64 %name-64-sse2 %name-64-sse3

Name:           powder
Version:        42.3
Release:        alt3

Summary:        Physical simulator which allows to construct objects using different materials
License:        GPLv2

Group:          Games/Educational
URL:            http://powder.hardwired.org.uk/

Packager: 	Anton Chernyshov <ach@altlinux.org>

Source0:        %name-%version.tar.gz
Source1:        %name.desktop
Patch0:		%name-%version-alt-makefile.patch

BuildPreReq:  	alternatives
BuildPreReq: 	bzlib-devel
BuildPreReq: 	ImageMagick-tools
BuildPreReq:    libSDL-devel
BuildPreReq: 	libSDL_mixer-devel 

# Automatically added by buildreq on Tue Nov 09 2010 (-bb)
BuildRequires: ImageMagick-tools bzlib-devel libSDL-devel

%description
The Powder Toy is a desktop version of the classic 'falling sand' physics sandbox,
it simulates air pressure and velocity as well as heat!
Note! This version of Powder Toy use ALT Linux alternatives system. Use it to select
your own flavour of Powder.

%description -l ru_RU.UTF-8
"The Powder Toy" - это версия симулятора физических процессов. Он может симулировать давление воздуха,
ускорение, тепловое воздействие и много чего еще! Множество примеров работы "The Powder Toy" можно найти на 
http://youtube.com
Внимание! Эта версия Powder Toy использует ATL Linux alternatives, благодаря чему после установки можно
выбрать нужный вариант Powder Toy.

%prep
%setup
%patch0 -p0

%build -v

# build more powder flavours
%ifarch x86_64
    for i in %names64; do
	%make $i 
    done
%else
   for i in %name %names32; do
	%make $i 
   done
%endif

%install
convert %name.ico %name.xpm

# install builded powder flavours in system
%ifarch x86_64
    for i in %names64 ; do
	%__install -D $i %buildroot/%_bindir/$i
    done
%else
# first rename powder generic version to appropriate name
# to suffice alternatives system
%__mv %name %name-generic
   for i in %name-generic %names32; do
	%__install -D $i %buildroot/%_bindir/$i
   done
%endif

%__install -D -m 0644 %name-2.xpm %buildroot/%_iconsdir/%name.xpm
%__install -D -m 0644 %{SOURCE1} %buildroot/%_desktopdir/%name.desktop

# generate alternatives file
%__mkdir_p %buildroot/%_altdir/

%ifarch x86_64
echo %_bindir/%name %_bindir/%name-64-sse2 50 > %buildroot/%_altdir/%name-64-sse2
echo %_bindir/%name %_bindir/%name-64-sse3 10 > %buildroot/%_altdir/%name-64-sse3
%else
echo %_bindir/%name %_bindir/%name-generic 50 > %buildroot/%_altdir/%name-generic
echo %_bindir/%name %_bindir/%name-sse 10 > %buildroot/%_altdir/%name-sse
echo %_bindir/%name %_bindir/%name-sse2 10 > %buildroot/%_altdir/%name-sse2
echo %_bindir/%name %_bindir/%name-sse3 10 > %buildroot/%_altdir/%name-sse3
%endif

%files
%_bindir/*
%_iconsdir/*
%_desktopdir/*
%_altdir/*

%changelog
* Tue Oct 19 2010 Anton Chernyshov <ach@altlinux.org> 42.3-alt3
- add new compile options - make powder with support sse,sse2,sse3
- add alternatives support to allow user select correct executable to run

* Tue Oct 19 2010 Anton Chernyshov <ach@altlinux.org> 42.3-alt2
- fix some macros in spec file
- fix wrong permissions for .desktop and .ico file
- adding Russian translation to package description and summary

* Mon Oct 11 2010 Anton Chernyshov <ach@altlinux.org> 42.3-alt1
- create spec file and build
