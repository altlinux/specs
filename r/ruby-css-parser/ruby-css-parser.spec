# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname css-parser
%define        gemname css_parser

Name:          ruby-%pkgname
Version:       1.7.0
Release:       alt1
Summary:       Ruby CSS Parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/premailer/css_parser
%vcs           https://github.com/premailer/css_parser.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%description
Load, parse and cascade CSS rule sets in Ruby.

%description   -l ru_RU.UTF8
Загружает, разбирает и упорядочивает наборы правил CSS в Рубине.


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
* Wed Jul 24 2019 Pavel Skrylev <majioa@altlinux.org> 1.7.0-alt1
- Bump to 1.7.0
- Use Ruby Policy 2.0

* Tue Sep 25 2018 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- Initial gemified build for Sisyphus
