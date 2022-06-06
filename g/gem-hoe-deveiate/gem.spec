%define        gemname hoe-deveiate

Name:          gem-hoe-deveiate
Version:       0.10.0
Release:       alt1
Summary:       A collection of Rake tasks and utility functions I use to maintain my Open Source projects
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://deveiate.org/hoe-deveiate
#Vcs:           https://github.com/ged/hoe-deveiate.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(hoe) >= 3.16 gem(hoe) < 4
BuildRequires: gem(hoe-highline) >= 0.2 gem(hoe-highline) < 1
BuildRequires: gem(hoe-mercurial) >= 1.4 gem(hoe-mercurial) < 2
BuildRequires: gem(mail) >= 2.6 gem(mail) < 3
BuildRequires: gem(rspec) >= 3.5 gem(rspec) < 4
BuildRequires: gem(rdoc) >= 6.0 gem(rdoc) < 7

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hoe) >= 3.16 gem(hoe) < 4
Requires:      gem(hoe-highline) >= 0.2 gem(hoe-highline) < 1
Requires:      gem(hoe-mercurial) >= 1.4 gem(hoe-mercurial) < 2
Requires:      gem(mail) >= 2.6 gem(mail) < 3
Requires:      gem(rspec) >= 3.5 gem(rspec) < 4
Requires:      gem(rdoc) >= 6.0 gem(rdoc) < 7
Provides:      gem(hoe-deveiate) = 0.10.0

%ruby_use_gem_version hoe-deveiate:0.10.0

%description
A collection of Rake tasks and utility functions I use to maintain my Open
Source projects. It's really only useful if you want to help maintain one of
them.


%package       -n gem-hoe-deveiate-doc
Version:       0.10.0
Release:       alt1
Summary:       A collection of Rake tasks and utility functions I use to maintain my Open Source projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-deveiate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-deveiate) = 0.10.0

%description   -n gem-hoe-deveiate-doc
A collection of Rake tasks and utility functions I use to maintain my Open
Source projects documentation files.

A collection of Rake tasks and utility functions I use to maintain my Open
Source projects. It's really only useful if you want to help maintain one of
them.

%description   -n gem-hoe-deveiate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-deveiate.


%package       -n gem-hoe-deveiate-devel
Version:       0.10.0
Release:       alt1
Summary:       A collection of Rake tasks and utility functions I use to maintain my Open Source projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-deveiate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-deveiate) = 0.10.0

%description   -n gem-hoe-deveiate-devel
A collection of Rake tasks and utility functions I use to maintain my Open
Source projects development package.

A collection of Rake tasks and utility functions I use to maintain my Open
Source projects. It's really only useful if you want to help maintain one of
them.

%description   -n gem-hoe-deveiate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-deveiate.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-hoe-deveiate-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-hoe-deveiate-devel
%doc README.rdoc


%changelog
* Fri May 13 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
