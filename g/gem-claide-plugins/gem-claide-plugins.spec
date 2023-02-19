%define        gemname claide-plugins

Name:          gem-claide-plugins
Version:       0.9.2.1
Release:       alt0.1
Summary:       CLAide plugin which shows info about available CLAide plugins
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/cocoapods/claide-plugins
Vcs:           https://github.com/cocoapods/claide-plugins.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(pry) >= 0
BuildRequires: gem(bacon) >= 0
BuildRequires: gem(mocha-on-bacon) >= 0
BuildRequires: gem(prettybacon) >= 0
BuildRequires: gem(vcr) >= 0
BuildRequires: gem(webmock) >= 0
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(nap) >= 0
BuildRequires: gem(cork) >= 0
BuildRequires: gem(open4) >= 1.3
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(open4) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
Requires:      gem(nap) >= 0
Requires:      gem(cork) >= 0
Requires:      gem(open4) >= 1.3
Conflicts:     gem(open4) >= 2
Provides:      gem(claide-plugins) = 0.9.2.1

%ruby_use_gem_version claide-plugins:0.9.2.1

%description
This CLAide plugin shows information about all available CLAide plugins (yes,
this is very meta!). This plugin adds the "plugins" subcommand to a binary so
that you can list all plugins (registered in the reference JSON hosted at
CocoaPods/cocoapods-plugins)


%package       -n gem-claide-plugins-doc
Version:       0.9.2.1
Release:       alt0.1
Summary:       CLAide plugin which shows info about available CLAide plugins documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета claide-plugins
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(claide-plugins) = 0.9.2.1

%description   -n gem-claide-plugins-doc
CLAide plugin which shows info about available CLAide plugins documentation
files.

This CLAide plugin shows information about all available CLAide plugins (yes,
this is very meta!). This plugin adds the "plugins" subcommand to a binary so
that you can list all plugins (registered in the reference JSON hosted at
CocoaPods/cocoapods-plugins)

%description   -n gem-claide-plugins-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета claide-plugins.


%package       -n gem-claide-plugins-devel
Version:       0.9.2.1
Release:       alt0.1
Summary:       CLAide plugin which shows info about available CLAide plugins development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета claide-plugins
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(claide-plugins) = 0.9.2.1
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Requires:      gem(pry) >= 0
Requires:      gem(bacon) >= 0
Requires:      gem(mocha-on-bacon) >= 0
Requires:      gem(prettybacon) >= 0
Requires:      gem(vcr) >= 0
Requires:      gem(webmock) >= 0
Requires:      gem(codeclimate-test-reporter) >= 0
Requires:      gem(rubocop) >= 0
Conflicts:     gem(bundler) >= 3

%description   -n gem-claide-plugins-devel
CLAide plugin which shows info about available CLAide plugins development
package.

This CLAide plugin shows information about all available CLAide plugins (yes,
this is very meta!). This plugin adds the "plugins" subcommand to a binary so
that you can list all plugins (registered in the reference JSON hosted at
CocoaPods/cocoapods-plugins)

%description   -n gem-claide-plugins-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета claide-plugins.


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

%files         -n gem-claide-plugins-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-claide-plugins-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.2.1-alt0.1
- ^ 0.9.2 -> 0.9.2.1

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.2-alt1
- + packaged gem with Ruby Policy 2.0
