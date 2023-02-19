%define        gemname audited

Name:          gem-audited
Version:       5.2.0
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
%if_with check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(rails) >= 5.0
BuildRequires: gem(rspec-rails) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(single_cov) >= 0
BuildRequires: gem(sqlite3) >= 1.3.6
BuildRequires: gem(mysql2) >= 0.3.20
BuildRequires: gem(pg) >= 0.18
BuildRequires: gem(activerecord) >= 5.0
BuildConflicts: gem(rails) >= 7.1
BuildConflicts: gem(pg) >= 2.0
BuildConflicts: gem(activerecord) >= 7.1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(activerecord) >= 5.0
Conflicts:     gem(activerecord) >= 7.1
Obsoletes:     ruby-audited < %EVR
Provides:      ruby-audited = %EVR
Provides:      gem(audited) = 5.2.0


%description
Audited (previously acts_as_audited) is an ORM extension that logs all changes
to your models. Audited can also record who made those changes, save comments
and associate models related to the changes.

Audited currently (4.x) works with Rails 6.0, 5.2, 5.1, 5.0 and 4.2.


%package       -n gem-audited-doc
Version:       5.2.0
Release:       alt1
Summary:       Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета audited
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(audited) = 5.2.0

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
Version:       5.2.0
Release:       alt1
Summary:       Audited (formerly acts_as_audited) is an ORM extension that logs all changes to your Rails models development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета audited
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(audited) = 5.2.0
Requires:      gem(appraisal) >= 0
Requires:      gem(rails) >= 5.0
Requires:      gem(rspec-rails) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(single_cov) >= 0
Requires:      gem(sqlite3) >= 1.3.6
Requires:      gem(mysql2) >= 0.3.20
Requires:      gem(pg) >= 0.18
Conflicts:     gem(rails) >= 7.1
Conflicts:     gem(pg) >= 2.0

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
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 5.2.0-alt1
- ^ 5.0.2 -> 5.2.0

* Thu Sep 01 2022 Pavel Skrylev <majioa@altlinux.org> 5.0.2-alt1
- ^ 5.0.1 -> 5.0.2

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
