Name: shared-color-profiles
Version: 0.1.5
Release: alt1

Summary: Shared color profiles to be used in color management aware applications
Group: Graphics
Url: http://github.com/hughsie/shared-color-profiles
License: GPLv2+ and Public Domain and zlib and MIT

Source: http://people.freedesktop.org/~hughsient/releases/%name-%version.tar.gz

BuildArch: noarch

%description
The shared-color-profiles package contains various profiles which are
useful for programs that are color management aware.

%package extra
Summary: More color profiles for color management that are less commonly used
Group: Graphics
Requires: %name = %version-%release

%description extra
More color profiles for color management that are less commonly used.
This may be useful for CMYK soft-proofing or for extra device support.

%prep
%setup

%build
%configure

%install
%make DESTDIR=%buildroot install

%files
%dir %_datadir/shared-color-profiles

# Argyll
%dir %_datadir/color/icc/Argyll
%dir %_datadir/shared-color-profiles/Argyll
%_datadir/shared-color-profiles/Argyll/*

# common colorspaces
%_datadir/color/icc/Argyll/lab2lab.icm
%_datadir/color/icc/Argyll/*RGB*.ic?

# so we can display at least something in the default dropdown
%_datadir/color/icc/Fogra27L.icc
%_datadir/color/icc/Oysonar/Gray.icc

# monitor test profiles
%_datadir/color/icc/bluish.icc
%_datadir/color/icc/AdobeGammaTest.icm

# abstract profiles
%_datadir/color/icc/Yamma
%_datadir/shared-color-profiles/Yamma

%doc AUTHORS NEWS README

%files extra
# Oysonar
%dir %_datadir/color/icc/Oysonar
%_datadir/color/icc/Oysonar/FOGRA*.icc
%_datadir/color/icc/Oysonar/GRACoL*.icc
%_datadir/color/icc/Oysonar/SNAP*.icc
%_datadir/color/icc/Oysonar/SWOP*.icc
%_datadir/color/icc/Oysonar/Gray-CIE_L.icc
%_datadir/color/icc/Fake*.icc
%_datadir/shared-color-profiles/Oysonar/*


%changelog
* Fri Jan 27 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.5-alt1
- 0.1.5

* Thu Oct 13 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- adapted for Sisyphus

* Fri Apr 08 2011 Richard Hughes <rhughes@redhat.com> - 0.1.4-1
- New upstream release.
- Much quicker colord startup when using colord >= 0.1.6

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 01 2010 Richard Hughes <rhughes@redhat.com> - 0.1.3-1
- New upstream release.
- Rename the Oyranos profiles to Oysonar to fix Kai-Uwe Behrmann's
  reported license violation.
- Resolves: #657552

* Fri Oct 01 2010 Richard Hughes <rhughes@redhat.com> - 0.1.2-1
- New upstream release.

* Tue Apr 06 2010 Richard Hughes <rhughes@redhat.com> - 0.1.1-1
- New upstream release.
- Update to the latest version of the Fedora Packaging Guidelines
- Install some CMYK profiles to an -extra subpackage as most users will not
  need these and they are over 15Mb in size and will clog up the desktop spin.

* Mon Dec 07 2009 Richard Hughes <richard@hughsie.com> 0.1.0-1
- Initial import of 0.1.0

