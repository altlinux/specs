%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rspec-retry

Name:          gem-rspec-retry
Version:       0.6.2.11
Release:       alt0.1
Summary:       retry intermittently failing rspec examples
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/NoRedInk/rspec-retry
Vcs:           https://github.com/noredink/rspec-retry.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(byebug) >= 9.0.6
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rspec-core) > 3.3
BuildConflicts: gem(byebug) >= 13
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency byebug >= 12.0,byebug < 13
Requires:      gem(rspec-core) > 3.3
Provides:      gem(rspec-retry) = 0.6.2.11

%ruby_use_gem_version rspec-retry:0.6.2.11

%description
retry intermittently failing rspec examples


%if_enabled    doc
%package       -n gem-rspec-retry-doc
Version:       0.6.2.11
Release:       alt0.1
Summary:       retry intermittently failing rspec examples documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rspec-retry
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-retry) = 0.6.2.11

%description   -n gem-rspec-retry-doc
retry intermittently failing rspec examples documentation files.

%description   -n gem-rspec-retry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rspec-retry.
%endif


%if_enabled    devel
%package       -n gem-rspec-retry-devel
Version:       0.6.2.11
Release:       alt0.1
Summary:       retry intermittently failing rspec examples development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rspec-retry
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(rspec-retry) = 0.6.2.11
Requires:      gem(appraisal) >= 0
Requires:      gem(byebug) >= 9.0.6
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rspec) >= 0
Conflicts:     gem(byebug) >= 13

%description   -n gem-rspec-retry-devel
retry intermittently failing rspec examples development package.

%description   -n gem-rspec-retry-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rspec-retry.
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
%doc LICENSE README.md changelog.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rspec-retry-doc
%doc LICENSE README.md changelog.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rspec-retry-devel
%doc LICENSE README.md changelog.md
%endif


%changelog
* Thu Nov 27 2025 Pavel Skrylev <majioa@altlinux.org> 0.6.2.11-alt0.1
- ^ 0.6.2 -> 0.6.2p11

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- + packaged gem with Ruby Policy 2.0
