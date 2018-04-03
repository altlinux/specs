%def_disable docs

Name: 	 ruby-gnome2
Version: 3.2.3
Release: alt1
 
Summary: Ruby bindings for GNOME
License: MIT/Ruby
Group:   Development/Ruby
Url:     https://github.com/ruby-gnome2/ruby-gnome2
 
Packager:  Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:  %name-%version.tar
Patch1:  glib2-disable-rake_extensiontask.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: ruby-tool-setup
BuildRequires: libruby-devel
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpixman-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: libexpat-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libdrm-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libvte-devel
BuildRequires: ruby-pkg-config
BuildRequires: gobject-introspection-devel
BuildRequires: ruby-native-package-installer
# TODO BuildRequires: ruby-cairo for GTK+ support

%filter_from_requires \,^ruby(\(cairo\|rake/extensiontask\|ruby_installer/runtime\))$,d

%description
This is a set of bindings for the GNOME 2.x and 3.x libraries to use
from Ruby 2.1, 2.2, 2.3 and 2.4.

%package -n ruby-glib2
Summary: GLib 2 bindings for the Ruby language
Group: Development/Ruby

%description -n ruby-glib2
GLib is a useful general-purpose C library, notably used by GTK+ and
GNOME. This package contains libraries for using GLib 2 with the Ruby
programming language. It is most likely useful in conjunction with Ruby
bindings for other libraries such as GTK+.

%package devel
Summary: Development files for GLib 2 bindings for the Ruby language
Group: Development/Ruby

%description devel
GLib is a useful general-purpose C library, notably used by GTK+ and
GNOME. This package contains libraries for using GLib 2 with the Ruby
programming language. It is most likely useful in conjunction with Ruby
bindings for other libraries such as GTK+.

This packages contains header files for ruby-glib2

%if_enabled docs
%package doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description doc
Documentation files for %{name}.
%endif

%prep
%setup
%patch1 -p1
%update_setup_rb
 
%build
%ruby_config
#ruby_build
%rake build
 
%install
#ruby_install
%makeinstall_std -C glib2
#makeinstall_std -C atk

%if_enabled docs
rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}
%endif

%check
#ruby_test_unit -Ilib:test test
 
%files -n ruby-glib2
%doc README*
%ruby_sitelibdir/glib2
%ruby_sitelibdir/glib2.rb
%ruby_sitearchdir/glib2.so

%files devel
%ruby_sitelibdir/gnome2
%ruby_sitelibdir/glib-mkenums.rb
%ruby_sitelibdir/gnome2-raketask.rb
%ruby_sitelibdir/mkmf-gnome2.rb
%ruby_sitearchdir/*.h

%if_enabled docs
%files doc
%ruby_ri_sitedir/*
%endif

%changelog
* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt1
- New version.

* Mon Apr 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.2-alt1
- New version.

* Sat Mar 31 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.
- Build with gstreamer1.0-devel.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Apr 21 2017 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build in Sisyphus
