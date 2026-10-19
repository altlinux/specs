%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname digest-crc

Name:          gem-digest-crc
Version:       0.7.0
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/postmodern/digest-crc#readme
Vcs:           https://github.com/postmodern/digest-crc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
BuildRequires: gem(github-markup) >= 1.1
%if_enabled check
BuildRequires: gem(bundler) >= 2.0.0
BuildRequires: gem(kramdown) >= 0
BuildRequires: gem(kramdown-parser-gfm) >= 0
BuildRequires: gem(rake) >= 12.0.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rubygems-tasks) >= 0.2
BuildRequires: gem(simplecov) >= 0.17
BuildRequires: gem(yard) >= 0.9
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rubygems-tasks) >= 1
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency github-markup >= 1.1
%ruby_use_gem_dependency rake >= 12.0
%ruby_use_gem_dependency simplecov >= 0.17
Requires:      ruby >= 3.0.0
Requires:      gem(rake) >= 12.0.0
Provides:      gem(digest-crc) = 0.7.0

%description
Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.


%if_enabled    doc
%package       -n gem-digest-crc-doc
Version:       0.7.0
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета digest-crc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.7.0

%description   -n gem-digest-crc-doc
A Cyclic Redundancy Check (CRC) library for Ruby documentation files.

Adds support for calculating Cyclic Redundancy Check (CRC) to the Digest module.

%description   -n gem-digest-crc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета digest-crc.
%endif


%if_enabled    devel
%package       -n gem-digest-crc-devel
Version:       0.7.0
Release:       alt1
Summary:       A Cyclic Redundancy Check (CRC) library for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета digest-crc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(digest-crc) = 0.7.0
Requires:      gem(bundler) >= 2.0.0
Requires:      gem(github-markup) >= 1.1
Requires:      gem(kramdown) >= 0
Requires:      gem(kramdown-parser-gfm) >= 0
Requires:      gem(rake) >= 12.0.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rubygems-tasks) >= 0.2
Requires:      gem(simplecov) >= 0.17
Requires:      gem(yard) >= 0.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rubygems-tasks) >= 1
Conflicts:     gem(yard) >= 1

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
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-digest-crc-doc
%doc ChangeLog.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-digest-crc-devel
%doc ChangeLog.md LICENSE.txt README.md
%ruby_includedir/digest/
%endif


%changelog
* Mon Oct 05 2026 Pavel Skrylev <majioa@altlinux.org> 0.7.0-alt1
- ^ 0.6.5 -> 0.7.0

* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.5-alt1
- ^ 0.6.4 -> 0.6.5

* Wed Mar 16 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.4-alt1
- ^ 0.6.3 -> 0.6.4

* Thu Jun 03 2021 Pavel Skrylev <majioa@altlinux.org> 0.6.3-alt1
- + packaged gem with Ruby Policy 2.0
