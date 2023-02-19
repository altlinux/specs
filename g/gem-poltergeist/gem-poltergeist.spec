%define        gemname poltergeist

Name:          gem-poltergeist
Version:       1.18.1.16
Release:       alt1
Summary:       PhantomJS driver for Capybara
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teampoltergeist/poltergeist
Vcs:           https://github.com/teampoltergeist/poltergeist.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coffee-script) >= 2.2
BuildRequires: gem(coffee-script-source) >= 1.12.2
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(guard-coffeescript) >= 2.0.0
BuildRequires: gem(image_size) >= 1.0
BuildRequires: gem(launchy) >= 2.0
BuildRequires: gem(listen) >= 3.0.6
BuildRequires: gem(pdf-reader) >= 1.3.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.7
BuildRequires: gem(puma) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(racc) >= 0
BuildRequires: gem(rubysl) >= 0
BuildRequires: gem(capybara) >= 2.1
BuildRequires: gem(cliver) >= 0.3.1
BuildRequires: gem(websocket-driver) >= 0.2.0
BuildConflicts: gem(coffee-script) >= 3
BuildConflicts: gem(coffee-script-source) >= 1.13
BuildConflicts: gem(guard-coffeescript) >= 2.1
BuildConflicts: gem(image_size) >= 2
BuildConflicts: gem(launchy) >= 3
BuildConflicts: gem(listen) >= 3.1
BuildConflicts: gem(pdf-reader) >= 3.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(sinatra) > 3.0
BuildConflicts: gem(capybara) >= 4
BuildConflicts: gem(cliver) >= 0.4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(capybara) >= 2.1
Requires:      gem(cliver) >= 0.3.1
Requires:      gem(websocket-driver) >= 0.2.0
Conflicts:     gem(capybara) >= 4
Conflicts:     gem(cliver) >= 0.4
Provides:      gem(poltergeist) = 1.18.1.16

%ruby_use_gem_version poltergeist:1.18.1.16

%description
Poltergeist is a driver for Capybara that allows you to run your tests on a
headless WebKit browser, provided by PhantomJS.


%package       -n gem-poltergeist-doc
Version:       1.18.1.16
Release:       alt1
Summary:       PhantomJS driver for Capybara documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета poltergeist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(poltergeist) = 1.18.1.16

%description   -n gem-poltergeist-doc
PhantomJS driver for Capybara documentation files.

Poltergeist is a driver for Capybara that allows you to run your tests on a
headless WebKit browser, provided by PhantomJS.

%description   -n gem-poltergeist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета poltergeist.


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

%files         -n gem-poltergeist-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 1.18.1.16-alt1
- ^ 1.18.1 -> 1.18.1p16 (no devel)

* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.18.1-alt1.1
- ! spec build requires

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.18.1-alt1
- + packaged gem with Ruby Policy 2.0
