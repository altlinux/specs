Name: iucode_tool
Version: 2.3.1
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
export CFLAGS=$RPM_OPT_FLAGS
%configure
%make_build

%install
make install DESTDIR=%buildroot INSTALL="install -p"

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%_man8dir/*
%_sbindir/%name

%changelog
* Mon Apr 30 2018 L.A. Kostis <lakostis@altlinux.ru> 2.3.1-alt1
- 2.3.1.

* Wed Sep 13 2017 L.A. Kostis <lakostis@altlinux.ru> 2.2-alt1
- 2.2.

* Thu May 25 2017 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt1
- Updated to 2.1.2.

* Fri Jan 06 2017 L.A. Kostis <lakostis@altlinux.ru> 2.1-alt1
- Updated to 2.1.

* Wed Jun 08 2016 L.A. Kostis <lakostis@altlinux.ru> 1.6.1-alt1
- first build for ALTinux.
