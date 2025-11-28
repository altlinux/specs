%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cuprite

Name:          gem-cuprite
Version:       0.17
Release:       alt1
Summary:       Headless Chrome driver for Capybara
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rubycdp/cuprite
Vcs:           https://github.com/rubycdp/cuprite.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         gem-cuprite-%EVR.patch
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(capybara) >= 3.0
BuildRequires: gem(chunky_png) >= 1.4
BuildRequires: gem(ferrum) >= 0.17.0
BuildRequires: gem(image_size) >= 3.0
BuildRequires: gem(launchy) >= 2.5
BuildRequires: gem(pdf-reader) >= 2.12
BuildRequires: gem(puma) >= 5.6.7
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.10
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(sinatra) >= 3.2
BuildConflicts: gem(capybara) >= 4
BuildConflicts: gem(chunky_png) >= 2
BuildConflicts: gem(ferrum) >= 0.18
BuildConflicts: gem(image_size) >= 4
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(pdf-reader) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(sinatra) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency sinatra >= 4.0,sinatra < 5
Requires:      ruby >= 2.7.0
Requires:      gem(capybara) >= 3.0
Requires:      gem(ferrum) >= 0.17.0
Conflicts:     gem(capybara) >= 4
Conflicts:     gem(ferrum) >= 0.18
Provides:      gem(cuprite) = 0.17

%description
Cuprite is a driver for Capybara that allows you to run your tests on a headless
Chrome browser


%if_enabled    doc
%package       -n gem-cuprite-doc
Version:       0.17
Release:       alt1
Summary:       Headless Chrome driver for Capybara documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cuprite
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cuprite) = 0.17

%description   -n gem-cuprite-doc
Headless Chrome driver for Capybara documentation files.

Cuprite is a driver for Capybara that allows you to run your tests on a headless
Chrome browser

%description   -n gem-cuprite-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cuprite.
%endif


%if_enabled    devel
%package       -n gem-cuprite-devel
Version:       0.17
Release:       alt1
Summary:       Headless Chrome driver for Capybara development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cuprite
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(cuprite) = 0.17
Requires:      gem(capybara) >= 3.0
Requires:      gem(chunky_png) >= 1.4
Requires:      gem(ferrum) >= 0.17.0
Requires:      gem(image_size) >= 3.0
Requires:      gem(launchy) >= 2.5
Requires:      gem(pdf-reader) >= 2.12
Requires:      gem(puma) >= 5.6.7
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.10
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(sinatra) >= 3.2
Conflicts:     gem(capybara) >= 4
Conflicts:     gem(chunky_png) >= 2
Conflicts:     gem(ferrum) >= 0.18
Conflicts:     gem(image_size) >= 4
Conflicts:     gem(launchy) >= 3
Conflicts:     gem(pdf-reader) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(sinatra) >= 5

%description   -n gem-cuprite-devel
Headless Chrome driver for Capybara development package.

Cuprite is a driver for Capybara that allows you to run your tests on a headless
Chrome browser

%description   -n gem-cuprite-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cuprite.
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
%doc LICENSE README.md CHANGELOG.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cuprite-doc
%doc LICENSE README.md CHANGELOG.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cuprite-devel
%doc LICENSE README.md CHANGELOG.md
%endif


%changelog
* Fri Nov 28 2025 Pavel Skrylev <majioa@altlinux.org> 0.17-alt1
- ^ 0.15.1 -> 0.17

* Tue Oct 22 2024 Pavel Skrylev <majioa@altlinux.org> 0.15.1-alt1
- ^ 0.15 -> 0.15.1

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.15-alt1
- + packaged gem with Ruby Policy 2.0
