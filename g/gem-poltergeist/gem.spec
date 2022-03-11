%define        gemname poltergeist

Name:          gem-poltergeist
Version:       1.18.1
Release:       alt1.1
Summary:       PhantomJS driver for Capybara
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teampoltergeist/poltergeist
Vcs:           https://github.com/teampoltergeist/poltergeist.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(capybara) >= 2.1 gem(capybara) < 4
BuildRequires: gem(websocket-driver) >= 0.2.0
BuildRequires: gem(cliver) >= 0.3.1 gem(cliver) < 0.4
BuildRequires: gem(launchy) >= 2.0 gem(launchy) < 3
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4
BuildRequires: gem(sinatra) <= 3.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(image_size) >= 1.0 gem(image_size) < 4
BuildRequires: gem(pdf-reader) < 3.0 gem(pdf-reader) >= 1.3.3
BuildRequires: gem(coffee-script) >= 2.2 gem(coffee-script) < 3
# BuildRequires: gem(guard-coffeescript) >= 2.0.0 gem(guard-coffeescript) < 2.1
BuildRequires: gem(coffee-script-source) >= 1.12.2 gem(coffee-script-source) < 1.13
BuildRequires: gem(listen) >= 3.0.6 gem(listen) < 4
BuildRequires: gem(erubi) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency image_size >= 2.1.2,image_size < 4
%ruby_use_gem_dependency listen >= 3.5.1,listen < 4
Requires:      gem(capybara) >= 2.1 gem(capybara) < 4
Requires:      gem(websocket-driver) >= 0.2.0
Requires:      gem(cliver) >= 0.3.1 gem(cliver) < 0.4
Provides:      gem(poltergeist) = 1.18.1


%description
Poltergeist is a driver for Capybara that allows you to run your tests on a
headless WebKit browser, provided by PhantomJS.


%package       -n gem-poltergeist-doc
Version:       1.18.1
Release:       alt1.1
Summary:       PhantomJS driver for Capybara documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета poltergeist
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(poltergeist) = 1.18.1

%description   -n gem-poltergeist-doc
PhantomJS driver for Capybara documentation files.

Poltergeist is a driver for Capybara that allows you to run your tests on a
headless WebKit browser, provided by PhantomJS.

%description   -n gem-poltergeist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета poltergeist.


%package       -n gem-poltergeist-devel
Version:       1.18.1
Release:       alt1.1
Summary:       PhantomJS driver for Capybara development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета poltergeist
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(poltergeist) = 1.18.1
Requires:      gem(launchy) >= 2.0 gem(launchy) < 3
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(sinatra) <= 3.0
Requires:      gem(rake) >= 0
Requires:      gem(image_size) >= 1.0 gem(image_size) < 4
Requires:      gem(pdf-reader) < 3.0 gem(pdf-reader) >= 1.3.3
Requires:      gem(coffee-script) >= 2.2 gem(coffee-script) < 3
# Requires:      gem(guard-coffeescript) >= 2.0.0 gem(guard-coffeescript) < 2.1
Requires:      gem(coffee-script-source) >= 1.12.2 gem(coffee-script-source) < 1.13
Requires:      gem(listen) >= 3.0.6 gem(listen) < 4
Requires:      gem(erubi) >= 0

%description   -n gem-poltergeist-devel
PhantomJS driver for Capybara development package.

Poltergeist is a driver for Capybara that allows you to run your tests on a
headless WebKit browser, provided by PhantomJS.

%description   -n gem-poltergeist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета poltergeist.


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

%files         -n gem-poltergeist-devel
%doc README.md


%changelog
* Fri Mar 11 2022 Pavel Skrylev <majioa@altlinux.org> 1.18.1-alt1.1
- ! spec build requires

* Fri Sep 03 2021 Pavel Skrylev <majioa@altlinux.org> 1.18.1-alt1
- + packaged gem with Ruby Policy 2.0
