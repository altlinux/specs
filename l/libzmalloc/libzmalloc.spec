%define _altdata_dir %_datadir/alterator

Name: libzmalloc
Version: 0.1
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Source:%name-%version.tar

Summary: simple malloc replacement
License: GPL
Group: System/Libraries

BuildPreReq: alterator >= 2.9-alt0.10, alterator-fbi >= 0.7-alt1

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator


%description
simple malloc replacement

%prep
%setup -q

%build
%make_build

%install
%makeinstall libdir=%buildroot/lib bindir=%buildroot/bin

%files
%doc test1.c test2.c 
/lib/*
/bin/*

%changelog
* Wed May 23 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial release
