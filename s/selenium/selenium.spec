# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname selenium-webdriver
%def_enable    check
%def_enable    doc
%def_enable    devel

Name:          selenium
Version:       4.19.0
Release:       alt1
Summary:       A browser automation framework and ecosystem
License:       Apache-2.0
Group:         Development/Tools
Url:           https://www.seleniumhq.org
Vcs:           https://github.com/SeleniumHQ/selenium.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(git) >= 1.19
BuildRequires: gem(rack) >= 2.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(webmock) >= 3.5
BuildRequires: gem(webrick) >= 1.7
BuildRequires: gem(yard) >= 0.9.11
BuildRequires: gem(debug) >= 1.7
BuildRequires: gem(steep) >= 1.5.0
BuildRequires: gem(base64) >= 0.2
BuildRequires: gem(rexml) >= 3.2.5
BuildRequires: gem(rubyzip) >= 1.2.2
BuildRequires: gem(websocket) >= 1.0
BuildConflicts: gem(git) >= 2
BuildConflicts: gem(rack) >= 4
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rspec) >= 3
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(webrick) >= 2
BuildConflicts: gem(debug) >= 2
BuildConflicts: gem(steep) >= 2
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(rexml) >= 4
BuildConflicts: gem(rubyzip) >= 3
BuildConflicts: gem(websocket) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency steep >= 1.6,steep < 2
%ruby_use_gem_dependency rack >= 3.0,rack < 4
Requires:      gem-selenium-webdriver = %version

#ruby_use_gem_version selenium-webdriver:%version

%description
Selenium is an umbrella project encapsulating a variety of tools and libraries
enabling web browser automation. Selenium specifically provides infrastructure
for the W3C WebDriver specification  a platform and language-neutral coding
interface compatible with all major web browsers.

The project is made possible by volunteer contributors who've generously
donated thousands of hours in code development and upkeep.


%package       -n gem-selenium-devtools
Version:       0.123.0
Release:       alt1
Summary:       DevTools Code for use with Selenium
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = 4.19.0
Provides:      gem(selenium-devtools) = 0.123.0

%description   -n gem-selenium-devtools
Selenium WebDriver now supports limited DevTools interactions. This project
allows users to specify desired versioning.


%if_enabled    doc
%package       -n gem-selenium-devtools-doc
Version:       0.123.0
Release:       alt1
Summary:       DevTools Code for use with Selenium documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета selenium-devtools
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(selenium-devtools) = 0.123.0

%description   -n gem-selenium-devtools-doc
DevTools Code for use with Selenium documentation files.

Selenium WebDriver now supports limited DevTools interactions. This project
allows users to specify desired versioning.

%description   -n gem-selenium-devtools-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета selenium-devtools.
%endif


%if_enabled    devel
%package       -n gem-selenium-devtools-devel
Version:       0.123.0
Release:       alt1
Summary:       DevTools Code for use with Selenium development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selenium-devtools
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selenium-devtools) = 0.123.0
Requires:      gem(git) >= 1.19
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(webmock) >= 3.5
Requires:      gem(webrick) >= 1.7
Requires:      gem(yard) >= 0.9.11
Requires:      gem(debug) >= 1.7
Requires:      gem(steep) >= 1.5.0
Conflicts:     gem(git) >= 2
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(debug) >= 2
Conflicts:     gem(steep) >= 2

%description   -n gem-selenium-devtools-devel
DevTools Code for use with Selenium development package.

Selenium WebDriver now supports limited DevTools interactions. This project
allows users to specify desired versioning.

%description   -n gem-selenium-devtools-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selenium-devtools.
%endif


%package       -n gem-selenium-webdriver
Version:       4.19.0
Release:       alt1
Summary:       Selenium is a browser automation tool for automated testing of webapps and more
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(base64) >= 0.2
Requires:      gem(rexml) >= 3.2.5
Requires:      gem(rubyzip) >= 1.2.2
Requires:      gem(websocket) >= 1.0
Conflicts:     gem(base64) >= 1
Conflicts:     gem(rexml) >= 4
Conflicts:     gem(rubyzip) >= 3
Conflicts:     gem(websocket) >= 2
Provides:      gem(selenium-webdriver) = 4.19.0
Obsoletes:     ruby-selenium-webdriver < %EVR
Provides:      ruby-selenium-webdriver = %EVR

