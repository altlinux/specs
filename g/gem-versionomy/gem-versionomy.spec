%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname versionomy

Name:          gem-versionomy
Version:       0.5.0
Release:       alt2
Summary:       Versionomy is a generalized version number library
License:       BSD-3-Clause
Group:         Development/Ruby
Url:           http://dazuma.github.io/versionomy
Vcs:           https://github.com/dazuma/versionomy.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
Patch:         rakefile.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(blockenspiel) >= 0.5.0
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rdoc) >= 4.2
BuildConflicts: gem(blockenspiel) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(blockenspiel) >= 0.5.0
Conflicts:     gem(blockenspiel) >= 1
Provides:      gem(versionomy) = 0.5.0


%description
Versionomy is a generalized version number library. It provides tools to
represent, manipulate, parse, and compare version numbers in the wide variety of
versioning schemes in use.


%if_enabled    doc
%package       -n gem-versionomy-doc
Version:       0.5.0
Release:       alt2
Summary:       Versionomy is a generalized version number library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета versionomy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(versionomy) = 0.5.0

%description   -n gem-versionomy-doc
Versionomy is a generalized version number library documentation
files.

Versionomy is a generalized version number library. It provides tools to
represent, manipulate, parse, and compare version numbers in the wide variety of
versioning schemes in use.

%description   -n gem-versionomy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета versionomy.
%endif


%if_enabled    devel
%package       -n gem-versionomy-devel
Version:       0.5.0
Release:       alt2
Summary:       Versionomy is a generalized version number library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета versionomy
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(versionomy) = 0.5.0
Requires:      gem(minitest) >= 5.8
Requires:      gem(rake) >= 10.0
Requires:      gem(rdoc) >= 4.2

%description   -n gem-versionomy-devel
Versionomy is a generalized version number library development
package.

Versionomy is a generalized version number library. It provides tools to
represent, manipulate, parse, and compare version numbers in the wide variety of
versioning schemes in use.

%description   -n gem-versionomy-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета versionomy.
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
%doc README.rdoc test/tc_readme_examples.rb
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-versionomy-doc
%doc README.rdoc test/tc_readme_examples.rb
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-versionomy-devel
%doc README.rdoc test/tc_readme_examples.rb
%endif


%changelog
* Mon Aug 19 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt2
- ! fixed rakefile loading to proper version detection

* Wed May 08 2024 Pavel Skrylev <majioa@altlinux.org> 0.5.0-alt1
- + packaged gem with Ruby Policy 2.0
