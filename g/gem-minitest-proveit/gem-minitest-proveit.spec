%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-proveit

Name:          gem-minitest-proveit
Version:       1.0.0
Release:       alt2
Summary:       minitest-proveit forces all tests to prove success
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-proveit
Vcs:           https://github.com/seattlerb/minitest-proveit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) > 5
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(minitest) > 5
Conflicts:     gem(minitest) >= 7
Provides:      gem(minitest-proveit) = 1.0.0


%description
Originally written by github user bradleyjames, minitest-proveit forces all
tests to prove success (via at least one assertion) rather than rely on the
absence of failure.


%if_enabled    doc
%package       -n gem-minitest-proveit-doc
Version:       1.0.0
Release:       alt2
Summary:       minitest-proveit forces all tests to prove success documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-proveit
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-proveit) = 1.0.0

%description   -n gem-minitest-proveit-doc
minitest-proveit forces all tests to prove success documentation
files.

Originally written by github user bradleyjames, minitest-proveit forces all
tests to prove success (via at least one assertion) rather than rely on the
absence of failure.

%description   -n gem-minitest-proveit-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-proveit.
%endif


%if_enabled    devel
%package       -n gem-minitest-proveit-devel
Version:       1.0.0
Release:       alt2
Summary:       minitest-proveit forces all tests to prove success development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-proveit
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-proveit) = 1.0.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-minitest-proveit-devel
minitest-proveit forces all tests to prove success development
package.

Originally written by github user bradleyjames, minitest-proveit forces all
tests to prove success (via at least one assertion) rather than rely on the
absence of failure.

%description   -n gem-minitest-proveit-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-proveit.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-proveit-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-proveit-devel
%doc README.rdoc
%endif


%changelog
* Wed Oct 23 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- ! fixed .gear and spec

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1.1
- ! spec

* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
