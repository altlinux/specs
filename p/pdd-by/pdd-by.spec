Name: pdd-by
Version: 0.3
Release: alt2.1

Summary: PDD training
License: GPLv3
Group: Education

Url: http://code.google.com/p/pdd-by/

Packager: Andrey Yurkovsky <anyr@altlinux.org>
Source0: %name.tar.gz
Source1: %name.desktop
Source2: %name.png

BuildPreReq: ccmake gcc-c++ glib2-devel gtk+-devel libgtk+2-devel 
BuildPreReq: libGConf-devel libpixman-devel libyaml-devel libsqlite3-devel
BuildPreReq: libXau-devel, libXdmcp-devel

%description
PDD trainig tool.

%description -l ru_RU.UTF-8
Обучающая программа по ПДД.

%prep
%setup -n %name

%build
cmake   -DCMAKE_INSTALL_PREFIX=%_prefix \
%if %_lib == lib64
        -DLIB_SUFFIX=64 \
%endif
        -DCMAKE_CXX_FLAGS:STRING="%optflags" \
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_SKIP_RPATH=YES \
        -G "Unix Makefiles" && make 

%install
mkdir -p %buildroot/%_bindir
cp pdd-by %buildroot/%_bindir
mkdir -p %buildroot%_datadir/%name
mkdir -p  %buildroot%_datadir/%name/data
cp data/* %buildroot%_datadir/%name/data
mkdir -p  %buildroot%_datadir/%name/ui
cp ui/* %buildroot%_datadir/%name/ui
%__install -pD -m744 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
%__install -pD -m644 %SOURCE2 %buildroot%_liconsdir/%name.png

%files
%_bindir/pdd-by
%_datadir/%name/*
%_liconsdir/%name.png
%_datadir/applications/%name.desktop
%dir %attr(755,root,root) %_datadir/%name

%changelog
* Thu Dec 16 2010 Dmitry V. Levin <ldv@altlinux.org> 0.3-alt2.1
- Blind rebuild without libyaml.

* Mon Nov 30 2009 Andrey Yurkovsky <anyr@altlinux.org> 0.3-alt2
- added semicolon (';') as trailing character in desktop file

* Wed Nov 25 2009 Andrey Yurkovsky <anyr@altlinux.org> 0.3-alt1
- initial build
