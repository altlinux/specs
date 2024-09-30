%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-highline

Name:          gem-hoe-highline
Version:       0.2.1.3
Release:       alt1
Summary:       A Hoe plugin for building interactive Rake tasks
License:       BSD
Group:         Development/Ruby
Url:           https://bitbucket.org/ged/hoe-highline
Vcs:           https://bitbucket.org/ged/hoe-highline.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(highline) >= 1.6
BuildRequires: gem(hoe) >= 3.11
BuildRequires: gem(hoe-mercurial) >= 1.4
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(highline) >= 3
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency highline >= 2.0.3,highline < 3
Requires:      gem(highline) >= 1.6
Requires:      gem(hoe) >= 3.11
Conflicts:     gem(highline) >= 3
Provides:      gem(hoe-highline) = 0.2.1.3


%description
A Hoe plugin for building interactive Rake tasks.

Hoe-highline, as you might have guessed from the name, adds prompting and
displaying functions from the HighLine[http://highline.rubyforge.org/] gem to
your Rake environment, allowing you to ask questions, prompt for passwords,
build menus, and other fun stuff.


%if_enabled    doc
%package       -n gem-hoe-highline-doc
Version:       0.2.1.3
Release:       alt1
Summary:       A Hoe plugin for building interactive Rake tasks documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-highline
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-highline) = 0.2.1.3

%description   -n gem-hoe-highline-doc
A Hoe plugin for building interactive Rake tasks documentation files.

%description   -n gem-hoe-highline-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-highline.
%endif


%if_enabled    devel
%package       -n gem-hoe-highline-devel
Version:       0.2.1.3
Release:       alt1
Summary:       A Hoe plugin for building interactive Rake tasks development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-highline
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-highline) = 0.2.1.3
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe-mercurial) >= 1.4

%description   -n gem-hoe-highline-devel
A Hoe plugin for building interactive Rake tasks development package.

%description   -n gem-hoe-highline-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-highline.
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
%files         -n gem-hoe-highline-doc
%doc History.rdoc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-highline-devel
%doc History.rdoc README.rdoc
%endif


%changelog
* Fri Aug 30 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.1.3-alt1
- ^ 0.2.1 -> 0.2.1p3

* Fri May 13 2022 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
