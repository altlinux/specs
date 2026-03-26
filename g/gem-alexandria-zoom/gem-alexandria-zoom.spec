%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%define        gemname alexandria-zoom

Name:          gem-alexandria-zoom
Version:       0.6.1
Release:       alt1
Summary:       Ruby bindings for the Z39.50 Object-Orientation Model (ZOOM)
License:       LGPL-2.1-or-later
Group:         Development/Ruby
Url:           https://github.com/mvz/alexandria-zoom
Vcs:           https://github.com/mvz/alexandria-zoom.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
BuildRequires: libyaz-devel
%if_enabled check
BuildRequires: gem(pkg-config) >= 1.6.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rake-manifest) >= 0.2.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(test-unit) >= 3.3
BuildConflicts: gem(pkg-config) >= 1.7
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rake-manifest) >= 0.3
BuildConflicts: gem(rdoc) >= 8
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Requires:      ruby >= 3.2.0
Requires:      gem(pkg-config) >= 1.6.0
Conflicts:     gem(pkg-config) >= 1.7
Provides:      gem(alexandria-zoom) = 0.6.1

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model (ZOOM),
an abstract object-oriented programming interface to a subset of the services
specified by the Z39.50 standard, also known as the international standard ISO
23950.


%if_enabled    devel
%package       -n gem-alexandria-zoom-devel
Version:       0.6.1
Release:       alt1
Summary:       Ruby bindings for the Z39.50 Object-Orientation Model (ZOOM) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета alexandria-zoom
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(alexandria-zoom) = 0.6.1
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rake-manifest) >= 0.2.0
Requires:      gem(rdoc) >= 6.1.1
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(test-unit) >= 3.3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rake-manifest) >= 0.3
Conflicts:     gem(rdoc) >= 8
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(test-unit) >= 4

%description   -n gem-alexandria-zoom-devel
Ruby bindings for the Z39.50 Object-Orientation Model (ZOOM) development
package.

Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation Model (ZOOM),
an abstract object-oriented programming interface to a subset of the services
specified by the Z39.50 standard, also known as the international standard ISO
23950.

%description   -n gem-alexandria-zoom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета alexandria-zoom.
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
%doc CHANGELOG.md ChangeLog.old LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    devel
%files         -n gem-alexandria-zoom-devel
%doc CHANGELOG.md ChangeLog.old LICENSE README.md
%ruby_includedir/*
%endif


%changelog
* Wed Mar 25 2026 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
