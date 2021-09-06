%define        gemname build-files

Name:          gem-build-files
Version:       1.7.1
Release:       alt1
Summary:       Abstractions for handling and mapping paths
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/build-files
Vcs:           https://github.com/ioquatix/build-files.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(rspec) >= 3.4 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(build-files) = 1.7.1


%description
Build::Files is a set of idiomatic classes for dealing with paths and
monitoring directories. File paths are represented with both root and relative
parts which makes copying directory structures intuitive.


%package       -n gem-build-files-doc
Version:       1.7.1
Release:       alt1
Summary:       Abstractions for handling and mapping paths documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета build-files
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(build-files) = 1.7.1

%description   -n gem-build-files-doc
Abstractions for handling and mapping paths documentation files.

Build::Files is a set of idiomatic classes for dealing with paths and
monitoring directories. File paths are represented with both root and relative
parts which makes copying directory structures intuitive.

%description   -n gem-build-files-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета build-files.


%package       -n gem-build-files-devel
Version:       1.7.1
Release:       alt1
Summary:       Abstractions for handling and mapping paths development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета build-files
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(build-files) = 1.7.1
Requires:      gem(bundler) >= 0
Requires:      gem(covered) >= 0
Requires:      gem(rspec) >= 3.4 gem(rspec) < 4

%description   -n gem-build-files-devel
Abstractions for handling and mapping paths development package.

Build::Files is a set of idiomatic classes for dealing with paths and
monitoring directories. File paths are represented with both root and relative
parts which makes copying directory structures intuitive.

%description   -n gem-build-files-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета build-files.


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

%files         -n gem-build-files-doc
%ruby_gemdocdir

%files         -n gem-build-files-devel


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- + packaged gem with Ruby Policy 2.0
