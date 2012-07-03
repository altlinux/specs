Name: mstflint
Version: 1.4
Release: alt2

Summary: Mellanox firmware burning application
License: GPL/BSD
Url: http://openib.org/

Group: System/Base
Source: http://www.openfabrics.org/downloads/%name-%version.tar
BuildRequires: zlib-devel gcc-c++

%description
This package contains a tool for burning updated firmware on to
Mellanox manufactured InfiniBand adapters.

%prep
%setup -q

%build
%configure
%make_build

%install
make DESTDIR=%buildroot install

%files
%_bindir/*
%_includedir/mtcr_ul/*.h

%changelog
* Tue Aug 17 2010 Andriy Stepanov <stanv@altlinux.ru> 1.4-alt2
- New version (OFED 1.5.1)

* Tue Dec 08 2009 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1
- Initial build

