%define        gemname danger

Name:          gem-danger
Version:       8.6.1
Release:       alt1
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
BuildRequires: gem(claide) >= 1.0 gem(claide) < 2
BuildRequires: gem(claide-plugins) >= 0.9.2
BuildRequires: gem(git) >= 1.7 gem(git) < 2
BuildRequires: gem(colored2) >= 3.1 gem(colored2) < 4
BuildRequires: gem(faraday) >= 0.9.0 gem(faraday) < 2.0
BuildRequires: gem(faraday-http-cache) >= 2.0 gem(faraday-http-cache) < 3
BuildRequires: gem(kramdown) >= 2.3 gem(kramdown) < 3
BuildRequires: gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
BuildRequires: gem(octokit) >= 4.7 gem(octokit) < 5
BuildRequires: gem(terminal-table) >= 1 gem(terminal-table) < 4
BuildRequires: gem(cork) >= 0.1 gem(cork) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(claide) >= 1.0 gem(claide) < 2
Requires:      gem(claide-plugins) >= 0.9.2
Requires:      gem(git) >= 1.7 gem(git) < 2
Requires:      gem(colored2) >= 3.1 gem(colored2) < 4
Requires:      gem(faraday) >= 0.9.0 gem(faraday) < 2.0
Requires:      gem(faraday-http-cache) >= 2.0 gem(faraday-http-cache) < 3
Requires:      gem(kramdown) >= 2.3 gem(kramdown) < 3
Requires:      gem(kramdown-parser-gfm) >= 1.0 gem(kramdown-parser-gfm) < 2
Requires:      gem(octokit) >= 4.7 gem(octokit) < 5
Requires:      gem(terminal-table) >= 1 gem(terminal-table) < 4
Requires:      gem(cork) >= 0.1 gem(cork) < 1
Provides:      gem(danger) = 8.6.1


%description
Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.


%package       -n danger
Version:       8.6.1
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета danger
Group:         Other
BuildArch:     noarch

Requires:      gem(danger) = 8.6.1

%description   -n danger
Like Unit Tests, but for your Team Culture executable(s).

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n danger -l ru_RU.UTF-8
Исполнямка для самоцвета danger.


%package       -n gem-danger-doc
Version:       8.6.1
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета danger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(danger) = 8.6.1

%description   -n gem-danger-doc
Like Unit Tests, but for your Team Culture documentation files.

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n gem-danger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета danger.


%package       -n gem-danger-devel
Version:       8.6.1
Release:       alt1
Summary:       Like Unit Tests, but for your Team Culture development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета danger
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(danger) = 8.6.1

%description   -n gem-danger-devel
Like Unit Tests, but for your Team Culture development package.

Stop Saying 'You Forgot To...' in Code Review. Formalize your Pull Request
etiquette.

%description   -n gem-danger-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета danger.


%prep
%setup
%autopatch

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

%files         -n danger
%doc README.md
%_bindir/danger

%files         -n gem-danger-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-danger-devel
%doc README.md


%changelog
* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 8.6.1-alt1
- + packaged gem with Ruby Policy 2.0
