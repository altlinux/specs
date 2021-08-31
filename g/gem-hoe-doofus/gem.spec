%define        gemname hoe-doofus

Name:          gem-hoe-doofus
Version:       1.0.0
Release:       alt1
Summary:       A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jbarnette/hoe-doofus
Vcs:           https://github.com/jbarnette/hoe-doofus.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(hoe-doofus) = 1.0.0


%description
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases.
It shows a configurable checklist when <tt>rake release</tt> is run, and
provides a chance to abort if anything's been forgotten.


%package       -n gem-hoe-doofus-doc
Version:       1.0.0
Release:       alt1
Summary:       A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-doofus
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-doofus) = 1.0.0

%description   -n gem-hoe-doofus-doc
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases
documentation files.

A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases.
It shows a configurable checklist when <tt>rake release</tt> is run, and
provides a chance to abort if anything's been forgotten.

%description   -n gem-hoe-doofus-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-doofus.


%package       -n gem-hoe-doofus-devel
Version:       1.0.0
Release:       alt1
Summary:       A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-doofus
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-doofus) = 1.0.0
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-hoe-doofus-devel
A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases
development package.

A Hoe plugin that helps me (and you, maybe?) keep from messing up gem releases.
It shows a configurable checklist when <tt>rake release</tt> is run, and
provides a chance to abort if anything's been forgotten.

%description   -n gem-hoe-doofus-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-doofus.


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

%files         -n gem-hoe-doofus-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-hoe-doofus-devel
%doc README.rdoc


%changelog
* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0
