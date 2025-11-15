%define        _unpackaged_files_terminate_build 1
%def_disable   check
%def_enable    doc
%def_enable    devel
%define        gemname regexp_property_values

Name:          gem-regexp-property-values
Version:       1.5.2
Release:       alt1
Summary:       Inspect property values supported by Ruby's regex engine
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jaynetics/regexp_property_values
Vcs:           https://github.com/jaynetics/regexp_property_values.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(character_set) >= 1.8.0
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rake-compiler) >= 1.0
BuildRequires: gem(range_compressor) >= 1.0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(character_set) >= 1.9
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(range_compressor) >= 2
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names regexp_property_values,regexp-property-values
Requires:      ruby >= 2.1.0
Provides:      gem(regexp_property_values) = 1.5.2

%description
This small library lets you see which property values are supported by the
regular expression engine of the Ruby version you are running, and what they
match.


%if_enabled    doc
%package       -n gem-regexp-property-values-doc
Version:       1.5.2
Release:       alt1
Summary:       Inspect property values supported by Ruby's regex engine documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета regexp_property_values
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(regexp_property_values) = 1.5.2

%description   -n gem-regexp-property-values-doc
Inspect property values supported by Ruby's regex engine documentation
files.

This small library lets you see which property values are supported by the
regular expression engine of the Ruby version you are running, and what they
match.

%description   -n gem-regexp-property-values-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета regexp_property_values.
%endif


%if_enabled    devel
%package       -n gem-regexp-property-values-devel
Version:       1.5.2
Release:       alt1
Summary:       Inspect property values supported by Ruby's regex engine development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета regexp_property_values
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(regexp_property_values) = 1.5.2
Requires:      gem(character_set) >= 1.8.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rake-compiler) >= 1.0
Requires:      gem(range_compressor) >= 1.0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(character_set) >= 1.9
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(range_compressor) >= 2
Conflicts:     gem(rspec) >= 4

%description   -n gem-regexp-property-values-devel
Inspect property values supported by Ruby's regex engine development
package.

This small library lets you see which property values are supported by the
regular expression engine of the Ruby version you are running, and what they
match.

%description   -n gem-regexp-property-values-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета regexp_property_values.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-regexp-property-values-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-regexp-property-values-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Thu Oct 30 2025 Pavel Skrylev <majioa@altlinux.org> 1.5.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
