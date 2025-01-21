%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname activerecord-import

Name:          gem-activerecord-import
Version:       2.0.0
Release:       alt1
Summary:       Bulk insert extension for ActiveRecord
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/zdennis/activerecord-import
Vcs:           https://github.com/zdennis/activerecord-import.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(activerecord) >= 4.2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.4.0
Requires:      gem(activerecord) >= 4.2
Provides:      gem(activerecord-import) = 2.0.0

%description
A library for bulk inserting data using ActiveRecord.


%if_enabled    doc
%package       -n gem-activerecord-import-doc
Version:       2.0.0
Release:       alt1
Summary:       Bulk insert extension for ActiveRecord documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета activerecord-import
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(activerecord-import) = 2.0.0

%description   -n gem-activerecord-import-doc
Bulk insert extension for ActiveRecord documentation files.

A library for bulk inserting data using ActiveRecord.

%description   -n gem-activerecord-import-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета activerecord-import.
%endif


%if_enabled    devel
%package       -n gem-activerecord-import-devel
Version:       2.0.0
Release:       alt1
Summary:       Bulk insert extension for ActiveRecord development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета activerecord-import
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activerecord-import) = 2.0.0
Requires:      gem(rake) >= 0

%description   -n gem-activerecord-import-devel
Bulk insert extension for ActiveRecord development package.

A library for bulk inserting data using ActiveRecord.

%description   -n gem-activerecord-import-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета activerecord-import.
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
%doc CHANGELOG.md LICENSE README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-activerecord-import-doc
%doc CHANGELOG.md LICENSE README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-activerecord-import-devel
%doc CHANGELOG.md LICENSE README.markdown
%endif


%changelog
* Mon Jan 20 2025 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
