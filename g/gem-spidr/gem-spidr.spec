%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname spidr

Name:          gem-spidr
Version:       0.7.2
Release:       alt1
Summary:       A versatile Ruby web spidering library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/spidr#readme
Vcs:           https://github.com/postmodern/spidr.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(base64) >= 0.1
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(nokogiri) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildRequires: gem(simplecov) >= 0.20
BuildRequires: gem(sinatra) >= 4.0
BuildRequires: gem(webmock) >= 3.0
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(yard-spellcheck) >= 0
BuildConflicts: gem(base64) >= 1
BuildConflicts: gem(nokogiri) >= 2
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(webmock) >= 4
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.0.0
Requires:      gem(base64) >= 0.1
Requires:      gem(nokogiri) >= 1.3
Conflicts:     gem(base64) >= 1
Conflicts:     gem(nokogiri) >= 2
Provides:      gem(spidr) = 0.7.2

%description
Spidr is a versatile Ruby web spidering library that can spider a site, multiple
domains, certain links or infinitely. Spidr is designed to be fast and easy to
use.


%if_enabled    doc
%package       -n gem-spidr-doc
Version:       0.7.2
Release:       alt1
Summary:       A versatile Ruby web spidering library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета spidr
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(spidr) = 0.7.2

%description   -n gem-spidr-doc
A versatile Ruby web spidering library documentation files.

Spidr is a versatile Ruby web spidering library that can spider a site, multiple
domains, certain links or infinitely. Spidr is designed to be fast and easy to
use.

%description   -n gem-spidr-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета spidr.
%endif


%if_enabled    devel
%package       -n gem-spidr-devel
Version:       0.7.2
Release:       alt1
Summary:       A versatile Ruby web spidering library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета spidr
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(spidr) = 0.7.2
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(kramdown) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubygems-tasks) >= 0.2
Requires:      gem(simplecov) >= 0.20
Requires:      gem(sinatra) >= 4.0
Requires:      gem(webmock) >= 3.0
Requires:      gem(yard) >= 0.9
Requires:      gem(yard-spellcheck) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(webmock) >= 4
Conflicts:     gem(yard) >= 1

%description   -n gem-spidr-devel
A versatile Ruby web spidering library development package.

Spidr is a versatile Ruby web spidering library that can spider a site, multiple
domains, certain links or infinitely. Spidr is designed to be fast and easy to
use.

%description   -n gem-spidr-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета spidr.
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
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-spidr-doc
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-spidr-devel
%doc ChangeLog.md LICENSE.txt README.md
%endif


%changelog
* Tue Mar 10 2026 Pavel Skrylev <majioa@altlinux.org> 0.7.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
