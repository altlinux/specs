%define        gemname mapping

Name:          gem-mapping
Version:       1.1.1
Release:       alt1
Summary:       Map an input model to an output model using a mapping model
License:       Unlicensed
Group:         Development/Ruby
Url:           https://github.com/ioquatix/mapping
Vcs:           https://github.com/ioquatix/mapping.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.11 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.0 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(mapping) = 1.1.1


%description
Map model objects based on their class to a given output model. Useful for
versioning external interfaces (e.g. JSON APIs) or processing structured data
from one format to another.


%package       -n gem-mapping-doc
Version:       1.1.1
Release:       alt1
Summary:       Map an input model to an output model using a mapping model documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mapping
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mapping) = 1.1.1

%description   -n gem-mapping-doc
Map an input model to an output model using a mapping model documentation
files.

Map model objects based on their class to a given output model. Useful for
versioning external interfaces (e.g. JSON APIs) or processing structured data
from one format to another.

%description   -n gem-mapping-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mapping.


%package       -n gem-mapping-devel
Version:       1.1.1
Release:       alt1
Summary:       Map an input model to an output model using a mapping model development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mapping
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mapping) = 1.1.1
Requires:      gem(bundler) >= 1.11 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.0 gem(rspec) < 4

%description   -n gem-mapping-devel
Map an input model to an output model using a mapping model development
package.

Map model objects based on their class to a given output model. Useful for
versioning external interfaces (e.g. JSON APIs) or processing structured data
from one format to another.

%description   -n gem-mapping-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mapping.


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

%files         -n gem-mapping-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mapping-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.1-alt1
- + packaged gem with Ruby Policy 2.0
