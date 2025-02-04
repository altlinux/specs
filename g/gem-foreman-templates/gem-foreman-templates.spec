%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_templates

Name:          gem-foreman-templates
Version:       10.0.0
Release:       alt1
Summary:       Template-syncing engine for Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_templates
Vcs:           https://github.com/theforeman/foreman_templates.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       .public.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0
BuildRequires: gem(diffy) >= 0
BuildRequires: gem(git) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_templates,foreman-templates
Requires:      gem(diffy) >= 0
Requires:      gem(git) >= 0
Provides:      gem(foreman_templates) = 10.0.0


%description
Engine to synchronise provisioning templates from GitHub


%if_enabled    doc
%package       -n gem-foreman-templates-doc
Version:       10.0.0
Release:       alt1
Summary:       Template-syncing engine for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_templates
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_templates) = 10.0.0

%description   -n gem-foreman-templates-doc
Template-syncing engine for Foreman documentation files.

Engine to synchronise provisioning templates from GitHub

%description   -n gem-foreman-templates-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_templates.
%endif


%if_enabled    devel
%package       -n gem-foreman-templates-devel
Version:       10.0.0
Release:       alt1
Summary:       Template-syncing engine for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_templates
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_templates) = 10.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(theforeman-rubocop) >= 0

%description   -n gem-foreman-templates-devel
Template-syncing engine for Foreman development package.

Engine to synchronise provisioning templates from GitHub

%description   -n gem-foreman-templates-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_templates.
%endif


%prep
%setup -a 1
%autopatch

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp .public %buildroot%_datadir/foreman/public

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%if_enabled    doc
%files         -n gem-foreman-templates-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-templates-devel
%doc README.md
%endif


%changelog
* Tue Oct 01 2024 Pavel Skrylev <majioa@altlinux.org> 10.0.0-alt1
- ^ 9.3.0 -> 10.0.0

* Thu Apr 06 2023 Pavel Skrylev <majioa@altlinux.org> 9.3.0-alt1.1
- ! public build

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 9.3.0-alt1
- ^ 9.1.0 -> 9.3.0

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 9.1.0-alt1
- + packaged gem with Ruby Policy 2.0
