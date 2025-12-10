%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rubygems-tasks

Name:          gem-rubygems-tasks
Version:       0.3.0
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/rubygems-tasks
Vcs:           https://github.com/postmodern/rubygems-tasks.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(irb) >= 1.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(rake) >= 10.0.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-spellcheck) >= 0
BuildConflicts: gem(irb) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0.0
Requires:      gem(irb) >= 1.0
Requires:      gem(rake) >= 10.0.0
Conflicts:     gem(irb) >= 2
Provides:      gem(rubygems-tasks) = 0.3.0

%description
The Rake tasks which you use to manage a Ruby project should not be coupled to
the project generator which you used to create the project. Project generators
have nothing to do with the Rake tasks used to build, install and release a Ruby
project.

Recently, many Ruby Developers began creating Ruby projects by hand,
building/releasing RubyGems using gem build / gem push. Sometimes this resulted
in RubyGems being released with uncommitted changes, or the developer forgetting
to tag the release. Ruby Developers should have access to agnostic and
unobtrusive Rake tasks, to automate the release process.

This is what rubygems-tasks seeks to provide.


%if_enabled    doc
%package       -n gem-rubygems-tasks-doc
Version:       0.3.0
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubygems-tasks
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubygems-tasks) = 0.3.0

%description   -n gem-rubygems-tasks-doc
rubygems-tasks provides agnostic and unobtrusive Rake tasks for building,
installing and releasing Ruby Gems documentation files.

The Rake tasks which you use to manage a Ruby project should not be coupled to
the project generator which you used to create the project. Project generators
have nothing to do with the Rake tasks used to build, install and release a Ruby
project.

Recently, many Ruby Developers began creating Ruby projects by hand,
building/releasing RubyGems using gem build / gem push. Sometimes this resulted
in RubyGems being released with uncommitted changes, or the developer forgetting
to tag the release. Ruby Developers should have access to agnostic and
unobtrusive Rake tasks, to automate the release process.

This is what rubygems-tasks seeks to provide.

%description   -n gem-rubygems-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rubygems-tasks.
%endif


%if_enabled    devel
%package       -n gem-rubygems-tasks-devel
Version:       0.3.0
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubygems-tasks
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rubygems-tasks) = 0.3.0
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(kramdown) >= 0
Requires:      gem(yard-spellcheck) >= 0

%description   -n gem-rubygems-tasks-devel
rubygems-tasks provides agnostic and unobtrusive Rake tasks for building,
installing and releasing Ruby Gems development package.

The Rake tasks which you use to manage a Ruby project should not be coupled to
the project generator which you used to create the project. Project generators
have nothing to do with the Rake tasks used to build, install and release a Ruby
project.

Recently, many Ruby Developers began creating Ruby projects by hand,
building/releasing RubyGems using gem build / gem push. Sometimes this resulted
in RubyGems being released with uncommitted changes, or the developer forgetting
to tag the release. Ruby Developers should have access to agnostic and
unobtrusive Rake tasks, to automate the release process.

This is what rubygems-tasks seeks to provide.

%description   -n gem-rubygems-tasks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rubygems-tasks.
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
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rubygems-tasks-doc
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rubygems-tasks-devel
%doc ChangeLog.md LICENSE.txt README.md
%endif


%changelog
* Tue Dec 09 2025 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- ^ 0.2.5 -> 0.3.0

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt1
- ^ 0.2.4 -> 0.2.5

* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
