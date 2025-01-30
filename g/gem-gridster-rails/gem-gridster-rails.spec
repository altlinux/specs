%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gridster-rails

Name:          gem-gridster-rails
Version:       0.5.6.9
Release:       alt1
Summary:       Use gridster with Rails 3+
License:       MIT
Group:         Development/Ruby
Url:           http://rubygems.org/gems/gridster-rails
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(railties) >= 3.1.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(railties) >= 3.1.0
Provides:      gem(gridster-rails) = 0.5.6.9

%description
This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+
application.


%if_enabled    doc
%package       -n gem-gridster-rails-doc
Version:       0.5.6.9
Release:       alt1
Summary:       Use gridster with Rails 3+ documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gridster-rails
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gridster-rails) = 0.5.6.9

%description   -n gem-gridster-rails-doc
Use gridster with Rails 3+ documentation files.

This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+
application.

%description   -n gem-gridster-rails-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gridster-rails.
%endif


%if_enabled    devel
%package       -n gem-gridster-rails-devel
Version:       0.5.6.9
Release:       alt1
Summary:       Use gridster with Rails 3+ development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gridster-rails
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gridster-rails) = 0.5.6.9

%description   -n gem-gridster-rails-devel
Use gridster with Rails 3+ development package.

This gem provides jquery.gridster.js and jquery.gridster.css for your Rails 3+
application.

%description   -n gem-gridster-rails-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gridster-rails.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gridster-rails-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gridster-rails-devel
%doc LICENSE README.md
%endif


%changelog
* Sat Jan 11 2025 Pavel Skrylev <majioa@altlinux.org> 0.5.6.9-alt1
- ^ 0.5.6.1 -> 0.5.6.9
- * define explicit dependencies

* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1.2
- ! closes build deps under check condition

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1.1
- ! spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 0.5.6.1-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.
