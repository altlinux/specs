%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname numerizer

Name:          gem-numerizer
Version:       0.2.0.50
Release:       alt0.1
Summary:       Numerizer is a gem to help with parsing numbers in natural language from strings (ex forty two)
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jduff/numerizer
Vcs:           https://github.com/jduff/numerizer.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 13
BuildConflicts: gem(rake) >= 14
%if_enabled check
BuildRequires: gem(minitest) >= 5.0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(numerizer) = 0.2.0.50

%ruby_use_gem_version numerizer:0.2.0.50

%description
Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two). It was extracted from the awesome Chronic gem
http://github.com/evaryont/chronic.


%if_enabled    doc
%package       -n gem-numerizer-doc
Version:       0.2.0.50
Release:       alt0.1
Summary:       Numerizer is a gem to help with parsing numbers in natural language from strings (ex forty two) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета numerizer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(numerizer) = 0.2.0.50

%description   -n gem-numerizer-doc
Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two) documentation files.

Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two). It was extracted from the awesome Chronic gem
http://github.com/evaryont/chronic.

%description   -n gem-numerizer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета numerizer.
%endif


%if_enabled    devel
%package       -n gem-numerizer-devel
Version:       0.2.0.50
Release:       alt0.1
Summary:       Numerizer is a gem to help with parsing numbers in natural language from strings (ex forty two) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета numerizer
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(numerizer) = 0.2.0.50
Requires:      gem(minitest) >= 5.0
Requires:      gem(rake) >= 13
Conflicts:     gem(minitest) >= 6
Conflicts:     gem(rake) >= 14

%description   -n gem-numerizer-devel
Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two) development package.

Numerizer is a gem to help with parsing numbers in natural language from strings
(ex forty two). It was extracted from the awesome Chronic gem
http://github.com/evaryont/chronic.

%description   -n gem-numerizer-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета numerizer.
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
%doc LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-numerizer-doc
%doc LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-numerizer-devel
%doc LICENSE README.rdoc
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.0.50-alt0.1
- ^ 0.2.0 -> 0.2.0p50
- * define explicit dependencies

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
