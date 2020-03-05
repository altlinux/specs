%define        pkgname audited

Name:          gem-%pkgname
Version:       4.9.0
Release:       alt1.1
Summary:       Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models.
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/collectiveidea/audited
Vcs:           https://github.com/collectiveidea/audited.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
Audited (previously acts_as_audited) is an ORM extension that logs all changes
to your models. Audited can also record who made those changes, save comments
and associate models related to the changes.

Audited currently (4.x) works with Rails 6.0, 5.2, 5.1, 5.0 and 4.2.


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
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 4.9.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.9.0-alt1
- updated (^) 4.8.0 -> 4.9.0
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- New version.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- Initial build for Sisyphus
