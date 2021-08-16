%define        gemname gnome_app_driver

Name:          gem-gnome-app-driver
Version:       0.3.0
Release:       alt1
Summary:       Test Ruby-GNOME2 applications using Atspi
License:       LGPL-2.1+
Group:         Development/Ruby
Url:           http://www.github.com/mvz/ruby-gnome2_app_driver
Vcs:           https://github.com/mvz/gnome_app_driver.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(gobject-introspection) >= 3.2 gem(gobject-introspection) < 4
BuildRequires: gem(gtk3) >= 3.2 gem(gtk3) < 4
BuildRequires: gem(minitest) >= 5.12 gem(minitest) < 6
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rubocop) >= 1.3.0 gem(rubocop) < 2
BuildRequires: gem(rubocop-minitest) >= 0.10.1 gem(rubocop-minitest) < 1
BuildRequires: gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
BuildRequires: gem(rubocop-performance) >= 1.8.0 gem(rubocop-performance) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
Requires:      gem(gobject-introspection) >= 3.2 gem(gobject-introspection) < 4
Provides:      gem(gnome_app_driver) = 0.3.0


%description
Driver to test the UI of applications using Ruby-GNOME2 by interacting with them
via Atspi.


%package       -n gem-gnome-app-driver-doc
Version:       0.3.0
Release:       alt1
Summary:       Test Ruby-GNOME2 applications using Atspi documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gnome_app_driver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gnome_app_driver) = 0.3.0

%description   -n gem-gnome-app-driver-doc
Test Ruby-GNOME2 applications using Atspi documentation files.

Driver to test the UI of applications using Ruby-GNOME2 by interacting with them
via Atspi.

%description   -n gem-gnome-app-driver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gnome_app_driver.


%package       -n gem-gnome-app-driver-devel
Version:       0.3.0
Release:       alt1
Summary:       Test Ruby-GNOME2 applications using Atspi development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gnome_app_driver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gnome_app_driver) = 0.3.0
Requires:      gem(gtk3) >= 3.2 gem(gtk3) < 4
Requires:      gem(minitest) >= 5.12 gem(minitest) < 6
Requires:      gem(pry) >= 0.13.1 gem(pry) < 1
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rubocop) >= 1.3.0 gem(rubocop) < 2
Requires:      gem(rubocop-minitest) >= 0.10.1 gem(rubocop-minitest) < 1
Requires:      gem(rubocop-packaging) >= 0.5.0 gem(rubocop-packaging) < 0.6
Requires:      gem(rubocop-performance) >= 1.8.0 gem(rubocop-performance) < 2

%description   -n gem-gnome-app-driver-devel
Test Ruby-GNOME2 applications using Atspi development package.

Driver to test the UI of applications using Ruby-GNOME2 by interacting with them
via Atspi.

%description   -n gem-gnome-app-driver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gnome_app_driver.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-gnome-app-driver-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-gnome-app-driver-devel
%doc README.md


%changelog
* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
