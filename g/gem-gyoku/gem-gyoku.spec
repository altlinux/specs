%define        pkgname gyoku

Name:          gem-%pkgname
Version:       1.3.1
Release:       alt1.1
Summary:       Translates Ruby Hashes to XML
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/savonrb/gyoku
Vcs:           https://github.com/savonrb/gyoku.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.


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
* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1.1
- ! spec tags

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0
