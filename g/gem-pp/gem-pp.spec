%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname pp

Name:          gem-pp
Version:       0.6.2
Release:       alt1
Summary:       Provides a PrettyPrinter for Ruby objects
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/pp
Vcs:           https://github.com/ruby/pp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(prettyprint) >= 0
BuildRequires: gem(ruby2_keywords) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(prettyprint) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Provides:      gem(pp) = 0.6.2

%description
Provides a PrettyPrinter for Ruby objects


%if_enabled    doc
%package       -n gem-pp-doc
Version:       0.6.2
Release:       alt1
Summary:       Provides a PrettyPrinter for Ruby objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета pp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(pp) = 0.6.2

%description   -n gem-pp-doc
Provides a PrettyPrinter for Ruby objects documentation files.

%description   -n gem-pp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета pp.
%endif


%if_enabled    devel
%package       -n gem-pp-devel
Version:       0.6.2
Release:       alt1
Summary:       Provides a PrettyPrinter for Ruby objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета pp
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(pp) = 0.6.2
Requires:      gem(ruby2_keywords) >= 0

%description   -n gem-pp-devel
Provides a PrettyPrinter for Ruby objects development package.

%description   -n gem-pp-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета pp.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-pp-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-pp-devel
%doc COPYING README.md
%endif


%changelog
* Mon Feb 17 2025 Pavel Skrylev <majioa@altlinux.org> 0.6.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
