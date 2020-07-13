%define        pkgname cheffish

Name:          gem-%pkgname
Version:       16.0.3
Release:       alt1
Summary:       Resources and tools for testing and interacting with Chef and Chef Server
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/chef/cheffish
Vcs:           https://github.com/chef/cheffish.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
%summary.

This library provides a variety of convergent resources for interacting with
the Chef Server; along the way, it happens to provide some very useful and
sophisticated ways of running Chef resources as recipes in RSpec examples.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Jul 13 2020 Pavel Skrylev <majioa@altlinux.org> 16.0.3-alt1
- ^ 14.0.9 -> 16.0.3
- ! spec tags and syntax

* Mon Apr 08 2019 Pavel Skrylev <majioa@altlinux.org> 14.0.9-alt1
- ^ 14.0.1 -> 14.0.9
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 14.0.1-alt1
- Initial build for Sisyphus
