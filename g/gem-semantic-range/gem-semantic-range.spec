%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname semantic_range

Name:          gem-semantic-range
Version:       2.3.1
Release:       alt1
Summary:       node-semver rewritten in ruby, for comparison and inclusion of semantic versions and ranges
License:       MIT
Group:         Development/Ruby
Url:           https://libraries.io/github/librariesio/semantic_range
Vcs:           https://github.com/librariesio/semantic_range.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 1.11
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(guard-rspec) >= 0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(semantic_range) = 2.3.1


%description
node-semver rewritten in ruby, for comparison and inclusion of semantic versions
and ranges


%if_enabled    doc
%package       -n gem-semantic-range-doc
Version:       2.3.1
Release:       alt1
Summary:       node-semver rewritten in ruby, for comparison and inclusion of semantic versions and ranges documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета semantic_range
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(semantic_range) = 2.3.1

%description   -n gem-semantic-range-doc
node-semver rewritten in ruby, for comparison and inclusion of semantic versions
and ranges documentation files.

node-semver rewritten in ruby, for comparison and inclusion of semantic versions
and ranges

%description   -n gem-semantic-range-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета semantic_range.
%endif


%if_enabled    devel
%package       -n gem-semantic-range-devel
Version:       2.3.1
Release:       alt1
Summary:       node-semver rewritten in ruby, for comparison and inclusion of semantic versions and ranges development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета semantic_range
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(semantic_range) = 2.3.1
Requires:      gem(bundler) >= 1.11
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.4
Requires:      gem(guard-rspec) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-semantic-range-devel
node-semver rewritten in ruby, for comparison and inclusion of semantic versions
and ranges development package.

node-semver rewritten in ruby, for comparison and inclusion of semantic versions
and ranges

%description   -n gem-semantic-range-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета semantic_range.
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

%if_enabled    doc
%files         -n gem-semantic-range-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-semantic-range-devel
%doc README.md
%endif


%changelog
* Tue Apr 23 2024 Pavel Skrylev <majioa@altlinux.org> 2.3.1-alt1
- + packaged gem with Ruby Policy 2.0
