%define        pkgname loquacious

Name:          gem-%pkgname
Version:       1.9.1
Release:       alt1
Summary:       tell everyone how to configure your project
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/loquacious
Vcs:           https://github.com/TwP/loquacious.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

Descriptive configuration files for Ruby written in Ruby.

Loquacious provides a very open configuration system written in ruby and
descriptions for each configuration attribute. The attributes and descriptions
can be iterated over allowing for helpful information about those attributes
to be displayed to the user.


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
* Thu Jul 11 2019 Pavel Skrylev <majioa@altlinux.org> 1.9.1-alt1
- + packaged as a gem with usage Ruby Policy 2.0.
