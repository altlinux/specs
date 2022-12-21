%define        gemname foreman_webhooks

Name:          gem-foreman-webhooks
Version:       3.0.5
Release:       alt1.1
Summary:       Configure webhooks for Foreman
License:       GPL-3.0
Group:         Development/Ruby
Url:           https://github.com/theforeman/foreman_webhooks
Vcs:           https://github.com/theforeman/foreman_webhooks.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Source1:       public.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(foreman_webhooks) = 3.0.5


%description
Plugin for Foreman that allows to configure Webhooks.


%package       -n gem-foreman-webhooks-doc
Version:       3.0.5
Release:       alt1.1
Summary:       Configure webhooks for Foreman documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета foreman_webhooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(foreman_webhooks) = 3.0.5

%description   -n gem-foreman-webhooks-doc
Configure webhooks for Foreman documentation files.

Plugin for Foreman that allows to configure Webhooks.

%description   -n gem-foreman-webhooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета foreman_webhooks.


%package       -n gem-foreman-webhooks-devel
Version:       3.0.5
Release:       alt1.1
Summary:       Configure webhooks for Foreman development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета foreman_webhooks
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(foreman_webhooks) = 3.0.5

%description   -n gem-foreman-webhooks-devel
Configure webhooks for Foreman development package.

Plugin for Foreman that allows to configure Webhooks.

%description   -n gem-foreman-webhooks-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета foreman_webhooks.


%prep
%setup
%setup -a 1

%build
%ruby_build

%install
%ruby_install
install -d %buildroot%_datadir/foreman
cp -rp public %buildroot%_datadir/foreman

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%_datadir/foreman/public

%files         -n gem-foreman-webhooks-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-foreman-webhooks-devel
%doc README.md


%changelog
* Fri Nov 11 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1.1
- ! fixed www data paths to store js/css in

* Fri Sep 23 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.5-alt1
- + packaged gem with Ruby Policy 2.0
