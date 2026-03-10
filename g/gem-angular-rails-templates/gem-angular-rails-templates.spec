%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname angular-rails-templates

Name:          gem-angular-rails-templates
Version:       1.4.0
Release:       alt1
Summary:       Use your angular templates with rails' asset pipeline
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/pitr/angular-rails-templates
Vcs:           https://github.com/pitr/angular-rails-templates.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(capybara) >= 0
BuildRequires: gem(coveralls_reborn) >= 0
BuildRequires: gem(haml) >= 0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(rails) >= 5.0
BuildRequires: gem(railties) >= 5.0
BuildRequires: gem(slim-rails) >= 0
BuildRequires: gem(sprockets) >= 3.0
BuildRequires: gem(sprockets-rails) >= 0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(uglifier) >= 0
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rails) >= 9
BuildConflicts: gem(railties) >= 8.2
BuildConflicts: gem(sprockets) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 5.0
Requires:      gem(sprockets) >= 3.0
Requires:      gem(sprockets-rails) >= 0
Requires:      gem(tilt) >= 0
Conflicts:     gem(railties) >= 8.2
Conflicts:     gem(sprockets) >= 5
Provides:      gem(angular-rails-templates) = 1.4.0

%description
Use your angular templates with rails' asset pipeline


%if_enabled    doc
%package       -n gem-angular-rails-templates-doc
Version:       1.4.0
Release:       alt1
Summary:       Use your angular templates with rails' asset pipeline documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета angular-rails-templates
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(angular-rails-templates) = 1.4.0

%description   -n gem-angular-rails-templates-doc
Use your angular templates with rails' asset pipeline documentation files.

%description   -n gem-angular-rails-templates-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета angular-rails-templates.
%endif


%if_enabled    devel
%package       -n gem-angular-rails-templates-devel
Version:       1.4.0
Release:       alt1
Summary:       Use your angular templates with rails' asset pipeline development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета angular-rails-templates
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(angular-rails-templates) = 1.4.0
Requires:      gem(capybara) >= 0
Requires:      gem(coveralls_reborn) >= 0
Requires:      gem(haml) >= 0
Requires:      gem(kramdown) >= 0
Requires:      gem(rails) >= 5.0
Requires:      gem(slim-rails) >= 0
Requires:      gem(uglifier) >= 0
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rails) >= 9

%description   -n gem-angular-rails-templates-devel
Use your angular templates with rails' asset pipeline development package.

%description   -n gem-angular-rails-templates-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета angular-rails-templates.
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
%doc LICENSE README.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-angular-rails-templates-doc
%doc LICENSE README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-angular-rails-templates-devel
%doc LICENSE README.md CHANGELOG.md
%endif


%changelog
* Tue Mar 10 2026 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
