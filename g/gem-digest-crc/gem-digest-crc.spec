%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname digest-crc

Name:          gem-digest-crc
Version:       0.6.5
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/digest-crc#readme
Vcs:           https://github.com/postmodern/digest-crc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         gemspec.yml.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 2.0
BuildRequires: gem(rake) >= 12.0.0
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0.9
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(kramdown-parser-gfm) >= 0
BuildRequires: gem(github-markup) >= 1.1
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(github-markup) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency github-markup >= 4.0,github-markup < 5
Requires:      gem(rake) >= 12.0.0
Conflicts:     gem(rake) >= 14
Provides:      gem(digest-crc) = 0.6.5


%description
Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.


%if_enabled    doc
%package       -n gem-digest-crc-doc
Version:       0.6.5
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета digest-crc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.6.5

%description   -n gem-digest-crc-doc
A Cyclic Redundancy Check (CRC) library for Ruby documentation files.

Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%description   -n gem-digest-crc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета digest-crc.
%endif


%if_enabled    devel
%package       -n gem-digest-crc-devel
Version:       0.6.5
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета digest-crc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.6.5
Requires:      gem(bundler) >= 2.0
Requires:      gem(rubygems-tasks) >= 0.2
Requires:      gem(rspec) >= 3.0
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0.9
Requires:      gem(kramdown) >= 0
Requires:      gem(kramdown-parser-gfm) >= 0
Requires:      gem(github-markup) >= 1.1
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(yard) >= 1
Conflicts:     gem(github-markup) >= 5

%description   -n gem-digest-crc-devel
A Cyclic Redundancy Check (CRC) library for Ruby development package.

Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%description   -n gem-digest-crc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета digest-crc.
%endif


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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-digest-crc-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-digest-crc-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.5-alt1
- ^ 0.6.4 -> 0.6.5

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- ^ 0.6.3 -> 0.6.4

* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- + packaged gem with Ruby Policy 2.0
