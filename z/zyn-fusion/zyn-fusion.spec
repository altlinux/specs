Name: zyn-fusion
Version: 3.0.6
Release: alt2

Summary: Zynaddsubfx UI
License: LGPL-2.1
Group: Sound
Url: https://github.com/mruby-zest/mruby-zest-build/

Source: %name-%version-%release.tar

BuildRequires: libglvnd-devel libuv-devel
BuildRequires: /usr/bin/ruby rake

%description
%summary

%prep
%setup -c
sed -ri 's,/opt/zyn-fusion,%_libdir/zyn-fusion,' test-libversion.c
sed -ri  's,\srake$, /usr/lib/ruby/bin/rake,' Makefile

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
* Thu Dec 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt2
- explicitly require rake for build

* Fri Dec 03 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.6-alt1
- initial
