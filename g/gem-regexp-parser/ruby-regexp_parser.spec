# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname regexp-parser
%define        gemname regexp_parser

Name:          gem-%pkgname
Version:       1.7.1
Release:       alt1
Summary:       A regular expression parser library for Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ammar/regexp_parser
Vcs:           https://github.com/ammar/regexp_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.


%package       -n %pkgname
Summary:       Executable file for %gemname gem
Summary(ru_RU.UTF-8): Исполнямка для самоцвета %gemname
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for %gemname gem.

%description   -n %pkgname -l ru_RU.UTF8
Исполнямка для %gemname самоцвета.


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
* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 1.7.1-alt1
- ^ 1.6.0 -> 1.7.1
- ! spec tags

* Tue Sep 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- updated to (^) v1.6.0
- fix (!) spec

* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.1-alt1
- updated to (^) Ruby Policy 2.0
- updated to (^) v1.5.1

* Tue Oct 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- added (+) initial build for Sisyphus
