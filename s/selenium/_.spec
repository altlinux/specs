# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname selenium-webdriver
%define        gemname selenium-webdriver

Name:          selenium
Version:       3.141.59
Release:       alt1
Summary:       A browser automation framework and ecosystem
License:       Apache-2.0
Group:         Development/Tools
Url:           https://www.seleniumhq.org
%vcs           https://github.com/SeleniumHQ/selenium.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%gem_replace_version childprocess ~> 2.0
Requires:      gem-%pkgname = %version

%description
Selenium is an umbrella project encapsulating a variety of tools and libraries
enabling web browser automation. Selenium specifically provides infrastructure
for the W3C WebDriver specification  a platform and language-neutral coding
interface compatible with all major web browsers.

The project is made possible by volunteer contributors who've generously
donated thousands of hours in code development and upkeep.


%package       -n gem-%pkgname
Summary:       Library files for %gemname gem
Summary(ru_RU.UTF-8): Файлы библиотеки для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n gem-%pkgname
Library files for %gemname gem.

%description   -n gem-%pkgname -l ru_RU.UTF8
Файлы библиотеки для самоцвета %gemname.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-%pkgname
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.141.59-alt1
- + initial build with a packaged gem with usage Ruby Policy 2.0
