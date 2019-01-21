%define     pkgname glib2

Name: 	    ruby-gnome2
Version:    3.3.1
Release:    alt1
 
Summary:    Ruby bindings for GNOME
License:    MIT
Group:      Development/Ruby
Url:        https://ruby-gnome2.osdn.jp/
# VCS:      https://github.com/ruby-gnome2/ruby-gnome2.git
Packager:   Ruby Maintainers Team <ruby@packages.altlinux.org>
 
Source:     %pkgname-%version.tar
Source1:    %pkgname-%version.gemspec
#Patch1:  glib2-disable-rake_extensiontask.patch
 
BuildRequires(pre): rpm-build-ruby
BuildRequires: libgtk+2-devel
BuildRequires: libgtk+3-devel
BuildRequires: libpixman-devel
BuildRequires: gstreamer1.0-devel
BuildRequires: libexpat-devel
BuildRequires: libharfbuzz-devel
BuildRequires: libdrm-devel
BuildRequires: libpcre-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXdamage-devel
BuildRequires: libXxf86vm-devel
BuildRequires: libvte3-devel
BuildRequires: gobject-introspection-devel
BuildRequires: ruby-pkg-config gem(native-package-installer) gem(cairo) gem(rake) gem(rake-compiler)
BuildRequires: ruby-mechanize


%description
This is a set of bindings for the GNOME 2.x and 3.x libraries to use
from Ruby 2.1, 2.2, 2.3 and 2.4.

%package -n ruby-%pkgname
Summary: GLib 2 bindings for the Ruby language
Group: Development/Ruby

%description -n ruby-%pkgname
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

This packages contains header files for ruby-%pkgname

%package -n ruby-%pkgname-doc
Summary: Documentation files for %name
Group: Documentation
 
BuildArch: noarch
 
%description -n ruby-%pkgname-doc
Documentation files for %{name}.

%prep
%setup -n %pkgname-%version
#%patch1 -p1
%update_setup_rb
cp %SOURCE1 ./
 
%build
%ruby_config -- --use-system-libraries
%ruby_build
%rake build
 
%install
%makeinstall_std -C glib2
%ruby_install

%rdoc lib/
# Remove unnecessary files
rm -f %buildroot%ruby_ri_sitedir/{Object/cdesc-Object.ri,cache.ri,created.rid}

%check
%ruby_test
 
%files -n ruby-%pkgname
%doc README*
%ruby_sitelibdir/%pkgname
%ruby_sitelibdir/%pkgname.rb
%ruby_sitearchdir/%pkgname.so
%rubygem_specdir/*

%files devel
#%ruby_sitelibdir/*.h
%ruby_sitelibdir/gnome2
%ruby_sitelibdir/glib-mkenums.rb
%ruby_sitelibdir/gnome2-raketask.rb
%ruby_sitelibdir/mkmf-gnome2.rb
%ruby_sitearchdir/*.h

%files -n ruby-%pkgname-doc
%ruby_ri_sitedir/*

%changelog
* Sun Jan 20 2019 Pavel Skrylev <majioa@altlinux.org> 3.3.1-alt1
- Bump to 3.3.1 gem.

* Fri Oct 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt2
- Fix build (add libpcre-devel).

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.9-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 07 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.7-alt1
- New version.

* Wed Jun 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.6-alt1
- New version.

* Wed May 02 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.5-alt1
- New version.

* Mon Apr 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.4-alt1
- New version.

* Tue Apr 03 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.3-alt2
- Build with libvte3.

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
