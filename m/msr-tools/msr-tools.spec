Summary: Collection of tools for reading/writing CPU model specific registers
Name: msr-tools
Version: 1.3
Release: alt1
Group: System/Base
License: GPLv2+
ExclusiveArch: %ix86 x86_64
Source0: %name-%version.tar
Url: https://01.org/msr-tools/

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
install -D cpuid %buildroot%_sbindir/cpuid

%files
%_sbindir/rdmsr
%_sbindir/wrmsr
%_sbindir/cpuid

%changelog
* Thu Oct 16 2014 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- new version

* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- Initial build for ALT Linux


