Summary: A printer filter for Minolta 1[234]xx W printers

Name: min12xxw
Version: 0.0.9
Release: alt1

Packager: Stanislav Ievlev <inger@altlinux.org>

Copyright: GPL
Group: Publishing

URL: http://www.hinterbergen.de/mala/min12xxw/
Source: http://www.hinterbergen.de/mala/min12xxw/%{name}-%{version}.tar.gz

%description
This is min12xxw, a filter to convert pbmraw data such as produced by
ghostscript to the printer language of Minolta 1[234]xx W printers.

%prep

%setup -q

%build

%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS COPYING ChangeLog FAQ NEWS README format.txt
%_bindir/*
%_man1dir/*


%changelog
* Wed Nov 07 2007 Stanislav Ievlev <inger@altlinux.org> 0.0.9-alt1
- Initial build
