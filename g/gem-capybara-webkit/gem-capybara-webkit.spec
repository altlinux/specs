# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname capybara-webkit

Name:          gem-capybara-webkit
Version:       1.15.1.17
Release:       alt1
Summary:       Headless Webkit driver for Capybara
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/thoughtbot/capybara-webkit
Vcs:           https://github.com/thoughtbot/capybara-webkit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: qt5-webkit-devel
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(capybara) >= 2.3
BuildRequires: gem(json) >= 0
BuildRequires: gem(launchy) >= 0
BuildRequires: gem(mini_magick) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.5
BuildRequires: gem(sinatra) >= 0
BuildConflicts: gem(capybara) >= 4.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(puma) >= 0
Requires:      gem(capybara) >= 2.3
Requires:      gem(json) >= 0
Conflicts:     gem(capybara) >= 4.0
Provides:      gem(capybara-webkit) = 1.15.1.17


%description
A Capybara driver for headless WebKit to test JavaScript web apps.


%if_enabled    doc
%package       -n gem-capybara-webkit-doc
Version:       1.15.1.17
Release:       alt1
Summary:       Headless Webkit driver for Capybara documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета capybara-webkit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(capybara-webkit) = 1.15.1.17

%description   -n gem-capybara-webkit-doc
Headless Webkit driver for Capybara documentation files.

A Capybara driver for headless WebKit to test JavaScript web apps.

%description   -n gem-capybara-webkit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета capybara-webkit.
%endif


%prep
%setup
%autopatch -p1

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CONTRIBUTING.md LICENSE README.md
%_bindir/webkit_server
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-capybara-webkit-doc
%doc CONTRIBUTING.md LICENSE README.md
%ruby_gemdocdir
%endif


%changelog
* Mon Aug 05 2024 Pavel Skrylev <majioa@altlinux.org> 1.15.1.17-alt1
- ^ 1.15.1 -> 1.15.1p17

* Tue Mar 31 2020 Pavel Skrylev <majioa@altlinux.org> 1.15.1-alt1.1
- ! spec tag

* Thu Sep 19 2019 Pavel Skrylev <majioa@altlinux.org> 1.15.1-alt1
- + packaged gem with usage Ruby Policy 2.0
