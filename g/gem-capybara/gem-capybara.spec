%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname capybara

Name:          gem-capybara
Version:       3.40.0
Release:       alt1
Summary:       Acceptance test framework for web applications
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/teamcapybara/capybara
Vcs:           https://github.com/teamcapybara/capybara.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(byebug) >= 0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(cucumber) >= 2.3.0
BuildRequires: gem(erubi) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(launchy) >= 2.0.4
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(puma) >= 0
BuildRequires: gem(rackup) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.5.0
BuildRequires: gem(rspec-instafail) >= 0
BuildRequires: gem(rubocop) >= 1.1
BuildRequires: gem(rubocop-minitest) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rake) >= 0
BuildRequires: gem(rubocop-rspec) >= 2.0
BuildRequires: gem(sauce_whisk) >= 0
BuildRequires: gem(selenium_statistics) >= 0
BuildRequires: gem(selenium-webdriver) >= 4.8
BuildRequires: gem(sinatra) >= 1.4.0
BuildRequires: gem(uglifier) >= 0
BuildRequires: gem(yard) >= 0.9.0
BuildRequires: gem(redcarpet) >= 0
BuildRequires: gem(addressable) >= 0
BuildRequires: gem(matrix) >= 0
BuildRequires: gem(mini_mime) >= 0.1.3
BuildRequires: gem(nokogiri) >= 1.11
BuildRequires: gem(rack) >= 1.6.0
BuildRequires: gem(rack-test) >= 0.6.3
BuildRequires: gem(regexp_parser) >= 1.5
BuildRequires: gem(xpath) >= 3.2
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(selenium-webdriver) >= 5
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(regexp_parser) >= 3.0
BuildConflicts: gem(xpath) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(addressable) >= 0
Requires:      gem(matrix) >= 0
Requires:      gem(mini_mime) >= 0.1.3
Requires:      gem(nokogiri) >= 1.11
Requires:      gem(rack) >= 1.6.0
Requires:      gem(rack-test) >= 0.6.3
Requires:      gem(regexp_parser) >= 1.5
Requires:      gem(xpath) >= 3.2
Conflicts:     gem(nokogiri) >= 2
Conflicts:     gem(regexp_parser) >= 3.0
Conflicts:     gem(xpath) >= 4
Obsoletes:     ruby-capybara < %EVR
Provides:      ruby-capybara = %EVR
Provides:      gem(capybara) = 3.40.0


%description
Capybara is an integration testing tool for rack based web applications. It
simulates how a user would interact with a website.

Capybara helps you test web applications by simulating how a real user would
interact with your app. It is agnostic about the driver running your tests and
comes with Rack::Test and Selenium support built in. WebKit is supported through
an external gem.


%if_enabled    doc
%package       -n gem-capybara-doc
Version:       3.40.0
Release:       alt1
Summary:       Acceptance test framework for web applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета capybara
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(capybara) = 3.40.0

%description   -n gem-capybara-doc
Acceptance test framework for web applications documentation files.

Capybara is an integration testing tool for rack based web applications. It
simulates how a user would interact with a website.

Capybara helps you test web applications by simulating how a real user would
interact with your app. It is agnostic about the driver running your tests and
comes with Rack::Test and Selenium support built in. WebKit is supported through
an external gem.

%description   -n gem-capybara-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета capybara.
%endif


%if_enabled    devel
%package       -n gem-capybara-devel
Version:       3.40.0
Release:       alt1
Summary:       Acceptance test framework for web applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета capybara
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(capybara) = 3.40.0
Requires:      gem(byebug) >= 0
Requires:      gem(coveralls) >= 0
Requires:      gem(cucumber) >= 2.3.0
Requires:      gem(erubi) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(launchy) >= 2.0.4
Requires:      gem(minitest) >= 0
Requires:      gem(puma) >= 0
Requires:      gem(rackup) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.5.0
Requires:      gem(rspec-instafail) >= 0
Requires:      gem(rubocop) >= 1.1
Requires:      gem(rubocop-minitest) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rake) >= 0
Requires:      gem(rubocop-rspec) >= 2.0
Requires:      gem(sauce_whisk) >= 0
Requires:      gem(selenium_statistics) >= 0
Requires:      gem(selenium-webdriver) >= 4.8
Requires:      gem(sinatra) >= 1.4.0
Requires:      gem(uglifier) >= 0
Requires:      gem(yard) >= 0.9.0
Requires:      gem(redcarpet) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(selenium-webdriver) >= 5

%description   -n gem-capybara-devel
Acceptance test framework for web applications development package.

Capybara is an integration testing tool for rack based web applications. It
simulates how a user would interact with a website.

Capybara helps you test web applications by simulating how a real user would
interact with your app. It is agnostic about the driver running your tests and
comes with Rack::Test and Selenium support built in. WebKit is supported through
an external gem.

%description   -n gem-capybara-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета capybara.
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
%files         -n gem-capybara-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-capybara-devel
%doc README.md
%endif


%changelog
* Sat Aug 03 2024 Pavel Skrylev <majioa@altlinux.org> 3.40.0-alt1
- ^ 3.37.1 -> 3.40.0

* Wed Nov 02 2022 Pavel Skrylev <majioa@altlinux.org> 3.37.1-alt1.2
- !closing gem build requires under check condition

* Wed Nov 02 2022 Pavel Skrylev <majioa@altlinux.org> 3.37.1-alt1.1
- !fix dep to regexp_parser gem

* Thu Sep 15 2022 Pavel Skrylev <majioa@altlinux.org> 3.37.1-alt1
- ^ 3.31.0 -> 3.37.1

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.31.0-alt1
- updated (^) 3.29.0 -> 3.31.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.29.0-alt1
- updated (^) 3.16.1 -> 3.29.0

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.16.1-alt1
- updated (^) 3.10.0 -> 3.16.1
- used (>) Ruby Policy 2.0

* Mon Oct 29 2018 Pavel Skrylev <majioa@altlinux.org> 3.10.0-alt1
- new version 3.10.0

* Thu Oct 04 2018 Andrey Cherepanov <cas@altlinux.org> 3.9.0-alt1
- New version.

* Thu Sep 27 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.2-alt1
- New version.

* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.1-alt1
- New version.

* Fri Sep 21 2018 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 3.7.2-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- Initial build for Sisyphus
