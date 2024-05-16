%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname importmap-rails

Name:          gem-importmap-rails
Version:       2.0.1
Release:       alt1
Summary:       Use ESM with importmap to manage modern JavaScript in Rails without transpiling or bundling
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/importmap-rails
Vcs:           https://github.com/rails/importmap-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rails) >= 6.1.0
BuildRequires: gem(sqlite3) >= 0
BuildConflicts: gem(rails) >= 6.2
%if_enabled check
BuildRequires: gem(actionpack) >= 6.0.0
BuildRequires: gem(activesupport) >= 6.0.0
BuildRequires: gem(railties) >= 6.0.0
BuildRequires: gem(turbo-rails) >= 0
BuildRequires: gem(stimulus-rails) >= 0
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(capybara) >= 0
BuildRequires: gem(selenium-webdriver) >= 0
BuildRequires: gem(webdrivers) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 6.0.0
Requires:      gem(activesupport) >= 6.0.0
Requires:      gem(actionpack) >= 6.0.0
Provides:      gem(importmap-rails) = 2.0.1


%description
Use ESM with importmap to manage modern JavaScript in Rails without transpiling
or bundling.


%if_enabled    doc
%package       -n gem-importmap-rails-doc
Version:       2.0.1
Release:       alt1
Summary:       Use ESM with importmap to manage modern JavaScript in Rails without transpiling or bundling documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета importmap-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(importmap-rails) = 2.0.1

%description   -n gem-importmap-rails-doc
Use ESM with importmap to manage modern JavaScript in Rails without transpiling
or bundling documentation files.

%description   -n gem-importmap-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета importmap-rails.
%endif


%if_enabled    devel
%package       -n gem-importmap-rails-devel
Version:       2.0.1
Release:       alt1
Summary:       Use ESM with importmap to manage modern JavaScript in Rails without transpiling or bundling development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета importmap-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(importmap-rails) = 2.0.1
Requires:      gem(rails) >= 6.1.0
Requires:      gem(sqlite3) >= 0
Requires:      gem(turbo-rails) >= 0
Requires:      gem(stimulus-rails) >= 0
Requires:      gem(byebug) >= 0
Requires:      gem(rexml) >= 0
Requires:      gem(capybara) >= 0
Requires:      gem(selenium-webdriver) >= 0
Requires:      gem(webdrivers) >= 0
Requires:      gem(railties) >= 6.0.0
Requires:      gem(activesupport) >= 6.0.0
Requires:      gem(actionpack) >= 6.0.0
Conflicts:     gem(rails) >= 6.2

%description   -n gem-importmap-rails-devel
Use ESM with importmap to manage modern JavaScript in Rails without transpiling
or bundling development package.

%description   -n gem-importmap-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета importmap-rails.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-importmap-rails-doc
%doc MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-importmap-rails-devel
%doc MIT-LICENSE README.md
%endif


%changelog
* Sun Apr 14 2024 Pavel Skrylev <majioa@altlinux.org> 2.0.1-alt1
- + packaged gem with Ruby Policy 2.0
