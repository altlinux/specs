%define        gemname zeitwerk

Name:          gem-zeitwerk
Version:       2.4.2
Release:       alt1
Summary:       Efficient and thread-safe constant autoloader
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fxn/zeitwerk
Vcs:           https://github.com/fxn/zeitwerk.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(zeitwerk) = 2.4.2


%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.


%package       -n gem-zeitwerk-doc
Version:       2.4.2
Release:       alt1
Summary:       Efficient and thread-safe constant autoloader documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета zeitwerk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(zeitwerk) = 2.4.2

%description   -n gem-zeitwerk-doc
Efficient and thread-safe constant autoloader documentation files.

Zeitwerk implements constant autoloading with Ruby semantics. Each gem and
application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading, reloading, and eager
loading.

%description   -n gem-zeitwerk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета zeitwerk.


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

%files         -n gem-zeitwerk-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue Jun 15 2021 Pavel Skrylev <majioa@altlinux.org> 2.4.2-alt1
- + packaged gem with Ruby Policy 2.0
