%define        pkgname roadie-rails

Name:          gem-%pkgname
Version:       2.1.1
Release:       alt1
Summary:       Making HTML emails comfortable for the Rails rockstars
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/Mange/roadie-rails
Vcs:           https://github.com/Mange/roadie-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
This gem hooks up your Rails application with Roadie to help you generate HTML
emails.

%description   -l ru_RU.UTF8
Самоцвет подцепляет Рельсовое приложение с Дорожками, чтобы облегчить вам
созданием писем HTML.

%package       doc
Summary:       Documentation files for %gemname gem
Group:         Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для %gemname gem

%prep
%setup

%build
%ruby_build --ignore=rails_60,rails_52,rails_51

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
* Wed Mar 11 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.1-alt1
- ^ 2.1.0 -> 2.1.1
- ! spec

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.0-alt1
- > Ruby Policy 2.0
- ^ 1.3.0 -> 2.1.0

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- Initial gemified build for Sisyphus
