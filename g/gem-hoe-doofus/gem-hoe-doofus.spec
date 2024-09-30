%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-doofus

Name:          gem-hoe-doofus
Version:       1.0.0
Release:       alt1.1
Summary:       A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jbarnette/hoe-doofus
Vcs:           https://github.com/jbarnette/hoe-doofus.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 4.2
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(rdoc) >= 7
%endif


%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(hoe-doofus) = 1.0.0


%description
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases.
It shows a configurable checklist when <tt>rake release</tt> is run, and
provides a chance to abort if anything's been forgotten.


%if_enabled    doc
%package       -n gem-hoe-doofus-doc
Version:       1.0.0
Release:       alt1.1
Summary:       A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-doofus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-doofus) = 1.0.0

%description   -n gem-hoe-doofus-doc
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases
documentation files.

%description   -n gem-hoe-doofus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-doofus.
%endif


%if_enabled    devel
%package       -n gem-hoe-doofus-devel
Version:       1.0.0
Release:       alt1.1
Summary:       A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-doofus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-doofus) = 1.0.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-hoe-doofus-devel
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases
development package.

%description   -n gem-hoe-doofus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-doofus.
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
%doc CHANGELOG.rdoc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hoe-doofus-doc
%doc CHANGELOG.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-doofus-devel
%doc CHANGELOG.rdoc README.rdoc
%endif


%changelog
* Fri Sep 27 2024 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1.1
- ! spec

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
