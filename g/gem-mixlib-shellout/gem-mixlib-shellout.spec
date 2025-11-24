%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname mixlib-shellout

Name:          gem-mixlib-shellout
Version:       3.4.9
Release:       alt1
Summary:       mixin library for subprocess management, output collection
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/mixlib-shellout
Vcs:           https://github.com/chef/mixlib-shellout.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(chef-utils) >= 0
BuildRequires: gem(cookstyle) >= 7.32.8
BuildRequires: gem(logger) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1
Requires:      gem(chef-utils) >= 0
Requires:      gem(logger) >= 0
Obsoletes:     ruby-mixlib-shellout < %EVR
Provides:      ruby-mixlib-shellout = %EVR
Provides:      gem(mixlib-shellout) = 3.4.9

%description
Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.


%if_enabled    doc
%package       -n gem-mixlib-shellout-doc
Version:       3.4.9
Release:       alt1
Summary:       mixin library for subprocess management, output collection documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mixlib-shellout
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(mixlib-shellout) = 3.4.9

%description   -n gem-mixlib-shellout-doc
mixin library for subprocess management, output collection documentation
files.

Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.

%description   -n gem-mixlib-shellout-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mixlib-shellout.
%endif


%if_enabled    devel
%package       -n gem-mixlib-shellout-devel
Version:       3.4.9
Release:       alt1
Summary:       mixin library for subprocess management, output collection development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mixlib-shellout
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(mixlib-shellout) = 3.4.9
Requires:      gem(cookstyle) >= 7.32.8
Requires:      gem(pry) >= 0
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rb-readline) >= 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rspec) >= 4

%description   -n gem-mixlib-shellout-devel
mixin library for subprocess management, output collection development
package.

Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.

%description   -n gem-mixlib-shellout-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mixlib-shellout.
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
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-mixlib-shellout-doc
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-mixlib-shellout-devel
%doc LICENSE CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%endif


%changelog
* Fri Nov 21 2025 Pavel Skrylev <majioa@altlinux.org> 3.4.9-alt1
- ^ 3.2.5 -> 3.4.9

* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 3.2.5-alt1
- ^ 3.1.4 -> 3.2.5

* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.1.4-alt1
- ^ 3.0.11 -> 3.1.4

* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.11-alt1
- > Ruby Policy 2.0
- ^ 2.4.0 -> 3.0.11

* Fri Aug 31 2018 Andrey Cherepanov <cas@altlinux.org> 2.4.0-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Feb 16 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- Initial build for ALT Linux
