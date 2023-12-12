# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname selenium-webdriver

Name:          selenium
Version:       3.142.7
Release:       alt1.2
Summary:       A browser automation framework and ecosystem
License:       Apache-2.0
Group:         Development/Tools
Url:           https://www.seleniumhq.org
Vcs:           https://github.com/SeleniumHQ/selenium.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 0.73.0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(webmock) >= 3.5
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(childprocess) >= 0.5
BuildRequires: gem(rubyzip) >= 1.2
BuildConflicts: gem(rack) >= 3
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(childprocess) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency rubyzip >= 2.3.2,rubyzip < 3
%ruby_use_gem_dependency childprocess >= 4.1.0,childprocess < 5
Requires:      gem-selenium-webdriver = %version

%ruby_use_gem_version selenium-webdriver:%version

%description
Selenium is an umbrella project encapsulating a variety of tools and libraries
enabling web browser automation. Selenium specifically provides infrastructure
for the W3C WebDriver specification  a platform and language-neutral coding
interface compatible with all major web browsers.

The project is made possible by volunteer contributors who've generously
donated thousands of hours in code development and upkeep.


%package       -n gem-selenium-webdriver
Summary:       Library files for %gemname gem
Summary(ru_RU.UTF-8): Файлы библиотеки для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(childprocess) >= 0.5
Requires:      gem(rubyzip) >= 1.2
Conflicts:     gem(childprocess) >= 5
Obsoletes:     ruby-selenium-webdriver < %EVR
Provides:      ruby-selenium-webdriver = %EVR
Provides:      gem(selenium-webdriver) = %version

%description   -n gem-selenium-webdriver
Library files for %gemname gem.

%description   -n gem-selenium-webdriver -l ru_RU.UTF8
Файлы библиотеки для самоцвета %gemname.


%package       -n gem-selenium-webdriver-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = %version

%description   -n gem-selenium-webdriver-doc
Documentation files for %gemname gem.

%description   -n gem-selenium-webdriver-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n gem-selenium-webdriver-devel
Summary:       The next generation developer focused tool for automated testing of webapps development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selenium-webdriver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = %version
Requires:      gem(ffi) >= 0
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 0.73.0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(webmock) >= 3.5
Requires:      gem(yard) >= 0.9.11
Conflicts:     gem(rack) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-selenium-webdriver-devel
The next generation developer focused tool for automated testing of webapps
development package.

WebDriver is a tool for writing automated tests of websites. It aims to mimic
the behaviour of a real user, and as such interacts with the HTML of the
application.

%description   -n gem-selenium-webdriver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selenium-webdriver.


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

%files         -n gem-selenium-webdriver
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-selenium-webdriver-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-selenium-webdriver-devel
%doc README.md

%changelog
* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1.2
- ! fixed deps to gems

* Thu Apr 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1.1
- + obsolete/provides pair for gem-selenium-webdriver

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1
- updated (^) 3.141.59 -> 3.142.7
- changed (*) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.141.59-alt1
- added (+) initial build with a packaged gem with usage Ruby Policy 2.0
