%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-deveiate

Name:          gem-hoe-deveiate
Version:       0.10.0.4
Release:       alt1
Summary:       A collection of Rake tasks and utility functions I use to maintain my Open Source projects
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://deveiate.org/hoe-deveiate
Vcs:           https://github.com/ged/hoe-deveiate.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 3.16
BuildRequires: gem(hoe-highline) >= 0.2
BuildRequires: gem(hoe-mercurial) >= 1.4
BuildRequires: gem(mail) >= 2.6
BuildRequires: gem(rdoc) >= 6.0
BuildRequires: gem(rspec) >= 3.5
BuildConflicts: gem(hoe-highline) >= 1
BuildConflicts: gem(hoe-mercurial) >= 2
BuildConflicts: gem(mail) >= 3
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(hoe) >= 3.16
Requires:      gem(hoe-highline) >= 0.2
Requires:      gem(hoe-mercurial) >= 1.4
Requires:      gem(mail) >= 2.6
Requires:      gem(rspec) >= 3.5
Requires:      gem(rdoc) >= 6.0
Conflicts:     gem(hoe-highline) >= 1
Conflicts:     gem(hoe-mercurial) >= 2
Conflicts:     gem(mail) >= 3
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rdoc) >= 7
Provides:      gem(hoe-deveiate) = 0.10.0.4


%description
A collection of Rake tasks and utility functions I use to maintain my Open
Source projects. It's really only useful if you want to help maintain one of
them.


%if_enabled    doc
%package       -n gem-hoe-deveiate-doc
Version:       0.10.0.4
Release:       alt1
Summary:       A collection of Rake tasks and utility functions I use to maintain my Open Source projects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-deveiate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-deveiate) = 0.10.0.4

%description   -n gem-hoe-deveiate-doc
A collection of Rake tasks and utility functions I use to maintain my Open
Source projects documentation files.

A collection of Rake tasks and utility functions I use to maintain my Open
Source projects. It's really only useful if you want to help maintain one of
them.

%description   -n gem-hoe-deveiate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-deveiate.
%endif


%if_enabled    devel
%package       -n gem-hoe-deveiate-devel
Version:       0.10.0.4
Release:       alt1
Summary:       A collection of Rake tasks and utility functions I use to maintain my Open Source projects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-deveiate
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-deveiate) = 0.10.0.4

%description   -n gem-hoe-deveiate-devel
A collection of Rake tasks and utility functions I use to maintain my Open
Source projects development package.

A collection of Rake tasks and utility functions I use to maintain my Open
Source projects. It's really only useful if you want to help maintain one of
them.

%description   -n gem-hoe-deveiate-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-deveiate.
%endif


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc History.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hoe-deveiate-doc
%doc History.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-deveiate-devel
%doc History.rdoc README.rdoc
%endif


%changelog
* Fri Aug 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.10.0.4-alt1
- ^ 0.10.0 -> 0.10.0.4

* Fri May 13 2022 Pavel Skrylev <majioa@altlinux.org> 0.10.0-alt1
- + packaged gem with Ruby Policy 2.0
