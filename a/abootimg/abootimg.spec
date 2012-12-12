Name: abootimg
Version: 0.6
Release: alt1

Summary: A tool to read/write/update android boot images
License: GPL
Group: System/Kernel and hardware
Url: http://gitorious.org/ac100/abootimg

Source: %name-%version-%release.tar

BuildRequires: libblkid-devel

%description
%summary

%prep
%setup

%build
make CFLAGS='%optflags'

%install
install -pm0755 abootimg -D %buildroot%_bindir/abootimg
install -pm0755 abootimg-*-initrd %buildroot%_bindir/
install -pm0644 -D debian/abootimg.1 %buildroot%_man1dir/abootimg.1

%files
%doc README
%_bindir/*
%_man1dir/abootimg.1*

%changelog
* Wed Dec 12 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6-alt1
- 0.6 released
