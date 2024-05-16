%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname blade-sauce_labs_plugin

Name:          gem-blade-sauce-labs-plugin
Version:       0.7.3
Release:       alt1
Summary:       Blade Runner plugin for Sauce Labs (saucelabs.com)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/javan/blade-sauce_labs_plugin
Vcs:           https://github.com/javan/blade-sauce_labs_plugin.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.10
BuildRequires: gem(blade) >= 0.5.0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(webmock) >= 1.21.0
BuildRequires: gem(selenium-webdriver) >= 0
BuildRequires: gem(faraday) >= 0
BuildRequires: gem(childprocess) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(webmock) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Requires:      gem(selenium-webdriver) >= 0
Requires:      gem(faraday) >= 0
Requires:      gem(childprocess) >= 0
Provides:      gem(blade-sauce_labs_plugin) = 0.7.3


%description
Blade Runner plugin for Sauce Labs (saucelabs.com)


%if_enabled    doc
%package       -n gem-blade-sauce-labs-plugin-doc
Version:       0.7.3
Release:       alt1
Summary:       Blade Runner plugin for Sauce Labs (saucelabs.com) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета blade-sauce_labs_plugin
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(blade-sauce_labs_plugin) = 0.7.3

%description   -n gem-blade-sauce-labs-plugin-doc
Blade Runner plugin for Sauce Labs (saucelabs.com) documentation files.

%description   -n gem-blade-sauce-labs-plugin-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета blade-sauce_labs_plugin.
%endif


%if_enabled    devel
%package       -n gem-blade-sauce-labs-plugin-devel
Version:       0.7.3
Release:       alt1
Summary:       Blade Runner plugin for Sauce Labs (saucelabs.com) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета blade-sauce_labs_plugin
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(blade-sauce_labs_plugin) = 0.7.3
Requires:      gem(bundler) >= 1.10
Requires:      gem(blade) >= 0.5.0
Requires:      gem(rake) >= 10.0
Requires:      gem(webmock) >= 1.21.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(webmock) >= 4

%description   -n gem-blade-sauce-labs-plugin-devel
Blade Runner plugin for Sauce Labs (saucelabs.com) development package.

%description   -n gem-blade-sauce-labs-plugin-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета blade-sauce_labs_plugin.
%endif


%prep
%setup

%build
%ruby_build

%install
rm -rf support
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-blade-sauce-labs-plugin-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-blade-sauce-labs-plugin-devel
%doc README.md
%endif


%changelog
* Wed Apr 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.7.3-alt1
- + packaged gem with Ruby Policy 2.0
