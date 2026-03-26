%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gnome_app_driver

Name:          gem-gnome-app-driver
Version:       0.3.4
Release:       alt1
Summary:       Test Ruby-GNOME2 applications using Atspi
License:       LGPL-2.1-or-later
Group:         Development/Ruby
Url:           http://www.github.com/mvz/ruby-gnome2_app_driver
Vcs:           https://github.com/mvz/gnome_app_driver.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(gobject-introspection) >= 3.2
BuildRequires: gem(gtk3) >= 3.2
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-packaging) >= 0.5.2
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildConflicts: gem(gobject-introspection) >= 5.0
BuildConflicts: gem(gtk3) >= 5.0
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_alias_names gnome_app_driver,gnome-app-driver
Requires:      ruby >= 3.2.0
Requires:      gem(gobject-introspection) >= 3.2
Conflicts:     gem(gobject-introspection) >= 5.0
Provides:      gnome_app_driver = %EVR
Provides:      gem(gnome_app_driver) = 0.3.4

%description
Driver to test the UI of applications using Ruby-GNOME2 by interacting with them
via Atspi.


%if_enabled    doc
%package       -n gem-gnome-app-driver-doc
Version:       0.3.4
Release:       alt1
Summary:       Test Ruby-GNOME2 applications using Atspi documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gnome_app_driver
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gnome_app_driver) = 0.3.4

%description   -n gem-gnome-app-driver-doc
Test Ruby-GNOME2 applications using Atspi documentation files.

Driver to test the UI of applications using Ruby-GNOME2 by interacting with them
via Atspi.

%description   -n gem-gnome-app-driver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gnome_app_driver.
%endif


%if_enabled    devel
%package       -n gem-gnome-app-driver-devel
Version:       0.3.4
Release:       alt1
Summary:       Test Ruby-GNOME2 applications using Atspi development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gnome_app_driver
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(gnome_app_driver) = 0.3.4
Requires:      gem(gobject-introspection) >= 3.2
Requires:      gem(gtk3) >= 3.2
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-packaging) >= 0.5.2
Requires:      gem(rubocop-performance) >= 1.11.3
Conflicts:     gem(gobject-introspection) >= 5.0
Conflicts:     gem(gtk3) >= 5.0
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2

%description   -n gem-gnome-app-driver-devel
Test Ruby-GNOME2 applications using Atspi development package.

Driver to test the UI of applications using Ruby-GNOME2 by interacting with them
via Atspi.

%description   -n gem-gnome-app-driver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gnome_app_driver.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Changelog.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gnome-app-driver-doc
%doc Changelog.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gnome-app-driver-devel
%doc Changelog.md LICENSE README.md
%endif


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.4-alt1
- ^ 0.3.2 -> 0.3.4

* Sat Jun 24 2023 Pavel Skrylev <majioa@altlinux.org> 0.3.2-alt1
- ^ 0.3.0 -> 0.3.2

* Thu Jul 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
