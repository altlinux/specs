# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname x-editable-rails

Name:          gem-x-editable-rails
Version:       1.5.5.2
Release:       alt0.1
Summary:       Edit fields easily with X-Editable helper
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/werein/x-editable-rails
Vcs:           https://github.com/werein/x-editable-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rails) >= 4.0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(sprockets) >= 0
BuildRequires: gem(sass-rails) >= 0
BuildRequires: gem(bootstrap-sass) >= 0
BuildRequires: gem(coffee-rails) >= 0
BuildRequires: gem(jquery-rails) >= 0
BuildRequires: gem(haml) >= 0
BuildRequires: gem(globalize) >= 0
BuildRequires: gem(responders) >= 0
BuildRequires: gem(pg) >= 0
BuildRequires: gem(rails_12factor) >= 0
BuildRequires: gem(uglifier) >= 0
BuildRequires: gem(railties) >= 0
BuildConflicts: gem(rails) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rails >= 6.1.3.2,rails < 7
Requires:      gem(railties) >= 0
Obsoletes:     ruby-x-editable-rails < %EVR
Provides:      ruby-x-editable-rails = %EVR
Provides:      gem(x-editable-rails) = 1.5.5.2

%ruby_use_gem_version x-editable-rails:1.5.5.2

%description
Edit fields easily with X-Editable helper.


%package       -n gem-x-editable-rails-doc
Version:       1.5.5.2
Release:       alt0.1
Summary:       Edit fields easily with X-Editable helper documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета x-editable-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(x-editable-rails) = 1.5.5.2

%description   -n gem-x-editable-rails-doc
Edit fields easily with X-Editable helper documentation files.

%description   -n gem-x-editable-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета x-editable-rails.


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

%files         -n gem-x-editable-rails-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.5.5.2-alt0.1
- ^ 1.5.5.1 -> 1.5.5[2] (no devel)

* Thu Jan 26 2023 Pavel Skrylev <majioa@altlinux.org> 1.5.5.1-alt4
- ! spec

* Wed May 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.5.5.1-alt3.1
- ! spec tags

* Wed Sep 25 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.5.1-alt3
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt2.1
- Rebuild with new Ruby autorequirements.

* Fri Jun 08 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt2
- Disable tests.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5.1-alt1
- New version.

* Thu May 31 2018 Andrey Cherepanov <cas@altlinux.org> 1.5.5-alt1
- Initial build for Sisyphus
