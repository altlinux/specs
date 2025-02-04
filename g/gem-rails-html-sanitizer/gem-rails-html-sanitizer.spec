%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rails-html-sanitizer

Name:          gem-rails-html-sanitizer
Version:       1.6.2
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
BuildRequires: gem(loofah) >= 2.21
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(nokogiri) >= 1.15.7
BuildConflicts: gem(loofah) >= 3
BuildConflicts: gem(nokogiri) >= 1.17.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(loofah) >= 2.21
Requires:      gem(minitest) >= 0
Requires:      gem(nokogiri) >= 1.15.7
Requires:      gem(rake) >= 0
Conflicts:     gem(loofah) >= 3
Conflicts:     gem(nokogiri) >= 1.17.0
Obsoletes:     ruby-rails-html-sanitizer < %EVR
Provides:      ruby-rails-html-sanitizer = %EVR
Provides:      rails-html-sanitizer = %EVR
Provides:      gem(rails-html-sanitizer) = 1.6.2

%description
In Rails 4.2 and above this gem will be responsible for sanitizing HTML
fragments in Rails applications, i.e. in the sanitize, sanitize_css, strip_tags
and strip_links methods.

Rails Html Sanitizer is only intended to be used with Rails applications. If you
need similar functionality in non Rails apps consider using Loofah directly
(that's what handles sanitization under the hood).


%if_enabled    doc
%package       -n gem-rails-html-sanitizer-doc
Version:       1.6.2
Release:       alt1
Summary:       This gem is responsible to sanitize HTML fragments in Rails applications documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rails-html-sanitizer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rails-html-sanitizer) = 1.6.2

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
%endif


%if_enabled    devel
%package       -n gem-rails-html-sanitizer-devel
Version:       1.6.2
Release:       alt1
Summary:       This gem is responsible to sanitize HTML fragments in Rails applications development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rails-html-sanitizer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rails-html-sanitizer) = 1.6.2

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
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc CHANGELOG.md MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-rails-html-sanitizer-doc
%doc CHANGELOG.md MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rails-html-sanitizer-devel
%doc CHANGELOG.md MIT-LICENSE README.md CONTRIBUTING.md
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 1.6.2-alt1
- ^ 1.5.0 -> 1.6.2

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
