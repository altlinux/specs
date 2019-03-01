%define        pkgname diff-lcs

Name:          ruby-%pkgname
Version:       1.3
Release:       alt1
Summary:       Port of Algorithm::Diff
License:       MIT
Group:         Development/Ruby
Url:           http://halostatue.github.io/diff-lcs/
# VCS:         https://github.com/halostatue/diff-lcs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Diff::LCS is a port of Algorithm::Diff that uses the McIlroy-Hunt
longest common subsequence (LCS) algorithm to compute intelligent
differences between two sequenced enumerable containers. The
implementation is based on Mario I. Wolczko's Smalltalk version (1.2,
1993) and Ned Konz's Perl version (Algorithm::Diff).


%package       doc
Summary:       Documentation files for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.


%package       -n ldiff
Summary:       Executable file for %gemname gem
Group:         Development/Documentation
BuildArch:     noarch

%description   -n ldiff
Executable file for %gemname gem.


%prep
%setup

%build
%gem_build

%install
%gem_install

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n ldiff
%_bindir/*

%changelog
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

