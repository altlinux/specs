%define        gemname audited

Name:          gem-audited
Version:       5.0.1
Release:       alt1
Summary:       Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/collectiveidea/audited
Vcs:           https://github.com/collectiveidea/audited.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 5.0 gem(activerecord) < 6.2
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rails) >= 5.0 gem(rails) < 6.2
BuildRequires: gem(rspec-rails) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(single_cov) >= 0
BuildRequires: gem(sqlite3) >= 1.3 gem(sqlite3) < 2
BuildRequires: gem(mysql2) >= 0.3.20
BuildRequires: gem(pg) >= 0.18 gem(pg) < 2.0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 5.0 gem(activerecord) < 6.2
Obsoletes:     ruby-audited < %EVR
Provides:      ruby-audited = %EVR
Provides:      gem(audited) = 5.0.1


%description
Audited (previously acts_as_audited) is an ORM extension that logs all changes
to your models. Audited can also record who made those changes, save comments
and associate models related to the changes.

Audited currently (4.x) works with Rails 6.0, 5.2, 5.1, 5.0 and 4.2.


%package       -n gem-audited-doc
Version:       5.0.1
Release:       alt1
Summary:       Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета audited
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(audited) = 5.0.1

%description   -n gem-audited-doc
Audited (formerly acts_as_audited) is an ORM extension that logs all changes to
your Rails models documentation files.

Audited (previously acts_as_audited) is an ORM extension that logs all changes
to your models. Audited can also record who made those changes, save comments
and associate models related to the changes.

Audited currently (4.x) works with Rails 6.0, 5.2, 5.1, 5.0 and 4.2.

%description   -n gem-audited-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета audited.


%package       -n gem-audited-devel
Version:       5.0.1
Release:       alt1
Summary:       Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета audited
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(audited) = 5.0.1
Requires:      gem(appraisal) >= 0
Requires:      gem(rails) >= 5.0 gem(rails) < 6.2
Requires:      gem(rspec-rails) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(single_cov) >= 0
Requires:      gem(sqlite3) >= 1.3 gem(sqlite3) < 2
Requires:      gem(mysql2) >= 0.3.20
Requires:      gem(pg) >= 0.18 gem(pg) < 2.0

%description   -n gem-audited-devel
Audited (formerly acts_as_audited) is an ORM extension that logs all changes to
your Rails models development package.

Audited (previously acts_as_audited) is an ORM extension that logs all changes
to your models. Audited can also record who made those changes, save comments
and associate models related to the changes.

Audited currently (4.x) works with Rails 6.0, 5.2, 5.1, 5.0 and 4.2.

%description   -n gem-audited-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета audited.


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

%files         -n gem-audited-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-audited-devel
%doc README.md


%changelog
* Mon Jun 21 2021 Pavel Skrylev <majioa@altlinux.org> 5.0.1-alt1
- ^ 4.9.0 -> 5.0.1

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 4.9.0-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 4.9.0-alt1
- updated (^) 4.8.0 -> 4.9.0
- used (>) Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- New version.

* Tue May 29 2018 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- Initial build for Sisyphus
