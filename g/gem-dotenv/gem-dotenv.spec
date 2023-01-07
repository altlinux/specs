%define        gemname dotenv

Name:          gem-dotenv
Version:       2.8.1
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
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(spring) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(rb-fsevent) >= 0
BuildRequires: gem(railties) >= 3.2
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(spring) >= 0
BuildRequires: gem(guard-rspec) >= 0
BuildRequires: gem(guard-bundler) >= 0
BuildRequires: gem(rb-fsevent) >= 0
BuildRequires: gem(railties) >= 3.2
BuildRequires: gem(rubocop) >= 1.15.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(dotenv) = 2.8.1


%description
Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a twelve-factor
app. Anything that is likely to change between deployment environments-such as
resource handles for databases or credentials for external services-should be
extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.


%package       -n gem-dotenv-rails
Version:       2.8.1
Release:       alt1
Summary:       Loads environment variables from `.env`
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(dotenv) = 2.8.1
Requires:      gem(railties) >= 3.2
Provides:      gem(dotenv-rails) = 2.8.1

%description   -n gem-dotenv-rails
Loads environment variables from `.env`.

%description   -n gem-dotenv-rails -l ru_RU.UTF-8
Файлы сведений для самоцвета dotenv-rails.


%package       -n gem-dotenv-rails-doc
Version:       2.8.1
Release:       alt1
Summary:       Loads environment variables from `.env` documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dotenv-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dotenv-rails) = 2.8.1

%description   -n gem-dotenv-rails-doc
Loads environment variables from `.env` documentation files.

%description   -n gem-dotenv-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dotenv-rails.


%package       -n dotenv
Version:       2.8.1
Release:       alt1
Summary:       Loads environment variables from `.env` executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета dotenv
Group:         Other
BuildArch:     noarch

Requires:      gem(dotenv) = 2.8.1
Conflicts:     python3-module-dotenv

%description   -n dotenv
Loads environment variables from `.env` executable(s).

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a twelve-factor
app. Anything that is likely to change between deployment environments-such as
resource handles for databases or credentials for external services-should be
extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.

%description   -n dotenv -l ru_RU.UTF-8
Исполнямка для самоцвета dotenv.


%package       -n gem-dotenv-doc
Version:       2.8.1
Release:       alt1
Summary:       Loads environment variables from `.env` documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета dotenv
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(dotenv) = 2.8.1

%description   -n gem-dotenv-doc
Loads environment variables from `.env` documentation files.

Shim to load environment variables from .env into ENV in development.

Storing configuration in the environment is one of the tenets of a twelve-factor
app. Anything that is likely to change between deployment environments-such as
resource handles for databases or credentials for external services-should be
extracted from the code into environment variables.

But it is not always practical to set environment variables on development
machines or continuous integration servers where multiple projects are run.
dotenv loads variables from a .env file into ENV when the environment is
bootstrapped.

%description   -n gem-dotenv-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета dotenv.


%package       -n dotenv-rails
Version:       2.8.1
Release:       alt1
Summary:       Loads environment variables from `.env` executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета dotenv-rails
Group:         Other
BuildArch:     noarch

Requires:      gem(dotenv-rails) = 2.8.1

%description   -n dotenv-rails
Autoload dotenv in Rails.


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
%ruby_gemspecdir/dotenv-rails-2.8.1.gemspec
%ruby_gemslibdir/dotenv-rails-2.8.1

%files         -n gem-dotenv-rails-doc
%doc README.md
%ruby_gemsdocdir/dotenv-rails-2.8.1

%files         -n dotenv
%doc README.md
%_bindir/dotenv

%files         -n gem-dotenv-doc
%doc README.md
%ruby_gemdocdir

%files         -n dotenv-rails
%doc README.md


%changelog
* Sat Jan 07 2023 Pavel Skrylev <majioa@altlinux.org> 2.8.1-alt1
- ^ 2.7.6 -> 2.8.1

* Sun Aug 01 2021 Pavel Skrylev <majioa@altlinux.org> 2.7.6-alt0.1
- + packaged gem with Ruby Policy 2.0
