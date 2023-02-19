# vim: set ft=spec: -*- rpm-spec -*-
%define        gemname gitlab-turbolinks-classic

Name:          gem-gitlab-turbolinks-classic
Version:       2.5.7
Release:       alt1.1
Summary:       Turbolinks makes navigating your web application faster
License:       MIT
Group:         Development/Ruby
Url:           https://gitlab.com/jamedjo/gitlab-turbolinks-classic/
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(coffee-rails) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(coffee-rails) >= 0
Provides:      gem(gitlab-turbolinks-classic) = 2.5.7


%description
Turbolinks makes navigating your web application faster.


%package       -n gem-gitlab-turbolinks-classic-doc
Version:       2.5.7
Release:       alt1.1
Summary:       Turbolinks makes navigating your web application faster documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gitlab-turbolinks-classic
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gitlab-turbolinks-classic) = 2.5.7

%description   -n gem-gitlab-turbolinks-classic-doc
Turbolinks makes navigating your web application faster documentation files.

%description   -n gem-gitlab-turbolinks-classic-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gitlab-turbolinks-classic.


%package       -n gem-gitlab-turbolinks-classic-devel
Version:       2.5.7
Release:       alt1.1
Summary:       Turbolinks makes navigating your web application faster development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gitlab-turbolinks-classic
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gitlab-turbolinks-classic) = 2.5.7

%description   -n gem-gitlab-turbolinks-classic-devel
Turbolinks makes navigating your web application faster development package.

%description   -n gem-gitlab-turbolinks-classic-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gitlab-turbolinks-classic.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-gitlab-turbolinks-classic-doc
%ruby_gemdocdir

%files         -n gem-gitlab-turbolinks-classic-devel


%changelog
* Sun Jan 29 2023 Pavel Skrylev <majioa@altlinux.org> 2.5.7-alt1.1
- ! by closing build deps under check condition

* Thu May 14 2020 Pavel Skrylev <majioa@altlinux.org> 2.5.7-alt1
- + packaged gem with usage Ruby Policy 2.0
