%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname diff-lcs

Name:          gem-diff-lcs
Version:       2.0.0
Release:       alt1
Summary:       Port of Algorithm::Diff
License:       MIT or Artistic-1.0-Perl or GPL-2.0-or-later
Group:         Development/Ruby
Url:           http://halostatue.github.io/diff-lcs/
Vcs:           https://github.com/halostatue/diff-lcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(fasterer) >= 0.11
BuildRequires: gem(hoe) >= 4.0
BuildRequires: gem(hoe-halostatue) >= 3.0
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(minitest-autotest) >= 1.0
BuildRequires: gem(minitest-focus) >= 1.1
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 6.0
BuildRequires: gem(simplecov) >= 0.9
BuildRequires: gem(simplecov-lcov) >= 0.9
BuildRequires: gem(standard) >= 1.50
BuildRequires: gem(standard-thread_safety) >= 1.0
BuildConflicts: gem(fasterer) >= 1
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-halostatue) >= 4
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(minitest-autotest) >= 2
BuildConflicts: gem(minitest-focus) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 8
BuildConflicts: gem(simplecov) >= 1
BuildConflicts: gem(simplecov-lcov) >= 1
BuildConflicts: gem(standard) >= 2
BuildConflicts: gem(standard-thread_safety) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 3.2.0
Conflicts:     ruby >= 5
Obsoletes:     ruby-diff-lcs < %EVR
Provides:      ruby-diff-lcs = %EVR
Provides:      diff-lcs = %EVR
Provides:      gem(diff-lcs) = 2.0.0

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).


%package       -n ldiff
Version:       2.0.0
Release:       alt1
Summary:       Port of Algorithm::Diff executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета diff-lcs
Group:         Other
BuildArch:     noarch

Requires:      gem(diff-lcs) = 2.0.0

%description   -n ldiff
Port of Algorithm::Diff executable(s).

Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).

%description   -n ldiff -l ru_RU.UTF-8
Исполнямка для самоцвета diff-lcs.


%if_enabled    doc
%package       -n gem-diff-lcs-doc
Version:       2.0.0
Release:       alt1
Summary:       Port of Algorithm::Diff documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета diff-lcs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(diff-lcs) = 2.0.0

%description   -n gem-diff-lcs-doc
Port of Algorithm::Diff documentation files.

Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).

%description   -n gem-diff-lcs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета diff-lcs.
%endif


%if_enabled    devel
%package       -n gem-diff-lcs-devel
Version:       2.0.0
Release:       alt1
Summary:       Port of Algorithm::Diff development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета diff-lcs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(diff-lcs) = 2.0.0
Requires:      gem(fasterer) >= 0.11
Requires:      gem(hoe) >= 4.0
Requires:      gem(hoe-halostatue) >= 3.0
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(minitest-autotest) >= 1.0
Requires:      gem(minitest-focus) >= 1.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 6.0
Requires:      gem(simplecov) >= 0.9
Requires:      gem(simplecov-lcov) >= 0.9
Requires:      gem(standard) >= 1.50
Requires:      gem(standard-thread_safety) >= 1.0
Conflicts:     gem(fasterer) >= 1
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-halostatue) >= 4
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(minitest-autotest) >= 2
Conflicts:     gem(minitest-focus) >= 2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 8
Conflicts:     gem(simplecov) >= 1
Conflicts:     gem(simplecov-lcov) >= 1
Conflicts:     gem(standard) >= 2
Conflicts:     gem(standard-thread_safety) >= 2

%description   -n gem-diff-lcs-devel
Port of Algorithm::Diff development package.

Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).

%description   -n gem-diff-lcs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета diff-lcs.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md licenses/COPYING.txt licenses/artistic.txt licenses/dco.txt licenses
%ruby_gemspec
%ruby_gemlibdir

%files         -n ldiff
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md licenses/COPYING.txt licenses/artistic.txt licenses/dco.txt licenses
%_bindir/ldiff

%if_enabled    doc
%files         -n gem-diff-lcs-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md licenses/COPYING.txt licenses/artistic.txt licenses/dco.txt licenses
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-diff-lcs-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md CONTRIBUTORS.md README.md licenses/COPYING.txt licenses/artistic.txt licenses/dco.txt licenses
%endif


%changelog
* Thu May 21 2026 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- ^ 1.5.1 -> 2.0.0

* Fri Aug 09 2024 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- ^ 1.4.3 -> 1.5.1

* Thu May 13 2021 Pavel Skrylev <majioa@altlinux.org> 1.4.3-alt1
- ^ 1.3 -> 1.4.3

* Fri Mar 01 2019 Pavel Skrylev <majioa@altlinux.org> 1.3-alt1
- Bump to 1.3;
- Use Ruby Policy 2.0.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Sep 21 2015 Andrey Cherepanov <cas@altlinux.org> 1.2.5-alt1
- New version

* Wed Dec 05 2012 Led <led@altlinux.ru> 1.1.2-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Jun 27 2009 Alexey I. Froloff <raorn@altlinux.org> 1.1.2-alt2
- Rebuilt with Ruby 1.9

* Mon Aug 25 2008 Sir Raorn <raorn@altlinux.ru> 1.1.2-alt1
- Built for Sisyphus
