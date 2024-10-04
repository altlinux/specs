%define sover   1

Name:           nftables
Epoch:          1
Version:        1.1.1
Release:        alt1
Summary:        nftables is the project that aims to replace the existing {ip,ip6,arp,eb}tables framework
Group:          System/Libraries
License:        GPL-2.0-only
URL:            http://netfilter.org/projects/nftables
Requires:       lib%name%sover = %EVR
# git://git.netfilter.org/nftables
Source:        %name-%version.tar

BuildRequires: libmnl-devel libnftnl-devel flex bison libgmp-devel libreadline-devel asciidoc-a2x libjansson-devel
BuildRequires(pre): docbook2X rpm-build-python3 python3-devel python3-module-setuptools

%description
libnftnl is a userspace library providing a low-level netlink programming interface (API) to the
in-kernel nf_tables subsystem. The library libnftnl has been previously known as libnftables.
This library is currently used by nftables.

%package -n lib%name%sover
Summary: Library for %name
Group: System/Libraries
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR


%description -n lib%name%sover
This package contains shared libraries used by %name.

%package -n lib%name-devel
Summary: Development package that includes the %name header files
Group: Development/C
Requires: lib%name%sover = %EVR

%description -n lib%name-devel
The devel package contains the include files

%package -n python3-module-%name
Summary: Python3 modules and extensions for %name
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%name
Python3 modules and extensions for %name

%prep
%setup

## py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')
sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    $(find ./ -name '*.py')
##

%build
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%autoreconf
%configure --enable-debug \
	   --enable-python \
	   --with-python-bin=/usr/bin/python3 \
	   --with-json \
	   --with-cli=readline
%make_build

%check
make check

%install
%makeinstall_std

( cd py && python3 setup.py install --root=%buildroot --prefix=%_prefix)

#mkdir -p %buildroot%_sysconfdir/nftables
install -dm0755 %buildroot%_docdir/%name
install -pDm0644 nftables.nft %buildroot%_sysconfdir/nftables/nftables.nft
install -dm0755 %buildroot%_unitdir
install -pDm0644 nftables.service %buildroot%_unitdir/nftables.service

%post
%post_service nftables

%files
%doc COPYING files/examples/*.nft files/nftables/*.nft
%dir %_sysconfdir/nftables
%dir %_sysconfdir/nftables/osf
%_sysconfdir/nftables/osf/*
%attr(644,root,root) %config %_sysconfdir/nftables/*.nft
%_unitdir/*
%_sbindir/*
%_man8dir/*

%files -n lib%name%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%_libdir/pkgconfig/*
%_man3dir/*
%_man5dir/*

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Fri Oct 04 2024 Alexei Takaseev <taf@altlinux.org> 1:1.1.1-alt1
- 1.1.1

* Tue Jul 23 2024 Alexei Takaseev <taf@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Mon Nov 20 2023 Alexei Takaseev <taf@altlinux.org> 1:1.0.9-alt2
- Rename lib%name to lib%name%sover (ALT #37280)

* Fri Oct 20 2023 Alexei Takaseev <taf@altlinux.org> 1:1.0.9-alt1
- 1.0.9

* Wed Jul 26 2023 Alexei Takaseev <taf@altlinux.org> 1:1.0.8-alt1
- 1.0.8

* Tue Mar 14 2023 Alexei Takaseev <taf@altlinux.org> 1:1.0.7-alt1
- 1.0.7

* Fri Dec 23 2022 Alexei Takaseev <taf@altlinux.org> 1:1.0.6-alt1
- 1.0.6

* Wed Aug 10 2022 Alexei Takaseev <taf@altlinux.org> 1:1.0.5-alt1
- 1.0.5

* Thu Jun 09 2022 Alexei Takaseev <taf@altlinux.org> 1:1.0.4-alt1
- 1.0.4

* Wed Jun 01 2022 Alexei Takaseev <taf@altlinux.org> 1:1.0.3-alt1
- 1.0.3

* Tue Feb 22 2022 Alexei Takaseev <taf@altlinux.org> 1:1.0.2-alt1
- Version 1.0.2
- Remove devel-static. Not supported by upstream.

* Mon Nov 22 2021 Alexei Takaseev <taf@altlinux.org> 1:1.0.1-alt1
- Version 1.0.1

* Wed Aug 25 2021 Alexei Takaseev <taf@altlinux.org> 1:1.0.0-alt2
- Added -ffat-lto-objects to %optflags_lto.

* Fri Aug 20 2021 Alexei Takaseev <taf@altlinux.org> 1:1.0.0-alt1
- Version 1.0.0

* Thu May 27 2021 Alexei Takaseev <taf@altlinux.org> 1:0.9.9-alt1
- Version 0.9.9

* Thu Mar 25 2021 Alexei Takaseev <taf@altlinux.org> 1:0.9.8-alt1
- Version 0.9.8

* Mon Nov 16 2020 Alexei Takaseev <taf@altlinux.org> 1:0.9.7-alt1
- Version 0.9.7

* Wed Jun 17 2020 Alexei Takaseev <taf@altlinux.org> 1:0.9.6-alt1
- Version 0.9.6

* Fri Apr 03 2020 Alexei Takaseev <taf@altlinux.org> 1:0.9.4-alt1
- Version 0.9.4

* Thu Mar 12 2020 Alexei Takaseev <taf@altlinux.org> 1:0.9.3-alt2
- Split to lib -devel and python subpackages
- Enable python and json features (ALT #38162)

* Tue Dec 03 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.3-alt1
- Version 0.9.3

* Tue Aug 20 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.2-alt1
- Version 0.9.2

* Wed Jun 26 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.1-alt1
- Version 0.9.1

* Tue Jan 15 2019 Alexei Takaseev <taf@altlinux.org> 1:0.9.0-alt2
- Add systemd unit and simple config

* Sat Jun 09 2018 Alexei Takaseev <taf@altlinux.org> 1:0.9.0-alt1
- Version 0.9.0

* Wed May 02 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.4-alt1
- Version 0.8.4

* Sun Mar 04 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.3-alt1
- Version 0.8.3
- Remove dblatex from BR

* Mon Feb 05 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.2-alt1
- Version 0.8.2

* Fri Jan 19 2018 Alexei Takaseev <taf@altlinux.org> 1:0.8.1-alt1
- Version 0.8.1

* Fri Oct 13 2017 Alexei Takaseev <taf@altlinux.org> 1:0.8-alt1
- Version 0.8
- disable pdf

* Wed Dec 21 2016 Alexei Takaseev <taf@altlinux.org> 1:0.7-alt1
- Version 0.7

* Fri Jun 03 2016 Alexei Takaseev <taf@altlinux.org> 1:0.6-alt1
- Version 0.6

* Mon Dec 21 2015 Alexei Takaseev <taf@altlinux.org> 1:0.5-alt1
- Version 0.5

* Wed Sep 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:0.3-alt1.git20140915
- Version 0.3

* Tue Jan 21 2014 Slava Dubrovskiy <dubrsl@altlinux.org> 0.100-alt1
- first build for ALT Linux
