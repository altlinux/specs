%define ver_major 3.2
%define api_ver 3.0
%def_enable introspection

Name: cinnamon-menus
Version: %ver_major.0
Release: alt1

Summary: Cinnamon desktop menu
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/cinnamon-menus
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildPreReq: rpm-build-gnome rpm-build-xdg

# From configure.in
BuildPreReq: intltool >= 0.35 gnome-common
BuildPreReq: libgio-devel >= 2.29.15
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}

%description
This package should not be in a repository. If you see this, please file
a bug to http://bugzilla.altlinux.org against cinnamon-menus component.

%package -n lib%name
Summary: Desktop Menu Library for Cinnamon
License: LGPLv2+
Group: System/Libraries
Provides: cinnamon-menus-common = %version-%release

%description -n lib%name
This package provides Desktop Menu Library for Cinnamon.

%package -n lib%name-devel
Summary: Development files for Cinnamon Desktop Menu Library
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Desktop Menu Library.

%package -n lib%name-devel-examples
Summary: Development utilities and examples for Cinnamon Desktop Menu Library
License: LGPLv2+
Group: Development/Python
BuildArch: noarch
Requires: lib%name = %version-%release

%description -n lib%name-devel-examples
This package provides some examples that use Desktop Menu Library.

%package -n lib%name-gir
Summary: GObject introspection data for the Cinnamon Desktop Menu Library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Cinnamon Desktop Menu Library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Cinnamon Desktop Menu Library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Cinnamon Desktop Menu Library

%add_findreq_skiplist %_xdgmenusdir/*


%prep
%setup -q
%patch0 -p1

%build
[ -d m4 ] || mkdir m4
%autoreconf
%configure \
    --disable-static \
    %{subst_enable introspection}

%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name-%api_ver

%files -n lib%name -f %name-%api_ver.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*
%endif


%changelog
* Fri Nov 11 2016 Vladimir Didenko <cow@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Jun 1 2016 Vladimir Didenko <cow@altlinux.org> 3.0.2-alt1
- 3.0.2

* Mon Apr 25 2016 Vladimir Didenko <cow@altlinux.org> 3.0.0-alt1
- 3.0.0

* Mon Oct 19 2015 Vladimir Didenko <cow@altlinux.org> 2.8.0-alt1
- 2.8.0

* Tue May 19 2015 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1
- 2.6.0

* Tue Apr 14 2015 Vladimir Didenko <cow@altlinux.org> 2.5.0-alt1
- 2.5.0

* Fri Jan 16 2015 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Fri Oct 31 2014 Vladimir Didenko <cow@altlinux.org> 2.4.0-alt1
- 2.4.0

* Mon Apr 14 2014 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Apr 4 2014 Vladimir Didenko <cow@altlinux.org> 2.1.0-alt1
- Initial build
