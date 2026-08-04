%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname travis

Name:          gem-travis
Version:       1.14.0.6.1
Release:       alt0.1
Summary:       Travis CI client
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/travis-ci/travis.rb
Vcs:           https://github.com/travis-ci/travis.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rspec) >= 3.10.0
BuildRequires: gem(rspec-its) >= 1.3.0
BuildRequires: gem(sinatra) >= 3.0.6
BuildRequires: gem(gh) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(activesupport) >= 6.1.3.2
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(rubocop-performance) >= 0
BuildRequires: gem(rubocop-rspec) >= 0
BuildRequires: gem(simplecov-console) >= 0
BuildRequires: gem(faraday) >= 2.6.0
BuildRequires: gem(faraday-rack) >= 2
BuildRequires: gem(highline) >= 2.1.0
BuildRequires: gem(json) >= 2.9
BuildRequires: gem(launchy) >= 2.5.2
BuildRequires: gem(pusher-client) >= 0.6.2
BuildRequires: gem(rack-test) >= 1.1.0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-its) >= 3
BuildConflicts: gem(sinatra) >= 5
BuildConflicts: gem(gh) >= 1
BuildConflicts: gem(activesupport) >= 8
BuildConflicts: gem(faraday) >= 3
BuildConflicts: gem(faraday-rack) >= 3
BuildConflicts: gem(highline) >= 4
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(launchy) >= 2.6
BuildConflicts: gem(pusher-client) >= 0.7
BuildConflicts: gem(rack-test) >= 2.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency activesupport >= 7.1,activesupport < 8
%ruby_use_gem_dependency rack-test >= 1.1.0,rack-test < 2
%ruby_use_gem_dependency faraday >= 2.6.0,faraday < 3
%ruby_use_gem_dependency sinatra >= 4,sinatra < 5
%ruby_use_gem_dependency highline >= 3.1.1,highline < 4
%ruby_use_gem_dependency rspec-its >= 2.0.0,rspec-its < 3
Requires:      gem(gh) >= 0
Requires:      gem(faraday) >= 2.6.0
Requires:      gem(faraday-rack) >= 2
Requires:      gem(highline) >= 2.1.0
Requires:      gem(json) >= 2.9
Requires:      gem(launchy) >= 2.5.2
Requires:      gem(pusher-client) >= 0.6.2
Requires:      gem(rack-test) >= 1.1.0
Conflicts:     gem(gh) >= 1
Conflicts:     gem(faraday) >= 3
Conflicts:     gem(faraday-rack) >= 3
Conflicts:     gem(highline) >= 4
Conflicts:     gem(json) >= 3
Conflicts:     gem(launchy) >= 2.6
Conflicts:     gem(pusher-client) >= 0.7
Conflicts:     gem(rack-test) >= 2.2
Provides:      gem(travis) = 1.14.0.6.1

%ruby_use_gem_version travis:%version

%description
The travis gem includes both a command line client and a Ruby library to
interface with a Travis CI service using GitHub account. Both work with
travis-ci.com or any custom Travis CI setup you might have. Check out the
installation instructions to get it running in no time.


%package       -n travis
Version:       1.14.0.6.1
Release:       alt0.1
Summary:       Travis CI client executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета travis
Group:         Other
BuildArch:     noarch

Requires:      gem(travis) = 1.14.0.6.1

%description   -n travis
Travis CI client executable(s).

The travis gem includes both a command line client and a Ruby library to
interface with a Travis CI service using GitHub account. Both work with
travis-ci.com or any custom Travis CI setup you might have. Check out the
installation instructions to get it running in no time.


%description   -n travis -l ru_RU.UTF-8
Исполнямка для самоцвета travis.


%if_enabled    doc
%package       -n gem-travis-doc
Version:       1.14.0.6.1
Release:       alt0.1
Summary:       Travis CI client documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета travis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(travis) = 1.14.0.6.1

%description   -n gem-travis-doc
Travis CI client documentation files.

The travis gem includes both a command line client and a Ruby library to
interface with a Travis CI service using GitHub account. Both work with
travis-ci.com or any custom Travis CI setup you might have. Check out the
installation instructions to get it running in no time.


%description   -n gem-travis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета travis.
%endif


%if_enabled    devel
%package       -n gem-travis-devel
Version:       1.14.0.6.1
Release:       alt0.1
Summary:       Travis CI client development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета travis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(travis) = 1.14.0.6.1
Requires:      gem(rspec) >= 3.10.0
Requires:      gem(rspec-its) >= 1.3.0
Requires:      gem(sinatra) >= 3.0.6
Requires:      gem(rake) >= 0
Requires:      gem(activesupport) >= 6.1.3.2
Requires:      gem(rubocop) >= 0
Requires:      gem(rubocop-performance) >= 0
Requires:      gem(rubocop-rspec) >= 0
Requires:      gem(simplecov-console) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-its) >= 3
Conflicts:     gem(sinatra) >= 5
Conflicts:     gem(activesupport) >= 8

%description   -n gem-travis-devel
Travis CI client development package.

The travis gem includes both a command line client and a Ruby library to
interface with a Travis CI service using GitHub account. Both work with
travis-ci.com or any custom Travis CI setup you might have. Check out the
installation instructions to get it running in no time.


%description   -n gem-travis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета travis.
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
%ruby_gemspec
%ruby_gemlibdir

%files         -n travis
%doc README.md
%_bindir/travis

%if_enabled    doc
%files         -n gem-travis-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-travis-devel
%doc README.md
%endif


%changelog
* Tue Aug 04 2026 Pavel Skrylev <majioa@altlinux.org> 1.14.0.6.1-alt0.1
- ^ 1.14.0p6 -> 1.14.0p6.1
- * changed dep from json_pure to json

* Sat Aug 01 2026 Pavel Skrylev <majioa@altlinux.org> 1.14.0.6-alt0.1
- ^ 1.14.0 -> 1.14.0p6

* Thu Feb 06 2025 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt2
- ! fixed deps for activesupport gem

* Fri Oct 18 2024 Pavel Skrylev <majioa@altlinux.org> 1.14.0-alt1
- + packaged gem with Ruby Policy 2.0
