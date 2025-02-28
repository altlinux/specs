%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname bigdecimal

Name:          gem-bigdecimal
Version:       3.1.9
Release:       alt1
Summary:       Arbitrary-precision decimal floating-point number library
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/bigdecimal
Vcs:           https://github.com/ruby/bigdecimal.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(benchmark_driver) >= 0
BuildRequires: gem(fiddle) >= 0
BuildRequires: gem(irb) >= 0
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(rake-compiler) >= 0.9
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(test-unit-ruby-core) >= 0
BuildConflicts: gem(minitest) >= 6
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
Requires:      ruby >= 2.5.0
Provides:      gem(bigdecimal) = 3.1.9

%description
This library provides arbitrary-precision decimal floating-point number class.


%if_enabled    doc
%package       -n gem-bigdecimal-doc
Version:       3.1.9
Release:       alt1
Summary:       Arbitrary-precision decimal floating-point number library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bigdecimal
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bigdecimal) = 3.1.9

%description   -n gem-bigdecimal-doc
Arbitrary-precision decimal floating-point number library documentation
files.

This library provides arbitrary-precision decimal floating-point number class.

%description   -n gem-bigdecimal-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bigdecimal.
%endif


%if_enabled    devel
%package       -n gem-bigdecimal-devel
Version:       3.1.9
Release:       alt1
Summary:       Arbitrary-precision decimal floating-point number library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bigdecimal
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bigdecimal) = 3.1.9
Requires:      gem(benchmark_driver) >= 0
Requires:      gem(fiddle) >= 0
Requires:      gem(irb) >= 0
Requires:      gem(rake) >= 12.3.3
Requires:      gem(rake-compiler) >= 0.9
Requires:      gem(test-unit) >= 0
Requires:      gem(test-unit-ruby-core) >= 0
Conflicts:     gem(minitest) >= 6

%description   -n gem-bigdecimal-devel
Arbitrary-precision decimal floating-point number library development
package.

This library provides arbitrary-precision decimal floating-point number class.

%description   -n gem-bigdecimal-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bigdecimal.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-bigdecimal-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-bigdecimal-devel
%doc LICENSE README.md
%ruby_includedir/*
%endif


%changelog
* Mon Feb 17 2025 Pavel Skrylev <majioa@altlinux.org> 3.1.9-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
