%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-mercurial

Name:          gem-hoe-mercurial
Version:       1.4.1
Release:       alt1.1
Summary:       This is a fork of the [hoe-hg]
License:       BSD
Group:         Development/Ruby
Url:           http://bitbucket.org/ged/hoe-mercurial
Vcs:           http://bitbucket.org/ged/hoe-mercurial.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency hoe >= 4.2.2,hoe < 5
Requires:      gem(hoe) >= 0
Provides:      gem(hoe-mercurial) = 1.4.1


%description
This is a fork of the [hoe-hg](https://bitbucket.org/mml/hoe-hg) plugin. I
forked it because I use quite a few additional Mercurial tasks for my
development workflow than are provided by the original, and I thought they'd
possibly be useful to someone else.

I've offered to push my changes back up to the original, but I gave up waiting
for a response.


%if_enabled    doc
%package       -n gem-hoe-mercurial-doc
Version:       1.4.1
Release:       alt1.1
Summary:       This is a fork of the [hoe-hg] documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-mercurial
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-mercurial) = 1.4.1

%description   -n gem-hoe-mercurial-doc
This is a fork of the [hoe-hg] documentation files.

This is a fork of the [hoe-hg](https://bitbucket.org/mml/hoe-hg) plugin. I
forked it because I use quite a few additional Mercurial tasks for my
development workflow than are provided by the original, and I thought they'd
possibly be useful to someone else.

I've offered to push my changes back up to the original, but I gave up waiting
for a response.

%description   -n gem-hoe-mercurial-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-mercurial.
%endif


%if_enabled    devel
%package       -n gem-hoe-mercurial-devel
Version:       1.4.1
Release:       alt1.1
Summary:       This is a fork of the [hoe-hg] development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-mercurial
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-mercurial) = 1.4.1
Requires:      gem(rdoc) >= 4.0

%description   -n gem-hoe-mercurial-devel
This is a fork of the [hoe-hg] development package.

This is a fork of the [hoe-hg](https://bitbucket.org/mml/hoe-hg) plugin. I
forked it because I use quite a few additional Mercurial tasks for my
development workflow than are provided by the original, and I thought they'd
possibly be useful to someone else.

I've offered to push my changes back up to the original, but I gave up waiting
for a response.

%description   -n gem-hoe-mercurial-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-mercurial.
%endif


%prep
%setup
%autopatch -p1

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

%if_enabled    doc
%files         -n gem-hoe-mercurial-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-mercurial-devel
%doc README.rdoc
%endif


%changelog
* Thu Sep 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1.1
- ! spec and git struct

* Fri May 13 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.1-alt1
- + packaged gem with Ruby Policy 2.0
