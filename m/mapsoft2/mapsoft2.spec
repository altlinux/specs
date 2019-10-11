Name:         mapsoft2
Version:      1.0
Release:      alt1

Summary:      mapsoft2 - programs for working with maps and geodata
Group:        Sciences/Geosciences
Url:          https://slazav.github.io/mapsoft2/
Packager:     Vladislav Zavjalov <slazav@altlinux.org>
License:      GPL3.0

Source:        %name-%version.tar

BuildRequires: gcc-c++ libgtkmm3-devel libcairomm-devel
BuildRequires: libjansson-devel libxml2-devel libzip-devel zlib-devel libproj-devel
BuildRequires: libjpeg-devel libgif-devel libtiff-devel libpng-devel libdb4.7-devel
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html /usr/bin/unzip

%description
mapsoft2 - programs for working with maps and geodata

%prep
%setup -q

%build
export SKIP_IMG_DIFFS=1
%make

%install
%makeinstall initdir=%buildroot%_initdir

%files
%_bindir/ms2*
%_mandir/man1/ms2*
%_mandir/man5/mapsoft2*
%_datadir/mapsoft2/mapsoft2.css

%changelog
* Wed Oct 09 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- v1.0 - first release, first build for altlinux
