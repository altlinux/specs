%define        gemname dotenv

Name:          gem-dotenv
Version:       2.7.6
Release:       alt1
Summary:       Loads environment variables from `.env`
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bkeepers/dotenv
Vcs:           https://github.com/bkeepers/dotenv.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(railties) >= 3.2
BuildRequires: gem(spring) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0.40.0 gem(rubocop) < 2

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
Requires:      gem(dotenv) = 2.7.6
Requires:      gem(railties) >= 3.2
Provides:      gem(dotenv-rails) = 2.7.6


%description
Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%package       -n gem-dotenv-rails
Version:       2.7.6
Release:       alt1
Summary:       Autoload dotenv in Rails
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(dotenv) = 2.7.6

%description   -n gem-dotenv-rails
Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%package       -n dotenv
Version:       2.7.6
Release:       alt1
Summary:       Loads environment variables from `.env` executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета dotenv
Group:         Other
BuildArch:     noarch

Requires:      gem(dotenv) = 2.7.6

%description   -n dotenv
Loads environment variables from `.env` executable(s).

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.

%description   -n dotenv -l ru_RU.UTF-8
Исполнямка для самоцвета dotenv.


%package       -n gem-dotenv-doc
Version:       2.7.6
Release:       alt1
Summary:       Loads environment variables from `.env` documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dotenv
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dotenv) = 2.7.6

%description   -n gem-dotenv-doc
Loads environment variables from `.env` documentation files.

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%description   -n gem-dotenv-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dotenv.


%package       -n gem-dotenv-devel
Version:       2.7.6
Release:       alt1
Summary:       Loads environment variables from `.env` development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dotenv
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dotenv) = 2.7.6
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0.40.0 gem(rubocop) < 2

%description   -n gem-dotenv-devel
Loads environment variables from `.env` development package.

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%description   -n gem-dotenv-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dotenv.


%package       -n dotenv-rails
Version:       2.7.6
Release:       alt1
Summary:       Autoload dotenv in Rails executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета dotenv-rails
Group:         Other
BuildArch:     noarch

Requires:      gem(dotenv-rails) = 2.7.6

%description   -n dotenv-rails
Autoload dotenv in Rails executable(s).

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%description   -n dotenv-rails -l ru_RU.UTF-8
Исполнямка для самоцвета dotenv-rails.


%package       -n gem-dotenv-rails-doc
Version:       2.7.6
Release:       alt1
Summary:       Autoload dotenv in Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dotenv-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dotenv-rails) = 2.7.6

%description   -n gem-dotenv-rails-doc
Autoload dotenv in Rails documentation files.

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%description   -n gem-dotenv-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dotenv-rails.


%package       -n gem-dotenv-rails-devel
Version:       2.7.6
Release:       alt1
Summary:       Autoload dotenv in Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета dotenv-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dotenv-rails) = 2.7.6
Requires:      gem(spring) >= 0

%description   -n gem-dotenv-rails-devel
Autoload dotenv in Rails development package.

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a
twelve-factor app. Anything that is likely to change between deployment
environments-such as resource handles for databases or credentials for external
services-should be extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%description   -n gem-dotenv-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета dotenv-rails.


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

%files         -n gem-dotenv-rails
%doc README.md
%ruby_gemspecdir/dotenv-rails-2.7.6.gemspec
%ruby_gemslibdir/dotenv-rails-2.7.6

%files         -n dotenv
%doc README.md
%_bindir/dotenv

%files         -n gem-dotenv-doc
%doc README.md
%ruby_gemsdocdir/dotenv-2.7.6

%files         -n gem-dotenv-devel
%doc README.md

%files         -n dotenv-rails
%doc README.md

%files         -n gem-dotenv-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-dotenv-rails-devel
%doc README.md


%changelog
* Sun Aug 01 2021 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt1
- + packaged gem with Ruby Policy 2.0
