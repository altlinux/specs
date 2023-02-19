%define        gemname rails-html-sanitizer

Name:          gem-rails-html-sanitizer
Version:       1.5.0
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
%if_with check
BuildRequires: gem(bundler) >= 1.3
BuildRequires: gem(rake) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rails-dom-testing) >= 0
BuildRequires: gem(nokogiri) >= 1.7
BuildRequires: gem(activesupport) >= 5
BuildRequires: gem(loofah) >= 2.19.1
BuildConflicts: gem(loofah) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names rails
Requires:      gem(loofah) >= 2.19.1
Conflicts:     gem(loofah) >= 3
Obsoletes:     ruby-rails-html-sanitizer
Provides:      ruby-rails-html-sanitizer
Provides:      gem(rails-html-sanitizer) = 1.5.0


%description
In Rails 4.2 and above this gem will be responsible for sanitizing HTML
fragments in Rails applications, i.e. in the sanitize, sanitize_css, strip_tags
and strip_links methods.

Rails Html Sanitizer is only intended to be used with Rails applications. If you
need similar functionality in non Rails apps consider using Loofah directly
(that's what handles sanitization under the hood).


%package       -n gem-rails-html-sanitizer-doc
Version:       1.5.0
Release:       alt1
Summary:       This gem is responsible to sanitize HTML fragments in Rails applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rails-html-sanitizer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rails-html-sanitizer) = 1.5.0

%description   -n gem-rails-html-sanitizer-doc
This gem is responsible to sanitize HTML fragments in Rails applications
documentation files.

In Rails 4.2 and above this gem will be responsible for sanitizing HTML
fragments in Rails applications, i.e. in the sanitize, sanitize_css, strip_tags
and strip_links methods.

Rails Html Sanitizer is only intended to be used with Rails applications. If you
need similar functionality in non Rails apps consider using Loofah directly
(that's what handles sanitization under the hood).

%description   -n gem-rails-html-sanitizer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rails-html-sanitizer.


%package       -n gem-rails-html-sanitizer-devel
Version:       1.5.0
Release:       alt1
Summary:       This gem is responsible to sanitize HTML fragments in Rails applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails-html-sanitizer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails-html-sanitizer) = 1.5.0
Requires:      gem(bundler) >= 1.3
Requires:      gem(rake) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(rails-dom-testing) >= 0
Requires:      gem(nokogiri) >= 1.7
Requires:      gem(activesupport) >= 5

%description   -n gem-rails-html-sanitizer-devel
This gem is responsible to sanitize HTML fragments in Rails applications
development package.

In Rails 4.2 and above this gem will be responsible for sanitizing HTML
fragments in Rails applications, i.e. in the sanitize, sanitize_css, strip_tags
and strip_links methods.

Rails Html Sanitizer is only intended to be used with Rails applications. If you
need similar functionality in non Rails apps consider using Loofah directly
(that's what handles sanitization under the hood).

%description   -n gem-rails-html-sanitizer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rails-html-sanitizer.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-rails-html-sanitizer-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rails-html-sanitizer-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- ^ 1.3.0 -> 1.5.0

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
