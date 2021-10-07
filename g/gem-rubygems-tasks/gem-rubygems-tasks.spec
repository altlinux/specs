%define        gemname rubygems-tasks

Name:          gem-rubygems-tasks
Version:       0.2.5
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/rubygems-tasks
Vcs:           https://github.com/postmodern/rubygems-tasks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(irb) >= 1.0 gem(irb) < 2
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4
BuildRequires: gem(yard) >= 0.8 gem(yard) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rubygems-project,rubygems-project-lite,bundler-project
Requires:      gem(irb) >= 1.0 gem(irb) < 2
Provides:      gem(rubygems-tasks) = 0.2.5


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


%package       -n gem-rubygems-tasks-doc
Version:       0.2.5
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rubygems-tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rubygems-tasks) = 0.2.5

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


%package       -n gem-rubygems-tasks-devel
Version:       0.2.5
Release:       alt1
Summary:       rubygems-tasks provides agnostic and unobtrusive Rake tasks for building, installing and releasing Ruby Gems development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rubygems-tasks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rubygems-tasks) = 0.2.5
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4
Requires:      gem(yard) >= 0.8 gem(yard) < 1

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

%files         -n gem-rubygems-tasks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rubygems-tasks-devel
%doc README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.5-alt1
- ^ 0.2.4 -> 0.2.5

* Tue Feb 26 2019 Pavel Skrylev <majioa@altlinux.org> 0.2.4-alt1
- Initial build for Sisyphus with usage of Ruby Policy 2.0.
