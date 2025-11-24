%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname chef-gyoku

Name:          gem-chef-gyoku
Version:       1.5.0
Release:       alt1
Summary:       Translates Ruby Hashes to XML
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/savonrb/chef-gyoku
Vcs:           https://github.com/savonrb/chef-gyoku.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(builder) >= 2.1.2
BuildRequires: gem(cookstyle) >= 8.0.0
BuildRequires: gem(coveralls) >= 0
BuildRequires: gem(fiddle) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rexml) >= 3.4
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(standard) >= 0
BuildConflicts: gem(rexml) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1
Requires:      gem(builder) >= 2.1.2
Requires:      gem(coveralls) >= 0
Requires:      gem(rexml) >= 3.4
Requires:      gem(simplecov) >= 0
Conflicts:     gem(rexml) >= 4
Provides:      gem(chef-gyoku) = 1.5.0

%description
Gyoku translates Ruby Hashes to XML


%if_enabled    doc
%package       -n gem-chef-gyoku-doc
Version:       1.5.0
Release:       alt1
Summary:       Translates Ruby Hashes to XML documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chef-gyoku
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-gyoku) = 1.5.0

%description   -n gem-chef-gyoku-doc
Translates Ruby Hashes to XML documentation files.

Gyoku translates Ruby Hashes to XML

%description   -n gem-chef-gyoku-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chef-gyoku.
%endif


%if_enabled    devel
%package       -n gem-chef-gyoku-devel
Version:       1.5.0
Release:       alt1
Summary:       Translates Ruby Hashes to XML development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chef-gyoku
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(chef-gyoku) = 1.5.0
Requires:      gem(cookstyle) >= 8.0.0
Requires:      gem(fiddle) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0
Requires:      gem(standard) >= 0

%description   -n gem-chef-gyoku-devel
Translates Ruby Hashes to XML development package.

Gyoku translates Ruby Hashes to XML

%description   -n gem-chef-gyoku-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chef-gyoku.
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
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-chef-gyoku-doc
%doc CHANGELOG.md MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-chef-gyoku-devel
%doc CHANGELOG.md MIT-LICENSE README.md
%endif


%changelog
* Sat Nov 22 2025 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
