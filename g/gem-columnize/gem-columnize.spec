%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname columnize

Name:          gem-columnize
Version:       0.9.1
Release:       alt0.1
Summary:       Module to format an Array as an Array of String aligned in columns
License:       Ruby or GPLv2
Group:         Development/Ruby
Url:           https://github.com/rocky/columnize
Vcs:           https://github.com/rocky/columnize.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 12.3.3
BuildRequires: gem(test-unit) >= 3.3.5
BuildRequires: gem(rdoc) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Provides:      gem(columnize) = 0.9.1

%ruby_use_gem_version columnize:0.9.1

%description
In showing a long lists, sometimes one would prefer to see the value arranged
aligned in columns. Some examples include listing methods of an object or
debugger commands. See Examples in the rdoc documentation for examples.


%if_enabled    doc
%package       -n gem-columnize-doc
Version:       0.9.1
Release:       alt0.1
Summary:       Module to format an Array as an Array of String aligned in columns documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета columnize
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(columnize) = 0.9.1

%description   -n gem-columnize-doc
Module to format an Array as an Array of String aligned in columns documentation
files.

In showing a long lists, sometimes one would prefer to see the value arranged
aligned in columns. Some examples include listing methods of an object or
debugger commands. See Examples in the rdoc documentation for examples.

%description   -n gem-columnize-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета columnize.
%endif


%if_enabled    devel
%package       -n gem-columnize-devel
Version:       0.9.1
Release:       alt0.1
Summary:       Module to format an Array as an Array of String aligned in columns development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета columnize
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(columnize) = 0.9.1
Requires:      gem(rake) >= 12.3.3
Requires:      gem(test-unit) >= 3.3.5
Requires:      gem(rdoc) >= 0

%description   -n gem-columnize-devel
Module to format an Array as an Array of String aligned in columns development
package.

In showing a long lists, sometimes one would prefer to see the value arranged
aligned in columns. Some examples include listing methods of an object or
debugger commands. See Examples in the rdoc documentation for examples.

%description   -n gem-columnize-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета columnize.
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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-columnize-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-columnize-devel
%doc README.md
%endif


%changelog
* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 0.9.1-alt0.1
- + packaged gem with Ruby Policy 2.0
