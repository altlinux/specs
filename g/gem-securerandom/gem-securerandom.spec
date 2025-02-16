%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname securerandom

Name:          gem-securerandom
Version:       0.4.1
Release:       alt1
Summary:       Interface for secure random number generator
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/securerandom
Vcs:           https://github.com/ruby/securerandom.git
Packager:      Baltix Maintainers Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 3.1.0
Requires:      gem(rake) >= 0
Requires:      gem(test-unit) >= 0
Provides:      gem(securerandom) = 0.4.1

%description
Interface for secure random number generator.


%if_enabled    doc
%package       -n gem-securerandom-doc
Version:       0.4.1
Release:       alt1
Summary:       Interface for secure random number generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета securerandom
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(securerandom) = 0.4.1

%description   -n gem-securerandom-doc
Interface for secure random number generator documentation files.

%description   -n gem-securerandom-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета securerandom.
%endif


%if_enabled    devel
%package       -n gem-securerandom-devel
Version:       0.4.1
Release:       alt1
Summary:       Interface for secure random number generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета securerandom
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(securerandom) = 0.4.1

%description   -n gem-securerandom-devel
Interface for secure random number generator development package.

%description   -n gem-securerandom-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета securerandom.
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
%doc COPYING README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-securerandom-doc
%doc COPYING README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-securerandom-devel
%doc COPYING README.md
%endif


%changelog
* Sat Feb 15 2025 Pavel Skrylev <majioa@altlinux.org> 0.4.1-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies
