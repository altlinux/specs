%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname stringio

Name:          gem-stringio
Version:       3.1.3
Release:       alt1
Summary:       Pseudo IO on String
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/stringio
Vcs:           https://github.com/ruby/stringio.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(rdoc) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7
Provides:      gem(stringio) = 3.1.3

%description
Pseudo `IO` class from/to `String`.


%if_enabled    doc
%package       -n gem-stringio-doc
Version:       3.1.3
Release:       alt1
Summary:       Pseudo IO on String documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stringio
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stringio) = 3.1.3

%description   -n gem-stringio-doc
Pseudo IO on String documentation files.

Pseudo `IO` class from/to `String`.

%description   -n gem-stringio-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stringio.
%endif


%if_enabled    devel
%package       -n gem-stringio-devel
Version:       3.1.3
Release:       alt1
Summary:       Pseudo IO on String development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета stringio
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(stringio) = 3.1.3
Requires:      gem(rake-compiler) >= 0
Requires:      gem(rdoc) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-stringio-devel
Pseudo IO on String development package.

Pseudo `IO` class from/to `String`.

%description   -n gem-stringio-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета stringio.
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
%doc COPYING LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-stringio-doc
%doc COPYING LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-stringio-devel
%doc COPYING LICENSE.txt README.md
%endif


%changelog
* Tue Feb 18 2025 Pavel Skrylev <majioa@altlinux.org> 3.1.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
