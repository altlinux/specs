# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname minitest-proveit

Name:          gem-%pkgname
Version:       1.0.0
Release:       alt1
Summary:       minitest-proveit forces all tests to prove success
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/minitest-proveit
%vcs           https://github.com/seattlerb/minitest-proveit.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe)

%add_findreq_skiplist %ruby_gemslibdir/**/*

%description
Originally written by github user bradleyjames, minitest-proveit forces all
tests to prove success (via at least one assertion) rather than rely on the
absence of failure.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Oct 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- added (+) packaged gem with usage Ruby Policy 2.0
