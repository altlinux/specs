%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname prettier_print

Name:          gem-prettier-print
Version:       1.2.1
Release:       alt1
Summary:       A drop-in replacement for the prettyprint gem with more functionality
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby-syntax-tree/prettier_print
Vcs:           https://github.com/ruby-syntax-tree/prettier_print.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(simplecov) >= 0
BuildRequires: gem(syntax_tree) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names prettier_print,prettier-print
Requires:      gem(rake) >= 0
Requires:      gem(simplecov) >= 0
Requires:      gem(syntax_tree) >= 0
Requires:      gem(test-unit) >= 0
Provides:      gem(prettier_print) = 1.2.1

%description
A drop-in replacement for the prettyprint gem with more functionality.


%if_enabled    doc
%package       -n gem-prettier-print-doc
Version:       1.2.1
Release:       alt1
Summary:       A drop-in replacement for the prettyprint gem with more functionality documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prettier_print
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prettier_print) = 1.2.1

%description   -n gem-prettier-print-doc
A drop-in replacement for the prettyprint gem with more functionality
documentation files.

%description   -n gem-prettier-print-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prettier_print.
%endif


%if_enabled    devel
%package       -n gem-prettier-print-devel
Version:       1.2.1
Release:       alt1
Summary:       A drop-in replacement for the prettyprint gem with more functionality development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prettier_print
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prettier_print) = 1.2.1

%description   -n gem-prettier-print-devel
A drop-in replacement for the prettyprint gem with more functionality
development package.

%description   -n gem-prettier-print-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prettier_print.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-prettier-print-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-prettier-print-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md LICENSE README.md
%endif


%changelog
* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
