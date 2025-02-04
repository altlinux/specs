%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname foreman_webhooks

Name:          gem-foreman-webhooks
Version:       4.0.0
Release:       alt1
Summary:       Configure webhooks for Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_webhooks
Vcs:           https://github.com/theforeman/foreman_webhooks.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source1:       .public.tar
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(theforeman-rubocop) >= 0.1.0
BuildConflicts: gem(theforeman-rubocop) >= 0.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names foreman_webhooks,foreman-webhooks
Provides:      gem(foreman_webhooks) = 4.0.0


%description
Plugin for Foreman that allows to configure Webhooks.


%if_enabled    doc
%package       -n gem-foreman-webhooks-doc
Version:       4.0.0
Release:       alt1
Summary:       Configure webhooks for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_webhooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_webhooks) = 4.0.0

%description   -n gem-foreman-webhooks-doc
Configure webhooks for Foreman documentation files.

Plugin for Foreman that allows to configure Webhooks.

%description   -n gem-foreman-webhooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_webhooks.
%endif


%if_enabled    devel
%package       -n gem-foreman-webhooks-devel
Version:       4.0.0
Release:       alt1
Summary:       Configure webhooks for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_webhooks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_webhooks) = 4.0.0
Requires:      gem(rake) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(theforeman-rubocop) >= 0.1.0
Conflicts:     gem(theforeman-rubocop) >= 0.2

%description   -n gem-foreman-webhooks-devel
Configure webhooks for Foreman development package.

Plugin for Foreman that allows to configure Webhooks.

%description   -n gem-foreman-webhooks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_webhooks.
%endif


%prep
%setup -a 1

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
%files         -n gem-foreman-webhooks-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-foreman-webhooks-devel
%doc README.md
%endif


%changelog
* Fri Oct 04 2024 Pavel Skrylev <majioa@altlinux.org> 4.0.0-alt1
- ^ 3.0.5 -> 4.0.0

* Fri Nov 11 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1.1
- ! fixed www data paths to store js/css in

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1
- + packaged gem with Ruby Policy 2.0
