%define        gemname immigrant

Name:          gem-immigrant
Version:       0.3.6
Release:       alt1
Summary:       Foreign key migration generator for Rails
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jenseng/immigrant
Vcs:           https://github.com/jenseng/immigrant.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 3.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 3.0
Provides:      gem(immigrant) = 0.3.6


%description
Adds a generator for creating a foreign key migration based on your current
model associations. Immigrant gives Rails a foreign key migration generator so
you can effortlessly find and add missing keys. This is particularly helpful
when you decide to add keys to an established Rails app.


%package       -n gem-immigrant-doc
Version:       0.3.6
Release:       alt1
Summary:       Foreign key migration generator for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета immigrant
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(immigrant) = 0.3.6

%description   -n gem-immigrant-doc
Foreign key migration generator for Rails documentation files.

Adds a generator for creating a foreign key migration based on your current
model associations. Immigrant gives Rails a foreign key migration generator so
you can effortlessly find and add missing keys. This is particularly helpful
when you decide to add keys to an established Rails app.


%description   -n gem-immigrant-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета immigrant.


%package       -n gem-immigrant-devel
Version:       0.3.6
Release:       alt1
Summary:       Foreign key migration generator for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета immigrant
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(immigrant) = 0.3.6

%description   -n gem-immigrant-devel
Foreign key migration generator for Rails development package.

Adds a generator for creating a foreign key migration based on your current
model associations. Immigrant gives Rails a foreign key migration generator so
you can effortlessly find and add missing keys. This is particularly helpful
when you decide to add keys to an established Rails app.


%description   -n gem-immigrant-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета immigrant.


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

%files         -n gem-immigrant-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-immigrant-devel
%doc README.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.6-alt1
- + packaged gem with Ruby Policy 2.0
