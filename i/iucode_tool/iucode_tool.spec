Name: iucode_tool
Version: 2.1
Release: alt1
Summary: Intel(r) 64 and IA-32 processor microcode tool 

Group: System/Base
License: GPLv2
Url: https://gitlab.com/iucode-tool
Source0: iucode-tool_%{version}.tar.xz 

%description
Tool to manipulate Intel IA32/X86_64 microcode bundles.

%prep
%setup -n iucode-tool_%{version}

%build
%autoreconf
%configure
%make_build

%install
make install DESTDIR=%buildroot INSTALL="install -p"

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_man8dir/*
%_sbindir/%name

%changelog
* Fri Jan 06 2017 L.A. Kostis <lakostis@altlinux.ru> 2.1-alt1
- Updated to 2.1.

* Wed Jun 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1.6.1-alt1
- first build for ALTinux.
