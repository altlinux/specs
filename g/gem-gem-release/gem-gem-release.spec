%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname gem-release

Name:          gem-gem-release
Version:       2.2.2.29
Release:       alt1
Summary:       Release your ruby gems with ease
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/svenfuchs/gem-release
Vcs:           https://github.com/svenfuchs/gem-release.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(geminabox) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(simplecov-lcov) >= 0
BuildRequires: gem(webmock) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(gem-release) = 2.2.2.29

%ruby_use_gem_version gem-release:2.2.2.29

%description
Release your ruby gems with ease. (What a bold statement for such a tiny plugin
...)


%if_enabled    doc
%package       -n gem-gem-release-doc
Version:       2.2.2.29
Release:       alt1
Summary:       Release your ruby gems with ease documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gem-release
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gem-release) = 2.2.2.29

%description   -n gem-gem-release-doc
Release your ruby gems with ease documentation files.

Release your ruby gems with ease. (What a bold statement for such a tiny plugin
...)
%description   -n gem-gem-release-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gem-release.
%endif


%if_enabled    devel
%package       -n gem-release-devel
Version:       2.2.2.29
Release:       alt1
Summary:       Release your ruby gems with ease development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gem-release
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gem-release) = 2.2.2.29
Requires:      gem(geminabox) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(simplecov-lcov) >= 0
Requires:      gem(webmock) >= 0

%description   -n gem-release-devel
Release your ruby gems with ease development package.

Release your ruby gems with ease. (What a bold statement for such a tiny plugin
...)
%description   -n gem-release-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gem-release.
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
%doc README.md README.md.erb
%ruby_gemspec
%ruby_gemplugin
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gem-release-doc
%doc README.md README.md.erb
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-release-devel
%doc README.md README.md.erb
%endif


%changelog
* Fri Mar 15 2024 Pavel Skrylev <majioa@altlinux.org> 2.2.2.29-alt1
- ^ 2.2.2 -> 2.2.2p29

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 2.2.2-alt1
- + packaged gem with Ruby Policy 2.0
