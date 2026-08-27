%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname minitest-global_expectations

Name:          gem-minitest-global-expectations
Version:       1.0.2
Release:       alt1
Summary:       Support minitest expectation methods for all objects
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/jeremyevans/minitest-global_expectations
Vcs:           https://github.com/jeremyevans/minitest-global_expectations.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(minitest) > 5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names minitest-global_expectations,minitest-global-expectations
Requires:      ruby >= 1.8
Requires:      gem(minitest) > 5
Provides:      gem(minitest-global_expectations) = 1.0.2

%description
minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling an
expectation method on with an underscore.


%if_enabled    doc
%package       -n gem-minitest-global-expectations-doc
Version:       1.0.2
Release:       alt1
Summary:       Support minitest expectation methods for all objects documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitest-global_expectations
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitest-global_expectations) = 1.0.2

%description   -n gem-minitest-global-expectations-doc
Support minitest expectation methods for all objects documentation
files.

minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling an
expectation method on with an underscore.

%description   -n gem-minitest-global-expectations-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitest-global_expectations.
%endif


%if_enabled    devel
%package       -n gem-minitest-global-expectations-devel
Version:       1.0.2
Release:       alt1
Summary:       Support minitest expectation methods for all objects development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitest-global_expectations
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitest-global_expectations) = 1.0.2

%description   -n gem-minitest-global-expectations-devel
Support minitest expectation methods for all objects development
package.

minitest-global_expectations allows you to keep using simple code in your
minitest specs, without having to wrap every single object you are calling an
expectation method on with an underscore.

%description   -n gem-minitest-global-expectations-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitest-global_expectations.
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
%doc CHANGELOG MIT-LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-minitest-global-expectations-doc
%doc CHANGELOG MIT-LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-minitest-global-expectations-devel
%doc CHANGELOG MIT-LICENSE README.rdoc
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- ^ 1.0.1 -> 1.0.2

* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- + packaged gem with Ruby Policy 2.0
