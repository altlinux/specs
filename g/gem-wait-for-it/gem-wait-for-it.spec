%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname wait_for_it

Name:          gem-wait-for-it
Version:       0.2.1
Release:       alt1
Summary:       Stop sleeping in your tests, instead wait for it
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zombocom/wait_for_it
Vcs:           https://github.com/zombocom/wait_for_it.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_alias_names wait_for_it,wait-for-it
Provides:      gem(wait_for_it) = 0.2.1

%description
Make your complicated integration tests more deterministic with wait for it


%if_enabled    doc
%package       -n gem-wait-for-it-doc
Version:       0.2.1
Release:       alt1
Summary:       Stop sleeping in your tests, instead wait for it documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета wait_for_it
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(wait_for_it) = 0.2.1

%description   -n gem-wait-for-it-doc
Stop sleeping in your tests, instead wait for it documentation files.

Make your complicated integration tests more deterministic with wait for it

%description   -n gem-wait-for-it-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета wait_for_it.
%endif


%if_enabled    devel
%package       -n gem-wait-for-it-devel
Version:       0.2.1
Release:       alt1
Summary:       Stop sleeping in your tests, instead wait for it development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета wait_for_it
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(wait_for_it) = 0.2.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-wait-for-it-devel
Stop sleeping in your tests, instead wait for it development package.

Make your complicated integration tests more deterministic with wait for it

%description   -n gem-wait-for-it-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета wait_for_it.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-wait-for-it-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-wait-for-it-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE.txt README.md
%endif


%changelog
* Thu Mar 06 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
