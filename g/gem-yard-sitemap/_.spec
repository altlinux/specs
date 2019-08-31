# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname yard-sitemap

Name:          gem-%pkgname
Version:       1.0.1
Release:       alt1
Summary:       A YARD plugin to build a sitemap.xml for generated HTML documentation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/lsegal/yard-sitemap
%vcs           https://github.com/lsegal/yard-sitemap.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*

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
* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
+ packaged gem with the Ruby Policy 2.0 usage
