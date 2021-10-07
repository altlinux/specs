%define        gemname packaging

Name:          gem-packaging
Version:       0.99.80
Release:       alt1
Summary:       Packaging automation for Puppet software
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/puppetlabs/packaging
Vcs:           https://github.com/puppetlabs/packaging.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         exec-fix.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rspec) >= 2.14.1 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0.24.1 gem(rubocop) < 2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(rake) >= 12.3 gem(rake) < 14
BuildRequires: gem(artifactory) >= 2 gem(artifactory) < 4
BuildRequires: gem(release-metrics) >= 0
BuildRequires: gem(csv) >= 3.1.5

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_version packaging:0.99.80
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency artifactory >= 3.0.1,artifactory < 4
%ruby_use_gem_dependency csv >= 3.1.5
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(artifactory) >= 2 gem(artifactory) < 4
Requires:      gem(release-metrics) >= 0
Requires:      gem(csv) >= 3.1.5
Obsoletes:     ruby-packaging < %EVR
Provides:      ruby-packaging = %EVR
Provides:      gem(packaging) = 0.99.80


%description
This is a repository for packaging automation for Puppet software. The goal is
to abstract and automate packaging processes beyond individual software projects
to a level where this repo can be cloned inside any project.


%package       -n gem-packaging-doc
Version:       0.99.80
Release:       alt1
Summary:       Packaging automation for Puppet software documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета packaging
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(packaging) = 0.99.80

%description   -n gem-packaging-doc
Packaging automation for Puppet software documentation files.

This is a repository for packaging automation for Puppet software. The goal is
to abstract and automate packaging processes beyond individual software projects
to a level where this repo can be cloned inside any project.

%description   -n gem-packaging-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета packaging.


%package       -n gem-packaging-devel
Version:       0.99.80
Release:       alt1
Summary:       Packaging automation for Puppet software development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета packaging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(packaging) = 0.99.80
Requires:      gem(rspec) >= 2.14.1 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.24.1 gem(rubocop) < 2
Requires:      gem(pry) >= 0
Requires:      gem(artifactory) >= 3.0 gem(artifactory) < 4

%description   -n gem-packaging-devel
Packaging automation for Puppet software development package.

This is a repository for packaging automation for Puppet software. The goal is
to abstract and automate packaging processes beyond individual software projects
to a level where this repo can be cloned inside any project.

%description   -n gem-packaging-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета packaging.


%prep
%setup
%patch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README-Solaris.md README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-packaging-doc
%doc README-Solaris.md README.md
%ruby_gemdocdir

%files         -n gem-packaging-devel
%doc README-Solaris.md README.md


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.99.80-alt1
- ^ 0.99.59 -> 0.99.80

* Mon Mar 16 2020 Pavel Skrylev <majioa@altlinux.org> 0.99.59-alt1
- ^ 0.99.36 -> 0.99.59

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.99.36-alt1
- fixed ! spec
- ^ 0.99.35 -> 0.99.36

* Thu Jun 13 2019 Pavel Skrylev <majioa@altlinux.org> 0.99.35-alt1
- used > Ruby Policy 2.0
- updated ^ 0.99.22 -> 0.99.35

* Mon Jan 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.99.22-alt1
- Version updated to 0.99.22

* Tue Dec 25 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.99.20-alt1
- Initial build for Sisyphus
