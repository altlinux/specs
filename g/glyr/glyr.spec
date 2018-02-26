Name: glyr
Version: 0.9.8
Release: alt1
Summary: Music related metadata searchengine
License: GPLv3
Group: System/Libraries
Url: https://github.com/sahib/glyr
Packager: Egor Glukhov <kaman@altlinux.org>
Source: %name-%version.tar

BuildPreReq: cmake rpm-macros-cmake
BuildRequires: glib2-devel libcurl-devel libsqlite3-devel

Requires: lib%name = %version-%release

%description
Glyr CLI tool.

The sort of metadata glyr is searching (and downloading) is usually the
data you see in your musicplayer. And indeed, originally it was written
to serve as internally library for a musicplayer, but has been extended
to work as a standalone program which is able to download:

* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example
  links to wikipedia;
* similar artists;
* similar songs.

%package -n lib%name
Summary: Searcheninge for Musicrelated Metadata
Group: System/Libraries

%description -n lib%name
Glyr shared library.

%package -n lib%name-devel
Summary: Searcheninge for Musicrelated Metadata
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Glyr development files.

%prep
%setup

%build
%cmake_insource
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS CHANGELOG README.textile TODO
%_bindir/glyrc

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%doc src/examples
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Fri Apr 20 2012 Egor Glukhov <kaman@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus
