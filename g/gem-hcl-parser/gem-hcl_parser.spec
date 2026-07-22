%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname hcl_parser

Name:          gem-hcl-parser
Version:       0.2.2
Release:       alt1
Summary:       HCL Variables Parser
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/boltops-tools/hcl_parser
Vcs:           https://github.com/boltops-tools/hcl_parser.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 13.0
BuildRequires: gem(rhcl) >= 0
BuildRequires: gem(rspec) >= 3.0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names hcl_parser,hcl-parser
%ruby_use_gem_dependency rake >= 13.0,rake < 14
Requires:      ruby >= 2.3.0
Requires:      gem(rake) >= 13.0
Requires:      gem(rhcl) >= 0
Requires:      gem(rspec) >= 3.0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4
Provides:      gem(hcl_parser) = 0.2.2

%description
HCL Variables Parser


%if_enabled    doc
%package       -n gem-hcl-parser-doc
Version:       0.2.2
Release:       alt1
Summary:       HCL Variables Parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета hcl_parser
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hcl_parser) = 0.2.2

%description   -n gem-hcl-parser-doc
HCL Variables Parser documentation files.

%description   -n gem-hcl-parser-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета hcl_parser.
%endif


%if_enabled    devel
%package       -n gem-hcl-parser-devel
Version:       0.2.2
Release:       alt1
Summary:       HCL Variables Parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета hcl_parser
Group:         Development/Ruby
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(hcl_parser) = 0.2.2

%description   -n gem-hcl-parser-devel
HCL Variables Parser development package.

%description   -n gem-hcl-parser-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета hcl_parser.
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

%if_enabled    doc
%files         -n gem-hcl-parser-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-hcl-parser-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 0.2.2-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
