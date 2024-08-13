%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname diff-lcs

Name:          gem-diff-lcs
Version:       1.5.1
Release:       alt1
Summary:       Port of Algorithm::Diff
License:       MIT or Artistic-2.0 or GPL-2.0-or-later
Group:         Development/Ruby
Url:           http://halostatue.github.io/diff-lcs/
Vcs:           https://github.com/halostatue/diff-lcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 3.0
BuildRequires: gem(hoe-doofus) >= 1.0
BuildRequires: gem(hoe-gemspec2) >= 1.1
BuildRequires: gem(hoe-git2) >= 1.7
BuildRequires: gem(hoe-rubygems) >= 1.0
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 6.1.1
BuildRequires: gem(rspec) >= 2.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(hoe-doofus) >= 2
BuildConflicts: gem(hoe-gemspec2) >= 2
BuildConflicts: gem(hoe-git2) >= 2
BuildConflicts: gem(hoe-rubygems) >= 2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
Requires:      gem(simplecov) >= 0.17
Requires:      gem(byebug) >= 0
Requires:      gem(standardrb) >= 0
Requires:      gem(fasterer) >= 0
Conflicts:     gem(simplecov) >= 1
Obsoletes:     ruby-diff-lcs < %EVR
Provides:      ruby-diff-lcs = %EVR
Provides:      gem(diff-lcs) = 1.5.1


%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).


%package       -n diff-lcs
Version:       1.5.1
Release:       alt1
Summary:       Port of Algorithm::Diff executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета diff-lcs
Group:         Other
BuildArch:     noarch

Requires:      gem(diff-lcs) = 1.5.1

%description   -n diff-lcs
Port of Algorithm::Diff executable(s).

Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).

%description   -n diff-lcs -l ru_RU.UTF-8
Исполнямка для самоцвета diff-lcs.


%if_enabled    doc
%package       -n gem-diff-lcs-doc
Version:       1.5.1
Release:       alt1
Summary:       Port of Algorithm::Diff documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета diff-lcs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(diff-lcs) = 1.5.1

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
Version:       1.5.1
Release:       alt1
Summary:       Port of Algorithm::Diff development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета diff-lcs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(diff-lcs) = 1.5.1
Requires:      gem(hoe) >= 3.0
Requires:      gem(hoe-doofus) >= 1.0
Requires:      gem(hoe-gemspec2) >= 1.1
Requires:      gem(hoe-git2) >= 1.7
Requires:      gem(hoe-rubygems) >= 1.0
Requires:      gem(rspec) >= 2.0
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 6.1.1
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(hoe-doofus) >= 2
Conflicts:     gem(hoe-gemspec2) >= 2
Conflicts:     gem(hoe-git2) >= 2
Conflicts:     gem(hoe-rubygems) >= 2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rdoc) >= 7

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
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc Contributing.md History.md License.md README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n diff-lcs
%doc Contributing.md History.md License.md README.rdoc
%_bindir/htmldiff
%_bindir/ldiff

%if_enabled    doc
%files         -n gem-diff-lcs-doc
%doc Contributing.md History.md License.md README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-diff-lcs-devel
%doc Contributing.md History.md License.md README.rdoc
%endif


%changelog
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
