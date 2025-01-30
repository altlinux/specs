%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_disable   devel
%define        gemname snowglobe

Name:          gem-snowglobe
Version:       0.3.0
Release:       alt1
Summary:       Create temporary Rails applications for use in testing
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mcmire/snowglobe
Vcs:           https://github.com/mcmire/snowglobe.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.1.4
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(appraisal) >= 0
BuildRequires: gem(pry-byebug) >= 0
BuildRequires: gem(rails) >= 0
BuildRequires: gem(rspec) >= 0
BuildRequires: gem(rubocop) >= 0
BuildRequires: gem(super_diff) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
Provides:      gem(snowglobe) = 0.3.0

%description
Snowglobe is a gem that helps erect and destroy Rails applications for use in
tests.


%if_enabled    doc
%package       -n gem-snowglobe-doc
Version:       0.3.0
Release:       alt1
Summary:       Create temporary Rails applications for use in testing documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета snowglobe
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(snowglobe) = 0.3.0

%description   -n gem-snowglobe-doc
Create temporary Rails applications for use in testing documentation
files.

Snowglobe is a gem that helps erect and destroy Rails applications for use in
tests.

%description   -n gem-snowglobe-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета snowglobe.
%endif


%if_enabled    devel
%package       -n gem-snowglobe-devel
Version:       0.3.0
Release:       alt1
Summary:       Create temporary Rails applications for use in testing development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета snowglobe
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(snowglobe) = 0.3.0
Requires:      gem(appraisal) >= 0
Requires:      gem(bundler) >= 2.1.4
Requires:      gem(pry-byebug) >= 0
Requires:      gem(rails) >= 0
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 0
Requires:      gem(rubocop) >= 0
Requires:      gem(super_diff) >= 0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(rake) >= 14

%description   -n gem-snowglobe-devel
Create temporary Rails applications for use in testing development
package.

Snowglobe is a gem that helps erect and destroy Rails applications for use in
tests.

%description   -n gem-snowglobe-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета snowglobe.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-snowglobe-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-snowglobe-devel
%doc LICENSE README.md
%endif


%changelog
* Mon Jan 13 2025 Pavel Skrylev <majioa@altlinux.org> 0.3.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
