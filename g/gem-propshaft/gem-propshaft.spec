%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname propshaft

Name:          gem-propshaft
Version:       1.3.1
Release:       alt1
Summary:       Deliver assets for Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/propshaft
Vcs:           https://github.com/rails/propshaft.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(actionpack) >= 7.0.0
BuildRequires: gem(activesupport) >= 7.0.0
BuildRequires: gem(debug) >= 0
BuildRequires: gem(rack) >= 0
BuildRequires: gem(rails) >= 7.0.1
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(actionpack) >= 7.0.0
Requires:      gem(activesupport) >= 7.0.0
Requires:      gem(rack) >= 0
Provides:      gem(propshaft) = 1.3.1

%description
Deliver assets for Rails.


%if_enabled    doc
%package       -n gem-propshaft-doc
Version:       1.3.1
Release:       alt1
Summary:       Deliver assets for Rails documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета propshaft
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(propshaft) = 1.3.1

%description   -n gem-propshaft-doc
Deliver assets for Rails documentation files.

%description   -n gem-propshaft-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета propshaft.
%endif


%if_enabled    devel
%package       -n gem-propshaft-devel
Version:       1.3.1
Release:       alt1
Summary:       Deliver assets for Rails development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета propshaft
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(propshaft) = 1.3.1
Requires:      gem(debug) >= 0
Requires:      gem(rails) >= 7.0.1
Requires:      gem(rake) >= 0

%description   -n gem-propshaft-devel
Deliver assets for Rails development package.

%description   -n gem-propshaft-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета propshaft.
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
%doc MIT-LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-propshaft-doc
%doc MIT-LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-propshaft-devel
%doc MIT-LICENSE README.md
%endif


%changelog
* Thu Oct 16 2025 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- ^ 1.1.0 -> 1.3.1 (closes ALT#53564)

* Wed Jan 15 2025 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
