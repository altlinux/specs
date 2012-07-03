Version: 0.3.1
Release: alt1.qa1
Name: liblscp
Summary: LinuxSampler control protocol API
License: LGPL
Group: Sound
Url: http://www.linuxsampler.org/
Source: %name-%version.tar.gz

# Automatically added by buildreq on Sat Nov 05 2005
BuildRequires: doxygen gcc-c++ libstdc++-devel

%package devel
Summary: Include files for developing apps which will use %name
Group: Development/C++
Requires: %name = %version-%release

%description
liblscp is an implementation of the LinuxSampler control protocol,
proposed as a C language API.

This package is required to use qsampler, GUI frontend to LinuxSampler.

%description devel
This package contains development files needed to develop programs that
use the %name library.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/*.so*
%doc ChangeLog AUTHORS README TODO

%files devel
%_libdir/pkgconfig/lscp.pc
%_includedir/*

%changelog
* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.3.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liblscp
  * postun_ldconfig for liblscp
  * postclean-05-filetriggers for spec file

* Sat Nov 05 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.3.1-alt1
- Initial build for ALT Linux

