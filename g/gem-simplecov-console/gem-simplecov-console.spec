%define        _unpackaged_files_terminate_build 1
%define        gemname simplecov-console

Name:          gem-simplecov-console
Version:       0.9.1
Release:       alt1
Summary:       Simple console output formatter
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/chetan/simplecov-console
Vcs:           https://github.com/chetan/simplecov-console.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(terminal-table) >= 0
BuildRequires: gem(ansi) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(bundler) >= 2.1
BuildRequires: gem(juwelier) >= 0
BuildConflicts: gem(bundler) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(simplecov) >= 0
Requires:      gem(terminal-table) >= 0
Requires:      gem(ansi) >= 0
Provides:      gem(simplecov-console) = 0.9.1


%description
Simple console output formatter for SimpleCov


%package       -n gem-simplecov-console-doc
Version:       0.9.1
Release:       alt1
Summary:       Simple console output formatter documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета simplecov-console
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(simplecov-console) = 0.9.1

%description   -n gem-simplecov-console-doc
Simple console output formatter documentation files.

Simple console output formatter for SimpleCov

%description   -n gem-simplecov-console-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета simplecov-console.


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

%files         -n gem-simplecov-console-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt1
- + packaged gem with Ruby Policy 2.0 without devel
