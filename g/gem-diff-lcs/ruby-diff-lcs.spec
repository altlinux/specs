%define        gemname diff-lcs

Name:          gem-diff-lcs
Version:       1.4.3
Release:       alt1
Summary:       Port of Algorithm::Diff
License:       MIT or Artistic-2.0 or GPL-2.0+
Group:         Development/Ruby
Url:           http://halostatue.github.io/diff-lcs/
Vcs:           https://github.com/halostatue/diff-lcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-diff-lcs < %EVR
Provides:      ruby-diff-lcs = %EVR
Provides:      gem(diff-lcs) = 1.4.3

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt longest common
subsequence (LCS) algorithm to compute intelligent differences between two
sequenced enumerable containers. The implementation is based on Mario I.
Wolczko's Smalltalk version (1.2, 1993) and Ned Konz's Perl version
(Algorithm::Diff).


%package       -n diff-lcs
Version:       1.4.3
Release:       alt1
Summary:       Diff::LCS computes the difference between two Enumerable sequences using the McIlroy-Hunt longest common subsequence (LCS) algorithm executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета diff-lcs
Group:         Other
BuildArch:     noarch

Requires:      gem(diff-lcs) = 1.4.3

%description   -n diff-lcs
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm
executable(s).

Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

This is release 1.4, providing a simple extension that allows for
Diff::LCS::Change objects to be treated implicitly as arrays. Ruby versions
below 2.5 are soft-deprecated.

This means that older versions are no longer part of the CI test suite. If any
changes have been introduced that break those versions, bug reports and patches
will be accepted, but it will be up to the reporter to verify any fixes prior to
release. A future release will completely break compatibility.

%description   -n diff-lcs -l ru_RU.UTF-8
Исполнямка для самоцвета diff-lcs.


%package       -n gem-diff-lcs-doc
Version:       1.4.3
Release:       alt1
Summary:       Diff::LCS computes the difference between two Enumerable sequences using the McIlroy-Hunt longest common subsequence (LCS) algorithm documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета diff-lcs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(diff-lcs) = 1.4.3

%description   -n gem-diff-lcs-doc
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm documentation
files.

Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

This is release 1.4, providing a simple extension that allows for
Diff::LCS::Change objects to be treated implicitly as arrays. Ruby versions
below 2.5 are soft-deprecated.

This means that older versions are no longer part of the CI test suite. If any
changes have been introduced that break those versions, bug reports and patches
will be accepted, but it will be up to the reporter to verify any fixes prior to
release. A future release will completely break compatibility.

%description   -n gem-diff-lcs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета diff-lcs.


%package       -n gem-diff-lcs-devel
Version:       1.4.3
Release:       alt1
Summary:       Diff::LCS computes the difference between two Enumerable sequences using the McIlroy-Hunt longest common subsequence (LCS) algorithm development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета diff-lcs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(diff-lcs) = 1.4.3
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-diff-lcs-devel
Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm development
package.

Diff::LCS computes the difference between two Enumerable sequences using the
McIlroy-Hunt longest common subsequence (LCS) algorithm. It includes utilities
to create a simple HTML diff output format and a standard diff-like tool.

This is release 1.4, providing a simple extension that allows for
Diff::LCS::Change objects to be treated implicitly as arrays. Ruby versions
below 2.5 are soft-deprecated.

This means that older versions are no longer part of the CI test suite. If any
changes have been introduced that break those versions, bug reports and patches
will be accepted, but it will be up to the reporter to verify any fixes prior to
release. A future release will completely break compatibility.

%description   -n gem-diff-lcs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета diff-lcs.


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

%files         -n diff-lcs
%doc README.rdoc
%_bindir/htmldiff
%_bindir/ldiff

%files         -n gem-diff-lcs-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-diff-lcs-devel
%doc README.rdoc


%changelog
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
