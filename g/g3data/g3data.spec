Name: g3data
Version: 1.5.4
Release: alt1

Packager: Vladislav Zavjalov <slazav@altlinux.org>

Source: %name-%version.tar

Summary: A tool for extracting data from scanned graphs
License: GPL
Group: Sciences/Other
Url: https://github.com/pn2200/g3data

BuildRequires: libgtk+2-devel

%description
g3data is a tool for extracting data from scanned graphs. For graphs
published in scientific articles the actual data is usually not
explicitly given; g3data makes the process of extracting this data easy.

%prep
%setup -q

%build
%autoreconf
%configure
%make

%install
%makeinstall
mkdir -p %buildroot%_liconsdir
mv %buildroot/usr/share/pixmaps/g3data-icon.png \
   %buildroot%_liconsdir
sed -i -e 's/g3data-icon.xpm/g3data-icon/'\
          %buildroot%_desktopdir/g3data.desktop

%files
%_bindir/*
%_mandir/man1/*
%_desktopdir/*
%_liconsdir/*

%changelog
* Sat Aug 24 2013 Vladislav Zavjalov <slazav@altlinux.org> 1.5.4-alt1
- first build for altlinux

