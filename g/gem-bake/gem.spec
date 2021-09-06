%define        gemname bake

Name:          gem-bake
Version:       0.16.1
Release:       alt1
Summary:       A replacement for rake with a simpler syntax
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/bake
Vcs:           https://github.com/ioquatix/bake.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(samovar) >= 2.1 gem(samovar) < 3
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(samovar) >= 2.1 gem(samovar) < 3
Provides:      gem(bake) = 0.16.1

%description
Bake is a task execution tool, inspired by Rake, but codifying many of the use
cases which are typically implemented in an ad-hoc manner.

Rake is an awesome tool and loved by the community. So, why reinvent it?
Bake provides the following features that Rake does not:

* On demand loading of files following a standard convention. This avoid loading
  all your rake tasks just to execute a single command.
* Better argument handling including support for positional and optional
  arguments.
* Focused on task execution not dependency resolution. Implementation is
  simpler and a bit more predictable.
* Canonical structure for integration with gems.

That being said, Rake and Bake can exist side by side in the same project.


%package       -n bake
Version:       0.16.1
Release:       alt1
Summary:       A replacement for rake with a simpler syntax executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета bake
Group:         Other
BuildArch:     noarch

Requires:      gem(bake) = 0.16.1

%description   -n bake
A replacement for rake with a simpler syntax executable(s).

Bake is a task execution tool, inspired by Rake, but codifying many of the use
cases which are typically implemented in an ad-hoc manner.

Rake is an awesome tool and loved by the community. So, why reinvent it?
Bake provides the following features that Rake does not:

* On demand loading of files following a standard convention. This avoid loading
  all your rake tasks just to execute a single command.
* Better argument handling including support for positional and optional
  arguments.
* Focused on task execution not dependency resolution. Implementation is
  simpler and a bit more predictable.
* Canonical structure for integration with gems.

That being said, Rake and Bake can exist side by side in the same project.

%description   -n bake -l ru_RU.UTF-8
Исполнямка для самоцвета bake.


%package       -n gem-bake-doc
Version:       0.16.1
Release:       alt1
Summary:       A replacement for rake with a simpler syntax documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bake
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bake) = 0.16.1

%description   -n gem-bake-doc
A replacement for rake with a simpler syntax documentation files.

Bake is a task execution tool, inspired by Rake, but codifying many of the use
cases which are typically implemented in an ad-hoc manner.

Rake is an awesome tool and loved by the community. So, why reinvent it?
Bake provides the following features that Rake does not:

* On demand loading of files following a standard convention. This avoid loading
  all your rake tasks just to execute a single command.
* Better argument handling including support for positional and optional
  arguments.
* Focused on task execution not dependency resolution. Implementation is
  simpler and a bit more predictable.
* Canonical structure for integration with gems.

That being said, Rake and Bake can exist side by side in the same project.

%description   -n gem-bake-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bake.


%package       -n gem-bake-devel
Version:       0.16.1
Release:       alt1
Summary:       A replacement for rake with a simpler syntax development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bake
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bake) = 0.16.1
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 0 gem(rspec) < 4

%description   -n gem-bake-devel
A replacement for rake with a simpler syntax development package.

Bake is a task execution tool, inspired by Rake, but codifying many of the use
cases which are typically implemented in an ad-hoc manner.

Rake is an awesome tool and loved by the community. So, why reinvent it?
Bake provides the following features that Rake does not:

* On demand loading of files following a standard convention. This avoid loading
  all your rake tasks just to execute a single command.
* Better argument handling including support for positional and optional
  arguments.
* Focused on task execution not dependency resolution. Implementation is
  simpler and a bit more predictable.
* Canonical structure for integration with gems.

That being said, Rake and Bake can exist side by side in the same project.

%description   -n gem-bake-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bake.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n bake
%_bindir/bake

%files         -n gem-bake-doc
%ruby_gemdocdir

%files         -n gem-bake-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.16.1-alt1
- + packaged gem with Ruby Policy 2.0
