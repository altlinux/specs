%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rabl

Name:          gem-rabl
Version:       0.16.1
Release:       alt1
Summary:       General ruby templating with json, bson, xml, plist and msgpack support
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/nesquena/rabl
Vcs:           https://github.com/nesquena/rabl.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rr) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(tilt) >= 0
BuildRequires: gem(oj) >= 0
BuildRequires: gem(msgpack) >= 1.0.0
BuildRequires: gem(bson) >= 1.7.0
BuildRequires: gem(plist) >= 0
BuildRequires: gem(i18n) >= 0.6
BuildRequires: gem(json) >= 0
BuildRequires: gem(builder) >= 0
BuildRequires: gem(rack-test) >= 0
BuildRequires: gem(activerecord) >= 4.0
BuildRequires: gem(sqlite3) >= 0
BuildRequires: gem(sinatra) >= 1.2.0
BuildRequires: gem(hashie) >= 0
BuildRequires: gem(riot) >= 0.12.3
BuildRequires: gem(activesupport) >= 2.3.14
BuildConflicts: gem(msgpack) >= 2
BuildConflicts: gem(bson) >= 6
BuildConflicts: gem(riot) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bson >= 5.0.1,bson < 6
%ruby_use_gem_dependency msgpack >= 1.7.2,msgpack < 2
%ruby_use_gem_dependency riot >= 0.12.3,riot < 1
Requires:      gem(activesupport) >= 2.3.14
Obsoletes:     ruby-rabl < %EVR
Provides:      ruby-rabl = %EVR
Provides:      gem(rabl) = 0.16.1


%description
RABL (Ruby API Builder Language) is a Rails and Padrino ruby templating system
for generating JSON, XML, MessagePack, PList and BSON. When using the
ActiveRecord 'to_json' method, I find myself wanting a more expressive and
powerful solution for generating APIs. This is especially true when the JSON
representation is complex or doesn't match the exact schema defined within the
database.

In particular, I want to easily:

* Create arbitrary nodes named based on combining data in an object * Pass
arguments to methods and store the result as a child node * Render partial
templates and inherit to reduce code duplication * Rename or alias attributes to
change the name from the model * Append attributes from a child into a parent
node * Include nodes only if a certain condition has been met

Anyone who has tried the 'to_json' method used in ActiveRecord for generating a
JSON response has felt the pain of this restrictive approach. RABL is a general
templating system created to solve these problems by approaching API response
generation in an entirely new way.

RABL at the core is all about adhering to MVC principles by deferring API data
representations to the view layer of your application. For a breakdown of common
misconceptions about RABL, please check out our guide to understanding RABL,
which can help clear up any confusion about this project.


%if_enabled    doc
%package       -n gem-rabl-doc
Version:       0.16.1
Release:       alt1
Summary:       General ruby templating with json, bson, xml, plist and msgpack support documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rabl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rabl) = 0.16.1

%description   -n gem-rabl-doc
General ruby templating with json, bson, xml, plist and msgpack support
documentation files.

RABL (Ruby API Builder Language) is a Rails and Padrino ruby templating system
for generating JSON, XML, MessagePack, PList and BSON. When using the
ActiveRecord 'to_json' method, I find myself wanting a more expressive and
powerful solution for generating APIs. This is especially true when the JSON
representation is complex or doesn't match the exact schema defined within the
database.

In particular, I want to easily:

* Create arbitrary nodes named based on combining data in an object * Pass
arguments to methods and store the result as a child node * Render partial
templates and inherit to reduce code duplication * Rename or alias attributes to
change the name from the model * Append attributes from a child into a parent
node * Include nodes only if a certain condition has been met

Anyone who has tried the 'to_json' method used in ActiveRecord for generating a
JSON response has felt the pain of this restrictive approach. RABL is a general
templating system created to solve these problems by approaching API response
generation in an entirely new way.

RABL at the core is all about adhering to MVC principles by deferring API data
representations to the view layer of your application. For a breakdown of common
misconceptions about RABL, please check out our guide to understanding RABL,
which can help clear up any confusion about this project.

%description   -n gem-rabl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rabl.
%endif


%if_enabled    devel
%package       -n gem-rabl-devel
Version:       0.16.1
Release:       alt1
Summary:       General ruby templating with json, bson, xml, plist and msgpack support development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rabl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rabl) = 0.16.1
Requires:      gem(rr) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(tilt) >= 0
Requires:      gem(oj) >= 0
Requires:      gem(msgpack) >= 1.0.0
Requires:      gem(bson) >= 1.7.0
Requires:      gem(plist) >= 0
Requires:      gem(i18n) >= 0.6
Requires:      gem(json) >= 0
Requires:      gem(builder) >= 0
Requires:      gem(rack-test) >= 0
Requires:      gem(activerecord) >= 4.0
Requires:      gem(sqlite3) >= 0
Requires:      gem(sinatra) >= 1.2.0
Requires:      gem(hashie) >= 0
Requires:      gem(riot) >= 0.12.3
Conflicts:     gem(msgpack) >= 2
Conflicts:     gem(bson) >= 6
Conflicts:     gem(riot) >= 1

%description   -n gem-rabl-devel
General ruby templating with json, bson, xml, plist and msgpack support
development package.

RABL (Ruby API Builder Language) is a Rails and Padrino ruby templating system
for generating JSON, XML, MessagePack, PList and BSON. When using the
ActiveRecord 'to_json' method, I find myself wanting a more expressive and
powerful solution for generating APIs. This is especially true when the JSON
representation is complex or doesn't match the exact schema defined within the
database.

In particular, I want to easily:

* Create arbitrary nodes named based on combining data in an object * Pass
arguments to methods and store the result as a child node * Render partial
templates and inherit to reduce code duplication * Rename or alias attributes to
change the name from the model * Append attributes from a child into a parent
node * Include nodes only if a certain condition has been met

Anyone who has tried the 'to_json' method used in ActiveRecord for generating a
JSON response has felt the pain of this restrictive approach. RABL is a general
templating system created to solve these problems by approaching API response
generation in an entirely new way.

RABL at the core is all about adhering to MVC principles by deferring API data
representations to the view layer of your application. For a breakdown of common
misconceptions about RABL, please check out our guide to understanding RABL,
which can help clear up any confusion about this project.

%description   -n gem-rabl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rabl.
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
%files         -n gem-rabl-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rabl-devel
%doc README.md
%endif


%changelog
* Wed Jul 31 2024 Pavel Skrylev <majioa@altlinux.org> 0.16.1-alt1
- ^ 0.16.0 -> 0.16.1

* Sat Oct 08 2022 Pavel Skrylev <majioa@altlinux.org> 0.16.0-alt1
- ^ 0.15.0 -> 0.16.0

* Tue Apr 19 2022 Pavel Skrylev <majioa@altlinux.org> 0.15.0-alt1
- ^ 0.14.3.1 -> 0.15.0

* Tue Jun 09 2020 Pavel Skrylev <majioa@altlinux.org> 0.14.3.1-alt1
- ^ 0.14.2 -> 0.14.3+
- ! fault to require to active_view explicitly in code by patch

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1.1
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 0.14.2-alt1
- updated (^) 0.13.1 -> 0.14.2
- used (>) Ruby Policy 2.0
- fixed (!) spec

* Mon Sep 24 2018 Pavel Skrylev <majioa@altlinux.org> 0.13.1-alt1
- Initial gemified build for Sisyphus
