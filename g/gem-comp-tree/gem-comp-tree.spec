%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname comp_tree

Name:          gem-comp-tree
Version:       1.1.3
Release:       alt1
Summary:       A simple framework for automatic parallelism
License:       Unlicense
Group:         Development/Ruby
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names comp_tree,comp-tree
Provides:      gem(comp_tree) = 1.1.3

%description
CompTree is a parallel computation tree structure based upon concepts from pure
functional programming.

CompTree has been tested on MRI versions 1.8.6, 1.8.7, 1.9.1, 1.9.2, and jruby
versions 1.4, 1.5, 1.6.


%if_enabled    doc
%package       -n gem-comp-tree-doc
Version:       1.1.3
Release:       alt1
Summary:       A simple framework for automatic parallelism documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета comp_tree
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(comp_tree) = 1.1.3

%description   -n gem-comp-tree-doc
A simple framework for automatic parallelism documentation files.

CompTree is a parallel computation tree structure based upon concepts from pure
functional programming.

CompTree has been tested on MRI versions 1.8.6, 1.8.7, 1.9.1, 1.9.2, and jruby
versions 1.4, 1.5, 1.6.

%description   -n gem-comp-tree-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета comp_tree.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-comp-tree-doc
%doc README.rdoc
%ruby_gemdocdir
%endif


%changelog
* Thu Oct 02 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.3-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
