%define        gemname danger

Name:          gem-danger
Version:       9.0.0
Release:       alt0.1
Summary:       Like Unit Tests, but for your Team Culture
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/danger/danger
Vcs:           https://github.com/danger/danger.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         patch.patch
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(chandler) >= 0
BuildRequires: gem(danger-gitlab) >= 0
BuildRequires: gem(danger-junit) >= 0.5 gem(danger-junit) < 1
BuildRequires: gem(fuubar) >= 2.5 gem(fuubar) < 3
BuildRequires: gem(guard) >= 2.16 gem(guard) < 3
BuildRequires: gem(guard-rspec) >= 4.7 gem(guard-rspec) < 5
BuildRequires: gem(guard-rubocop) >= 1.2 gem(guard-rubocop) < 2
BuildRequires: gem(listen) = 3.0.7
BuildRequires: gem(pry) >= 0.13 gem(pry) < 1
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(rspec_junit_formatter) >= 0.4 gem(rspec_junit_formatter) < 1
BuildRequires: gem(rubocop) >= 0.82 gem(rubocop) < 2
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(webmock) >= 2.1 gem(webmock) < 4
BuildRequires: gem(yard) >= 0.9.11 gem(yard) < 0.10
BuildRequires: gem(claide) >= 1.0 gem(claide) < 2
BuildRequires: gem(claide-plugins) >= 0.9.2
BuildRequires: gem(git) >= 1.7 gem(git) < 2
BuildRequires: gem(colored2) >= 3.1 gem(colored2) < 4
BuildRequires: gem(faraday) >= 0.9.0 gem(faraday) < 3
BuildRequires: gem(faraday-http-cache) >= 2.0 gem(faraday-http-cache) < 3
BuildRequires: gem(kramdown) >= 2.3 gem(kramdown) < 3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
BuildRequires: gem(octokit) >= 5.0 gem(octokit) < 6
BuildRequires: gem(terminal-table) >= 1 gem(terminal-table) < 4
BuildRequires: gem(cork) >= 0.1 gem(cork) < 1
BuildRequires: gem(no_proxy_fix) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency webmock >= 3.13.0,webmock < 4
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency faraday >= 2.0,faraday < 3
Requires:      gem(claide) >= 1.0 gem(claide) < 2
Requires:      gem(claide-plugins) >= 0.9.2
Requires:      gem(git) >= 1.7 gem(git) < 2
Requires:      gem(colored2) >= 3.1 gem(colored2) < 4
Requires:      gem(faraday) >= 0.9.0
Requires:      gem(faraday-http-cache) >= 2.0 gem(faraday-http-cache) < 3
Requires:      gem(kramdown) >= 2.3 gem(kramdown) < 3
Requires:      gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
Requires:      gem(octokit) >= 5.0 gem(octokit) < 6
Requires:      gem(terminal-table) >= 1 gem(terminal-table) < 4
Requires:      gem(cork) >= 0.1 gem(cork) < 1
Requires:      gem(no_proxy_fix) >= 0
Provides:      gem(danger) = 9.0.0


%description
Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.


%package       -n danger
Version:       9.0.0
Release:       alt0.1
Summary:       Like Unit Tests, but for your Team Culture executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета danger
Group:         Other
BuildArch:     noarch

Requires:      gem(danger) = 9.0.0

%description   -n danger
Like Unit Tests, but for your Team Culture executable(s).

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n danger -l ru_RU.UTF-8
Исполнямка для самоцвета danger.


%package       -n gem-danger-doc
Version:       9.0.0
Release:       alt0.1
Summary:       Like Unit Tests, but for your Team Culture documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета danger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(danger) = 9.0.0

%description   -n gem-danger-doc
Like Unit Tests, but for your Team Culture documentation files.

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n gem-danger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета danger.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md lib/danger/commands/plugins/plugin_readme.rb lib/danger/plugin_support/templates/readme_table.html.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n danger
%doc README.md lib/danger/commands/plugins/plugin_readme.rb lib/danger/plugin_support/templates/readme_table.html.erb
%_bindir/danger

%files         -n gem-danger-doc
%doc README.md lib/danger/commands/plugins/plugin_readme.rb lib/danger/plugin_support/templates/readme_table.html.erb
%ruby_gemdocdir


%changelog
* Fri Oct 14 2022 Pavel Skrylev <majioa@altlinux.org> 9.0.0-alt0.1
- ^ 8.6.1 -> 9.0.0

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 8.6.1-alt1
- + packaged gem with Ruby Policy 2.0
