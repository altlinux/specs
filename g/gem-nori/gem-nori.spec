%define        pkgname nori

Name:          gem-%pkgname
Version:       2.6.0
Release:       alt1.1
Summary:       XML to Hash translator
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/savonrb/nori
Vcs:           https://github.com/savonrb/nori.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Really simple XML parsing ripped from Crack which ripped it from Merb.
Nori was created to bypass the stale development of Crack, improve its XML parse
and fix certain issues.


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

%files doc
%ruby_gemdocdir

%changelog
* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1.1
- ! spec syntax

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 2.6.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
