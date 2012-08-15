
Name: libzmalloc
Version: 0.2
Release: alt1

Packager: Packager: Andriy Stepanov <stanv@altlinux.ru>

Source:%name-%version.tar
Source1: %name.control

Summary: simple malloc replacement
License: GPL
Group: System/Libraries

PreReq: control

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator


%description
simple malloc replacement

%prep
%setup -q

%pre
%pre_control %name

%post
%post_control -s disable %name
echo "WARNING: zmalloc-disable & zmalloc-enable deprecated! Use zmalloc-ctrl instead." >&2

%build
%make_build

%install
%makeinstall libdir=%buildroot/lib bindir=%buildroot/bin
%__install -pD -m755 %SOURCE1 %buildroot%_controldir/%name

%files
%doc test1.c test2.c 
%_controldir/%name
/lib/*
/bin/*

%changelog
* Wed Aug 15 2012 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Use "control" system. Use one ctrl binary.

* Wed May 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
