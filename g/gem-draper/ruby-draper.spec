%define        pkgname draper

Name:          gem-%pkgname
Version:       4.0.1
Release:       alt1
Summary:       Decorators/View-Models for Rails Applications
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/drapergem/draper/
Vcs:           https://github.com/drapergem/draper.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Draper adds an object-oriented layer of presentation logic to your Rails
application.

Without Draper, this functionality might have been tangled up in procedural
helpers or adding bulk to your models. With Draper decorators, you can wrap
your models with presentation-related logic to organise - and test - this layer
of your app much more effectively.


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
* Thu Dec 17 2020 Pavel Skrylev <majioa@altlinux.org> 4.0.1-alt1
- ^ 3.0.1 -> 4.0.1
- * policify name

* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 3.0.1-alt1
- Initial build for Sisyphus
