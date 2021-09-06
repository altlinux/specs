%define        gemname coffee-script-source

Name:          gem-coffee-script-source
Version:       2.1.1
Release:       alt2.1
Summary:       CoffeeScript js sources
License:       MIT
Group:         Development/Ruby
Url:           http://coffeescript.org/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 1.16 gem(bundler) < 3
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(coffee-script-source) = 2.1.1


%description
CoffeeScript is a little language that compiles into JavaScript. Underneath all
of those embarrassing braces and semicolons, JavaScript has always had a
gorgeous object model at its heart. CoffeeScript is an attempt to expose the
good parts of JavaScript in a simple way.

This is the CoffeeScript js sources.


%package       -n gem-coffee-script-source-doc
Version:       2.1.1
Release:       alt2.1
Summary:       CoffeeScript js sources documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета coffee-script-source
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(coffee-script-source) = 2.1.1

%description   -n gem-coffee-script-source-doc
CoffeeScript js sources documentation files.

CoffeeScript is a little language that compiles into JavaScript. Underneath all
of those embarrassing braces and semicolons, JavaScript has always had a
gorgeous object model at its heart. CoffeeScript is an attempt to expose the
good parts of JavaScript in a simple way.

This is the CoffeeScript js sources.

%description   -n gem-coffee-script-source-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета coffee-script-source.


%package       -n gem-coffee-script-source-devel
Version:       2.1.1
Release:       alt2.1
Summary:       CoffeeScript js sources development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета coffee-script-source
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(coffee-script-source) = 2.1.1
Requires:      gem(bundler) >= 1.16 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14

%description   -n gem-coffee-script-source-devel
CoffeeScript js sources development package.

CoffeeScript is a little language that compiles into JavaScript. Underneath all
of those embarrassing braces and semicolons, JavaScript has always had a
gorgeous object model at its heart. CoffeeScript is an attempt to expose the
good parts of JavaScript in a simple way.

This is the CoffeeScript js sources.

%description   -n gem-coffee-script-source-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета coffee-script-source.


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

%files         -n gem-coffee-script-source-doc
%ruby_gemdocdir

%files         -n gem-coffee-script-source-devel


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt2.1
- ! spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt2
- ! spec according to changelog rules

* Fri Aug 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- + packaged gem with usage Ruby Policy 2.0
