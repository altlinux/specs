%define        gemname hoe-git

Name:          gem-hoe-git
Version:       1.6.0
Release:       alt1
Summary:       A set of Hoe plugins for tighter Git integration
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jbarnette/hoe-git
Vcs:           https://github.com/jbarnette/hoe-git.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(hoe-git) = 1.6.0


%description
A set of Hoe plugins for tighter Git integration. Provides tasks to automate
release tagging and pushing and changelog generation. I expect it'll learn a few
more tricks in the future.


%package       -n gem-hoe-git-doc
Version:       1.6.0
Release:       alt1
Summary:       A set of Hoe plugins for tighter Git integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-git
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-git) = 1.6.0

%description   -n gem-hoe-git-doc
A set of Hoe plugins for tighter Git integration documentation files.

A set of Hoe plugins for tighter Git integration. Provides tasks to automate
release tagging and pushing and changelog generation. I expect it'll learn a few
more tricks in the future.

%description   -n gem-hoe-git-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-git.


%package       -n gem-hoe-git-devel
Version:       1.6.0
Release:       alt1
Summary:       A set of Hoe plugins for tighter Git integration development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-git
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-git) = 1.6.0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-hoe-git-devel
A set of Hoe plugins for tighter Git integration development package.

A set of Hoe plugins for tighter Git integration. Provides tasks to automate
release tagging and pushing and changelog generation. I expect it'll learn a few
more tricks in the future.

%description   -n gem-hoe-git-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-git.


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

%files         -n gem-hoe-git-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-hoe-git-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- + packaged gem with Ruby Policy 2.0
