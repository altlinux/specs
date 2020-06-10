%define  pkgname coffee-rails

Name:          gem-%pkgname
Version:       5.0.0
Release:       alt1
Summary:       CoffeeScript adapter for the Rails asset pipeline. Also adds support for .coffee views.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/coffee-rails
#Vcs:           https://github.com/rails/coffee-rails.git

Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
CoffeeScript adapter for the Rails asset pipeline. Also adds support to
use CoffeeScript to respond to JavaScript requests (use .coffee views).


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
* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 5.0.0-alt1
- ^ 4.2.2 -> 5.0.0
- ! spec name and syntax

* Thu Jul 26 2018 Andrey Cherepanov <cas@altlinux.org> 4.2.2-alt1
- Initial build for Sisyphus
