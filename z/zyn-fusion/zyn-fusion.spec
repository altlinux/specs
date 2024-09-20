Name: zyn-fusion
Version: 3.0.6
Release: alt4

Summary: Zynaddsubfx UI
License: LGPL-2.1
Group: Sound
Url: https://github.com/mruby-zest/mruby-zest-build/

Source0: %name-%version-%release.tar
Source1: deps.tar

BuildRequires: libglvnd-devel libuv-devel
BuildRequires: /usr/bin/ruby rake

%description
%summary

%prep
%setup
tar ixf %SOURCE1
sed -ri 's,/opt/zyn-fusion,%_libdir/zyn-fusion,' zest.c

%build
make all pack

%install
mkdir -p %buildroot%_bindir %buildroot%_libdir/zyn-fusion
tar c -C package .|tar x -C %buildroot%_libdir/zyn-fusion
rm -v %buildroot%_libdir/zyn-fusion/mruby 
rm -vr %buildroot%_libdir/zyn-fusion/completions
ln -srv %buildroot%_libdir/zyn-fusion/zest %buildroot%_bindir/zyn-fusion

%files
%_bindir/*
%_libdir/zyn-fusion

%changelog
* Fri Sep 20 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.6-alt4
- 3.0.6-58-g7ca265d

* Thu Mar 21 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.6-alt3
- fixed FTBFS after rake mess, again

* Thu Dec 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt2
- explicitly require rake for build

* Fri Dec 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt1
- initial
