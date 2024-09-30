%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hoe-seattlerb

Name:          gem-hoe-seattlerb
Version:       1.3.5
Release:       alt1.1
Summary:       Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and email providing full front-to-back release/announce automation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/seattlerb/hoe-seattlerb
Vcs:           https://github.com/seattlerb/hoe-seattlerb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 5.17.0
BuildRequires: gem(rdoc) >= 4.0
BuildRequires: gem(hoe) >= 4.2
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
BuildConflicts: gem(hoe) >= 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Provides:      gem(hoe-seattlerb) = 1.3.5


%description
Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation.


%if_enabled    doc
%package       -n gem-hoe-seattlerb-doc
Version:       1.3.5
Release:       alt1.1
Summary:       Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and email providing full front-to-back release/announce automation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hoe-seattlerb
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(hoe-seattlerb) = 1.3.5

%description   -n gem-hoe-seattlerb-doc
Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation documentation
files.

%description   -n gem-hoe-seattlerb-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hoe-seattlerb.
%endif


%if_enabled    devel
%package       -n gem-hoe-seattlerb-devel
Version:       1.3.5
Release:       alt1.1
Summary:       Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and email providing full front-to-back release/announce automation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hoe-seattlerb
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(hoe-seattlerb) = 1.3.5
Requires:      gem(minitest) >= 5.17.0
Requires:      gem(rdoc) >= 4.0
Requires:      gem(hoe) >= 4.2
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7
Conflicts:     gem(hoe) >= 5

%description   -n gem-hoe-seattlerb-devel
Hoe plugins providing tasks used by seattle.rb including minitest, perforce, and
email providing full front-to-back release/announce automation development
package.

%description   -n gem-hoe-seattlerb-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hoe-seattlerb.
%endif


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-hoe-seattlerb-doc
%doc README.txt
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hoe-seattlerb-devel
%doc README.txt
%endif


%changelog
* Thu Sep 26 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1.1
- ! spec and .gear

* Sat Jul 17 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.5-alt1
- + packaged gem with Ruby Policy 2.0
