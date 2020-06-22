Name:         mapsoft2
Version:      1.1.1
Release:      alt2

Summary:      mapsoft2 - programs for working with maps and geodata
Group:        Sciences/Geosciences
Url:          https://slazav.github.io/mapsoft2/
Packager:     Vladislav Zavjalov <slazav@altlinux.org>
License:      GPL3.0

Source:        %name-%version.tar

BuildRequires: gcc-c++ libgtkmm3-devel libcairomm-devel
BuildRequires: libjansson-devel libxml2-devel libzip-devel zlib-devel libproj-devel
BuildRequires: libjpeg-devel libgif-devel libtiff-devel libpng-devel libdb4.7-devel
BuildRequires: librsvg-devel libcurl-devel
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html /usr/bin/unzip

ExcludeArch: armh

%description
mapsoft2 - programs for working with maps and geodata

%prep
%setup -q

%build
tar -xvf modules.tar
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
* Mon Jun 22 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1.1-alt2
- ExcludeArch: armh (libjpeg + c++ exceptions problem)

* Sun Jun 21 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1.1-alt1
- update documentation, add GB projection alias, further development

* Sat Apr 04 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt2
- fix build on i586 (rounding errors in modules/geom_tools/np.test.cpp)

* Sat Apr 04 2020 Vladislav Zavjalov <slazav@altlinux.org> 1.1-alt1
- add ms2mapdb program - work with mapsoft2 vector maps
  (conversion to/from mp/vmap, rendering)
- basic support for mapdb in ms2view
- ms2proj: --scale, --shift options
- update documentation
- change packaging, use git-submodules, fix a few errors.

* Wed Oct 09 2019 Vladislav Zavjalov <slazav@altlinux.org> 1.0-alt1
- v1.0 - first release, first build for altlinux
