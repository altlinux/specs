%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname autotest-suffix

Name:          gem-autotest-suffix
Version:       1.1.0
Release:       alt1
Summary:       Enable suffix named tests in Autotest
License:       MIT
Group:         Development/Ruby
Url:           http://blowmage.com/autotest-suffix
Vcs:           https://github.com/blowmage/autotest-suffix.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(hoe) >= 3.13
BuildRequires: gem(minitest) >= 5.7
BuildRequires: gem(rdoc) >= 4.0
BuildConflicts: gem(hoe) >= 5
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency hoe >= 4.23,hoe < 5
%ruby_use_gem_dependency rdoc >= 6.12,rdoc < 7
Provides:      gem(autotest-suffix) = 1.1.0

%description
Autotest plugin to enable rails-style test filenames.


%if_enabled    doc
%package       -n gem-autotest-suffix-doc
Version:       1.1.0
Release:       alt1
Summary:       Enable suffix named tests in Autotest documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета autotest-suffix
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(autotest-suffix) = 1.1.0

%description   -n gem-autotest-suffix-doc
Enable suffix named tests in Autotest documentation files.

Autotest plugin to enable rails-style test filenames.

%description   -n gem-autotest-suffix-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета autotest-suffix.
%endif


%if_enabled    devel
%package       -n gem-autotest-suffix-devel
Version:       1.1.0
Release:       alt1
Summary:       Enable suffix named tests in Autotest development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета autotest-suffix
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(autotest-suffix) = 1.1.0
Requires:      gem(hoe) >= 3.13
Requires:      gem(minitest) >= 5.7
Requires:      gem(rdoc) >= 4.0
Conflicts:     gem(hoe) >= 5
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rdoc) >= 7

%description   -n gem-autotest-suffix-devel
Enable suffix named tests in Autotest development package.

Autotest plugin to enable rails-style test filenames.

%description   -n gem-autotest-suffix-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета autotest-suffix.
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
%doc History.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-autotest-suffix-doc
%doc History.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-autotest-suffix-devel
%doc History.txt README.md
%endif


%changelog
* Fri Oct 31 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
