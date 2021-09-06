%define        gemname samovar

Name:          gem-samovar
Version:       2.1.4
Release:       alt1
Summary:       Samovar is a flexible option parser excellent support for sub-commands and help documentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/samovar
Vcs:           https://github.com/ioquatix/samovar.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mapping) >= 1.0 gem(mapping) < 2
BuildRequires: gem(console) >= 1.0 gem(console) < 2
# BuildRequires: gem(covered) >= 0
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.6 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Requires:      gem(mapping) >= 1.0 gem(mapping) < 2
Requires:      gem(console) >= 1.0 gem(console) < 2
Provides:      gem(samovar) = 2.1.4

%description
Samovar is a modern framework for building command-line tools and applications.
It provides a declarative class-based DSL for building command-line parsers
that include automatic documentation generation. It helps you keep your
functionality clean and isolated where possible.


%package       -n gem-samovar-doc
Version:       2.1.4
Release:       alt1
Summary:       Samovar is a flexible option parser excellent support for sub-commands and help documentation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета samovar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(samovar) = 2.1.4

%description   -n gem-samovar-doc
Samovar is a flexible option parser excellent support for sub-commands and help
documentation documentation files.

Samovar is a modern framework for building command-line tools and applications.
It provides a declarative class-based DSL for building command-line parsers
that include automatic documentation generation. It helps you keep your
functionality clean and isolated where possible.

%description   -n gem-samovar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета samovar.


%package       -n gem-samovar-devel
Version:       2.1.4
Release:       alt1
Summary:       Samovar is a flexible option parser excellent support for sub-commands and help documentation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета samovar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(samovar) = 2.1.4
Requires:      gem(covered) >= 0
Requires:      gem(bundler) >= 0 gem(bundler) < 3
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.6 gem(rspec) < 4

%description   -n gem-samovar-devel
Samovar is a flexible option parser excellent support for sub-commands and help
documentation development package.

Samovar is a modern framework for building command-line tools and applications.
It provides a declarative class-based DSL for building command-line parsers
that include automatic documentation generation. It helps you keep your
functionality clean and isolated where possible.

%description   -n gem-samovar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета samovar.


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

%files         -n gem-samovar-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-samovar-devel
%doc README.md


%changelog
* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 2.1.4-alt1
- + packaged gem with Ruby Policy 2.0
