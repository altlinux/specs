%define        gemname acts_as_list

Name:          gem-acts-as-list
Version:       1.0.4
Release:       alt1.1
Summary:       A gem adding sorting, reordering capabilities to an active_record model
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/brendon/acts_as_list
Vcs:           https://github.com/brendon/acts_as_list.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activerecord) >= 4.2
BuildRequires: gem(bundler) >= 1.0.0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_alias_names acts_as_list,acts-as-list
Requires:      gem(activerecord) >= 4.2


%description
This "acts_as" extension provides the capabilities for sorting and reordering a
number of objects in a list. The class that has this specified needs to have a
"position" column defined as an integer on the mapped database table.


%package       -n gem-acts-as-list-doc
Version:       1.0.4
Release:       alt1.1
Summary:       A gem adding sorting, reordering capabilities to an active_record model documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета acts_as_list
Group:         Development/Documentation
BuildArch:     noarch

%description   -n gem-acts-as-list-doc
A gem adding sorting, reordering capabilities to an active_record model
documentation files.

This "acts_as" extension provides the capabilities for sorting and reordering a
number of objects in a list. The class that has this specified needs to have a
"position" column defined as an integer on the mapped database table.

%description   -n gem-acts-as-list-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета acts_as_list.


%package       -n gem-acts-as-list-devel
Version:       1.0.4
Release:       alt1.1
Summary:       A gem adding sorting, reordering capabilities to an active_record model development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета acts_as_list
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bundler) >= 1.0.0 gem(bundler) < 3

%description   -n gem-acts-as-list-devel
A gem adding sorting, reordering capabilities to an active_record model
development package.

This "acts_as" extension provides the capabilities for sorting and reordering a
number of objects in a list. The class that has this specified needs to have a
"position" column defined as an integer on the mapped database table.

%description   -n gem-acts-as-list-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета acts_as_list.


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

%files         -n gem-acts-as-list-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-acts-as-list-devel
%doc README.md


%changelog
* Fri Jan 20 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1.1
- ! add adomatic alias finding macros

* Wed Sep 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.4-alt1
- + packaged gem with Ruby Policy 2.0
