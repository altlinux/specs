Name:		deco
Summary:	deco is a universal archive file extractor
Version:	1.3
Release:	alt1
Group:		Archiving/Compression
License:	BSD
Packager: 	Mikhail Pokidko <pma@altlinux.org>
URL:		http://awesome.naquadah.org/
Source:		%name-%version.tar.gz
Patch1:		%name.patch

%description
deco is a universal archive file extractor that has a consistent command line interface 
("deco 1.tar.bz2 2.zip 3.flac 4.rar 5.deb" will just work) and consistent behavior 
(never deleting archives after extraction and extracting relative to the current working directory,
just verbosely enough, all unless explicitly requested otherwise). 
It creates an extraction directory if there is more than one file or directory at the archive top level, 
and it is able to fix strange permissions. Dozens of archive formats are supported out of the box, 
and the modular design makes adding support for others very easy.

%prep
%setup -q
%patch1 -p1

%build
#configure
%make

%install
%make_install DESTDIR=%buildroot install

%files
%_bindir/%name
%_datadir/%name/*

%changelog
* Wed Jul 30 2008 Mikhail Pokidko <pma@altlinux.org> 1.3-alt1
- Initial ALT build

