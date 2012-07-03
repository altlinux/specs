%define _name gmime
%def_disable static
%define ver_major 2.4

Name: lib%_name%ver_major
Version: %ver_major.32
Release: alt1

Summary: MIME library
License: LGPLv2+
Group: System/Legacy libraries
Url: http://spruce.sourceforge.net/%_name/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %name-%version.tar

BuildPreReq: rpm-build-mono rpm-build-gnome
BuildPreReq: glib2-devel >= 2.12.0 libgio-devel
BuildPreReq: zlib-devel
BuildPreReq: libgtk-sharp2-devel >= 2.4.0 libgtk-sharp2-gapi
BuildPreReq: gtk-doc >= 1.8 docbook-utils
BuildRequires: gcc-c++ mono-mcs mono-devel
BuildRequires: /proc

%description
GMime is a set of utilities for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME)

%package sharp
Summary: C# bindings
Group: Development/Other
PreReq: %name = %version-%release

%description sharp
C# bindings for %_name

%prep
%setup -q

%build
gtkdocize --copy
#./autogen.sh
%autoreconf
%configure  %{subst_enable static} \
	    --disable-rpath \
	    --enable-mono \
	    --enable-largefile \
	    --disable-gtk-doc
%make

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog README
%_libdir/lib*.so.*

%files sharp
%_monogacdir/gmime-sharp
%_monodir/gmime-sharp-*


%changelog
* Mon Apr 23 2012 Alexey Shabalin <shaba@altlinux.ru> 2.4.32-alt1
- 2.4.32
- build as legacy libraries for compat

* Tue Feb 14 2012 Alexey Shabalin <shaba@altlinux.ru> 2.4.31-alt1
- 2.4.31

* Mon Oct 24 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.26-alt1
- 2.4.26

* Tue Mar 22 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.23-alt1
- 2.4.23
- drop upstreamed patch

* Mon Jan 31 2011 Alexey Shabalin <shaba@altlinux.ru> 2.4.22-alt1
- 2.4.22

* Tue Nov 09 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.20-alt1
- 2.4.20

* Wed May 26 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.17-alt1
- 2.4.17

* Thu Feb 04 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.15-alt1
- 2.4.15

* Thu Jan 07 2010 Alexey Shabalin <shaba@altlinux.ru> 2.4.11-alt1
- 2.4.11
- fixed build with new gtk-doc

* Mon Oct 12 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Wed Jul 08 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.7-alt2
- move pkgconfig files from main to devel package
- cleanup spec

* Mon Apr 27 2009 Yuri N. Sedunov <aris@altlinux.org> 2.4.7-alt1
- 2.4.7

* Mon Apr 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.4.6-alt1
- 2.4.6

* Wed Mar 18 2009 Alexey Shabalin <shaba@altlinux.ru> 2.4.4-alt1
- 2.4.4
- removed obsoleted pre/post scripts

* Mon Oct 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Tue Oct 07 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.2-alt1
- 2.4.2
- fix library name in gmime-sharp.dll.config

* Sat Sep 27 2008 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- 2.4.0
- build devel-doc as noarch

* Sun Jul 20 2008 Yuri N. Sedunov <aris@altlinux.org> 2.2.22-alt1
- new version

* Thu Jun 05 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.21-alt1
- 2.2.21

* Thu May 15 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.19-alt1
- 2.2.19

* Mon Mar 24 2008 Alexey Shabalin <shaba@altlinux.ru> 2.2.18-alt1
- 2.2.18

* Thu Dec 13 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.11-alt1
- 2.2.11
- fix dll.config in sharp package
- enable support for large files 
- enable workarounds for broken rfc2047 encodings

* Sat Sep 08 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.10-alt1
- 2.2.10

* Sun Jul 15 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.9-alt1
- Updated to 2.2.9 (thanks php-coder@)
- /usr/include/gmime-2.0 now belongs to package (#10511)
- Spec cleanup:
  + Added full url to Source tag
  + Removed packages-info-i18n-common from BuildRequires
  + s|%%setup -q|%%setup|
  + s|%%prefix/bin|%%_bindir|
  + Exclude NEWS (was empty) and standard COPYING files from package
  + s|%%_libdir/pkgconfig|%%_pkgconfigdir|
  + Fixed typo in %%changelog: s|beaagle|beagle|

* Mon Apr 02 2007 Alexey Shabalin <shaba@altlinux.ru> 2.2.4-alt1
- 2.2.4

* Thu Nov 23 2006 Alexey Shabalin <shaba@altlinux.ru> 2.2.3-alt1
- NMU: 2.2.3 (needed for beagle-0.2.13)
- move pkgconfig/gmime-sharp.pc to package gmime-sharp
- disable build static libs
- change home url

* Tue Jan 24 2006 Vital Khilko <vk@altlinux.ru> 2.1.19-alt1
- NMU: 2.1.19 (needed for beagle-0.2)

* Wed Jan 18 2006 Vital Khilko <vk@altlinux.ru> 2.1.17-alt1.1
- NMU: added mono bindings

* Fri Dec 23 2005 Andrey Semenov <mitrofan@altlinux.ru> 2.1.17-alt1
- new version

* Fri Sep 16 2005 Andrey Semenov <mitrofan@altlinux.ru> 2.1.14-alt1
- 2.1.14

* Tue Oct 05 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.1.9-alt1
- new version

* Thu Jul 22 2004 Andrey Semenov <mitrofan@altlinux.ru> 2.1.7-alt1
- First version of RPM package
