Summary: Collection of tools for reading/writing CPU model specific registers
Name: msr-tools
Version: 1.2
Release: alt1
Group: System/Base
License: GPLv2+
Source0: http://www.kernel.org/pub/linux/utils/cpu/msr-tools/%name-%version.tar
ExclusiveArch: %ix86 x86_64
Url: http://www.kernel.org/pub/linux/utils/cpu/msr-tools/

%description
This is a small collection of tools to allow reading and writing
of CPU model specific registers

%prep
%setup

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
install -D rdmsr %buildroot%_sbindir/rdmsr
install -D wrmsr %buildroot%_sbindir/wrmsr

%files
%_sbindir/rdmsr
%_sbindir/wrmsr

%changelog
* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- Initial build for ALT Linux


