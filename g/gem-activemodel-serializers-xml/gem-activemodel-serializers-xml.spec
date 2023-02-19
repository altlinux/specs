%define        gemname activemodel-serializers-xml

Name:          gem-activemodel-serializers-xml
Version:       1.0.2.1
Release:       alt0.1
Summary:       This gem provides XML serialization for your Active Model objects and Active Record models
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/activemodel-serializers-xml/
Vcs:           https://github.com/rails/activemodel-serializers-xml.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(activerecord) >= 5.0.0
BuildRequires: gem(sqlite3) >= 1.3.6
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(activesupport) >= 5.0.0
BuildRequires: gem(activemodel) >= 5.0.0
BuildRequires: gem(builder) >= 3.1
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(sqlite3) >= 2
BuildConflicts: gem(builder) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency sqlite3 >= 1.5.4,sqlite3 < 2
%ruby_alias_names activemodel-serializers-xml,activemodel-serializers-xml
Requires:      gem(activesupport) >= 5.0.0
Requires:      gem(activemodel) >= 5.0.0
Requires:      gem(builder) >= 3.1
Conflicts:     gem(builder) >= 4
Obsoletes:     ruby-activemodel-serializers-xml < %EVR
Provides:      ruby-activemodel-serializers-xml = %EVR
Provides:      gem(activemodel-serializers-xml) = 1.0.2.1

%ruby_use_gem_version activemodel-serializers-xml:1.0.2.1

%description
This gem provides XML serialization for your Active Model objects and Active
Record models.


%package       -n gem-activemodel-serializers-xml-doc
Version:       1.0.2.1
Release:       alt0.1
Summary:       This gem provides XML serialization for your Active Model objects and Active Record models documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activemodel-serializers-xml
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activemodel-serializers-xml) = 1.0.2.1

%description   -n gem-activemodel-serializers-xml-doc
This gem provides XML serialization for your Active Model objects and Active
Record models documentation files.

%description   -n gem-activemodel-serializers-xml-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activemodel-serializers-xml.


%package       -n gem-activemodel-serializers-xml-devel
Version:       1.0.2.1
Release:       alt0.1
Summary:       This gem provides XML serialization for your Active Model objects and Active Record models development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activemodel-serializers-xml
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activemodel-serializers-xml) = 1.0.2.1
Requires:      gem(rake) >= 10.0
Requires:      gem(activerecord) >= 5.0.0
Requires:      gem(sqlite3) >= 1.3.6
Requires:      gem(rexml) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(sqlite3) >= 2

%description   -n gem-activemodel-serializers-xml-devel
This gem provides XML serialization for your Active Model objects and Active
Record models development package.

%description   -n gem-activemodel-serializers-xml-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activemodel-serializers-xml.


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

%files         -n gem-activemodel-serializers-xml-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-activemodel-serializers-xml-devel
%doc README.md


%changelog
* Sat Jan 21 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.2.1-alt0.1
- ^ 1.0.2 -> 1.0.2[1]

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt2
- > Ruby Policy 2.0
- ! spec tags

* Tue Oct 02 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
