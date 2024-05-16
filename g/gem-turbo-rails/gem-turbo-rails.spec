%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname turbo-rails

Name:          gem-turbo-rails
Version:       2.0.5
Release:       alt1
Summary:       The speed of a single-page web application without having to write any JavaScript
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/hotwired/turbo-rails
Vcs:           https://github.com/hotwired/turbo-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rails) >= 6.1.3.2
BuildRequires: gem(sprockets-rails) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(importmap-rails) >= 0
BuildRequires: gem(capybara) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(cuprite) >= 0.9
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(activejob) >= 6.0.0
BuildRequires: gem(actionpack) >= 6.0.0
BuildRequires: gem(railties) >= 6.0.0
BuildConflicts: gem(rails) >= 7.2
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(cuprite) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
%ruby_use_gem_dependency rack < 4
Requires:      gem(activejob) >= 6.0.0
Requires:      gem(actionpack) >= 6.0.0
Requires:      gem(railties) >= 6.0.0
Provides:      gem(turbo-rails) = 2.0.5


%description
The speed of a single-page web application without having to write any
JavaScript.


%if_enabled    doc
%package       -n gem-turbo-rails-doc
Version:       2.0.5
Release:       alt1
Summary:       The speed of a single-page web application without having to write any JavaScript documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета turbo-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(turbo-rails) = 2.0.5

%description   -n gem-turbo-rails-doc
The speed of a single-page web application without having to write any
JavaScript documentation files.
%description   -n gem-turbo-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета turbo-rails.
%endif


%if_enabled    devel
%package       -n gem-turbo-rails-devel
Version:       2.0.5
Release:       alt1
Summary:       The speed of a single-page web application without having to write any JavaScript development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета turbo-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(turbo-rails) = 2.0.5
Requires:      gem(rails) >= 6.1.3.2
Requires:      gem(sprockets-rails) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(puma) >= 0
Requires:      gem(importmap-rails) >= 0
Requires:      gem(capybara) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(cuprite) >= 0.9
Requires:      gem(sqlite3) >= 0
Conflicts:     gem(rails) >= 7.2
Conflicts:     gem(rack) >= 4
Conflicts:     gem(cuprite) >= 1

%description   -n gem-turbo-rails-devel
The speed of a single-page web application without having to write any
JavaScript development package.
%description   -n gem-turbo-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета turbo-rails.
%endif


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

%if_enabled    doc
%files         -n gem-turbo-rails-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-turbo-rails-devel
%doc README.md
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.5-alt1
- + packaged gem with Ruby Policy 2.0
