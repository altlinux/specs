%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ferrum

Name:          gem-ferrum
Version:       0.17.1
Release:       alt1
Summary:       Ruby headless Chrome driver
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubycdp/ferrum
Vcs:           https://github.com/rubycdp/ferrum.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(addressable) >= 2.5
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(chunky_png) >= 1.3
BuildRequires: gem(concurrent-ruby) >= 1.1
BuildRequires: gem(image_size) >= 2.0
BuildRequires: gem(kramdown) >= 2.0
BuildRequires: gem(pdf-reader) >= 2.12
BuildRequires: gem(puma) >= 5.6.7
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.8
BuildRequires: gem(rspec-wait) >= 0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(sinatra) >= 3.2
BuildRequires: gem(webrick) >= 1.7
BuildRequires: gem(websocket-driver) >= 0.7
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(addressable) >= 3
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(chunky_png) >= 2
BuildConflicts: gem(concurrent-ruby) >= 2
BuildConflicts: gem(image_size) >= 4
BuildConflicts: gem(kramdown) >= 3
BuildConflicts: gem(pdf-reader) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(webrick) >= 2
BuildConflicts: gem(websocket-driver) >= 1
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency sinatra >= 4.0.0,sinatra < 5
%ruby_use_gem_dependency image_size >= 3.4,image_size < 4
Requires:      ruby >= 2.7.0
Requires:      gem(addressable) >= 2.5
Requires:      gem(base64) >= 0.2
Requires:      gem(concurrent-ruby) >= 1.1
Requires:      gem(rspec-wait) >= 0
Requires:      gem(webrick) >= 1.7
Requires:      gem(websocket-driver) >= 0.7
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(base64) >= 1
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(websocket-driver) >= 1
Provides:      gem(ferrum) = 0.17.1

%description
Ferrum allows you to control headless Chrome browser


%if_enabled    doc
%package       -n gem-ferrum-doc
Version:       0.17.1
Release:       alt1
Summary:       Ruby headless Chrome driver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ferrum
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(ferrum) = 0.17.1

%description   -n gem-ferrum-doc
Ruby headless Chrome driver documentation files.

Ferrum allows you to control headless Chrome browser

%description   -n gem-ferrum-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ferrum.
%endif


%if_enabled    devel
%package       -n gem-ferrum-devel
Version:       0.17.1
Release:       alt1
Summary:       Ruby headless Chrome driver development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ferrum
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(ferrum) = 0.17.1
Requires:      gem(addressable) >= 2.5
Requires:      gem(base64) >= 0.2
Requires:      gem(chunky_png) >= 1.3
Requires:      gem(concurrent-ruby) >= 1.1
Requires:      gem(image_size) >= 2.0
Requires:      gem(kramdown) >= 2.0
Requires:      gem(pdf-reader) >= 2.12
Requires:      gem(puma) >= 5.6.7
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.8
Requires:      gem(rspec-wait) >= 0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(sinatra) >= 3.2
Requires:      gem(webrick) >= 1.7
Requires:      gem(websocket-driver) >= 0.7
Requires:      gem(yard) >= 0.9
Conflicts:     gem(addressable) >= 3
Conflicts:     gem(base64) >= 1
Conflicts:     gem(chunky_png) >= 2
Conflicts:     gem(concurrent-ruby) >= 2
Conflicts:     gem(image_size) >= 4
Conflicts:     gem(kramdown) >= 3
Conflicts:     gem(pdf-reader) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(websocket-driver) >= 1
Conflicts:     gem(yard) >= 1

%description   -n gem-ferrum-devel
Ruby headless Chrome driver development package.

Ferrum allows you to control headless Chrome browser

%description   -n gem-ferrum-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ferrum.
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
%files         -n gem-ferrum-doc
%doc LICENSE README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ferrum-devel
%doc LICENSE README.md CHANGELOG.md
%endif


%changelog
* Fri Nov 28 2025 Pavel Skrylev <majioa@altlinux.org> 0.17.1-alt1
- ^ 0.15 -> 0.17.1

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.15-alt1
- + packaged gem with Ruby Policy 2.0
