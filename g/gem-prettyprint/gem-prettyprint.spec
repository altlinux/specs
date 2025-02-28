%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname prettyprint

Name:          gem-prettyprint
Version:       0.2.0
Release:       alt1
Summary:       Implements a pretty printing algorithm for readable structure
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/prettyprint
Vcs:           https://github.com/ruby/prettyprint.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.3.0
Provides:      gem(prettyprint) = 0.2.0

%description
Implements a pretty printing algorithm for readable structure.


%if_enabled    doc
%package       -n gem-prettyprint-doc
Version:       0.2.0
Release:       alt1
Summary:       Implements a pretty printing algorithm for readable structure documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prettyprint
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prettyprint) = 0.2.0

%description   -n gem-prettyprint-doc
Implements a pretty printing algorithm for readable structure documentation
files.

%description   -n gem-prettyprint-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prettyprint.
%endif


%if_enabled    devel
%package       -n gem-prettyprint-devel
Version:       0.2.0
Release:       alt1
Summary:       Implements a pretty printing algorithm for readable structure development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prettyprint
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prettyprint) = 0.2.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0

%description   -n gem-prettyprint-devel
Implements a pretty printing algorithm for readable structure development
package.

%description   -n gem-prettyprint-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prettyprint.
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
%doc LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-prettyprint-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-prettyprint-devel
%doc LICENSE.txt README.md
%endif


%changelog
* Mon Feb 17 2025 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
