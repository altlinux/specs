Name: cups-filter-sl-watermark
Version: 0.1
Release: alt1

Summary: SeLinux watermarking of printed documents
License: GPL
Group: System/Configuration/Printing
BuildArch: noarch
BuildRequires: rpm-build-python3
Source: %name-%version.tar

%description
Special CUPS filter adding security level watermarks
on printed documents

%prep
%setup

%install
%define cupsdir %_datadir/cups
mkdir -p %buildroot%cupsdir/{data,mime}
mkdir -p %buildroot%_libexecdir/cups/filter
mkdir -p %buildroot/%_sysconfdir
install -pm755 watermark{,.py} %buildroot%_libexecdir/cups/filter/
install -pm644 watermark.{pdf,odt} %buildroot%cupsdir/data/
install -pm644 sl-watermark.{convs,types} %buildroot%cupsdir/mime/
install -pm644 cups-filter-sl-watermark.cfg %buildroot%_sysconfdir/

%files
%_libexecdir/cups/filter/*
%cupsdir/data/*
%cupsdir/mime/*
%_sysconfdir/*

%changelog
* Fri Oct 19 2018 Anton V. Boyarshinov <boyarsh@altlinux.org> 0.1-alt1
- first build


