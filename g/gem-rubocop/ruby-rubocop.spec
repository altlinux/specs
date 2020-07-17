%define        pkgname rubocop

Name:          gem-%pkgname
Version:       0.88.0
Release:       alt1.1
Summary:       A Ruby static code analyzer and formatter.
License:       MIT
Group:         Development/Ruby
Url:           https://www.rubocop.org/
Vcs:           https://github.com/rubocop-hq/rubocop.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler)
BuildRequires: gem(bump)
BuildRequires: gem(rack)
# fix #38650
Requires:      gem-regexp-parser >= 1.7.1-alt1.1
Requires:      gem-parser >= 2.7.1.4-alt1.1

%description
A Ruby static code analyzer and formatter, based on the community Ruby style
guide.

%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       -n %pkgname
Summary:       Executable file for rubocop.
Group:         Development/Ruby
BuildArch:     noarch

%description   -n %pkgname
Executable file for rubocop.

%description   -n %pkgname -l ru_RU.UTF-8
Исполнямки для рубокопа.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         -n %pkgname
%_bindir/*

%changelog
* Fri Jul 17 2020 Pavel Skrylev <majioa@altlinux.org> 0.88.0-alt1.1
- ! dep to gem-regexp-parser, and gem-parser (closes #38650)
- ! spec syntax

* Tue Jul 14 2020 Pavel Skrylev <majioa@altlinux.org> 0.88.0-alt1
- ^ 0.74.0 -> 0.88.0
- ! executable runnning (closes #38650)

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.74.0-alt1.1
- ! spec according to changelog rules

* Sat Aug 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.74.0-alt1
- ^ v0.74.0
- ! spec

* Thu Apr 04 2019 Pavel Skrylev <majioa@altlinux.org> 0.66.0-alt1
- Bump to 0.66.0

* Wed Feb 27 2019 Pavel Skrylev <majioa@altlinux.org> 0.65.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
