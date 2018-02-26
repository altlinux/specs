Name:		edid-decode
Version:	20100205
Release:	alt1
Summary:	EDID decoder and conformance tester
Source:		%name-%version.tar
Group:		System/X11
License:	MIT

%description
%summary

%prep
%setup

%build
%make

%install
%makeinstall
mkdir -p %buildroot/%_datadir
cp -a data %buildroot/%_datadir/

%files
%_bindir/*
%_datadir/*

%changelog
* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 20100205-alt1
- Initial build

