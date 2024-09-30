%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rake-manifest

Name:          gem-rake-manifest
Version:       0.2.3
Release:       alt1
Summary:       Rake tasks to generate and check a manifest file
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mvz/rake-manifest
Vcs:           https://github.com/mvz/rake-manifest.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubocop) >= 1.15.0
BuildRequires: gem(rubocop-packaging) >= 0.5.0
BuildRequires: gem(rubocop-performance) >= 1.11.3
BuildRequires: gem(rubocop-rake) >= 0.6.0
BuildRequires: gem(rubocop-rspec) >= 2.4.0
BuildRequires: gem(simplecov) >= 0.17
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubocop) >= 2
BuildConflicts: gem(rubocop-packaging) >= 1
BuildConflicts: gem(rubocop-performance) >= 2
BuildConflicts: gem(rubocop-rake) >= 1
BuildConflicts: gem(rubocop-rspec) >= 4.0
BuildConflicts: gem(simplecov) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency rubocop-rspec >= 2.4.0,rubocop-rspec < 3
%ruby_use_gem_dependency rubocop-performance >= 1.11.3,rubocop-performance < 2
%ruby_use_gem_dependency rubocop-rake >= 0.6.0,rubocop-rake < 1
%ruby_use_gem_dependency rubocop-packaging >= 0.5.2,rubocop-packaging < 1
%ruby_ignore_names cgi_multipart_eof_fix,gem_plugin,(?-mix:mongrel_),fastthread,(?-mix:project)
Provides:      gem(rake-manifest) = 0.2.3


%description
Rake tasks to generate and check a manifest file


%if_enabled    doc
%package       -n gem-rake-manifest-doc
Version:       0.2.3
Release:       alt1
Summary:       Rake tasks to generate and check a manifest file documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rake-manifest
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rake-manifest) = 0.2.3

%description   -n gem-rake-manifest-doc
Rake tasks to generate and check a manifest file documentation files.

%description   -n gem-rake-manifest-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rake-manifest.
%endif


%if_enabled    devel
%package       -n gem-rake-manifest-devel
Version:       0.2.3
Release:       alt1
Summary:       Rake tasks to generate and check a manifest file development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rake-manifest
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rake-manifest) = 0.2.3
Requires:      gem(rake) >= 13.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubocop) >= 1.15.0
Requires:      gem(rubocop-packaging) >= 0.5.0
Requires:      gem(rubocop-performance) >= 1.11.3
Requires:      gem(rubocop-rake) >= 0.6.0
Requires:      gem(rubocop-rspec) >= 2.4.0
Requires:      gem(simplecov) >= 0.17
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubocop) >= 2
Conflicts:     gem(rubocop-packaging) >= 1
Conflicts:     gem(rubocop-performance) >= 2
Conflicts:     gem(rubocop-rake) >= 1
Conflicts:     gem(rubocop-rspec) >= 4.0
Conflicts:     gem(simplecov) >= 1

%description   -n gem-rake-manifest-devel
Rake tasks to generate and check a manifest file development package.

%description   -n gem-rake-manifest-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rake-manifest.
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
%files         -n gem-rake-manifest-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rake-manifest-devel
%doc README.md
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.3-alt1
- + packaged gem with Ruby Policy 2.0
