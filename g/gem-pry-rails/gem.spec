%define        gemname pry-rails

Name:          gem-pry-rails
Version:       0.3.9
Release:       alt1
Summary:       Use Pry as your rails console
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rweng/pry-rails
Vcs:           https://github.com/rweng/pry-rails.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(pry) >= 0.10.4 gem(pry) < 1
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(minitest) >= 0 gem(minitest) < 6

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(pry) >= 0.10.4 gem(pry) < 1
Provides:      gem(pry-rails) = 0.3.9

%description
Avoid repeating yourself, use pry-rails instead of copying the initializer to
every rails project. This is a small gem which causes rails console to open pry.
It therefore depends on pry.


%package       -n gem-pry-rails-doc
Version:       0.3.9
Release:       alt1
Summary:       Use Pry as your rails console documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pry-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pry-rails) = 0.3.9

%description   -n gem-pry-rails-doc
Use Pry as your rails console documentation files.

Avoid repeating yourself, use pry-rails instead of copying the initializer to
every rails project. This is a small gem which causes rails console to open pry.
It therefore depends on pry.

%description   -n gem-pry-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pry-rails.


%package       -n gem-pry-rails-devel
Version:       0.3.9
Release:       alt1
Summary:       Use Pry as your rails console development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pry-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pry-rails) = 0.3.9
Requires:      gem(appraisal) >= 0
Requires:      gem(minitest) >= 0 gem(minitest) < 6

%description   -n gem-pry-rails-devel
Use Pry as your rails console development package.

Avoid repeating yourself, use pry-rails instead of copying the initializer to
every rails project. This is a small gem which causes rails console to open pry.
It therefore depends on pry.

%description   -n gem-pry-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pry-rails.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Readme.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-pry-rails-doc
%doc Readme.md
%ruby_gemdocdir

%files         -n gem-pry-rails-devel
%doc Readme.md


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 0.3.9-alt1
- + packaged gem with Ruby Policy 2.0
