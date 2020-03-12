%define        pkgname deep-cloneable
%define        gemname deep_cloneable

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1.1
Summary:       Gives every ActiveRecord::Base object the possibility to do a deep clone
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/moiristo/deep_cloneable
Vcs:           http://github.com/moiristo/deep_cloneable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname
Provides:      ruby-%pkgname

%description
This gem gives every ActiveRecord::Base object the possibility to do a deep
clone that includes user specified associations. It is a rails 3+ upgrade of
the deep_cloning plugin.


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
%doc readme*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- used (>) Ruby Policy 2.0
- updated (^) 2.3.2 -> 3.0.0

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1.1
- Rebuild with new Ruby autorequirements.
- Disable tests.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 2.3.2-alt1
- Initial build for Sisyphus