%description   -n gem-selenium-webdriver
Selenium implements the W3C WebDriver protocol to automate popular browsers. It
aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing, but any
web-based task can automated.


%if_enabled    doc
%package       -n gem-selenium-webdriver-doc
Version:       4.19.0
Release:       alt1
Summary:       Selenium is a browser automation tool for automated testing of webapps and more documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета selenium-webdriver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = 4.19.0

%description   -n gem-selenium-webdriver-doc
Selenium is a browser automation tool for automated testing of webapps and more
documentation files.

Selenium implements the W3C WebDriver protocol to automate popular browsers. It
aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing, but any
web-based task can automated.

%description   -n gem-selenium-webdriver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета selenium-webdriver.
%endif


%if_enabled    devel
%package       -n gem-selenium-webdriver-devel
Version:       4.19.0
Release:       alt1
Summary:       Selenium is a browser automation tool for automated testing of webapps and more development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета selenium-webdriver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(selenium-webdriver) = 4.19.0
Requires:      gem(git) >= 1.19
Requires:      gem(rack) >= 2.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(webmock) >= 3.5
Requires:      gem(webrick) >= 1.7
Requires:      gem(yard) >= 0.9.11
Requires:      gem(debug) >= 1.7
Requires:      gem(steep) >= 1.5.0
Requires:      gem(selenium-devtools) = 0.123.0
Conflicts:     gem(git) >= 2
Conflicts:     gem(rack) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rspec) >= 3
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(webrick) >= 2
Conflicts:     gem(debug) >= 2
Conflicts:     gem(steep) >= 2

%description   -n gem-selenium-webdriver-devel
Selenium is a browser automation tool for automated testing of webapps and more
development package.

Selenium implements the W3C WebDriver protocol to automate popular browsers. It
aims to mimic the behaviour of a real user as it interacts with the
application's HTML. It's primarily intended for web application testing, but any
web-based task can automated.

%description   -n gem-selenium-webdriver-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета selenium-webdriver.
%endif


%if_enabled    devel
%package       -n selenium-devel
Version:       4.19.0
Release:       alt1
Summary:       A browser automation framework and ecosystem development package
Summary(ru_RU.UTF-8): Файлы для разработки selenium
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem-selenium-webdriver-devel = %EVR
Requires:      gem-selenium-devtools-devel

%description   -n selenium-devel
A browser automation framework and ecosystem development package.

%description   -n selenium-devel -l ru_RU.UTF-8
Файлы для разработки selenium.
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

%files         -n gem-selenium-devtools
%doc %ruby_gemslibdir/selenium-devtools-0.123.0/lib/selenium/devtools/README.md
%ruby_gemspecdir/selenium-devtools-0.123.0.gemspec
%ruby_gemslibdir/selenium-devtools-0.123.0

%if_enabled    doc
%files         -n gem-selenium-devtools-doc
%doc %ruby_gemslibdir/selenium-devtools-0.123.0/lib/selenium/devtools/README.md
%ruby_gemsdocdir/selenium-devtools-0.123.0
%endif

%if_enabled    devel
%files         -n gem-selenium-devtools-devel
%doc %ruby_gemslibdir/selenium-devtools-0.123.0/lib/selenium/devtools/README.md
%endif

%files         -n gem-selenium-webdriver
%doc README.md
%ruby_gemspecdir/selenium-webdriver-4.19.0.gemspec
%ruby_gemslibdir/selenium-webdriver-4.19.0

%if_enabled    doc
%files         -n gem-selenium-webdriver-doc
%doc README.md
%ruby_gemsdocdir/selenium-webdriver-4.19.0
%endif

%if_enabled    devel
%files         -n gem-selenium-webdriver-devel
%doc README.md
%endif

%if_enabled    devel
%files         -n selenium-devel
%endif

%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 4.19.0-alt1
- ^ 3.142.7 -> 4.19.0

* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1.2
- ! fixed deps to gems

* Thu Apr 16 2020 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1.1
- + obsolete/provides pair for gem-selenium-webdriver

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 3.142.7-alt1
- updated (^) 3.141.59 -> 3.142.7
- changed (*) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.141.59-alt1
- added (+) initial build with a packaged gem with usage Ruby Policy 2.0
