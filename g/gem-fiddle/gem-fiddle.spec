%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fiddle

Name:          gem-fiddle
Version:       1.1.6
Release:       alt1
Summary:       A libffi wrapper for Ruby
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/fiddle
Vcs:           https://github.com/ruby/fiddle.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: libffi-devel
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(test-unit-ruby-core) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
Requires:      ruby >= 2.5.0
Provides:      gem(fiddle) = 1.1.6

%description
A libffi wrapper for Ruby.


%if_enabled    doc
%package       -n gem-fiddle-doc
Version:       1.1.6
Release:       alt1
Summary:       A libffi wrapper for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fiddle
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fiddle) = 1.1.6

%description   -n gem-fiddle-doc
A libffi wrapper for Ruby documentation files.

%description   -n gem-fiddle-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fiddle.
%endif


%if_enabled    devel
%package       -n gem-fiddle-devel
Version:       1.1.6
Release:       alt1
Summary:       A libffi wrapper for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fiddle
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fiddle) = 1.1.6
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 3.3.5
Requires:      gem(test-unit-ruby-core) >= 0

%description   -n gem-fiddle-devel
A libffi wrapper for Ruby development package.

%description   -n gem-fiddle-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fiddle.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-fiddle-doc
%doc LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fiddle-devel
%doc LICENSE.txt README.md
%ruby_includedir/*
%endif


%changelog
* Mon Feb 17 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.6-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
