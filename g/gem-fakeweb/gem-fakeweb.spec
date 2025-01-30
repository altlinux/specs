%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fakeweb

Name:          gem-fakeweb
Version:       1.3.0.124
Release:       alt1
Summary:       A tool for faking responses to HTTP requests
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/chrisk/fakeweb
Vcs:           https://github.com/chrisk/fakeweb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 12.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(ZenTest) >= 4.9
BuildRequires: gem(json) >= 1.7
BuildRequires: gem(mocha) >= 0
BuildRequires: gem(sdoc) >= 0
BuildRequires: gem(simplecov) >= 0.7
BuildRequires: gem(simplecov-console) >= 0.1
BuildRequires: gem(test-unit) >= 3.2
BuildRequires: gem(yard) >= 0
BuildConflicts: gem(ZenTest) >= 5
BuildConflicts: gem(json) >= 3
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-console) >= 1
BuildConflicts: gem(test-unit) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 2.0,mocha < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency json >= 2.3.0,json < 3
%ruby_use_gem_dependency psych >= 4.0.4,psych < 5
Provides:      gem(fakeweb) = 1.3.0.124

%description
FakeWeb is a helper for faking web requests in Ruby. It works at a global level,
without modifying code or writing extensive stubs.


%if_enabled    doc
%package       -n gem-fakeweb-doc
Version:       1.3.0.124
Release:       alt1
Summary:       A tool for faking responses to HTTP requests documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fakeweb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fakeweb) = 1.3.0.124

%description   -n gem-fakeweb-doc
A tool for faking responses to HTTP requests documentation files.

FakeWeb is a helper for faking web requests in Ruby. It works at a global level,
without modifying code or writing extensive stubs.

%description   -n gem-fakeweb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fakeweb.
%endif


%if_enabled    devel
%package       -n gem-fakeweb-devel
Version:       1.3.0.124
Release:       alt1
Summary:       A tool for faking responses to HTTP requests development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fakeweb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fakeweb) = 1.3.0.124
Requires:      gem(ZenTest) >= 4.9
Requires:      gem(json) >= 1.7
Requires:      gem(mocha) >= 1.0
Requires:      gem(rake) >= 12.0
Requires:      gem(sdoc) >= 0
Requires:      gem(simplecov) >= 0.7
Requires:      gem(simplecov-console) >= 0.1
Requires:      gem(test-unit) >= 3.2
Conflicts:     gem(ZenTest) >= 5
Conflicts:     gem(json) >= 3
Conflicts:     gem(mocha) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-console) >= 1
Conflicts:     gem(test-unit) >= 4

%description   -n gem-fakeweb-devel
A tool for faking responses to HTTP requests development package.

FakeWeb is a helper for faking web requests in Ruby. It works at a global level,
without modifying code or writing extensive stubs.

%description   -n gem-fakeweb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fakeweb.
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
%doc CHANGELOG LICENSE.txt README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fakeweb-doc
%doc CHANGELOG LICENSE.txt README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fakeweb-devel
%doc CHANGELOG LICENSE.txt README.rdoc
%endif


%changelog
* Mon Jan 27 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.0.124-alt1
- ^ 1.3.0 -> 1.3.0.124

* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0
