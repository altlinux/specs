%define        pkgname rails-html-sanitizer

Name:          gem-%pkgname
Version:       1.3.0
Release:       alt1
Summary:       This gem is responsible to sanitize HTML fragments in Rails applications
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/rails-html-sanitizer
Vcs:           https://github.com/rails/rails-html-sanitizer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
In Rails 4.2 and above this gem will be responsible for sanitizing HTML
fragments in Rails applications, i.e. in the sanitize, sanitize_css, strip_tags
and strip_links methods.

Rails Html Sanitizer is only intended to be used with Rails applications. If
you need similar functionality in non Rails apps consider using Loofah directly
(that's what handles sanitization under the hood).


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
* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- updated (^) 1.2.0 -> 1.3.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 1.0.4 -> 1.2.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus
