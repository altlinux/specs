%define        _unpackaged_files_terminate_build 1
%define        gemname sprockets-rails

Name:          gem-sprockets-rails
Version:       3.4.2.25
Release:       alt0.1
Summary:       Sprockets Rails integration
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/sprockets-rails
Vcs:           https://github.com/rails/sprockets-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(sass) >= 0
BuildRequires: gem(uglifier) >= 0
BuildRequires: gem(rack) >= 2.2
BuildRequires: gem(sprockets) >= 3.0.0
BuildRequires: gem(actionpack) >= 5.2
BuildRequires: gem(activesupport) >= 5.2
BuildRequires: gem(railties) >= 5.2
BuildConflicts: gem(rack) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(sprockets) >= 3.0.0
Requires:      gem(actionpack) >= 5.2
Requires:      gem(activesupport) >= 5.2
Obsoletes:     ruby-sprockets-rails < %EVR
Provides:      ruby-sprockets-rails = %EVR
Provides:      gem(sprockets-rails) = 3.4.2.25

%ruby_use_gem_version sprockets-rails:3.4.2.25

%description
Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.


%package       -n gem-sprockets-rails-doc
Version:       3.4.2.25
Release:       alt0.1
Summary:       Sprockets Rails integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета sprockets-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(sprockets-rails) = 3.4.2.25

%description   -n gem-sprockets-rails-doc
Sprockets Rails integration documentation files.

Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.

%description   -n gem-sprockets-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета sprockets-rails.


%package       -n gem-sprockets-rails-devel
Version:       3.4.2.25
Release:       alt0.1
Summary:       Sprockets Rails integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета sprockets-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(sprockets-rails) = 3.4.2.25
Requires:      gem(rake) >= 0
Requires:      gem(sass) >= 0
Requires:      gem(uglifier) >= 0
Requires:      gem(rack) >= 2.2
Requires:      gem(railties) >= 5.2
Conflicts:     gem(rack) >= 3

%description   -n gem-sprockets-rails-devel
Sprockets Rails integration development package.

Provides Sprockets implementation for Rails 4.x (and beyond) Asset Pipeline.

%description   -n gem-sprockets-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета sprockets-rails.


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

%files         -n gem-sprockets-rails-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-sprockets-rails-devel
%doc README.md


%changelog
* Fri Mar 10 2023 Pavel Skrylev <majioa@altlinux.org> 3.4.2.25-alt0.1
- ^ 3.4.2 -> 3.4.2p25

* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 3.4.2-alt1
- + packaged gem with Ruby Policy 2.0
