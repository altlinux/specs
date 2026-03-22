%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname voxpupuli-rubocop

Name:          gem-voxpupuli-rubocop
Version:       5.2.0
Release:       alt1
Summary:       Helper Gem that pulls in all the RuboCop related gems and provides a RuboCop configuration
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/voxpupuli/voxpupuli-rubocop
Vcs:           https://github.com/voxpupuli/voxpupuli-rubocop.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-minitest) >= 0.13.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 3.7.0
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-minitest) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 3.7.0,rubocop-rspec < 4
%ruby_use_gem_dependency rubocop-minitest >= 0.13.0,rubocop-minitest < 1
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
Requires:      ruby >= 3.2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4
Provides:      gem(voxpupuli-rubocop) = 5.2.0

%description
Used in Vox Pupuli gems to configure RuboCop in a unified and centralised way


%if_enabled    doc
%package       -n gem-voxpupuli-rubocop-doc
Version:       5.2.0
Release:       alt1
Summary:       Helper Gem that pulls in all the RuboCop related gems and provides a RuboCop configuration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета voxpupuli-rubocop
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(voxpupuli-rubocop) = 5.2.0

%description   -n gem-voxpupuli-rubocop-doc
Helper Gem that pulls in all the RuboCop related gems and provides a RuboCop
configuration documentation files.

Used in Vox Pupuli gems to configure RuboCop in a unified and centralised way

%description   -n gem-voxpupuli-rubocop-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета voxpupuli-rubocop.
%endif


%if_enabled    devel
%package       -n gem-voxpupuli-rubocop-devel
Version:       5.2.0
Release:       alt1
Summary:       Helper Gem that pulls in all the RuboCop related gems and provides a RuboCop configuration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета voxpupuli-rubocop
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(voxpupuli-rubocop) = 5.2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-minitest) >= 0.13.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 3.7.0
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-minitest) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4

%description   -n gem-voxpupuli-rubocop-devel
Helper Gem that pulls in all the RuboCop related gems and provides a RuboCop
configuration development package.

Used in Vox Pupuli gems to configure RuboCop in a unified and centralised way

%description   -n gem-voxpupuli-rubocop-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета voxpupuli-rubocop.
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
%doc CHANGELOG.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-voxpupuli-rubocop-doc
%doc CHANGELOG.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-voxpupuli-rubocop-devel
%doc CHANGELOG.md LICENSE README.md
%endif


%changelog
* Sun Mar 22 2026 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
